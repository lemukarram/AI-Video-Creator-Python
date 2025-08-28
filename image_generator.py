# image_generator.py
import os
from openai import OpenAI
from utils.config import OPENAI_API_KEY, GEMINI_API_KEY
from utils.file_utils import ensure_dir
import google.generativeai as genai

client = OpenAI(api_key=OPENAI_API_KEY)

# Setup Gemini
genai.configure(api_key=GEMINI_API_KEY)

IMAGES_DIR = "assets/images"

def generate_image_prompts(expanded_script, style="realistic"):
    prompts = []
    for i, scene in enumerate(expanded_script, 1):
        prompt = f"""
        Create a {style} illustration of the following scene.
        Keep character appearances consistent with previous scenes.
        Scene {i}: {scene}
        """
        prompts.append(prompt.strip())
    return prompts


def generate_images(prompts, use_gemini=False):
    ensure_dir(IMAGES_DIR)

    for idx, prompt in enumerate(prompts, 1):
        print(f"🖼️ Generating image {idx}: {prompt[:60]}...")

        if not use_gemini:
            try:
                response = client.images.generate(
                    model="gpt-image-1",
                    prompt=prompt,
                    size="1024x1024"
                )
                image_url = response.data[0].url
                os.system(f"curl {image_url} -o {IMAGES_DIR}/scene_{idx}.png")
                continue
            except Exception as e:
                print(f"⚠️ OpenAI image gen failed: {e}, falling back to Gemini...")

        # Gemini fallback
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content([prompt])
        with open(f"{IMAGES_DIR}/scene_{idx}.txt", "w", encoding="utf-8") as f:
            f.write(response.text)

    print("✅ Images (or descriptions) saved in assets/images/")
