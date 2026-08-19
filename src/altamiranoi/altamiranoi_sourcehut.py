from urllib.error import HTTPError
from http.client import HTTPResponse
from typing import Any
from typing import cast
from urllib.parse import urlparse
from .altamiranoi_forge import AltamiranoiForge


class AltamiranoiSourceHut(AltamiranoiForge):

    def convert_forge_url_to_api_url(self, user_url: str) -> str | None:
        """
        This is a dummy function that returns repository_url.
        """

        return user_url

    def get_forge_user_name(self, user_url: str) -> str | None:
        """
        This is a dummy function that returns a dummy user name.
        """

        parts: list[str] = user_url.strip().split("/")

        if len(parts) < 4:
            return None

        user: str = parts[3]

        return user

    def fetch_forge_repository_data(
        self, api_url: str
    ) -> HTTPResponse | HTTPError | None:
        """
        This is a dummy function that returns 'None'.
        """

        return None

    def fetch_forge_repositories(
        self,
        personal_repos_flag: bool,
        starred_repos_flag: bool,
        org_repos_flag: bool,
        url: str,
        user_name: str,
    ) -> list[str]:
        """
        This is a dummy function that returns 'url'.
        """

        return [url]

    def normalize_forge_user_url(self, user_url: str) -> str:
        """
        Normalize the provided forge URL, leaving only the base URL, the user, and the repository name.
        """

        user: str | None = self.get_forge_user_name(user_url)
        base_url: Any = urlparse(user_url).netloc

        return f"https://{base_url}/{user}"

    def get_repository_programming_language(
        self, api_url: str, response: HTTPResponse | HTTPError | None
    ) -> str | Any:
        """
        This is a dummy function that returns 'SourceHut'
        """

        return "SourceHut"

    def get_forge_name(self) -> str:
        """
        This is a dummy function that returns "SourceHut".
        """

        return "SourceHut"

    def __init__(self):
        pass
