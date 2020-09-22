import random

lottery_tickets_list = []
print("creating 100 random lottery tickets")
for i in range(100):
    lottery_tickets_list.append(random.randrange(1000000000, 9999999999))

valid = True
lottery_tickets_list.sort()
for i in range(len(lottery_tickets_list)):
	if i < len(lottery_tickets_list) - 1 and lottery_tickets_list[i] == lottery_tickets_list[i+1]:
		print("invalid list")
		valid = False
		break
if valid == True:
    winners = random.choice(lottery_tickets_list)
    print("Lucky lottery ticket is", winners)
else:
	  print("Please try it again.")
