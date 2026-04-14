import os
import anthropic
import json

def write_script(prompt):
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""You are a viral video script writer. Write a short engaging script for a faceless YouTube video about: {prompt}

Return a JSON object with exactly this format:
{{
    "script": "the full narration text",
    "scenes": [
        {{"scene": 1, "visual": "detailed description of what to show", "duration": 5}},
        {{"scene": 2, "visual": "detailed description of what to show", "duration": 5}}
    ]
}}

Keep it to 6-8 scenes. Make it dramatic and curiosity-driven. Return only the JSON, nothing else."""
            }
        ]
    )
    
    response = json.loads(message.content[0].text)
    return response["script"], response["scenes"]
