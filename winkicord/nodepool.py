# winkicord/nodepool.py

from typing import Optional, Dict

class NodePoolCreds:
    _creds: Optional[Dict[str, any]] = None

    @classmethod
    async def set_creds(
        cls, 
        identifier: str, 
        host: str, 
        port: int, 
        password: str, 
        inactive_timeout: Optional[int] = 14000, 
        cache: Optional[int] = 100) -> None:
        """
        Sets the node pool credentials with validation on port, timeout, and cache.
        
        Parameters:
        - identifier (str): The identifier for the node.
        - host (str): The host of the server.
        - port (int): The port of the server.
        - password (str): The password for the node connection.
        - inactive_timeout (Optional[int]): Timeout value for inactive connections.
        - cache (Optional[int]): Cache size, default is 100.
        
        Raises:
        - ValueError: If any of the parameters are out of the expected range.
        """
        
        if not (1 <= port <= 65535):
            raise ValueError("Port must be between 1 and 65535.")

        if inactive_timeout is not None and inactive_timeout <= 0:
            raise ValueError("Inactive timeout must be a positive integer.")

        if cache is not None and cache <= 0:
            raise ValueError("Cache size must be a positive integer.")
        
        cls._creds = {
            "identifier": identifier,
            "host": host,
            "port": port,
            "password": password,
            "inactive_timeout": inactive_timeout,
            "cache": cache
        }

    @classmethod
    async def get_creds(cls) -> Dict[str, any]:
        """
        Returns the stored node pool credentials.
        
        Raises:
        - ValueError: If credentials are not set.
        
        Returns:
        - Dict[str, any]: A dictionary containing node credentials.
        """
        if cls._creds is None:
            raise ValueError("NodePool credentials not set.")
        return cls._creds
