# video_editor.py
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip
from utils.file_utils import ensure_dir

FINAL_DIR = "assets/final"
MUSIC_DIR = "assets/music"

def assemble_final_video(clips_folder="assets/clips", output_filename="final_video.mp4"):
    """
    Concatenates all video clips in /assets/clips into one final video.
    Optionally adds background music from /assets/music/.
    Saves final video in /assets/final/.
    """
    ensure_dir(FINAL_DIR)

    # Collect all video clips
    clips = []
    for filename in sorted(os.listdir(clips_folder)):
        if not filename.lower().endswith(".mp4"):
            continue

        clip_path = os.path.join(clips_folder, filename)
        print(f"📂 Adding {clip_path} to final video...")
        clips.append(VideoFileClip(clip_path))

    if not clips:
        print("⚠️ No clips found in assets/clips/")
        return

    # Concatenate clips
    final_video = concatenate_videoclips(clips, method="compose")

    # Add background music if available
    music_file = None
    if os.path.exists(MUSIC_DIR):
        music_files = [f for f in os.listdir(MUSIC_DIR) if f.lower().endswith((".mp3", ".wav"))]
        if music_files:
            music_file = os.path.join(MUSIC_DIR, music_files[0])
            print(f"🎶 Adding background music: {music_file}")
            audio_clip = AudioFileClip(music_file).volumex(0.2)  # lower volume
            audio_clip = audio_clip.set_duration(final_video.duration)
            final_video = final_video.set_audio(audio_clip)

    # Export final video
    output_path = os.path.join(FINAL_DIR, output_filename)
    print(f"💾 Exporting final video -> {output_path}")
    final_video.write_videofile(output_path, fps=24)

if __name__ == "__main__":
    assemble_final_video()
