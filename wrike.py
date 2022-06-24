import requests


class Wrike:
    """
    A wrapper for Wrike API calls

    Parameters:
        base_url (string): Base Wrike URL, it should look like "https://<host>/api/v4/" (the trailing / is important)
        perm_access_token (string): A permanent access token obtained from Wrike's dashboard
        ssl_verify (bool): May need to set to false during testing
    """

    def __init__(self, base_url: str, perm_access_token: str, ssl_verify: bool = True):
        self.base_url = base_url
        self.ssl_verify = ssl_verify
        self.__headers = {
            "Accept": "application/json",
            "Authorization": "Bearer " + perm_access_token,
        }

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

    def query_contact_all(self) -> requests.Response:
        return self.__get("contacts")

    def query_contact_myself(self) -> requests.Response:
        return self.__get("contacts?me=true")

    # endregion

    # region Folders

    def query_folder(self, folder_id) -> requests.Response:
        return self.__get(f"folders/{folder_id}")

    def query_folder_all(self) -> requests.Response:
        return self.__get(f"folders")

    # endregion
