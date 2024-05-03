from rest_framework_simplejwt.tokens import RefreshToken

def generate_tokens(user):
    refresh = RefreshToken.for_user(user)
    print(user.active)
    print("within the tokens")
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }