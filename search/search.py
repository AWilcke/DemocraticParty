from apiclient.discovery import build

DEVELOPER_KEY = "Insert API key here"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(song):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)
  #get top 5 results
  search_response = youtube.search().list(
    q=song,
    part="id,snippet",
    maxResults=5
  ).execute()
  
  results = search_response.get('items', [])
  #return first video
  for result in results:
    if result["id"]["kind"] == "youtube#video":
        return "https://www.youtube.com/watch?v=" + result["id"]["videoId"]         

