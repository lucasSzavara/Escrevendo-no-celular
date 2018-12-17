from Frase import Frase

texto = str(input('Digite o texto: '))

# Verificar o tamanho maximo da frase
if len(texto) > 255:
    texto = texto[:256]

frase = Frase(texto)
print('Para escrever {} voce deve digitar: \n{}'.format(texto, frase.transformar_para_numero()))
