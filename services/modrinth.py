import requests

def search_mods(mod_name):
    url = "https://api.modrinth.com/v2/search"

    parameters = {
        "query": mod_name,
        "limit": 10
    }

    response = requests.get(url, params=parameters)
    response.raise_for_status()
    data = response.json()
    results = data["hits"]

    project_id = results[0]["project_id"]
    return project_id

def get_compatible_version(project_id, mc_version, loader):
    url = f"https://api.modrinth.com/v2/project/{project_id}/version"

    parameters = {
        "game_versions": f'["{mc_version}"]',
        "loaders": f'["{loader}"]'
    }

    response = requests.get(url, params=parameters)
    response.raise_for_status()
    versions = response.json()

    if not versions:
        return None

    return versions[0]