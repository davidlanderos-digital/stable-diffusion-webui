import requests
import os
import shutil
import pathlib
import json

script_path = os.path.dirname(os.path.realpath(__file__))

def dowloadFile(url, output_file_path):
    filename = os.path.basename(output_file_path)
    if os.path.exists(output_file_path):
        print(f"Downloaded 100% ({filename})")
        return
    directory = os.path.dirname(output_file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.5',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Brave";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }
    with requests.get(url, headers=headers, stream=True) as response:
        if response.status_code == 200:
            total_size = int(response.headers.get('content-length', 0))
            with open(output_file_path + ".unconfirmed", 'wb') as file:
                chunk_size = 1024  # Adjust the chunk size as needed
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    percentage = int(file.tell() / total_size * 100)
                    print(f"Downloaded {percentage}% ({filename})", end='\r')
            os.rename(output_file_path + ".unconfirmed", output_file_path)
            print(f"Downloaded 100% ({filename})")
        else:
            print(f'Request failed with status code: {response.status_code}')

models_to_download_filename = os.path.join(script_path, "models_to_download.json")
models_to_download = json.load(open(models_to_download_filename))

for model in models_to_download:
    url = model["url"]
    output_file_path = os.path.join(script_path, model["path"])
    dowloadFile(url, output_file_path)