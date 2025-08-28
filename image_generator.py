# image_generator.py
import os
from openai import OpenAI
from utils.config import OPENAI_API_KEY
from utils.file_utils import ensure_dir

client = OpenAI(api_key=OPENAI_API_KEY)

IMAGES_DIR = "assets/images"

def generate_image_prompts(expanded_script, style="realistic"):
    """
    Generate image prompts from expanded script.
    Ensures characters remain consistent across all scenes.
    """
    prompts = []
    for i, scene in enumerate(expanded_script, 1):
        prompt = f"""
        Create a {style} illustration of the following scene.
        Keep character appearances consistent with previous scenes.
        Scene {i}: {scene}
        """
        prompts.append(prompt.strip())
    return prompts

def generate_images(prompts):
    """
    Generate images from prompts using OpenAI Images API.
    Saves them into /assets/images/.
    """
    ensure_dir(IMAGES_DIR)

    for idx, prompt in enumerate(prompts, 1):
        print(f"🖼️ Generating image {idx}: {prompt[:60]}...")

        response = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1024"
        )

        image_url = response.data[0].url
        os.system(f"curl {image_url} -o {IMAGES_DIR}/scene_{idx}.png")

    print("✅ All images generated and saved in assets/images/")
