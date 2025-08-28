# story_expander.py
import openai

# Load your OpenAI key (or Gemini later via config file)
from utils.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def expand_story(story: str, duration: int):
    """
    Expands a short story into a scene-based script matching video duration.
    Returns a list of scene descriptions.
    """
    # Assume each scene ~5-8 seconds
    num_scenes = max(1, duration // 6)

    prompt = f"""
    You are a creative video scriptwriter.
    Expand the following short story into {num_scenes} scenes.
    Each scene should be 2-3 sentences, descriptive, and visual.
    Keep characters consistent.

    Story: "{story}"
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    raw_text = response["choices"][0]["message"]["content"].strip()
    # Split scenes by line breaks
    scenes = [s.strip() for s in raw_text.split("\n") if s.strip()]
    
    return scenes
