# This is a sample Python script.
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import settings
import logging.config
from log_config import LOG_CONFIG
import handlers

logging.config.dictConfig(LOG_CONFIG)
log = logging.getLogger('bot')


class UserState:
    """Состояние пользователя внутри сценария. """

    def __init__(self, scenario_name, step_name, context=None):
        self.scenario_name = scenario_name
        self.step_name = step_name
        self.context = context or {}


class Bot:
    """
    Vk Bot
    use python 3.9
    Поддерживает ответы на вопросы про дату и место проведения и сценарий регистрации:
    - спрашиваем имя
    - спрашиваем email
    - говорим об успешной регистрации
    Если шаг не пройден, задаем уточняющий вопрос пока шаг не будет пройден.
    """

    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=self.token)
        self.long_poller = VkBotLongPoll(group_id=self.group_id, vk=self.vk)
        self.api = self.vk.get_api()
        self.user_states = dict()  # user_id

    def run(self):
        for event in self.long_poller.listen():
            print(event)
            log.debug(f"Получено сообщение")
            try:
                self.on_event(event)
            except Exception:
                log.exception('ошибка в обработке событий')

    def on_event(self, event):
        print(event)
        if event.type != VkBotEventType.MESSAGE_NEW:
            log.info(f'Мы пока не умеем обрабатывать такие сообщения')
            return

        user_id = event.object['message']['peer_id']  # event.object['message']['peer_id']#event.object.message.peer_id
        text = event.object['message']['text']  # event.object['message']['text']#event.object.message.text
        if user_id in self.user_states:
            text_to_send = self.continue_scenario(user_id=user_id, text=text)

        else:
            for intent in settings.INTENTS:
                log.debug(f'User gest {intent}')
                if any(token in text.lower() for token in intent['tokens']):
                    if intent['answer']:
                        text_to_send = intent['answer']
                    else:
                        self.start_scenario(user_id, intent['scenario'])
                    break
            else:
                text_to_send = settings.DEFAULT_ANSWER
        self.api.messages.send(message=text_to_send,  # event.object['message']['text']
                               peer_id=user_id,  # event.object['message']['peer_id']
                               random_id=random.randint(0, 2 ** 20))

    def start_scenario(self, user_id, scenario_name):
        scenario = settings.SCENARIOS[scenario_name]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        text_to_send = step['text']
        self.user_states[user_id] = UserState(scenario_name=scenario_name, step_name=first_step)
        return text_to_send

    def continue_scenario(self, user_id, text):
        state = self.user_states[user_id]
        steps = settings.SCENARIOS[state.scenario_name]['steps']
        step = steps[state.step_name]

        handler = getattr(handlers, step['handler'])
        if handler(text=text, context=state.context):
            next_step = steps[step['next_step']]
            text_to_send = next_step['text'].format(**state.context)
            if next_step['next_step']:
                state.step_name = step['next_step']
            else:
                log.info('Зарегистрирован: {name} {email}'.format(**state.context))
                self.user_states.pop(user_id)

        else:
            text_to_send = step['failure_text'].format(**state.context)

        return text_to_send


if __name__ == '__main__':
    bot = Bot(group_id=settings.GROUP_ID
              , token=settings.TOKEN)
    bot.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
