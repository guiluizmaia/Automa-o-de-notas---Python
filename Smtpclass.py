from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib
import os
import configparser

config = configparser.ConfigParser()
config.read('./arquivos/Config.ini')



senha = config.get('smtp', 'senha')
caminho = os.listdir('./Email')

for cam in caminho:
    try:
        mensagem = MIMEMultipart()
        mensagem['De'] = config.get('smtp', 'de')
        img = f'./Email/{cam}'
    
        fp = open(img, 'rb')
        mensagem.attach(MIMEImage(fp.read()))
        fp.close()
    
        para = cam[:-4]
        mensagem['Para'] = f"{para}.com"
    
        servidor = smtplib.SMTP('smtp.gmail.com: 587')
    
        servidor.starttls()

        servidor.login(mensagem['De'], senha)

        servidor.sendmail(mensagem['De'], mensagem['Para'], mensagem.as_string())

        
        servidor.quit()
        del mensagem
        print(f"{para}.com enviado")
    except:
        print(f"Email invalido: {para}.com")
        del mensagem
