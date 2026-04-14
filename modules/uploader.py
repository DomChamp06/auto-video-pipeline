import os
import google.oauth2.credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def upload_to_youtube(video_path, prompt):
    flow = InstalledAppFlow.from_client_secrets_file(
        os.getenv("YOUTUBE_CLIENT_SECRETS"), SCOPES
    )
    credentials = flow.run_local_server(port=0)
    youtube = build("youtube", "v3", credentials=credentials)
    
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": prompt[:100],
                "description": "Auto-generated video",
                "tags": ["viral", "facts", "interesting"],
                "categoryId": "22"
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=MediaFileUpload(video_path, chunksize=-1, resumable=True)
    )
    
    response = request.execute()
    print(f"  Uploaded! Video ID: {response['id']}")
    return response["id"]
