# animator.py
import os
from moviepy.editor import ImageClip
from utils.file_utils import ensure_dir

CLIPS_DIR = "assets/clips"

def animate_image(image_path, output_path, duration=5):
    """
    Applies a simple Ken Burns (zoom in) effect to a static image.
    Saves as a video clip.
    """
    clip = (
        ImageClip(image_path)
        .set_duration(duration)
        .resize(height=720)  # standard HD
        .fx(lambda c: c.resize(lambda t: 1 + 0.05 * t))  # zoom effect
    )

    clip.write_videofile(output_path, fps=24)

def animate_images_from_folder(images_folder="assets/images", duration=5):
    """
    Animates all images in the given folder.
    Saves clips into assets/clips.
    """
    ensure_dir(CLIPS_DIR)

    for idx, filename in enumerate(os.listdir(images_folder), 1):
        if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
            continue

        image_path = os.path.join(images_folder, filename)
        output_path = os.path.join(CLIPS_DIR, f"scene_{idx}.mp4")

        print(f"🎞️ Animating {filename} -> {output_path}")
        animate_image(image_path, output_path, duration)

if __name__ == "__main__":
    animate_images_from_folder()
