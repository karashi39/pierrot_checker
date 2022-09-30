import requests


def get_page_body(url: str) -> bytes:
    result = requests.get(url)
    return result.content
