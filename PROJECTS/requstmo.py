from html.parser import HTMLParser
from pathlib import Path

import requests


class ProfileImageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.image_url = None

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "meta" and attributes.get("property") == "og:image":
            self.image_url = attributes.get("content")
user=input("enter your user name to donlode pofiele picture of intagram :")
profile_url = "https://www.instagram.com/user/"
page_response = requests.get(profile_url, timeout=30)
page_response.raise_for_status()

parser = ProfileImageParser()
parser.feed(page_response.text)
if not parser.image_url:
    raise RuntimeError("Instagram did not provide a profile image URL")

image_response = requests.get(parser.image_url, timeout=30)
image_response.raise_for_status()
if not image_response.headers.get("content-type", "").startswith("image/"):
    raise RuntimeError("The profile image URL did not return an image")

Path("profile_picture.jpg").write_bytes(image_response.content)