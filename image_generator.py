# image_generator.py
import os
import openai
from utils.character_manager import extract_characters
from utils.file_utils import ensure_dir
from utils.prompt_utils import scene_prompt
from utils.config import OPENAI_API_KEY

IMAGES_DIR = "assets/images"

openai.api_key = OPENAI_API_KEY

def generate_image_prompts(script_scenes, style="cinematic realistic illustration"):
    """
    Creates image prompts for each scene using prompt templates.
    Ensures consistent characters across all scenes.
    """
    if not script_scenes:
        return []

    # Extract character traits from the first scene
    characters = extract_characters(script_scenes[0])

    prompts = []
    for idx, scene in enumerate(script_scenes, 1):
        prompt = scene_prompt(scene, characters, style)
        prompts.append(prompt.strip())

    return prompts


def generate_images(prompts, size="1024x1024"):
    """
    Calls OpenAI Image API to generate images for each prompt.
    Saves images to /assets/images/.
    """
    ensure_dir(IMAGES_DIR)

    for idx, prompt in enumerate(prompts, 1):
        print(f"🎨 Generating image {idx}...")

        response = openai.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size=size
        )

        image_url = response.data[0].url

        # Save image locally
        image_path = os.path.join(IMAGES_DIR, f"scene_{idx}.png")
        os.system(f"curl -s {image_url} -o {image_path}")

        print(f"✅ Saved {image_path}")


if __name__ == "__main__":
    # Example usage for testing
    example_scenes = [
        "A young boy with curly hair finds a glowing stone in the forest.",
        "He shows it to his wise grandmother in their cozy wooden cabin.",
        "The stone begins to shine, filling the room with light."
    ]

    prompts = generate_image_prompts(example_scenes)
    for i, p in enumerate(prompts, 1):
        print(f"\n--- Image Prompt {i} ---\n{p}\n")

    # Uncomment to test actual image generation
    # generate_images(prompts)
