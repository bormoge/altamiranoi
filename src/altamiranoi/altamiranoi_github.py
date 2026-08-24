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

    def get_forge_user_name(self, user_url: str) -> str | None:
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
        Normalize the provided forge URL, leaving only the base URL and the user name.
        """

        user: str | None = self.get_forge_user_name(user_url)

        return f"https://github.com/{user}"

    def convert_forge_url_to_api_url(self, user_url: str) -> str | None:
        """
        Convert forge URL to forge API URL.
        """

        user: str | None = self.get_forge_user_name(user_url)

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

    def fetch_forge_repositories(
        self,
        personal_repos_flag: bool,
        starred_repos_flag: bool,
        org_repos_flag: bool,
        url: str,
        user_name: str,
    ) -> list[str]:
        """
        Fetch a user's repositories and, optionally, starred repositories and a organization's members' repositories.
        """

        return [url]

    def check_if_rate_limit_has_been_reached(
        self,
    ) -> bool:
        """
        Check if the rate limit for the GitHub API has been reached.
        """

        return False

    def get_rate_limit_date(
        self,
    ) -> int:
        """
        Get the GitHub API rate limit.
        """

        return -1

    def set_rate_limit_date(
        self,
    ) -> int:
        """
        Set the GitHub API rate limit as a variable.
        """

        return -1

    def convert_response_to_dict(self, response: HTTPResponse) -> dict:
        """
        Convert an HTTP response into a dictionary.
        """
        response_bytes: bytes = response.read()
        response_dict: dict = json.loads(response_bytes.decode("utf-8"))

        return response_dict

    def get_forge_name(self) -> str:
        """
        Return the string "GitHub".
        """

        return "GitHub"

    def __init__(self):
        self.def_context: ssl.SSLContext = ssl.create_default_context()
