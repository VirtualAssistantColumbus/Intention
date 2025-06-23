from dataclasses import dataclass
from enum import StrEnum, auto
from logging import Logger
import os

from utils.cached_field import CachedField

# Load in local environment variables
from utils.load_local_environment_variables import load_local_environment_variables
load_local_environment_variables()


class EnvSetupError(Exception):
    """ Exception when environment variables aren't set properly. """

class RuntimeEnvironment(StrEnum):
    PRODUCTION = auto()
    LOCAL = auto()

@dataclass
class Environment:
    runtime_environment: RuntimeEnvironment
    
    @property
    def is_local(self) -> bool:
        return self.runtime_environment == RuntimeEnvironment.LOCAL
    
    @property
    def gtag_debug_mode(self) -> bool:
        """Enable Google Analytics debug mode only in local environment"""
        return self.is_local

    def __str__(self) -> str:
        fields = []
        for field in self.__dataclass_fields__:
            value = getattr(self, field)
            fields.append(f"    {field}={value}")
        return "Environment(\n" + ",\n".join(fields) + "\n)"

class Shared:
    """ Singleton class that provides access to shared dependencies.

    Benefits:
        - Modules that import this instance make it clear that they are relying on shared dependencies
        - Lazy initialization eliminates circular dependencies by delaying instantiation of each dependency until needed.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Shared, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        pass
    
    @CachedField
    def logger(self) -> Logger:
        from utils.logger import create_logger
        return create_logger()
    
    @CachedField
    def environment(self) -> Environment:
        self.logger.info("Setting up environment configuration...")
        
        RUNTIME_ENVIRONMENT = os.environ.get('RUNTIME_ENVIRONMENT')
        if not RUNTIME_ENVIRONMENT:
            # Default to production if not set
            self.logger.info("RUNTIME_ENVIRONMENT not set, defaulting to production")
            runtime_environment = RuntimeEnvironment.PRODUCTION
        else:
            self.logger.info(f"Found RUNTIME_ENVIRONMENT: '{RUNTIME_ENVIRONMENT}'")
            try:
                runtime_environment = RuntimeEnvironment(RUNTIME_ENVIRONMENT.lower())
                self.logger.info(f"Successfully parsed runtime environment: {runtime_environment}")
            except ValueError:
                self.logger.error(f"Invalid RUNTIME_ENVIRONMENT specified: '{RUNTIME_ENVIRONMENT}'. Must be 'local' or 'production'.")
                raise EnvSetupError(f"Invalid RUNTIME_ENVIRONMENT specified: '{RUNTIME_ENVIRONMENT}'. Must be 'local' or 'production'.")

        environment = Environment(
            runtime_environment=runtime_environment
        )
        
        self.logger.info(f"Environment setup complete:\n{environment}")
        return environment

shared = Shared() 