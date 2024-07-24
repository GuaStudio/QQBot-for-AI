import botpy
import requests
from botpy.message import GroupMessage

class MyClient(botpy.Client):
    async def on_group_at_message_create(self, message: GroupMessage):
        response = requests.post(url='http://这里填入你的AI域名或IP/v1/chat/completions', headers={"Content-Type": "application/json","Authorization": "Bearer 这里填入你的AIKey"}, json={"model": "glm4","messages": [{"role": "user","content": message.content}]}).json()
        await message.reply(content=f"{response["choices"][0]["message"]["content"]}")

if __name__ == "__main__":
    intents = botpy.Intents(public_messages=True)
    client = MyClient(intents=intents)
    client.run(appid="这里填入你的机器人APPID", secret="这里填入你的机器人APPSecret")
