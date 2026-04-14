import os
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips, TextClip, CompositeVideoClip
import whisper

def edit_video(clip_paths, audio_path, script):
    print("  Loading clips...")
    clips = [VideoFileClip(p) for p in clip_paths]
    final_clip = concatenate_videoclips(clips)
    
    print("  Adding voiceover...")
    audio = AudioFileClip(audio_path)
    final_clip = final_clip.set_audio(audio)
    
    print("  Generating captions...")
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    
    caption_clips = []
    for segment in result["segments"]:
        txt = TextClip(
            segment["text"],
            fontsize=50,
            color="white",
            stroke_color="black",
            stroke_width=2,
            font="Arial-Bold",
            method="caption",
            size=(final_clip.w * 0.9, None)
        )
        txt = txt.set_start(segment["start"]).set_end(segment["end"])
        txt = txt.set_position(("center", 0.7), relative=True)
        caption_clips.append(txt)
    
    print("  Compositing final video...")
    final = CompositeVideoClip([final_clip] + caption_clips)
    
    output_path = "output/final_video.mp4"
    final.write_videofile(output_path, fps=24, codec="libx264")
    
    for clip in clips:
        clip.close()
    
    return output_path
