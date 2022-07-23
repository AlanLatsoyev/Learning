# This is a sample Python script.
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import settings


class Bot:
    """
    Vk Bot
    use python 3.9
    """
    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=self.token)
        self.long_poller = VkBotLongPoll(group_id=self.group_id, vk=self.vk)
        self.api = self.vk.get_api()

    def run(self):
        for event in self.long_poller.listen():
            print("получено событие")
            try:
                self.on_event(event)
            except Exception as exc:
                print(exc)


    def on_event(self, event):
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event.object['message']['text'])
            print(event.object)
            self.api.messages.send(message=event.object['message']['text'],
                                   peer_id=event.object['message']['peer_id'],
                                   random_id=random.randint(0, 2**20))
        else:
            print(event.type)



if __name__ == '__main__':
    bot = Bot(group_id=settings.GROUP_ID
              , token=settings.TOKEN)
    bot.run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
