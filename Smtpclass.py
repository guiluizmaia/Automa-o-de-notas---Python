from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib
import os


mensagem = MIMEMultipart()
mensagem['De'] = "guilhermemaia201450@gmail.com"
senha = "113311gm"
caminho = os.listdir('./Email')
for cam in caminho:
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