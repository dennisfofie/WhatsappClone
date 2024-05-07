from whatsappServiceApi.models import Room, Message

from whatsappServiceApi.Repositories.chatRepository import ChatRepository

class MessageDatabaseService:
    
    def __init__(self) -> None:
        self.repo = ChatRepository()

    def GetAllMessages(self):
        return self.repo.GetAllMessages()
    
    def GetMessage(self, id):
        return self.repo.GetMessage(id)
    
    def CreateMessage(self, message:Message, toUser, fromUser):
        return self.repo.CreateMessage(message, toUser, fromUser)
    
    def removeMessage(self, id):
        return self.repo.removeMessage(id)
    
    def createRoom(self, user, room):
        return self.repo.createRoom(user, room)
    
    def GetRoom(self, roomId):
        return self.repo.GetRoom(roomId)
    
    def UpdateRoom(self, roomId, room:Room):
        return self.repo.UpdateRoom(roomId, room)
    
    def DeleteRoom(self, roomId):
        return self.repo.DeleteRoom(roomId)
    
