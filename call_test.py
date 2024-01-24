import requests
import os
import sys
def read_json_file(file):
   try:
      with open(file,'r') as file:
         data = file.read()
         print("json file content::")
         print(data)
   except FileNotFoundError:
      print(f"file not found : {file}")      
   # print("Hello World")
   # url="https://jsonplaceholder.typicode.com/todos"
   # r= requests.get(url)
   # print(r.json())

if __name__ == "__main__":
   json_file_path = sys.argv[1]
   read_json_file(json_file_path)
