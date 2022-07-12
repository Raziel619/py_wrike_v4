# py_wrike

A python wrapper for the Wrike API V4. This wrapper provides convenience methods for accessing Wrike's API endpoints. Be sure to familiarize yourself with their documentation [here](https://developers.wrike.com/) before using this package.

# Getting Started

To get started, all you need to provide is the base API endpoint and a permanent access token. You can find documentation on how to acquire a permanent access token [here](https://developers.wrike.com/oauth-20-authorization/).

```python
from py_wrike import Wrike

wrike = Wrike(BASE_URL, PERM_ACCESS_TOKEN, SSL_VERIFY)

```

The `SSL_VERIFY` parameter can be set to `False` during testing but should be set to `True` in production.

# Wrike Object

Once you've got a valid `Wrike` object, you're ready to get started!

## Getter Properties

The Wrike object performs some internal caching on these properties to reduce the number of API calls it may need to make. Upon querying wrike for a certain data type, this library may first retrieve all objects of that data type and store it internally. Then, if you're searching for a specific object, it will extract it from that cache. If you ever need to clear this cache, simple call `wrike.reinitialize()`

1. `contacts`
2. `custom_fields` - A dictionary containing all custom fields used by projects in the workspace
3. `folders` - A dictionary containing all folders in the workspace. Includes all subtrees

## Query Methods

The following queries are available in the Wrike object.

- Contacts
  - query_contacts
  - query_contacts_all
  - query_contacts_me
- Custom Fields
  - query_custom_fields
  - query_custom_fields_all
- Folders
  - query_folders

# Contributing
