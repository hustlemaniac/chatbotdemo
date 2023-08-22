from libraries import *
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
