from functools import wraps

class CachedField:
    """Decorator that caches the result of a method call in the instance."""
    
    def __init__(self, func):
        self.func = func
        self.attr_name = f"_cached_{func.__name__}"
        
    def __get__(self, instance, owner):
        if instance is None:
            return self
            
        if not hasattr(instance, self.attr_name):
            result = self.func(instance)
            setattr(instance, self.attr_name, result)
        
        return getattr(instance, self.attr_name) 