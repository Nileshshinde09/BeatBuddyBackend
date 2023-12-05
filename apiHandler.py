from imports import *

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_secret='dcffd029266947f1b019245ec3a8aabd',client_id='847de36f322d48cfb6b22f213925fd71'))


def ArtistTopTracks(name='Red Hot Chili Peppers'):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_secret='dcffd029266947f1b019245ec3a8aabd',client_id='847de36f322d48cfb6b22f213925fd71'))

    name=name.strip()

    dict1={
        "track_name":[],
        "audio_url":[],
        "conver_image":[]
    }

    results = spotify.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
    lz_uri = artist['uri']

    results = spotify.artist_top_tracks(lz_uri)

    for track in results['tracks']:
        try:
            
            dict1['track_name'].append(track['name'])
            dict1['audio_url'].append(track['preview_url'])
            dict1['conver_image'].append(track['album']['images'][0]['url'])
            
        except Exception:
            pass
    return dict1

def ArtistImage(name):
    try:

        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_secret='dcffd029266947f1b019245ec3a8aabd',client_id='847de36f322d48cfb6b22f213925fd71'))

        results = spotify.search(q='artist:' + name, type='artist')
        items = results['artists']['items']
        if len(items) > 0:
            artist = items[0]
            return artist['images'][0]['url']
    except Exception :
        return False

def AlbumImage(name): 
    try:  
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_secret='dcffd029266947f1b019245ec3a8aabd',client_id='847de36f322d48cfb6b22f213925fd71'))

        results = spotify.search(q='album:' + name, type='album')
        items = results['albums']['items']
        if len(items) > 0:
            artist = items[0]
            return artist['images'][0]['url']
    except Exception :
        return False   
def NameToId(name):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_secret='dcffd029266947f1b019245ec3a8aabd',client_id='847de36f322d48cfb6b22f213925fd71'))
    results = spotify.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
        return artist['uri'].split(':')[-1]
        # print(artist['uri'])


if __name__=="__main__":
    ArtistTopTracks()
    ArtistImage()
    AlbumImage()
    NameToId()

