import requests
import os
import sys
import zipfile
def store_json_to_temp(json_file_path):
   try:
       workspace_path = os.getenv("GITHUB_WORKSPACE")
       destination_path = os.path.join(workspace_path, "tmp")
       zip_file_path = os.path.join(destination_path,"jfrog-test"+".zip")

       with zipfile.ZipFile(zip_file_path, 'w') as zipf:
         zipf.writestr("jfrog-test.txt","hello")
       print("ZIP file path : ",zip_file_path)
            # set zip file path as output
       os.system("echo pkp_zip_path={} >> $GITHUB_OUTPUT".format(zip_file_path))   

       print(f"JSON file '{json_file_path}' copied to workspace at: {destination_path}")
   except Exception as e:
        print(f"Error copying JSON file: {e}")    
if __name__ == "__main__":
   json_file_path = sys.argv[1]
   store_json_to_temp(json_file_path)
