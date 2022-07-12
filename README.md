# py_wrike_v4

A python wrapper for the Wrike API V4. This wrapper provides convenience methods for accessing Wrike's API endpoints. Be sure to familiarize yourself with their documentation [here](https://developers.wrike.com/) before using this package. Wrike uses unique IDs to identify any of their data objects. These IDs are what's used to make requests to the Wrike API. Consider the example where you'd like to query a `folder/project` but only know its title. You may first need to query all folders in the workspace then determine the folder ID by matching the title. You can then use that folder ID to perform additional queries. This package provides some methods so simplify that flow in some cases.

# Getting Started

To get started, all you need to provide is the base API endpoint and a permanent access token. You can find documentation on how to acquire a permanent access token [here](https://developers.wrike.com/oauth-20-authorization/).

```python
from _py_wrike_v4 import Wrike

wrike = Wrike(BASE_URL, PERM_ACCESS_TOKEN, SSL_VERIFY)
```

The `SSL_VERIFY` parameter can be set to `False` during testing but should be set to `True` in production.

# Wrike Object

Once you've got a valid `Wrike` object, you're ready to get started!

## Getter Properties

The Wrike object performs some internal caching on these properties to reduce the number of API calls it may need to make. Upon querying wrike for a certain data type, this library may first retrieve all objects of that data type and store it internally. Then, if you're searching for a specific object, it will extract it from that cache. If you ever need to clear this cache, simple call `wrike.reinitialize()`.

1. `contacts` - A dictionary containing all contacts in the workspace
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
  - query_folders_all
  - query_folder_by_title
  - query_folder_subtrees
  - query_folder_subtrees_by_title
- Groups
  - query_group
  - query_groups_all
- Tasks
  - query_tasks
  - query_tasks_all
  - query_tasks_in_folder
- Users
  - query_user

# Contributing

Currently, this package only provides a small set of query methods. You can refer to the Wrike API documentation for a full list of functionality that they provide. The main file for adding convenience methods is `wrike.py`. Feel free to create a PR if you'd like to add any additional functionality.
