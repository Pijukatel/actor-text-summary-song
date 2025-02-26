from logging import getLogger

import requests
import json


def generate_songs(
    lyrics: str, api_key: str, genre: str = "Hip Hop", logger=getLogger(__name__)
) -> [str]:
    """Generate song and return generated song link."""
    api_url = "https://api.topmediai.com/v1/music"

    payload = {"is_auto": 0, "prompt": genre, "lyrics": lyrics}
    headers = {"x-api-key": api_key, "Content-Type": "application/json"}

    response = requests.request("POST", api_url, json=payload, headers=headers)
    if response.status_code != 200:
        raise RuntimeError(response.text)

    songs = json.loads(response.text)["data"]

    return [song["audio_file"] for song in songs]


def get_song(link: str) -> bytes:
    """Get song from link."""
    return requests.request("GET", link).content
