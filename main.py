import getpass

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
   mensagem += letra + ' '
  else:
   mensagem += '_ '
 print(mensagem)
 print('voce ja errou: ' + letras_errad)

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
 
