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

    if not results:
        return None

    return results[0]

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

    version = versions[0]
    files = version["files"]
    if not files:
        return None
    file = None
    
    for current_file in files:
        if current_file["primary"]:
            file = current_file
            break
    
    if file is None:
        file = files[0]

    version["selected_file"] = file
    return version

def download_mod(version, dest_folder):
    file = version["selected_file"]

    download_url = file["url"]
    response = requests.get(download_url)
    response.raise_for_status()

    filename = file["filename"]
    file_path = f"{dest_folder}/{filename}"
    with open(file_path, "wb") as mod_file:
        mod_file.write(response.content)

    return file_path