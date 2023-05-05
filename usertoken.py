from helpers.time import Time
from helpers.random import Random
from helpers.encoding import Encode

class UserToken:
    def generate(user_id: int) -> str:    
        return f"{Encode.string(str(user_id))}.{Encode.string(str(Time.seconds_since_epoch(2023, 1, 6)))}.{Encode.string(Random.string())}"