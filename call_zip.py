import requests
import os

def download_zip(api_url):
    response = requests.get(api_url, stream=True)

    destination_path = os.path.join(os.getenv("GITHUB_WORKSPACE"),"tmp", os.path.basename("pkp.zip"))
    if response.status_code == 200:
        with open(destination_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=128):
                file.write(chunk)
        print(f"ZIP file downloaded and saved to: {destination_path}")
    else:
        print(f"Failed to download ZIP file. Status code: {response.status_code}")

if __name__ == "__main__":
    # Set the URL of the API endpoint that provides the ZIP file
    api_url = "https://www.free-css.com/assets/files/free-css-templates/download/page296/mediplus-lite.zip"

    download_zip(api_url)