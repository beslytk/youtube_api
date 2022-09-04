
# Google Developers Console - https://console.developers.google.com/

# Google API Python Client - https://github.com/googleapis/google-...

# YouTube API - https://developers.google.com/youtube/v3

from googleapiclient.discovery import build
import os

api_key = os.environ.get('YT_API_KEY') # make sure you have the environment variable containing the youtube-api-key from  https://console.developers.google.com/

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
        part='statistics',
        forUsername='beslytk'
    )

response = request.execute()

print(response)
