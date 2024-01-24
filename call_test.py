import requests
import shutil
import os
import sys
def store_json_to_temp(json_file_path):
   try:
      # with open(file,'r') as file:
         # data = file.read()
         # print("json file content::")
         # print(data)
      # Determine the destination path in the workspace
        destination_path = os.path.join(os.getenv("GITHUB_WORKSPACE"), os.path.basename("test.json"))
       # Copy the JSON file to the workspace
        shutil.copyfile(json_file_path, destination_path)
        print(f"JSON file '{json_file_path}' copied to workspace at: {destination_path}")
   except Exception as e:
        print(f"Error copying JSON file: {e}")    
if __name__ == "__main__":
   json_file_path = sys.argv[1]
   store_json_to_temp(json_file_path)
