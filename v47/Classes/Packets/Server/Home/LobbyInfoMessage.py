from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
import time
import psutil


class LobbyInfoMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVInt(ClientsManager.GetCount())
        self.writeString("██████████████████████\nProject DBS \nCreator: Danil DEV\nCoder: Danil DEV\n{time.asctime()}\nRAM: {psutil.virtual_memory().percent}%\nCPU: {psutil.cpu_percent()}%\n"f"Version: {player.ClientVersion}\n██████████████████████\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\Ping:32ms\n\n\n\n\n\n\n\n\nn\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        self.writeVInt(0)

    def decode(self):
        fields = {}
        fields["PlayerCount"] = self.readVInt()
        fields["Text"] = self.readString()
        fields["Unk1"] = self.readVInt()
        super().decode(fields)
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 23457

    def getMessageVersion(self):
        return self.messageVersion
