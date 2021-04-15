import requests

with open('urls.txt') as file:
    for line in file.readlines():
        url = line.rstrip("\n")
        try:
            response = requests.head(url)
            if response.status_code == 200:
                print(f'{url} STATUS {str(response.status_code)}')
        except requests.ConnectionError:
            print(f'ConnectionError using URL {url}')
            pass
