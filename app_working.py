import streamlit as st
import time
import requests
from generate_video_prompt import VideoPromptGenerator, generate_veo3_video

# Load the API
generator = VideoPromptGenerator()

# Page settings
st.set_page_config(page_title="🎬 Video Prompt Generator", layout="centered")

st.title("🎬 One-Line Video Prompt Generator")
st.markdown("Enter a **movie or show title**, and we'll dynamically build and render a cinematic handheld video using Perplexity + FAL.")

user_input = st.text_input("🎥 Movie/Show Title", placeholder="e.g. Barbie, Toy Story, Pirates of the Caribbean")

if user_input:
    st.markdown("#### 🔍 Extracting visual & narrative details...")
    step = st.empty()

    # Narrative animation steps
    for msg in [
        "🌍 Understanding cinematic universe and genre...",
        "🎭 Identifying main character and key sidekick...",
        "🎨 Extracting outfit, material, and environmental textures...",
        "🏙 Framing the background setting and side activities...",
        "🗣 Generating in-character cinematic dialogue line..."
    ]:
        step.markdown(msg)
        time.sleep(0.6)

    try:
        prompt_data = generator.generate_prompt_data(user_input)
        final_prompt = generator.render_template(prompt_data)

        step.markdown("✅ All cinematic variables extracted.")
        st.markdown("#### 🎬 Composing final video prompt...")
        st.code(final_prompt, language="markdown")

        with st.expander("🧩 Raw variable data"):
            st.json(prompt_data)

        st.markdown("#### 🎥 Generating cinematic video with FAL...")
        video_status = st.empty()
        video_status.info("⏳ Video is being rendered... please wait (usually under 1 minute)")

        video_url = generate_veo3_video(final_prompt)

        # ⬇️ Added video preview + download UI
        if video_url:
            video_status.success("✅ Video generated successfully!")

            if isinstance(video_url, dict):
                video_url = video_url.get("url")

            if not video_url:
                video_status.error("⚠️ Video URL not found in response.")
            else:
                st.markdown(
                    f"""
                    <div style="border: 2px dashed #28a745; padding: 1rem; border-radius: 10px; background-color: #f0fff5; margin-top: 1rem;">
                        <h4 style="color: #28a745; margin-bottom: 0.5rem;">🎉 Your cinematic video is ready!</h4>
                        <a href="{video_url}" target="_blank" style="font-size: 1.1rem; color: #155724; text-decoration: underline;">🔗 Click here to view or download your video</a><br>
                        <span style="font-size: 0.9rem; color: #6c757d;">(hosted via FAL)</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                video_path = "generated_veo3_video.mp4"
                with open(video_path, "wb") as f:
                    response = requests.get(video_url, stream=True)
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)

                st.video(video_path)
        else:
            video_status.error("❌ Failed to generate video via FAL.")

    except Exception as e:
        step.markdown("❌ Perplexity or FAL failed.")
        st.error(f"💥 Error: {str(e)}")
