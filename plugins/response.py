from slackbot.bot import respond_to
from slackbot.bot import default_reply

import pya3rt
import jaconv
import wikipedia

@respond_to('ジーク')
def zeon(message):
    message.reply('ジオン！！')

@respond_to('(.*)について知りたい件')
def searchWiki(message, something):
    response_string = ''
    wikipedia.set_lang('ja')
    try:
        wiki_page = wikipedia.page(something)
        message.reply('なるほど、{0}についてですね。'.format(something))
        message.reply(wiki_page.url)
    except wikipedia.exceptions.DisambiguationError  as e:
        message.reply('エラー、wikiの結果が上手く返ってきませんでした。')

@default_reply()
def talkA3rt(message):
    apikey = ''
    client = pya3rt.TalkClient(apikey)
    api_response = client.talk(message.body['text'])
    # レスポンスがokの時返事を返す
    if api_response['message'] == 'ok':
        reply_message = api_response['results'][0]['reply']
        message.reply(jaconv.hira2kata(reply_message) + '…ロボ')
        # 普通の返事
        # message.reply(reply_message)
    # APIエラーの時はmessageを返す
    else:
        message.reply('エラー、ウマク返事ガデキマセン [ERROR:' + api_response['message'] + ']')
