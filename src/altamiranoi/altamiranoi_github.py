import json
import os
import ssl
import urllib.request
from http.client import HTTPResponse
from typing import Any, cast
from urllib.error import HTTPError

from .altamiranoi_forge import AltamiranoiForge


class AltamiranoiGitHub(AltamiranoiForge):

    def assign_token_to_headers(self) -> dict[str, Any]:
        """
        Get forge headers.
        """

        # Get the GitHub token
        github_token: str = os.environ.get("ALTAMIRANOI_GITHUB_TOKEN", "")

        # By default the headers are empty
        github_headers: dict[str, Any] = {}

        # If a token exists create the headers
        if github_token:
            github_headers["Authorization"] = f"token {github_token}"

        return github_headers

    def get_forge_user_name(
        self, user_url: str
    ) -> str | None:
        """
        Get the user name from the provided URL.
        """

        parts: list[str] = user_url.strip().split("/")

        if len(parts) < 4:
            return None

        user: str = parts[3]

        return user

    def normalize_forge_user_url(self, user_url: str) -> str:
        """
        Normalize the provided forge URL, leaving only the base URL, the user, and the repository name.
        """

        user: str | None = self.get_forge_user_name(user_url)

        return f"https://github.com/{user}"

    def convert_forge_url_to_api_url(
        self, user_url: str
    ) -> str | None:
        """
        Convert forge URL to forge API URL.
        """

        user: str | None = self.get_forge_user_name(
            user_url
        )

        if user is None:
            return None

        return f"https://api.github.com/{user}/starred"

    def fetch_forge_repository_data(
        self, api_url: str
    ) -> HTTPResponse | HTTPError | None:
        """
        Fetch the necessary data from GitHub.
        """

        # Create a request.
        request: urllib.request.Request = urllib.request.Request(
            url=api_url, headers=self.assign_token_to_headers()
        )

        # Try to call the API.
        try:
            response: HTTPResponse = urllib.request.urlopen(
                url=request, context=self.def_context
            )
            return response

        except HTTPError as http_error:
            return http_error

    def convert_response_to_dict(self, response: HTTPResponse) -> dict:
        """
        Convert an HTTP response into a dictionary.
        """
        response_bytes: bytes = response.read()
        response_dict: dict = json.loads(response_bytes.decode("utf-8"))

        return response_dict

    def get_repository_programming_language(
        self, api_url: str, response: HTTPResponse | HTTPError | None
    ) -> str | Any:
        """
        Get the main programming language of the provided repository URL.
        """

        # Check if response exists. If it doesn't, it means we know it's a GitHub
        # URL but it's not a repository.
        if response is None or isinstance(response, HTTPError):
            return "GitHub_URL"

        # Generate a dictionary using the response object.
        response_dict: dict = self.convert_response_to_dict(response)

        # If the dictionary generated is empty then we know there are no
        # programming languages in that repository.
        if (len(response_dict) == 0) or (response_dict == {}):
            return "No_Programming_Language"

        # Get the most used language in the repository.
        main_language: str | Any = max(response_dict, key=lambda k: response_dict[k])

        return main_language

    def get_forge_name(self) -> str:
        """
        Return the string "GitHub".
        """

        return "GitHub"

    def __init__(self):
        self.def_context: ssl.SSLContext = ssl.create_default_context()
