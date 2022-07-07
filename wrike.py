import requests

from py_wrike.helpers import convert_list_to_string


class Wrike:
    """
    A wrapper for Wrike API calls. Some API calls save data to a cache which this object manages. If at some point you'd like to clear those caches, simply call wrike.reinitialize()

    Args:
        :param base_url (string): Base Wrike URL, it should look like "https://<host>/api/v4/" (the trailing / is important)
        :param perm_access_token (string): A permanent access token obtained from Wrike's dashboard
        :param ssl_verify (bool): May need to set to false during testing

    """

    def __init__(self, base_url: str, perm_access_token: str, ssl_verify: bool = True):
        self.base_url = base_url
        self.ssl_verify = ssl_verify
        self.__headers = {
            "Accept": "application/json",
            "Authorization": "Bearer " + perm_access_token,
        }
        self.reinitialize()

    def reinitialize(self):
        self._contacts = None
        self._custom_fields = None
        self._folders = None

    # region Properties (Does Caching)

    @property
    def contacts(self) -> list:
        if not self._contacts:
            self._contacts = self.query_contacts_all().json()["data"]
        return self._contacts

    @property
    def custom_fields(self) -> list:
        if not self._custom_fields:
            self._custom_fields = self.query_custom_fields_all().json()["data"]
        return self._custom_fields

    @property
    def folders(self) -> list:
        if not self._folders:
            self._folders = self.query_folders_all().json()["data"]
        return self._folders

    # endregion

    # region Base HTTP Methods

    def __get(self, path: str) -> requests.Response:
        response = requests.get(
            self.base_url + path, headers=self.__headers, verify=self.ssl_verify
        )
        return response

    def __post(self, path: str, body: dict) -> requests.Response:
        response = requests.post(
            self.base_url + path,
            json=body,
            headers=self.__headers,
            verify=self.ssl_verify,
        )
        return response

    # endregion

    # region Contacts
    def query_contacts(self, ids: list) -> requests.Response:
        ids = convert_list_to_string(ids)
        return self.__get(f"contacts/{ids}")

    def query_contacts_all(self) -> requests.Response:
        return self.__get("contacts")

    def query_contact_me(self) -> requests.Response:
        return self.__get("contacts?me=true")

    # endregion

    # region Custom Fields

    def query_custom_fields(self, ids: list) -> requests.Response:
        ids = convert_list_to_string(ids)
        return self.__get(f"customfields/{ids}")

    def query_custom_fields_all(self) -> requests.Response:
        return self.__get("customfields")

    # endregion

    # region Folders

    def query_folders(self, ids: list) -> requests.Response:
        ids = convert_list_to_string(ids)
        return self.__get(f"folders/{ids}")

    def query_folders_all(self) -> requests.Response:
        return self.__get("folders")

    # endregion

    # region Groups

    def query_group(self, group_id: str) -> requests.Response:
        return self.__get(f"groups/{group_id}")

    def query_groups_all(self) -> requests.Response:
        return self.__get(f"groups")

    # endregion

    # region Tasks

    def query_tasks(self, ids: list) -> requests.Response:
        ids = convert_list_to_string(ids)
        return self.__get(f"tasks/{ids}")

    def query_tasks_all(self) -> requests.Response:
        return self.__get("tasks")

    def query_tasks_in_folder(self, folder_id: str) -> requests.Response:
        return self.__get(f"folders/{folder_id}/tasks")

    # endregion

    # region Users

    def query_user(self, user_id: str) -> requests.Response:
        return self.get(f"users/{user_id}")

    # endregion
