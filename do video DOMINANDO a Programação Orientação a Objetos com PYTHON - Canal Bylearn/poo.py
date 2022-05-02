class Caneca:
    logo = ''
    cor = ''
    nome = ''
    
    def beber(self):
        print('Estou bebendo da caneca', self.nome)
    
caneca1 = Caneca()
caneca1.nome = 'Teste'
caneca1.logo = 'Logo'
caneca1.cor = 'Verde'

print(caneca1.nome, caneca1.logo, caneca1.cor)
caneca1.beber()

Caneca.logo = 'Padrão'

caneca2 = Caneca()
print(caneca2.logo)