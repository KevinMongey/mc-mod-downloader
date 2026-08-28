import requests

def search_mods(mod_name):
    url = "https://api.modrinth.com/v2/search"

    parameters = {
        "query": mod_name,
        "limit": 10
    }

    response = requests.get(url, params=parameters)
    response.raise_for_status
    data = response.json()
    return data["hits"]
