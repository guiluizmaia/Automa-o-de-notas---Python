import Openpyxls
from PIL import Image, ImageDraw, ImageFont

#Instanciar a fonte ultilizada num objeto e o tamanho 
Font1 = ImageFont.truetype("./arquivos/FonteBase.ttf", size=40)

#Um for para andar em todos os itens da lista da classe Openpyxls
for i in range(0, len(Openpyxls.pronto)):
    #Coloquei a imagem que vou usar em um objeto do tipo image
    imagem = Image.open("./arquivos/ImagemBase.png").convert("RGBA")

    #Criar um objeto para escrever na imagem
    Escr = ImageDraw.Draw(imagem)
    
    #Comparo se o aluno passou, a NotaMedia é estipulada pelo usuário
    #Se a pessoa não passou
    if (Openpyxls.pronto[i][0][3] <= Openpyxls.NotaMedia):
            #Chamo a função text do objeto que escreve na tela
            Escr.text(
                #Posição que o texto vai aparecer
                (250, 305),
                #Texto(é o nome do aluno)
                text=f"{Openpyxls.pronto[i][0][1]}",
                #Cor
                fill="#000",
                #Fonte
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
            #Coloco o email em uma variável
            var = Openpyxls.pronto[i][0][2]
            #Esse if é apenas para se o valor vir = a none e evitar erros
            if (var != None):
                #Tiro todos os espaços do email, para evitar erros
                var = var.strip()
                #Apago os 4 ultimos caracteres para apagar o ".com"
                #Pois se haver o ponto, teremos problemas na próxima etapa
                var = var[:-4]
                #E por fim salvo, com o valor do email
                imagem.save(f"./Email/{var}.png")    
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
        var = Openpyxls.pronto[i][0][2]
        if (var != None):
            var = var.strip()
            var = var[:-4]
            imagem.save(f"./Email/{var}.png")
               
             
