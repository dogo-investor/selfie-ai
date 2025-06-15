# selfie-ai

# 🎬 One-Line Cinematic Video Prompt Generator

Turn any movie or show title into a fully imagined, cinematic, handheld video scene — powered by **Perplexity's Sonar model** + **FAL's Veo3 video generation API**.

Built with ❤️ using **Streamlit**, **Python**, and ✨ some serious AI magic.

---

## 🌟 Live Demo

👉 [**Launch the App** on Streamlit](https://selfie-ai.streamlit.app)

---

## 📽️ What It Does

Just enter a movie/show title (e.g. `Barbie`, `Star Wars`, `Jimmy Neutron`) and:

1. 🔍 **Extracts visual + narrative details** using Perplexity
2. 🧠 Dynamically builds a **cinematic handheld scene**
3. 🎥 Generates a **real video** using FAL's Veo3 model
4. ✅ Streams back your **video preview + download link**

---

## ✨ Features

- 🧠 **Narrative Thinking Steps**
- 📜 Cinematic prompt templating
- 🤖 Perplexity Sonar integration
- 🎬 FAL Veo3 video API calls
- 🖼 Live video preview and download link
- ⚡ Beautiful & animated Streamlit UI

---

## 📸 Screenshots

| Prompted | Generated |
|----------|-----------|
| `Jimmy Neutron` | ![Preview](https://your-image-url.com/preview.gif) |

---

## 🧰 Tech Stack

| Tool            | Purpose                      |
|-----------------|------------------------------|
| 🐍 Python        | Core app logic                |
| 🎈 Streamlit     | Frontend + UI animations      |
| 🤖 Perplexity API | AI prompt generation         |
| 🎥 FAL Veo3 API   | AI video rendering            |
| 🔐 dotenv        | API key management            |

---

## 🚀 Getting Started

### 1️⃣ Install Requirements

```bash
pip install -r requirements.txt

---
```

## 2️⃣ Set your Environment

PPLX_API_KEY=your_perplexity_key
FAL_KEY=your_fal_key

---

## 3️⃣ Run the App
streamlit run app.py

---

## 🧠 How It Works

1. Perplexity returns a JSON schema with cinematic elements.
2. Those are templated into a video-style prompt.
3. FAL Veo3 renders a video based on that text prompt.
4. Final output is previewed and downloadable.

---

## 🛡️ License

MIT © 2025 — [@dogo-investor](https://github.com/dogo-investor)


---

## 🙌 Special Thanks

- 🤯 [Perplexity](https://perplexity.ai)
- 🎥 [FAL](https://fal.ai)
- 🧵 [Streamlit](https://streamlit.io)
- 🪄 GPT-4o for co-building this

---

> 💬 *Feel free to star ⭐, fork 🍴, or raise an issue if you’d like to contribute or have ideas!*

---



