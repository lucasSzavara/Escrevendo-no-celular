class Frase():

    def __init__(self, texto):
        self.texto = texto.lower()
        self.letras_de_cada_numero = {
            '0': [' '] ,
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        self.sequencias_numericas = {}

        # Transforma as letras na sequencia numerica que deve ser pressionada
        for key, item in self.letras_de_cada_numero.items():
            for i in range(len(item)):
                numero = (i + 1) * key
                self.sequencias_numericas[item[i]] = numero
    

    def transformar_para_numero(self):
        sequencia = ''
        for letra in self.texto:
            if letra in self.sequencias_numericas:
                if len(sequencia) != 0 and self.sequencias_numericas[letra][0] == sequencia[-1]:
                    sequencia += '_'

                codigo = self.sequencias_numericas[letra]
                sequencia += codigo
            else:
                print('A letra {} nao pode ser usada'.format(letra))
                break
        return sequencia