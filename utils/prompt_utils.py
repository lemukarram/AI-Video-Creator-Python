# utils/prompt_utils.py

def scene_prompt(scene_text: str, characters: str, style: str = "cinematic realistic illustration"):
    """
    Builds a consistent prompt for image generation.
    :param scene_text: The description of the scene from script
    :param characters: Character consistency description
    :param style: The chosen art style (realistic, ceramic, anime, etc.)
    :return: A formatted prompt string
    """
    return f"""
    {style}.
    Scene: {scene_text}
    Main characters: {characters}.
    Maintain consistent appearance and style across scenes.
    """
    

def narration_prompt(scene_text: str):
    """
    Generates a narration script prompt for voiceover if needed.
    """
    return f"Create a short narration line for the following scene: {scene_text}"


def music_prompt(story_theme: str):
    """
    Generates a description of background music based on the story theme.
    """
    return f"Suggest background music style that fits this theme: {story_theme}"
