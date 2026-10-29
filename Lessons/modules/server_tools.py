# =============================================================================
# Module used in Lesson 03 - server_tools
# -----------------------------------------------------------------------------
# A module is just a .py file. Every function and variable defined here can
# be imported and used by other files (see 03-functions-and-modules.py).
# =============================================================================


# A module-level variable - can be imported just like a function
DEFAULT_PORT = 8080


def check_server(name):
    """Return a status message for a server."""
    return f"{name} is online"


def build_address(host, port=DEFAULT_PORT):
    """Combine a host and port into an address, e.g. 'server01:8080'."""
    return f"{host}:{port}"
