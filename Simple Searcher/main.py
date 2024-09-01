import json
from colorama import Fore, Back, Style, init
import os
import time

init()

def preparing_data(file_path: str) -> dict:
    data: dict= {}
    with open(file_path, "r") as file:
        i = 0
        print(Fore.GREEN+ "Preparing data..." )
        tokens = file.read().splitlines()
        for line in tokens:
            i += 1
            token = line.split(" ")
            for word in token:
                if word.endswith(("?", "!", ",", ".")):
                    word = word[:-1]


                if word not in data:
                    data[word] = [i]

                else:
                    data[word].append(i)

    with open("data.json", "w") as file:
        json.dump({"words":data}, file, indent=3)

    time.sleep(3)
    print("The data is Done" + Fore.RESET)
    time.sleep(2)
    if os.name == "nt":
        os.system("cls")
    else:
        os.system('clear')


    return data


def request_word(word: str, file_path: str) -> str:
    data: dict = preparing_data(file_path)
    if word not in data:
        return Fore.RED + "Not Found" + Fore.RESET
    with open(file_path , "r") as file:
        file_lines = file.readlines()
        for i in data[word]:
            yield file_lines[i - 1]

    return "Found"


if __name__ == "__main__":
    path = input("Write File Path : ")
    word = input("Enter The Word you Want to search on it : ")
    result = list(request_word(word, path))
    if len(result) < 1:
        print(Fore.RED + "Not Found" + Fore.RESET)
    else:
        print(Fore.CYAN + "Results : " + Fore.RESET)
        print(Fore.CYAN  + f"Count of Searchs {len(result)}" + Fore.RESET)
        for idx, val in enumerate(result):
            print(Fore.YELLOW + f"{idx + 1} - {val}" + Fore.RESET)

                
                