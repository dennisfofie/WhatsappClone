from whatsappServiceApi.models import User
from whatsappServiceApi.models import ResetPassword
from datetime import datetime, timezone
from django.db.models import Q

class UserRepository:
    USER_MODEL = User
    RESET_PASSWORD = ResetPassword

    def CreateUser(self, modelInstance: User):
        if not isinstance(modelInstance, User):
            return 'The model must be instance of User'
        
        model = self.__getModel__(self.USER_MODEL)

        context = model.objects.create(
            email = modelInstance.email,
            fullName = modelInstance.fullName,
            password = modelInstance.password,
            created = datetime.now(timezone.utc),
            modified = datetime.now(timezone.utc),
            createdBy = 'user.service',
            modifiedBy = 'user.service'
        )
        print(context)

        if context is None:
            return None
        
        return context
    
    def GetUser(self, userId):
        if userId is None:
            return "The userId must be specified and not None"
        
        context = self.__getModel__(self.USER_MODEL)
        record = context.objects.get(pk=userId)

        if record is None:
            return None
        
        return record
    
    def GetAllUsers(self, searchTerm=None):
        context = self.__getModel__(self.USER_MODEL)
        records = None

        if searchTerm is None:
            records = context.objects.all()
        else:
            records = context.objects.filter(
                Q(email__icontains=searchTerm)|
                Q(fullName__icontains=searchTerm)
            )
        
        if records is None:
            return None
        
        return records
    
    def ActivateUser(self, userId):
        if userId is None:
            return "userId must be specified and not None"
        
        context = self.__getModel__(self.USER_MODEL)

        record = context.objects.get(pk=userId)

        if record is None:
            return None
        
        record.active = True
        record.modified = datetime.now(timezone.utc)
        record.save()

        return record
    
    def DeactivateUser(self, userId):
        if userId is None:
            return "userId must be specified and not None"
        
        context = self.__getModel__(self.USER_MODEL)

        record = context.objects.get(pk=userId)

        if record is None:
            return None
        
        record.active = False
        record.modified = datetime.now(timezone.utc)
        record.save()

        return record
    
    def ChangeProfilePic(self, userId, modelInstance):
        if userId is None:
            return "The userId must be specified and not None"
        
        context = self.__getModel__(self.USER_MODEL)

        if not isinstance(modelInstance, self.USER_MODEL):
            return "The model must be instance of user"
        
        record = context.objects.get(pk=userId)

        if record is None:
            return record
        
        record.profilePic = modelInstance
        record.modified = datetime.now(timezone.utc)
        record.save()

        return record
    
    def UpdateUserProfile(self, userId, modelInstance):
        if userId is None:
            return "The userId must be specified and not None"
        
        context = self.__getModel__(self.USER_MODEL)

        if not isinstance(modelInstance, self.USER_MODEL):
            return "The model must be instance of user"
        
        record = context.objects.get(pk=userId)

        if record is None:
            return None
        
        record.fullName = modelInstance.fullName
        record.profilePic = modelInstance.profilePic
        record.save()

        return record
    
    def ResetPassword(self, modelInstance, resetModel):
        if modelInstance.id is None:
            return None

        resetContext = self.__getModel__(self.RESET_PASSWORD)
        
        reset = resetContext.objects.create(
            resetUser = modelInstance,
            oldPassword = resetModel.oldPassword,
            newPassword = resetModel.newPassword,
            confirmPassword = resetModel.confirmPassword,
            created = datetime.now(timezone.utc),
            modified = datetime.now(timezone.utc),
            modifiedBy = 'user.service',
        )

        if reset is None:
            return None
        
        return "User password has been updated successfully"

    def GetUserByEmail(self, email):
        if email is None:
            return None
        
        context = self.__getModel__(self.USER_MODEL)

        record = context.objects.get(email = email)

        if record is None:
            return None
        
        return record


    def __getModel__(self, model = ''):
        if model is None or model == '':
            return None
        
        return model