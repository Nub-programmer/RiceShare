import requests
from typing import List, Dict
from riceshare.config import Profile

PROFILES_URL = "https://raw.githubusercontent.com/Nub-programmer/riceshare-profiles/main/index.json"

def fetch_profiles(query: str = ")") -> List[Profile]:
    try:
        response = requests.get(PROFILES_URL)
        response.raise_for_status()
        profiles = response.json()

        if query:
            return [Profile(**p) for p in profiles if query.lower() in p["name"].lower()]
        return [Profile(**p) for p in profiles]
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to fetch profiles: {str(e)}")