import requests

# ------------------------------------------------------------------------------

key = "put_your_key_here"
token = "put_your_token_here"

# ------------------------------------------------------------------------------

base_url = "https://api.trello.com/1/"

board_name = "New Test Board"
board_desc = "A dummy description tet for the new test board."

list_names = [
    "List A",
    "List B",
    "List C",
]

# ------------------------------------------------------------------------------

# https://developer.atlassian.com/cloud/trello/rest/#api-members-id-boards-get
result = requests.get(base_url + "members/me/boards?key={}&token={}".format(key, token))

if result.status_code != 200:
    print(result, result.reason)
    exit(0)

for board_info in result.json():
    if board_info["name"] == board_name:
        print("Warning: The specified board name is already used in existing (either open or closed) boards.")

# https://developer.atlassian.com/cloud/trello/rest/#api-boards-post
data = {
    "name": board_name,
    "defaultLabels": "true",
    "defaultLists": "false",
    "desc": board_desc,
    "prefs_permissionLevel": "private",
    "prefs_voting": "disabled",
    "prefs_comments": "disabled",
    "prefs_invitations": "admins",
    "prefs_selfJoin": "true",
    "prefs_cardCovers": "false",
    "prefs_background": "grey",
    "prefs_cardAging": "regular",
    "key": key,
    "token": token,
}

result = requests.post(base_url + "boards", data=data)

if result.status_code != 200:
    print(result, result.reason)
    exit(0)

board_id = result.json()["id"]

print("Message: Created a new board (board_id = {})".format(board_id))


for list_name in list_names:
    # https://developer.atlassian.com/cloud/trello/rest/#api-boards-id-lists-post
    data = {
        "name": list_name,
        "pos": "bottom",
        "key": key,
        "token": token,
    }

    result = requests.post(base_url + "boards/{}/lists".format(board_id), data=data)

    if result.status_code != 200:
        print(result, result.reason)
        exit(0)

    list_id = result.json()["id"]

    print("Message: Created a new list (list_id = {})".format(list_id))

print("Message: Done.")
