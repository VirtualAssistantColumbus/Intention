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
    
    # Automatically find project root directory and load .env from there
    current_file_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_file_dir)  # Go up one level from utils/ to project root
    dotenv_path = os.path.join(project_root, ".env")
    
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    else:
        pass

    loaded = True