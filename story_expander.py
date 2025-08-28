# story_expander.py
from openai import OpenAI
from utils.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def expand_story(story, duration):
    """
    Expands a short user-provided story into multiple scenes.
    Ensures total script length matches approximate duration.
    """
    prompt = f"""
    You are a script writer. Expand the following short story into
    multiple cinematic scenes for a video of {duration} seconds.
    Keep each scene short (1–3 sentences). 

    Story: {story}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful script writer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )

    # Extract text response
    expanded_text = response.choices[0].message.content.strip()

    # Split scenes by line breaks
    scenes = [s.strip() for s in expanded_text.split("\n") if s.strip()]
    return scenes
