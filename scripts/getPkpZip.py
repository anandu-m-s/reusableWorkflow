import sys
import time
import requests
import os

def generate_pkp_zip(json_file_path):
    try:
        pkp_url = os.environ.get('PKP_URL')
        print ("url",pkp_url)
        auth_token = os.environ.get('AUTH_TOKEN')
        communication_channel = os.environ.get('COMMUNICATION_CHANNEL')
        headers = {'X-Auth-Token':auth_token,'X-Communication-Id':communication_channel}
        response = None
        print("response :",response)
        print("file path",json_file_path)
        if json_file_path.endswith('.json'):
            files = {'file': open(json_file_path, 'rb')}
            response = requests.post(pkp_url,files=files,headers=headers)
            print("response :",response.status_code)
        if response.status_code in [400,404,500]:
            print("Error occurred while fetching pkp download URL with status code: ",response.status_code)
            return None
        elif response.status_code in [200,202]:
            print("Successfully fetched pkp zip download url, status_code: ",response.status_code)
            return response.text

    except Exception as e:
        print ("Exception at generate_pkp_zip: ", e)

def download_pkp_zip(download_url,json_file_name):
    try:
        auth_token = os.environ.get('AUTH_TOKEN')
        communication_channel = os.environ.get('COMMUNICATION_CHANNEL')
        headers = {'X-Auth-Token':auth_token,'X-Communication-Id':communication_channel}
        response = None
        retry_count = 0
        time.sleep(10)
        while response is None or response.status_code ==202 and retry_count<=15:
            response = requests.get(download_url,headers=headers,verify=False, stream=True)
            print("waiting for zip file to be available ..... ")
            time.sleep(10)
            retry_count+=1
            if response.status_code in [400,404]:
                print("invalid request with status_code: ",response.status_code)
            elif response.status_code == 500:
                print("internal error , try after some times, status_code: ",response.status_code)

        if retry_count>= 15:
            print("Maximum retry limit reached, Please verify the provided doc ids")

        if response.status_code == 200:
            workspace_path = os.getenv("GITHUB_WORKSPACE")
            destination_path = os.path.join(workspace_path, "tmp")
            zip_file_name = os.path.splitext(json_file_name)[0]
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
            zip_file_path = os.path.join(destination_path,zip_file_name+".zip")
            with open(zip_file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=128):
                    file.write(chunk)
            print("ZIP file downloaded and saved to: ",zip_file_path)
            # set zip file path as output
            os.system("echo pkp_zip_path={} >> $GITHUB_OUTPUT".format(zip_file_path))
        else:
            print("Failed to download ZIP file. Status code: ",response.status_code)

    except Exception as e:
        print ("Exception occured in download_pkp_zip", e)

if __name__ == "__main__":
    json_file_path = sys.argv[1]
    json_file_name = sys.argv[2]
    download_url = generate_pkp_zip(json_file_path)
    print("download_url : ",download_url)
    if download_url is not None:
        download_pkp_zip(download_url,json_file_name)
    else:
        print("Not able to generate pkp zip ")