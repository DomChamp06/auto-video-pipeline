import os
from elevenlabs.client import ElevenLabs

def generate_voiceover(script):
    client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
    
    audio = client.generate(
        text=script,
        voice="Adam",
        model="eleven_monolingual_v1"
    )
    
    output_path = "output/voiceover.mp3"
    with open(output_path, "wb") as f:
        for chunk in audio:
            f.write(chunk)
    
    return output_path
