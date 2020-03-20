import requests


url = "http://api.baicaiyouxuan.com/index.php?g=api&m=flash_sale&a=add_notice"

h = {
    "Cookie": "PHPSESSID=kaa2e1jknt5oeos8r3euedt833;user_info=think%3A%7B%22id%22%3A%2230832%22%2C%22password%22%3A%220%22%7D",
    "bcyx": "%7B%22channel%22%3A2%2C%22r_id%22%3A%221a0018970a3e9e5313a%22%2C%22sex%22%3A2%2C%22udid%22%3A%222ddfe6f99d597c41%22%2C%22v%22%3A%221%22%2C%22version%22%3A%223.1.2%22%7D"
}

body = {
    "num_iid": "605468888767",
    "session_id": "72"
}
r = requests.post(url, headers=h, data=body)
print(r.text)
print(r.json())