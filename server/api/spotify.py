#! /usr/bin/env python
###############################################################################
#     File Name           :     spotify.py
#     Created By          :     vikram
#     Creation Date       :     [2017-01-21 00:57]
#     Last Modified       :     [2017-01-21 13:28]
#     Description         :     Interacts with the python file
###############################################################################

# import sys
import spotipy

name = "Drake"


def findSong(name):
    """TODO: Docstring for findSong.

    :arg1: TODO
    :returns: TODO

    """
    spotify = spotipy.Spotify()
    results = spotify.search(q=name, type='track')

    items = results['tracks']['items']

    return items[0] if len(items) > 0 else None


def findArtist(arg1):
    """TODO: Docstring for findArtist.

    :arg1: TODO
    :returns: TODO

    """
    spotify = spotipy.Spotify()
    results = spotify.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
        print(artist['name'], artist['images'][0]['url'])


if __name__ == "__main__":
    findSong("Jimi Hendrix - Purple Haze")
