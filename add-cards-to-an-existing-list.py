import requests

# ------------------------------------------------------------------------------

key = "put_your_key_here"
token = "put_your_token_here"

# ------------------------------------------------------------------------------

base_url = "https://api.trello.com/1/"

target_board_id = "put_your_target_board_id_here"

card_name_list = ["Dummy card name #{}".format(i + 1) for i in range(10)]
card_desc_list = ["Dummy description #{}".format(i + 1) for i in range(10)]

# ------------------------------------------------------------------------------

# https://developer.atlassian.com/cloud/trello/rest/#api-boards-id-lists-get
result = requests.get(base_url + "boards/{}/lists?key={}&token={}".format(target_board_id, key, token))

num_lists = len(result.json())

if num_lists == 0:
    print("Found no list in this board (board_id = {}); exit without adding cards.".format(target_board_id))
    exit(0)

list_id = result.json()[0]["id"]

print("Message: Found {} lists in this board (board_id = {})".format(num_lists, target_board_id))
print("Message: Will add cards to the first list (list_id = {}).".format(list_id))

card_ids = []

for card_name, card_desc in zip(card_name_list, card_desc_list):
    # https://developer.atlassian.com/cloud/trello/rest/#api-cards-post
    data = {
        "name": card_name,
        "desc": card_desc,
        "idList": list_id,
        "key": key,
        "token": token,
    }
    result = requests.post(base_url + "cards", data=data)

    if result.status_code != 200:
        print(result, result.reason)
        exit(0)

    card_id = result.json()["id"]
    card_ids += [card_id]

    print("Message: Created a new card (card_id = {})".format(card_id))

print("Message: Done.")
