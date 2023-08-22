import sys
import os
from langchain.document_loaders import *
from langchain.indexes import VectorstoreIndexCreator

def loaderCall():
    # print(globals())
    listDocLoaders = [i for i in globals() if 'Loader' in i ]
    print(f'{len(listDocLoaders)} loaders have been retrieved')
    print("**** Loaders available ****")
    for i in range(len(listDocLoaders)):
        print(f"{i + 1}. {listDocLoaders[i]}")
    loaderChoosen = input("Choose a loader(mind the spelling) : ")
    while loaderChoosen not in listDocLoaders:
        if loaderChoosen.lower() == "quit":
            sys.exit("User chose to quit")
        print("**** Loader not found ****")
        loaderChoosen = input("Choose a loader(mind the spelling), type quit to exit: ")
    print(f"You have choosen {loaderChoosen}")
    in_source = input("Give appropriate source : ")
    loader_class = globals()[loaderChoosen]
    loader = loader_class(in_source)
    return loader
def chat(index):
    while True:
        uquery = input("User : ")
        if uquery.lower() == "quit":
            sys.exit("User chose to quit")
        print(f"ChatBot : {index.query(uquery)}")

def indexAndquery(loader):
    index = VectorstoreIndexCreator().from_loaders([loader])
    print("Start messaging with the bot (type quit to stop)!")
    chat(index)

def main():
    args = sys.argv[1:]
    if len(args) > 0:
        try:
            # export OPENAI_API_KEY= args
            os.environ['OPENAI_API_KEY'] = args[0]  # Replace 'args' with your actual API key
            print("API key set successfully.")
            loader = loaderCall()
            indexAndquery(loader)
        except Exception as e:
            sys.exit("Error setting API key:", str(e))
    else:
        sys.exit("NO OPEN API KEY PASSED.")

if __name__ == "__main__":
    main()