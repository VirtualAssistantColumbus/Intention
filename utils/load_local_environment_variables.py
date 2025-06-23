import os

from dotenv import load_dotenv


loaded = False

def load_local_environment_variables() -> None:
    """ Loads local environment variables from .env file when running locally.
    
    - Local: When running this application locally, this function will load in the environment variables from the local .env file. 
    - Deployed: For a deployed application, this function will do nothing. You must actually set the environment variables in the environment for deployed applications. 
    
    Also includes a flag so that the environment variables are only loaded (or attempted to be loaded) once per application's life cycle. """
    
    global loaded
    if loaded:
        return
    
    # Locally, you can set an actual OS environment variable: INTENTION_APP_PATH = C:\Path\To\Website\
    LOCAL_APPLICATION_PATH = os.environ.get("INTENTION_APP_PATH")
    if LOCAL_APPLICATION_PATH:
        dotenv_path = LOCAL_APPLICATION_PATH + ".env"
        load_dotenv(dotenv_path)
    else:
        # Try loading from current directory
        load_dotenv()

    loaded = True 