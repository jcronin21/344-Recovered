from flask import Flask
import requests
from pprint import pprint

# initializes flask app:
app = Flask(__name__)

current_user = {
    'name': 'Walter',
    'username': 'walt2020',
    'profile_pic': 'https://i.picsum.photos/id/237/200/300'
}

@app.route('/')
def user_greeting():
    return '''
        <!DOCTYPE html>
        <html lang="en" >
        <head>
            <title>Demo</title>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css">
        </head>
        <body>
            <h1>Hello World!</h1>
        </body>
        </html>
    '''

@app.route('/e2')
def exercise2():
    '''
    Embed a spotify album by the first artist in the returned list
    '''
    search_term = 'Beyonce'
    url = 'https://www.apitutor.org/spotify/simple/v1/search?q={term}&type=artist'.format(term=search_term)
    response = requests.get(url)
    artists = response.json()
    pprint(artists)
    return '''
        <!DOCTYPE html>
        <html lang="en" >
        <head>
            <title>Artist Player Here</title>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css">
        </head>
        <body>
            <h1>Artist Player Here</h1>
            <iframe 
                src="https://open.spotify.com/embed/artist/0yNLKJebCb8Aueb54LYya3?utm_source=generator" 
                width="100%" 
                height="380" 
                frameBorder="0" 
                allowfullscreen="" 
                allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
            ></iframe>
        </body>
        </html>
    '''

'''
# You can also look at the Spotify documentation to find out 
# how to embed a playlist for an artist or an album.


'''

# enables flask app to run using "python3 app.py"
if __name__ == '__main__':
    app.run()
