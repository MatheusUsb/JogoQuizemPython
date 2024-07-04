class Quiz: 
    def __init__(self):
        self.questions = [
            {
                'question': 'Qual é o maior animal terrestre?',
                'options': ['Elefante', 'Rinoceronte', 'Girafa', 'Hipopótamo'],
                'answer': 'Elefante'
            },
            
            {
                'question': 'Qual é o maior peixe do oceano?',
                'options': ['Tubarão-baleia', 'Tubarão-branco', 'Baleia-azul', 'Atum'],
                'answer': 'Tubarão-baleia'
            }
        ]
        self.score = 0

    def run(self):
        print("Bem-vindo ao Quiz sobre o Mundo Animal!")
        print("Responda corretamente o maior número de perguntas.")
        print("---------------------------------------------")
        for question in self.questions:
            print(question['question'])
            for i, option in enumerate(question['options']):
                print(f"{i + 1}. {option}")

            user_answer = input("Sua resposta (digite o número da opção): ")
            if user_answer == str(question['options'].index(question['answer']) + 1):
                print("Resposta correta!")
                self.score += 1
            else:
                print(f"Resposta incorreta! A resposta correta era: {question['answer']}")
            print("---------------------------------------------")

        print("Fim do jogo!")
        print(f"Sua pontuação final é: {self.score}/{len(self.questions)}")


quiz = Quiz()
quiz.run()

