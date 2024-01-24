import requests
import zipfile
import os
import sys
def create_zip_file(json_file_path):
   try:
      # with open(file,'r') as file:
         # data = file.read()
         # print("json file content::")
         # print(data)
      zip_file_path = f".github/workflows/{os.path.basename(json_file_path).replace('.json', '_archive.zip')}"
      with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
            # Add the JSON file to the zip file
            zip_file.write(json_file_path, os.path.basename(json_file_path))
            print(f"Zip file '{zip_file_path}' created containing: {os.path.basename(json_file_path)}")
   except Exception as e:
        print(f"Error creating zip file: {e}")    
if __name__ == "__main__":
   json_file_path = sys.argv[1]
   create_zip_file(json_file_path)
