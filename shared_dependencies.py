from dataclasses import dataclass
from enum import StrEnum, auto
from logging import Logger
import os
from typing import Callable, List, Optional, Any

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


@dataclass
class RouteInfo:
    """Information about a route to be registered"""
    rule: str  # URL pattern like '/users/<id>'
    endpoint: str  # Endpoint name for url_for()
    view_func: Callable  # The view function
    methods: Optional[List[str]] = None  # HTTP methods like ['GET', 'POST']
    options: dict = None  # Additional Flask route options
    
    def __post_init__(self):
        if self.options is None:
            self.options = {}


class RouteRegistry:
    """Registry for storing route information before Flask app creation"""
    
    def __init__(self):
        self._routes: List[RouteInfo] = []
    
    def register(self, rule: str, endpoint: str = None, methods: List[str] = None, **options) -> Callable:
        """Decorator to register a route"""
        def decorator(func: Callable) -> Callable:
            route_info = RouteInfo(
                rule=rule,
                endpoint=endpoint or func.__name__,
                view_func=func,
                methods=methods or ['GET'],
                options=options
            )
            self._routes.append(route_info)
            return func
        return decorator
    
    def get_routes(self) -> List[RouteInfo]:
        """Get all registered routes"""
        return self._routes.copy()
    
    def apply_routes(self, app):
        """Apply all registered routes to a Flask app"""
        for route in self._routes:
            app.add_url_rule(
                rule=route.rule,
                endpoint=route.endpoint,
                view_func=route.view_func,
                methods=route.methods,
                **route.options
            )


# Global route registry instance
route_registry = RouteRegistry()

# Convenience decorator
def route(rule: str, endpoint: str = None, methods: List[str] = None, **options) -> Callable:
    """Custom @route decorator that registers routes in the registry"""
    return route_registry.register(rule, endpoint, methods, **options) 