import getpass

forca = """
 ____
|   |
|   |
|   º
|
-----
"""
vazio = """

"""

cabeca = """
    O
"""
tronco = """
    O
    |
"""
braco_esquerdo = """
    O
   /|
"""
braco_direito = """
    O
   /|\\
"""
perna_esquerda = """
    O
   /|\\
   /
"""
perna_direita = """
    O
   /|\\
   / \\
"""

chances = [
vazio,
cabeca,
tronco,
braco_esquerdo,
braco_direito,
perna_esquerda,
perna_direita

]

print(f'{forca}bem vindo ao jogo da forca')

palavra = getpass.getpass('informe uma palavra: ').upper()

acertos = 0
erros = 0
letras_acert = ''
letras_errad = ''

print('_ ' *len(palavra))

while acertos != len(palavra) and erros != 6:
 mensagem = ''
 for letra in palavra:
  if letra in letras_acert:
   mensagem += f'{letra} '
  else:
   mensagem += '_ '
 print(mensagem)
 print(forca + chances[erros])

 letra = input('digite a letra: ').upper()

 if letra in palavra: 
  print('voce acertou a letra')
  letras_acert += letra
  acertos  += 1

 else:
  print('voce errou a letra ')
  letras_errad += letra
  erros += 1

print(palavra)
 
