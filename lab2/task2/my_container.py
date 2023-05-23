import re
import json
import os


class MyContainer:
    def __init__(self, username):
        self.username = username
        self.storage = set()
        self.switch(username)

    def add(self, key):
        if key not in self.storage:
            self.storage.add(key)

    def remove(self, key):
        if key in self.storage:
            self.storage.remove(key)

    def find(self, key):
        notfound = True
        for el in key:
            if el in self.storage:
                print(f"{el}")
                notfound = False
        if notfound:
            print("No such elements")

    def list(self):
        for key in self.storage:
            print(f'{key}')

    def grep(self, regex):
        is_something_match = False
        for key in self.storage:
            if re.match(regex, key):
                print(f"{key}")
                is_something_match = True
        if not is_something_match:
            print("No such elements")

    def save(self):
        os.makedirs(os.path.dirname(f'./containers/{self.username}.json'), exist_ok=True)
        with open(f'./containers/{self.username}.json', 'w') as fp:
            json.dump(list(self.storage), fp)

    def load(self):
        if os.path.exists(f'./containers/{self.username}.json'):
            with open(f'./containers/{self.username}.json', 'r') as fp:
                self.storage.update(set(json.load(fp)))
        else:
            name = input("Enter name of file: ")
            if os.path.exists(f'./containers/{name}.json'):
                with open(f'./containers/{name}.json', 'r') as fp:
                    self.storage.update(set(json.load(fp)))
            else:
                print(f"There is no such file!")

    def switch(self, username):
        self.username = username
        self.storage.clear()
        if os.path.exists(f'./containers/{self.username}.json'):
            answer = input("Do you want to load the container?(y,n): ")
            if answer.lower() == "y":
                self.load()
        else:
            print(f"Created new container for user {self.username}")
            #s = {1, 2, 3, 4, 5}
            #s[::-1]
