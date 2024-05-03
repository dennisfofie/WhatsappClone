from whatsappServiceApi.Repositories.userRepository import UserRepository

from whatsappServiceApi.models import User, ResetPassword

class UserDatabaseService:
    repo = None

    def __init__(self) -> None:
        self.repo = UserRepository()

    def CreateUser(self, model:User):
        return self.repo.CreateUser(modelInstance=model)
    
    def GetUser(self, userId:User.userId):
        return self.repo.GetUser(userId=userId)
    
    def GetAllUser(self, searchTerm):
        return self.repo.GetAllUsers(searchTerm=searchTerm)
    
    def Activate(self, user:User.userId):
        return self.repo.ActivateUser(userId=user)
    
    def Deactivate(self, user:User.userId):
        return self.repo.DeactivateUser(userId=user)
    
    def ChangePic(self, user, model):
        return self.repo.ChangeProfilePic(user, model)
    
    def UpdateUserInfo(self, user, model):
        return self.repo.UpdateUserProfile(user, model)
    
    def ResetPassword(self, user:User, reset:ResetPassword):
        return self.repo.ResetPassword(user, reset)
    