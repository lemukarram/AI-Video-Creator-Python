# main.py
from story_expander import expand_story
from image_generator import generate_image_prompts, generate_images
from animator import animate_images_from_folder
from video_editor import assemble_final_video

def main():
    print("🎬 AI Video Creator")

    # Step 1: User input
    story = input("Enter a short story (1–3 sentences): ")
    duration = int(input("Enter desired video duration (seconds): "))
    style = input("Choose visual style (realistic, anime, ceramic, watercolor, etc.): ")

    # Step 2: Expand story into script
    print("\n⏳ Expanding story...")
    expanded_script = expand_story(story, duration)

    print("\n📜 Expanded Script by Scenes:")
    for idx, scene in enumerate(expanded_script, 1):
        print(f"\n--- Scene {idx} ---\n{scene}")

    # Step 3: Generate image prompts
    print("\n📝 Generating image prompts...")
    prompts = generate_image_prompts(expanded_script, style=style)

    # Step 4: Generate images
    print("\n🎨 Creating images...")
    generate_images(prompts)

    # Step 5: Animate images into clips
    print("\n🎞️ Animating images into clips...")
    animate_images_from_folder()

    # Step 6: Assemble final video
    print("\n🎥 Assembling final video...")
    assemble_final_video()

    print("\n✅ Video creation complete! Find your video in /assets/final/")

if __name__ == "__main__":
    main()
