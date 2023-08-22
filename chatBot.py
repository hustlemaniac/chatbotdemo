from libraries import *
from loaderScript import *
from pipeline import *
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