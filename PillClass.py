import Openpyxls
from PIL import Image, ImageDraw, ImageFont

#Instanciar a fonte ultilizada num objeto e o tamanho 
Font1 = ImageFont.truetype("./arquivos/FonteBase.ttf", size=40)
Font2 = ImageFont.truetype("./arquivos/FonteBase.ttf", size=25)


for i in range(0, len(Openpyxls.pronto)):
    #Coloquei a imagem que vou usar em um objeto do tipo image
    imagem = Image.open("./arquivos/ImagemBase.png").convert("RGBA")

    #Criar um objeto para escrever na imagem
    Escr = ImageDraw.Draw(imagem)
    
    if (Openpyxls.pronto[i][0][3] <= Openpyxls.NotaMedia):
            Escr.text(
                (250, 305),
                text=f"{Openpyxls.pronto[i][0][1]}",
                fill="#000",
                font=Font1
            )
            Escr.text(
                (250, 350),
                text="Voce reprovou",
                fill="#000",
                font=Font1
            )
            Escr.text(
                (250, 395),
                text=f"RA: {Openpyxls.pronto[i][0][0]}",
                fill="#000",
                font=Font1
            )
            Escr.text(
                (250, 445),
                text=f"Atividades enviadas: \n{Openpyxls.pronto[i][0][3]}",
                fill="#000",
                font=Font1
            )
            imagem.save(f"./Email/{Openpyxls.pronto[i][0][2]}.png")    
    else:
        Escr.text(
            (250, 305),
            text=f"PARABENS {Openpyxls.pronto[i][0][1]}",
            fill="#000",
            font=Font1
        )
        Escr.text(
            (250, 350),
            text="Voce passou",
            fill="#000",
            font=Font1
        )
        Escr.text(
            (250, 395),
            text=f"RA: {Openpyxls.pronto[i][0][0]}",
            fill="#000",
            font=Font1
        )
        Escr.text(
            (250, 445),
            text=f"Atividades enviadas: {Openpyxls.pronto[i][0][3]}",
            fill="#000",
            font=Font1
        )
        
        imagem.save(f"./Email/{Openpyxls.pronto[i][0][2]}.png")       
             
