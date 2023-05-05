from helpers.encoding import Encode

class UserToken:
    def generate(user_id: int) -> str:
        token_structure: str = f""
        
        token_structure += f"{Encode.string(str(user_id))}."
        print(token_structure)
        
if __name__ == '__main__':
    UserToken.generate(80088516616269824)