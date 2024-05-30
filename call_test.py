import os
import sys
import zipfile
def store_json_to_temp():
   try:
       workspace_path = os.getenv("GITHUB_WORKSPACE")
       destination_path = os.path.join(workspace_path, "tmp")
       if not os.path.exists(destination_path):
                os.makedirs(destination_path)
       zip_file_path = os.path.join(destination_path,"jfrog-test2"+".zip")

       with zipfile.ZipFile(zip_file_path, 'w') as zipf:
         zipf.writestr("jfrog-test.txt","hello")
       print("ZIP file path : ",zip_file_path)
            # set zip file path as output
       os.system("echo pkp_zip_path={} >> $GITHUB_OUTPUT".format(zip_file_path))   

   except Exception as e:
        print(f"Error in store_json_to_temp : {e}")    
if __name__ == "__main__":
   store_json_to_temp()
