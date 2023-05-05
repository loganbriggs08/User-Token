from helpers.encoding import Encode

class UserToken:
    def generate(user_id: int) -> str:
        encoded_user_id = Encode.string(str(user_id))
        print(encoded_user_id)
        
if __name__ == '__main__':
    UserToken.generate(80088516616269824)