import streamlit as st
from generate_video_prompt import VideoPromptGenerator
import time
# import fal_client

# Load the API
generator = VideoPromptGenerator()

# Page settings
st.set_page_config(page_title="🎬 Video Prompt Generator", layout="centered")

# Modern CSS
st.markdown("""
    <style>
    .step-box {
        background-color: #f8f9fa;
        padding: 1.25rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
        transition: all 0.3s ease-in-out;
    }
    .step-box:hover {
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .fade {
        opacity: 0.95;
        transition: opacity 0.6s ease-in;
    }
    .small-text {
        font-size: 0.85rem;
        color: #6c757d;
    }
    </style>
""", unsafe_allow_html=True)

# UI title
st.title("🎬 One-Line Video Prompt Generator")
st.markdown("Enter a **movie or show title**, and we'll dynamically build a cinematic handheld prompt using the Perplexity API.")

# Input
user_input = st.text_input("🎥 Movie/Show Title", placeholder="e.g. Barbie, Toy Story, Pirates of the Caribbean")

# Main logic
if user_input:
    st.markdown('<div class="step-box fade">🔍 <strong>Step 1: Perplexity begins sourcing visual & narrative details</strong></div>', unsafe_allow_html=True)
    step_box = st.empty()

    # Simulate thought process with flushed steps
    step_box.markdown('<div class="step-box fade">🌍 Understanding cinematic universe and genre...</div>', unsafe_allow_html=True)
    time.sleep(0.7)

    step_box.markdown('<div class="step-box fade">🎭 Identifying main character and key sidekick...</div>', unsafe_allow_html=True)
    time.sleep(0.7)

    step_box.markdown('<div class="step-box fade">🎨 Extracting outfit, material, and environmental textures...</div>', unsafe_allow_html=True)
    time.sleep(0.7)

    step_box.markdown('<div class="step-box fade">🏙 Framing the background setting and side activities...</div>', unsafe_allow_html=True)
    time.sleep(0.7)

    step_box.markdown('<div class="step-box fade">🗣 Generating in-character cinematic dialogue line...</div>', unsafe_allow_html=True)
    time.sleep(0.7)

    # ⏳ NOW call the API
    try:
        prompt_data = generator.generate_prompt_data(user_input)

        step_box.markdown('<div class="step-box fade">✅ <strong>All cinematic variables successfully extracted!</strong></div>', unsafe_allow_html=True)
        time.sleep(0.5)

        st.markdown('<div class="step-box fade">📦 <strong>Step 2: Finalizing structured visual data</strong></div>', unsafe_allow_html=True)
        time.sleep(0.4)

        final_prompt = generator.render_template(prompt_data)

        st.markdown('<div class="step-box fade">🎬 <strong>Step 3: Composing prompt for AI video model</strong></div>', unsafe_allow_html=True)
        time.sleep(0.5)

        st.subheader("📽️ Generated Prompt")
        st.code(final_prompt, language='markdown')

        with st.expander("🧩 Raw variable data"):
            st.json(prompt_data)

    except Exception as e:
        step_box.markdown('<div class="step-box fade">❌ <strong>Error: Perplexity failed to complete the query.</strong></div>', unsafe_allow_html=True)
        st.error(f"API Error: {str(e)}")

# Footer
st.markdown("""
<hr style="margin-top:2rem;margin-bottom:1rem"/>
<div class="small-text">Built with 🧠 using Perplexity + Streamlit • Created by Brandon + GPT-4o</div>
""", unsafe_allow_html=True)
