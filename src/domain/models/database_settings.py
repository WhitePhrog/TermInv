from dataclasses import dataclass


@dataclass
class DatabaseSettings:
    user: str
    host: str
    password: str
    port: int
    database: str