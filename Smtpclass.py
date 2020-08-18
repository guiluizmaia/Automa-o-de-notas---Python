#Importações necessárias para o envio
from email.mine.multipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.mime.text import MIMEText
import smtplib

#criar um objeto para instanciar
mensagem = MIMEMultipart()

#Parâmetros de envio
password = "sua senha"
mensagem['From'] = "seu email"
mensagem['To'] = "email a enviar"
mensagem['Subject'] = "tema"

# anexando a imagem a mensagem
mensagem.attach(MIMEImage(file("coloca o arquivo").read()))

#Cria o servidor, usando o smtp do email
#Nesse caso é do gmail
servidor = smtplib.SMTP('smtp.gmail.com: 587')
servidor.starttls()