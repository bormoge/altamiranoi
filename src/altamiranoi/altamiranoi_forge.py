from urllib.error import HTTPError
from http.client import HTTPResponse
from typing import Any
from abc import ABC, abstractmethod


class AltamiranoiForge(ABC):

    @abstractmethod
    def convert_forge_url_to_api_url(self, user_url: str) -> str | None:
        pass

    @abstractmethod
    def get_forge_user_name(self, user_url: str) -> str | None:
        pass

    @abstractmethod
    def fetch_forge_repository_data(
        self, api_url: str
    ) -> HTTPResponse | HTTPError | None:
        pass

    @abstractmethod
    def fetch_forge_repositories(
        self,
        personal_repos_flag: bool,
        starred_repos_flag: bool,
        org_repos_flag: bool,
        url: str,
        user_name: str,
    ) -> list[str]:
        pass

    @abstractmethod
    def check_if_rate_limit_has_been_reached(
        self,
    ) -> bool:
        pass

    @abstractmethod
    def get_rate_limit_date(
        self,
    ) -> int:
        pass

    @abstractmethod
    def set_rate_limit_date(
        self,
    ) -> int:
        pass

    @abstractmethod
    def normalize_forge_user_url(self, user_url: str) -> str:
        pass

    @abstractmethod
    def get_forge_name(self) -> str:
        pass

    @abstractmethod
    def __init__(self):
        pass
