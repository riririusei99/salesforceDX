from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('I can understand hi or HI!')
    # 絵文字のリアクション
    message.react('+1')

@respond_to('I love you')
def love(message):
    message.reply('I love you too!')

@listen_to('Can someone help me?')
def help(message):
    # メンションをつけてくれます
    message.reply('Yes, I can!')

    # チャンネルに向けて発言してくれます
    message.send('I can help everybody!')

    # スレッドで返信
    message.reply("Here's a threaded reply", in_thread=True)
