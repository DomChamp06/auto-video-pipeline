import os
from dotenv import load_dotenv
from modules.script_writer import write_script
from modules.voiceover import generate_voiceover
from modules.video_generator import generate_video_clips
from modules.video_editor import edit_video
from modules.uploader import upload_to_youtube

load_dotenv()

def main():
    prompt = input("Enter your video prompt: ")
    print("\n[1/5] Writing script...")
    script, scenes = write_script(prompt)
    print("[2/5] Generating voiceover...")
    audio_path = generate_voiceover(script)
    print("[3/5] Generating video clips...")
    clip_paths = generate_video_clips(scenes)
    print("[4/5] Editing video...")
    final_video = edit_video(clip_paths, audio_path, script)
    print("[5/5] Uploading to YouTube...")
    upload_to_youtube(final_video, prompt)
    print("\nDone! Video uploaded successfully.")

if __name__ == "__main__":
    main()
