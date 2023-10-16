import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} Para adotar um de nossos doguinhos basta filtrar por cães no Menu de busca avançada e escolher seu mais novo amiguinho, lá você também pode filtrar por características do animal.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} Para adotar um de nossos gatinhos basta filtrar por gatos no Menu de busca avançada e escolher seu mais novo amiguinho, lá você também pode filtrar por características do animal.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, Os principais cuidados com um animal de estimação (pet) variam dependendo da espécie, raça, idade e necessidades individuais do animal. No entanto, existem algumas práticas gerais que se aplicam à maioria dos pets. Aqui estão os principais cuidados a serem considerados. Alimentação - Ofereça uma dieta adequada ao tipo, idade e tamanho do seu pet. Consulte um veterinário para obter orientação sobre o melhor alimento e a quantidade apropriada. Água - Certifique-se de que seu pet tenha acesso a água fresca o tempo todo. Abrigo - Proporcione um local seguro e confortável para seu pet, seja uma casinha, um aquário, uma gaiola ou um viveiro, dependendo do tipo de animal. Higiene - Mantenha seu pet limpo, incluindo banhos regulares, escovação, corte de unhas e cuidados com a higiene bucal, conforme necessário. Exercício - Forneça exercícios e estimulação mental adequados para o seu pet. Cada espécie tem necessidades diferentes em termos de atividade física e mental. Saúde - Leve seu pet ao veterinário regularmente para check-ups, vacinações e prevenção de parasitas. Esteja atento a sinais de doença e lesões. Socialização - Se seu pet é sociável, permita que ele interaja com outros animais e pessoas de forma adequada. Treinamento - Invista tempo em treinar seu pet para comportamentos adequados e obediência básica. O treinamento é importante para a segurança e o bem-estar do animal. Estimulação mental - Forneça brinquedos e atividades que desafiem a mente do seu pet. Isso é especialmente importante para pets inteligentes e ativos. Identificação - Certifique-se de que seu pet tenha uma forma de identificação, como uma coleira com etiqueta de identificação ou um microchip. Castração - Considere a esterilização/castração do seu pet, a menos que você tenha planos específicos de reprodução. Segurança - Mantenha seu pet seguro, impedindo o acesso a substâncias tóxicas, mantendo-o dentro de áreas seguras e protegendo-o de perigos. Amor e atenção - Dê ao seu pet amor e carinho. A interação social e o afeto são fundamentais para o bem-estar emocional do animal. Planejamento a longo prazo - Lembre-se de que a adoção de um pet é um compromisso de longo prazo. Esteja preparado para cuidar do seu animal durante toda a vida dele. Lembre-se de que as necessidades individuais do seu pet podem variar com base na espécie, raça e personalidade. Portanto, é importante conhecer bem o seu pet e consultar um veterinário ou um especialista em animais de estimação para obter orientações específicas..{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome} para um melhor passeio com seu pet, vale seguir algumas dicas, como usar sempre a guia de passeio, se atentar aos horários por causa do sol, levar água, petiscos e a sacolinha para recolher o cocô do seu pet. Planejar o passeio é uma boa pedida para não haver surpresas, além de existir a possibilidade de combinar passeio com exercício físico. Para uma maior diversão do seu filhote de quatro patas deixe-o interagir e brincar com outros pets. Bom passeio!{os.linesep}')
    else:
        print('Digite apenas 1, 2, 3 ou 4')


def start():
    # Apresentar o Adotebot
    print('Olá, bem-vindo ao Adotebot')
    # Pedir o nome
    nome = input('Digite seu nome:')
    # Pedir o email
    email = input('Digite seu email:')
    while True:
        # Oferecer o menu de opções
        resposta = input(f'Como podemos te ajudar hoje?{os.linesep} [1] - Adoção de cães{os.linesep} [2] - Adoção de gatos{os.linesep} [3] - Cuidados com o pet{os.linesep} [4] - Dicas de passeios{os.linesep}')
        # Processar a resposta enviada
        processar_resposta(resposta, nome)

if __name__ == '__main__':
    start()