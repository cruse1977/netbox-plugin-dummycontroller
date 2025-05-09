import os
import requests


if __name__ == "__main__":
    names = []
    url = f'{os.environ.get("NETBOX_URL")}/api/plugins/dummycontroller/pdus/'
    headers = {'Authorization': f'Token {os.environ.get("NETBOX_TOKEN")}' }
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        for item in r.json():
            print(item["name"])
            names.append(item["name"])
    for name in names:
        iurl = f'{url}?name={name}'
        print(f'== {name} ===')
        r = requests.get(iurl, headers=headers)
        if r.status_code == 200:     
            print(r.json())