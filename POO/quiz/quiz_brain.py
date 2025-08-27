class QUiz_funcoes:
    def __init__(self,q_list):
        self.numero_questao = 0
        self.pontos = 0
        self.lista_questoes = q_list

    def aind_tem_questoes(self):
        return self.numero_questao < len(self.lista_questoes)
    
    def proxima_questao(self):
        questao_atual = self.lista_questoes[self.numero_questao]
        self.numero_questao +=1
        user_answer = input(f'Q.{self.numero_questao}: {questao_atual.texto} (Verdadeiro/Falso): ')
        self.checa_resposta (user_answer, questao_atual.resposta)

    def checa_resposta(self, resposta_usuario, resposta_correta):
        if resposta_usuario.lower() == resposta_correta.lower():
            self.pontos +=1
            print("Acertou!")
        else:
            print("Está errado.")
            print(f'A resposta correta era: {resposta_correta}.')

        print(f'Sua pontuação atual é: {self.pontos}/{self.numero_questao}')
        print("\n")

        