import requests

# ------------------------------------------------------------------------------

key = "put_your_key_here"
token = "put_your_token_here"

# ------------------------------------------------------------------------------

base_url = "https://api.trello.com/1/"

board_exact_name = "New Test Board"

# ------------------------------------------------------------------------------

# https://developer.atlassian.com/cloud/trello/rest/#api-members-id-boards-get
result = requests.get(base_url + "members/me/boards?key={}&token={}".format(key, token))

if result.status_code != 200:
    print(result, result.reason)
    exit(0)

deleted = False

for board_info in result.json():

    if board_info["name"] == board_exact_name:

        board_id = board_info["id"]

        # https://developer.atlassian.com/cloud/trello/rest/#api-boards-id-delete
        result = requests.delete(base_url + "boards/{}?key={}&token={}".format(board_id, key, token))

        if result.status_code != 200:
            print(result, result.reason)
            exit(0)

        print("Message: Deleted a board (board_id = {}).".format(board_id))

        deleted = True

if deleted:
    print("Message: Done.")
else:
    print("Message: No board with the specified name was found.")
