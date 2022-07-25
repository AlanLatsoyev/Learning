import unittest
from unittest.mock import Mock, patch, ANY

from vk_api.bot_longpoll import VkBotMessageEvent

from vk_bot import Bot


class MyTestCase(unittest.TestCase):
    RAW_EVENT = {'group_id': 214555043,
                 'type': 'message_new',
                 'event_id': '020e72e909d71a5ee4be636a365b7d818dfa9c22',
                 'v': '5.131',
                 'object': {'message':
                                {'date': 1658755276, 'from_id': 372180020, 'id': 0, 'out': 0,
                                 'attachments': [], 'conversation_message_id': 61, 'fwd_messages': [],
                                 'important': False, 'is_hidden': False, 'peer_id': 2000000001, 'random_id': 0,
                                 'text': 'wewe'},
                            'client_info': {'button_actions':
                                                ['text', 'vkpay', 'open_app', 'location', 'open_link', 'callback',
                                                 'intent_subscribe', 'intent_unsubscribe'],
                                            'keyboard': True, 'inline_keyboard': True, 'carousel': True, 'lang_id': 0}}}
    def test_run(self):
        count = 5
        obj = {'a': 1}
        events = [obj] * count
        long_poller_mock = Mock(return_value=events)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock

        with patch('vk_bot.vk_api.VkApi'):
            with patch('vk_bot.VkBotLongPoll', return_value=long_poller_listen_mock):
                bot = Bot('', '')
                bot.on_event = Mock()
                bot.run()

                bot.on_event.assert_called()
                bot.on_event.assert_any_call(obj)
                assert bot.on_event.call_count == count

    def test_on_event(self):
        event = VkBotMessageEvent(raw=self.RAW_EVENT)
        send_mock = Mock()
        with patch('vk_bot.vk_api.VkApi'):
            with patch('vk_bot.VkBotLongPoll'):
                bot = Bot('', '')
                bot.api = Mock()
                bot.api.messages.send = send_mock

                bot.on_event(event)

        send_mock.assert_called_once_with(
            message=self.RAW_EVENT['object']['message']['text'],
            peer_id=self.RAW_EVENT['object']['message']['peer_id'],
            random_id=ANY

        )


if __name__ == '__main__':
    unittest.main()
