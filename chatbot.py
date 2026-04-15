"""
Descrição do LetterBot:
Este programa em Python simula um chatbot interativo chamado LetterBot, que ajuda o usuário a escolher um filme com base no gênero desejado (ação, comédia ou terror). 
Ele apresenta três opções de filmes, permite ao usuário escolher uma delas e, em seguida, exibe a descrição (ou resenha) e, opcionalmente, a avaliação do filme.
O programa continua rodando até o usuário decidir sair. 

Instruções:
1-Certifique-se de ter o Python instalado no computador.
2-Copie e cole o código em um arquivo com extensão .py (por exemplo: chatbot_filmes.py).
3-Execute o arquivo em um terminal ou no ambiente de desenvolvimento (como VS Code, PyCharm ou IDLE).
4-Interaja com o chatbot digitando o gênero desejado, escolhendo um filme e respondendo às perguntas exibidas na tela.
"""

filmes = {
    "ação": [
        {"titulo": "Mad Max: Estrada da Fúria",
         "descricao": "Em um futuro pós-apocalíptico, uma mulher se rebela contra um tirano e foge com um grupo de prisioneiras em um caminhão de guerra.",
         "nota": "8.1"},
        {"titulo": "John Wick",
         "resenha": "Um ex-assassino de aluguel sai da aposentadoria para caçar os mafiosos que tiraram tudo o que ele tinha.",
         "nota": "7.4"},
        {"titulo": "Top Gun: Maverick",
         "descricao": "Após 30 anos de serviço, um dos melhores aviadores da Marinha treina um novo grupo de pilotos para uma missão perigosa.",
         "nota": "8.3"}
    ],
    "comédia": [
        {"titulo": "As Branquelas",
         "descricao": "Dois agentes do FBI se disfarçam de socialites loiras para investigar um plano de sequestro e proteger duas herdeiras.",
         "nota": "5.7"},
        {"titulo": "Se Beber, Não Case!",
         "descricao": "Três amigos acordam em Las Vegas após uma despedida de solteiro sem nenhuma memória da noite anterior e com o noivo desaparecido.",
         "nota": "7.7"},
        {"titulo": "Superbad",
         "descricao": "Dois adolescentes inseparáveis tentam comprar bebidas para uma festa de formatura, mas acabam se envolvendo em confusões épicas.",
         "nota": "7.6"}
    ],
    "terror": [
        {"titulo": "Invocação do Mal",
         "descricao": "Dois investigadores paranormais ajudam uma família que está sendo aterrorizada por uma presença sombria em sua nova fazenda.",
         "nota": "7.5"},
        {"titulo": "O Iluminado",
         "descricao": "Um homem aceita um emprego como zelador de um hotel isolado durante o inverno, onde forças sinistras começam a afetar sua sanidade.",
         "nota": "8.4"},
        {"titulo": "Hereditário",
         "descricao": "Após a morte da avó, uma família começa a descobrir segredos assustadores sobre seus ancestrais e tenta escapar de um destino trágico.",
         "nota": "7.3"}
    ]
}

print("Olá! Que alegria te ver por aqui!")
print("Eu sou seu amigo LetterBot e vou te ajudar a escolher um filme incrível.")

while True:
    print("\nOs gêneros que eu conheço são: ação, comédia e terror.")
    genero = input("Qual desses você prefere hoje? (ou digite 'sair'): ").lower().strip()

    if genero == "sair":
        print("\nAh, que pena que você já vai! Mas espero que seu filme seja ótimo. Até logo!")
        break

    if genero in filmes:
        print(f"\nOba! É uma ótima escolha! Aqui estão 3 opções para você:")

        for i, filme in enumerate(filmes[genero], 1):
            print(f"{i}. {filme['titulo']}")

        escolha = input("\nQual desses te chamou mais atenção? Digite o número (1, 2 ou 3): ")

        if escolha in ["1", "2", "3"]:
            f = filmes[genero][int(escolha) - 1]
            print(f"\nÓtima escolha boboca!'{f['titulo']}':")
            print(f"Descrição: {f.get('descricao', f.get('resenha'))}")

            quermais = input("\nVocê quer saber a avaliação do filme? (sim/não): ").lower()
            if quermais == "sim" or quermais == "s":
                print(f"Avaliação do povo: {f['nota']}/10")

            print("\nEspero que você goste! Quer ver mais algum?")
        else:
            print("\nOps! Não entendi esse número. Vamos tentar de novo?")
    else:
        print("\n Gênero inválido boboca, tente novamente!")