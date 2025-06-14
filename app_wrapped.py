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

        if video_url:
            video_status.success("✅ Video generated successfully!")

            # 🎉 Wrapped block with preview and download link (CHANGE HERE)
            st.markdown(
                """
                🎬 **Your cinematic video is ready!**
                --- 
                """
            )
            st.video(video_url)
            st.markdown(f"[✨ **Click here to view or download your video**]({video_url})")

        else:
            video_status.error("❌ Failed to generate video via FAL.")

    except Exception as e:
        step.markdown("❌ Perplexity or FAL failed.")
        st.error(f"💥 Error: {str(e)}")
