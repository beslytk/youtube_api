
import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

credentials = None
if os.path.exists("token.pickle"):
    print('loading credentials from file:')
    with open("token.pickle",'rb') as token:
        credentials = pickle.load(token)

if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        print('refreshing access token')
        credentials.refresh(Request())
    else:
        print('access new tokens..')
        #run local web server, to login to google acc and allow the script access to data
        # the flow object allows us to do that
        flow = InstalledAppFlow.from_client_secrets_file(r"01-Getting-Started\client_secret_bp.json",
                                     scopes=["https://www.googleapis.com/auth/youtube.readonly"],
                                     )


        # we receive several tokens once we get authorized to google acc:  Access token, Refresh token
        flow.run_local_server(port=8080, prompt="consent", authorization_prompt_message="")
        # will run a local server and open a page to login to google acc. Once logged in and authorized, it sets credential within flow object

        # to access those credentials..
        credentials = flow.credentials
        # SAVE CREDENTIALS FOR NEXT RUN
        with open('token.pickle', 'wb') as f:
            print('saving cred for future use..')
            pickle.dump(credentials, f)

print(credentials.to_json())


youtube = build('youtube', 'v3', credentials=credentials)

request = youtube.playlistItems().list(
        part="status, contentDetails",
        playlistId ="PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU"
    )

response = request.execute()

for item in response['items']:
    vid_id = item["contentDetails"]["videoId"]
    yt_link = f"https://youtu.be/{vid_id}"
    print(yt_link)
