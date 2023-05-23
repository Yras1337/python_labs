import my_container


if __name__ == "__main__":

    username = input("Enter username: ")
    container = my_container.MyContainer(username)
    is_executing = True

    while is_executing:
        command_list = '''
            add <key> [key, …]
            remove <key>
            find <key> [key, …]
            list
            grep <regex>
            save
            load
            switch
            exit
            '''
        print(command_list)
        command = input("Enter command: ")
        key = command.split()
        com = key.pop(0)
        match com:
            case "add":
                for el in key:
                    container.add(el)

            case "remove":
                if len(key) == 0:
                    continue
                container.remove(key[0])
            case "find":
                container.find(tuple(key))
            case "list":
                container.list()
            case "grep":
                if len(key) == 0:
                    continue
                container.grep(key[0])
            case "save":
                container.save()
            case "load":
                container.load()
            case "switch":
                answer = input("Do you want save your container?(y/n): ")
                if answer.lower() == 'y':
                    container.save()
                user = input("Enter username to switch: ")
                container.switch(user)
            case "exit":
                answer = input("Do you want save your container?(y/n): ")
                if answer.lower() == 'y':
                    container.save()
                is_executing = False
            case _:
                print("There is no such command")
