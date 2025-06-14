import json
import os
import requests
from pathlib import Path
from typing import Optional

import streamlit as st

# ✅ Use Streamlit's secrets management
os.environ["FAL_KEY"] = st.secrets["FAL_KEY"]
PPLX_API_KEY = st.secrets["PPLX_API_KEY"]

import fal_client

class VideoPromptGenerator:
    API_URL = "https://api.perplexity.ai/chat/completions"
    DEFAULT_MODEL = "sonar-pro"
    PROMPT_FILE = "video_prompt_agent.md"

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or PPLX_API_KEY  # ✅ Use secret directly

        print("🔐 API Key Loaded:", "✅ YES" if self.api_key else "❌ MISSING")

        self.system_prompt = self._load_prompt(self.PROMPT_FILE)

    def _load_api_key(self):
        # ✅ No longer needed since we load directly from secrets
        return PPLX_API_KEY

    def _load_prompt(self, file_path):
        try:
            prompt = Path(file_path).read_text()
            print(f"📄 Prompt loaded from {file_path} (length: {len(prompt)} chars)")
            return prompt
        except Exception as e:
            raise RuntimeError(f"Failed to load system prompt: {e}")

    def generate_prompt_data(self, title: str):
        user_prompt = f"Create a cinematic handheld prompt preset for: {title}"
        print(f"🎬 Generating prompt for: {title}")

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        body = {
            "model": self.DEFAULT_MODEL,
            "messages": [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "response_format": {
                "type": "json_schema",
                "json_schema": {
                    "schema": {
                        "type": "object",
                        "properties": {key: {"type": "string"} for key in [
                            "camera_style", "location", "time_of_day", "main_character", "main_character_outfit",
                            "face_visibility", "light_source", "outfit_material", "background_setting",
                            "background_activity", "location_description", "secondary_character",
                            "secondary_action_description", "dialogue_line"
                        ]},
                        "required": ["main_character", "location", "dialogue_line"]
                    }
                }
            }
        }

        print(f"📤 Sending POST request to: {self.API_URL}")
        print(f"🧾 Headers: {headers}")
        print(f"📝 Body: {json.dumps(body, indent=2)[:500]}...")  # truncate long payload

        try:
            res = requests.post(self.API_URL, headers=headers, json=body)
            print(f"📡 Status Code: {res.status_code}")
            res.raise_for_status()
            content = res.json()["choices"][0]["message"]["content"]
            print("✅ Response received successfully.")
            return json.loads(content)
        except requests.exceptions.HTTPError as http_err:
            print(f"❌ HTTP error: {http_err}")
            print("📨 Response body:", res.text)
            raise
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            raise

    def render_template(self, data: dict):
        template = """
A cinematic handheld {camera_style} medium shot, set in a {location} in the {time_of_day}. {main_character} in {main_character_outfit} holds the camera at arm’s length, {face_visibility}, as sunlight glistens in from {light_source}. His {outfit_material} is glossy and shining. Behind him, {background_setting} – {background_activity}. The {location_description}. {main_character} slowly pans the camera sideways, revealing {secondary_character} {secondary_action_description}. Sun glistens off his frame as it shines through the window. Back on camera, {main_character} yells with a sense of urgency: “{dialogue_line}”
"""
        return template.format(**data)
    
def generate_veo3_video(prompt_text: str) -> str:
    def on_queue_update(update):
        if isinstance(update, fal_client.InProgress):
            for log in update.logs:
                print("🔄", log.get("message", ""))

    result = fal_client.subscribe(
        "fal-ai/veo3",
        arguments={
            "prompt": prompt_text,
            "aspect_ratio": "16:9",
            "duration": "8s",
            "enhance_prompt": True,
            "generate_audio": True
        },
        on_queue_update=on_queue_update,
        with_logs=True,
    )

    return result.get("video", None)
