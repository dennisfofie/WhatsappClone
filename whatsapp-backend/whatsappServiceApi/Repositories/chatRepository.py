from datetime import datetime, timezone

from whatsappServiceApi.models import (Message, Room , User)

class ChatRepository:
    
    MESSAGE_MODEL = Message
    ROOM_MODEL = Room
    USER_MODEL = User

    def __init__(self) -> None:
        pass

    def GetAllMessages(self):
        context = self.MESSAGE_MODEL.objects.all().order_by('created')

        if context is None:
            return None
        
        return context
    
    def GetMessage(self, id):
        if id is None:
            return None
        
        context = self.MESSAGE_MODEL.objects.get(id=id)

        return context if not None else None
    
    def CreateMessage(self, message, toUser, fromUser):
        if not isinstance(message, self.MESSAGE_MODEL):
            return None
        
        context = self.MESSAGE_MODEL.objects.create(
            toUser = toUser,
            fromUser = fromUser,
            chats = message.chats,
            audio = message.audio,
            image = message.image,
            status = message.status,
            createdBy = 'Message.Service',
            ModifiedBy = "Message.Service",
            created = datetime.now(timezone.utc),
            modified = datetime.now(timezone.utc)
        )

        return context if not None else None

    def removeMessage(self, id):
        if id is None:
            return None
        
        context = self.MESSAGE_MODEL.objects.get(id = id)

        if context is None:
            return None
        
        context.delete()

        return "Message deleted"
    
    def createRoom(self, user, room):
        if not isinstance(room , self.ROOM_MODEL):
            return None
        
        context = self.__getModel__(self.ROOM_MODEL)

        record = context.objects.create(
            roomName = room.roomName,
            creator = user,
            users = user,
            icon = room.icon,
            created = datetime.now(timezone.utc),
            modified = datetime.now(timezone.utc),
            modifiedBy = 'Room.Service'
        )
        
        return record if not None else None
    
    def GetRoom(self, roomId):
        if roomId is None:
            return None
        
        record = self.__getModel__(self.ROOM_MODEL).objects.get(pk = roomId)

        return record if not None else None
    
    def UpdateRoom(self, roomId, room):
        if roomId is None:
            return None
        
        if not isinstance(room ,self.ROOM_MODEL):
            return None
        
        context = self.__getModel__(self.ROOM_MODEL)

        record = context.objects.get(pk=roomId)

        if record is None:
            return None
        
        record.roomName = room.roomName
        record.icon = room.icon
        room.modified = datetime.now(timezone.utc)

        record.save()

        return record
    
    def DeleteRoom(self, roomId):
        if roomId is None:
            return None
        
        context =self.__getModel__(self.ROOM_MODEL)

        record = context.objects.get(pk=roomId)

        if record is None:
            return None
        
        record.delete()

        return "room sucessfully deleted"
    

        

    

    def __getModel__(self, model=None):
        if model is None or model == "":
            return None
        return model
    