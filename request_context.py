from dataclasses import dataclass
from enum import StrEnum

from flask import g


class Version(StrEnum):
    A = "a"  # basic
    # B = "b"  # enhanced - When ready

@dataclass
class RequestContext:
    version: Version = Version.A
    update_cookie: bool = False
    utm_source: str = ""

def set_context(version: Version, update_cookie: bool = False, utm_source: str = "") -> None:
    g._context = RequestContext(version=version, update_cookie=update_cookie, utm_source=utm_source)

def get_context() -> RequestContext:
    if not hasattr(g, '_context'):
        g._context = RequestContext()
    return g._context