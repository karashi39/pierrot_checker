import requests


def get_page_body(url: str) -> str:
    result = requests.get(url)
    return str(result.content)
