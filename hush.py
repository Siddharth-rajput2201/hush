rom chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')

conv = open('/home/sidd/jupyter note/chats','r').readlines()
print(conv)

trainer = ListTrainer(bot)
trainer.train(conv)
#bot.set_trainer(ListTrainer)

while True :
    request = input('YOU : ')
    response = bot.get_response(request)
    
    print('HUSH : ',response)

