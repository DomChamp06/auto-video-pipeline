import os
import fal_client
import requests

def generate_video_clips(scenes):
    clip_paths = []
    
    for i, scene in enumerate(scenes):
        print(f"  Generating clip {i+1} of {len(scenes)}...")
        
        result = fal_client.submit(
            "fal-ai/kling-video/v2/standard/text-to-video",
            arguments={
                "prompt": scene["visual"],
                "duration": str(scene["duration"]),
                "aspect_ratio": "9:16"
            }
        ).get()
        
        video_url = result["video"]["url"]
        clip_path = f"output/clip_{i+1}.mp4"
        
        response = requests.get(video_url)
        with open(clip_path, "wb") as f:
            f.write(response.content)
        
        clip_paths.append(clip_path)
    
    return clip_paths
