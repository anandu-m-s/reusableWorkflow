import requests
import os
import sys
def main():
   print("Hello World")
   url="https://jsonplaceholder.typicode.com/todos"
   r= requests.get(url)
   print(r.json())

if __name__ == "__main__":
  main()
