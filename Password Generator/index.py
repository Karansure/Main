import secrets
import pyperclip

uppercase="ABCDEFGHIKLMNOPQRSTUVXYZ"
lowercase='abcdefghiklmnopqrstuvwxyz'
number=1234567890
sp_charcters='@#$^&*'

total=uppercase+lowercase+str(number)+sp_charcters
input=int(input("enter a number :"))

tot="".join(secrets.choice(total) for x in range(input))
pyperclip.copy(tot)

print(tot)

