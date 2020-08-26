AUTOMAÇÃO DAS NOTAS PYTHON
.Primeiro de tudo vou falar o motivo desse projeto
	.Na faculdade estamos aprendendo java e c++, mas curioso como todo programador é fui atrás dessa linguagem que todo mundo fala, e descobri o quão maravilhosa ela é. Basicamente existe biblioteca sobre tudo em Python!!!
	.Isso só me deu mais vontade ainda de aprende-la, e pensei em um projeto relativamente ousado para alguém que não conhece muito sobre a linguagem. Bom vamos explicar do que se trata o projeto
  
  
  .O projeto funcionará de tal forma:
		.O professor (nosso cliente fictício), criará um Google Forms pedindo ao aluno o nome completo, e-mail, a atividade que ele estará enviando e o arquivo da atividade. Com tudo isso ele irá criar uma planilha com os resultados (o Google Forms faz isso automaticamente), o nosso código feito em Python irá pegar os dados da tabela, fazer uma média da nota, baseada nos envios e verificar se o aluno passou ou não. Após isso ele colocará o nome do aluno em uma imagem de um certificado (com o resultado "PASSOU" ou "NÃO PASSOU") e enviará por e-mail para ele.
    

    .Bem legal, não é mesmo? Agora que já tinha o algoritmo fui em busca das biblioteca que podiam me auxiliar, ai estão elas:
		- Openpyxl - Para importarmos e manipularmos as tabelas 
		- Pill - Para colocar o nome do aluno na imagem
		- Simple Mail Transfer Protocol (SMTP) - Para enviarmos para o e-mail do aluno
	.PS: Trarei toda a documentação dessas bibliotecas traduzidas para o blog
  
  
  O projeto está com todas as funcionalidades propostas no início completa, porem agora pretendo colocar um arquivo de configuração .ini para facilitar o acesso do usuário
  link do meu blog: https://www.programadoruniversitario.com.br/
