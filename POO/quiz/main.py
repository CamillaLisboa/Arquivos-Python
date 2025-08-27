from question_model import Question
from data import dados_pergunta
from quiz_brain import QUiz_funcoes

banco_questoes = []

for questao in dados_pergunta:
    texto_questão = questao['question']
    resposta_questao = questao['correct_answer']
    nova_questao = Question(texto_questão, resposta_questao)
    banco_questoes.append(nova_questao)

quiz = QUiz_funcoes(banco_questoes)
while quiz.aind_tem_questoes():
    quiz.proxima_questao()

print('Voce terminou o quiz!')
print(f'Sua pontuação foi: {quiz.pontos}/{quiz.numero_questao}')