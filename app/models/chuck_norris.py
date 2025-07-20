import requests
from typing import Optional, Dict, Any

class ChuckNorris:
    def __init__(self):
        self.api_url = "https://api.chucknorris.io/jokes/random?category=dev"

    def get_joke(self) -> Optional[Dict[str, Any]]:
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            joke_data = response.json()
            return joke_data["value"].replace("Chuck Norris", "Meow Norris")
        except requests.RequestException as e:
            print(f"Error fetching joke: {e}")
            return None