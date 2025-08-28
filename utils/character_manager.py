# utils/character_manager.py
import re

def extract_characters(scene_text: str):
    """
    Naive character extraction from first scene.
    Later can be improved with LLM for robust entity extraction.
    """
    # Simple heuristic: Look for "boy", "girl", "man", "woman", "child", etc.
    keywords = ["boy", "girl", "man", "woman", "child", "grandmother", "grandfather", "teacher", "soldier"]
    found = [word for word in keywords if word in scene_text.lower()]

    if not found:
        return "Main characters as described in the story"

    return ", ".join(found)
