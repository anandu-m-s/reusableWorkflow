import requests
import os

def download_zip(api_url):
    response = requests.get(api_url, stream=True)
    
    workspace_path = os.getenv("GITHUB_WORKSPACE")
    destination_path = os.path.join(workspace_path, "tmp")
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    zip_file_path = os.path.join(destination_path,"pkp.zip")
    
    if response.status_code == 200:
        with open(zip_file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=128):
                file.write(chunk)
        print(f"ZIP file downloaded and saved to: {zip_file_path}")
        # upload zip file as artifact
        os.system(f"echo '::set-output name=zipFilePath::{zip_file_path}'")
    else:
        print(f"Failed to download ZIP file. Status code: {response.status_code}")

if __name__ == "__main__":
    # Set the URL of the API endpoint that provides the ZIP file
    api_url = "https://www.free-css.com/assets/files/free-css-templates/download/page296/mediplus-lite.zip"

    download_zip(api_url)