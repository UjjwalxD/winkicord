from typing import Optional, Dict, Any

async def NodePoolCreds(
    identifier:str,
    host: str,
    port: int,
    password: str,
    inactive_timeout: Optional[int] = None,
    cache: Optional[int] = None
) -> Dict[str, Any]:
    """
    Creates a connection to the server and returns a dictionary containing the node pool credentials.
    
    Parameters:
        identifier (str): The identifier for the node pool.
        host (str): The host of the server.
        port (int): The port of the server.
        password (str): The password for the connection.
        inactive_timeout (Optional[int]): Timeout for inactive connections.
        cache (Optional[int]): Cache size. Defaults to 100 if None.

    Returns:
        Dict[str, Any]: A dictionary containing the node pool credentials.
    """
    if cache is None:
        cache = 100

    return {
        "identifier": identifier,
        "host": host,
        "port": port,
        "password": password,
        "inactive_timeout": inactive_timeout,
        "cache": cache
    }