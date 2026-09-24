from requests import post
from sys import argv,exit

url = "https://moderator.adaface.com/compile"

def run(file_name,stdin):
        try:
                with open(file_name,"r") as f :
                        code = f.read()
        except :
                print("File Not Found !")
                exit(0)
        payload = {
                "language_id": 100,
                "source_code":code,
                "stdin": stdin
        }

        response = post(url,data=payload)

        return response.json()

def display(output):
        if output["statusCode"]!=200:
                print("NETWORK :\n")
                print("Internet Is Poor !")
                return
        output = output["responseToSend"]

        if output["stdout"]!="":
                print("OUTPUT :\n")
                print(output["stdout"])
                return
        if output["stderr"]!="":
                print("Error : \n")
                print(output["stderr"])
                return
        if output["error"]!="":
                print("Main Error :\n")
                print(output["error"])

print()

if len(argv)<2:
        print("USAGE : dart file_name.dart input1 ...only if you have !")
else:
        display(run(argv[1],' '.join(argv)[2:]if len(argv)>2 else ""))
