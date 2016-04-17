import soundcloud
from fuzzywuzzy import fuzz

client = soundcloud.Client(client_id='Insert API key here')

def fuzzy_search(song):
    tracks = client.get('tracks', q=song)
    maxi = 0
    best = ''
    for track in tracks:
        match = fuzz.token_sort_ratio(track.title, song)
        if match>maxi:
            best = track.permalink_url
            maxi = match
    return best
    
def search(song):
    tracks = client.get('tracks',q=song)
    return tracks[0]
    return tracks[0].permalink_url
