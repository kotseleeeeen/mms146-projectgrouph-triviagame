from questions import PopCultureQuestions, AnimeQuestions, GameQuestions
import random

quiz_questions = {
    "Pop Culture": {
        "Celebrity Culture": [
            {
                "question": "Who was the first Black woman to win the Academy Award for Best Actress in 2002?",
                "options": ["Halle Berry", "Viola Davis", "Whoopi Goldberg", "Angela Bassett"],
                "answer": "Halle Berry"
            },
            {
                "question": "Which rap song holds the record for winning the most Grammy Awards?",
                "options": ["Lose Yourself – Eminem", "God’s Plan – Drake", "Alright – Kendrick Lamar", "Not Like Us – Kendrick Lamar"],
                "answer": "Alright – Kendrick Lamar"
            },
            {
                "question": "What was the name of the 2019 YouTube video in which Tati Westbrook ended her friendship with James Charles?",
                "options": ["Breaking My Silence", "Bye James", "Bye Sister", "Sisters No More"],
                "answer": "Bye Sister"
            }
        ],
        "Movies": [
            {
                "question": "What is the highest-grossing film of all time?",
                "options": ["Avengers: Endgame", "Titanic", "Avatar", "Star Wars: The Force Awakens"],
                "answer": "Avatar"
            },
            {
                "question": "Which historical document does Nicholas Cage’s character steal in National Treasure?",
                "options": ["The Declaration of Independence", "The U.S. Constitution", "The Bill of Rights", "The Articles of Confederation"],
                "answer": "The Declaration of Independence"
            },
            {
                "question": "Which of the following is the longest non-experimental narrative film ever made?",
                "options": ["Logistics", "Amra Ekta Cinema Banabo", "The Cure for Insomnia", "Out 1"],
                "answer": "Amra Ekta Cinema Banabo"
            }
        ],
        "TV": [
            {
                "question": "Which TV show ends by suddenly cutting to black?",
                "options": ["True Detective", "The Sopranos", "Breaking Bad", "Lost"],
                "answer": "The Sopranos"
            },
            {
                "question": "Game of Thrones is based on which book series by George R.R. Martin?",
                "options": ["A Song of Ice and Fire", "A Clash of Kings", "A Dance with Dragons", "The Witcher"],
                "answer": "A Song of Ice and Fire"
            },
            {
                "question": "What was the name of the coffee shop in Friends?",
                "options": ["Brewster’s", "The Daily Grind", "Bean There", "Central Perk"],
                "answer": "Central Perk"
            },
            {
                "question": "Which morning TV show was involved in a scandal when two anchors were revealed to be in an extramarital relationship?",
                "options": ["CBS This Morning", "Morning Joe", "Good Morning America", "Today"],
                "answer": "Good Morning America"
            }
        ]
    },
    "Game Trivia": {
        "Video Games": [
            {
                "question": "Which game features the character Link?",
                "options": ["Super Mario", "Zelda", "Halo", "Minecraft"],
                "answer": "Zelda"
            },
            {
                "question": "Which video game series has creatures called 'Pokémon'?",
                "options": ["Digimon", "Pokémon", "Yu-Gi-Oh!", "Dragon Ball Z"],
                "answer": "Pokémon"
            },
            {
                "question": "What is the best-selling video game of all time?",
                "options": ["Minecraft", "Tetris", "Grand Theft Auto V", "Wii Sports"],
                "answer": "Minecraft"
            }
        ]
    },
    "Anime Trivia": {
        "Popular Anime": [
            {
                "question": "Who is the main character of Naruto?",
                "options": ["Sasuke Uchiha", "Naruto Uzumaki", "Kakashi Hatake", "Sakura Haruno"],
                "answer": "Naruto Uzumaki"
            },
            {
                "question": "Which anime features a giant humanoid creature called a Titan?",
                "options": ["One Piece", "Attack on Titan", "Dragon Ball Z", "Bleach"],
                "answer": "Attack on Titan"
            },
            {
                "question": "In One Piece, what is the name of the main pirate crew?",
                "options": ["Blackbeard Pirates", "Straw Hat Pirates", "Red Hair Pirates", "Whitebeard Pirates"],
                "answer": "Straw Hat Pirates"
            }
        ]
    }
}

class QuizGame:
    def __init__(self):
        self.__question_bank = []
        self.__score = 0

    def add_question(self, question_object):
        self.__question_bank.append(question_object)

    def get_score(self):
        return self.__score
    
    def load_from_nested_dict(self, nested): 
        for category, subcats in nested.items():
            for subcategory, questions in subcats.items():
                for q in questions:
                    self.__question_bank.append({
                        "question_text": q["question"],
                        "answers": q["options"],
                        "correct_answer": q["answer"],
                        "category": category,
                        "subcategory": subcategory,
                    })
    
    def display_question(self, index):
        '''
        Returns question and its multiple choice answers
        '''
        if index < 0 or index >= len(self.__question_bank):
            return None, []
        
        q = self.__question_bank[index]

        if isinstance(q, dict):
            question_text = q["question_text"]
            answers = q["answers"]
        else:
            question_text = q.get_question_text()
            answers = q.get_answer()
        
        print ("\n" + question_text)
        letters = ["a", "b", "c", "d"]
        for i, option in enumerate (answers):
            if i < len(letters):
                print(f"{letters[i]}) {option}")
        
        return question_text, answers
    
    def check_answer(self, index, player_answer):
        if index < 0 or index >= len(self.__question_bank):
            return False
        
        q = self.__question_bank[index]

        if isinstance(q, dict):
            correct = q["correct_answer"]
            answers = q["answers"]
        else:
            correct = q.get_correct_answers()
            if isinstance(correct, list):
                correct = correct[0] if correct else ""
            answers = q.get_answer()

        letters = ["a", "b", "c", "d"]
        '''
        Allows user to input a, b, c, or d as their answer if they don't want to type the full answer.
        '''
        guess = player_answer.strip().lower()
        if guess in letters:
            idx = letters.index(guess)
            if idx < len(answers):
                player_answer = answers[idx]

        is_ok = player_answer.strip().lower() == str(correct).strip().lower()
        if is_ok:
            self.__score += 1
        return is_ok

    def shuffle_question_bank(self):
        '''
        Shuffles so the player doesn't know what to expect each time they play
        '''
        random.shuffle(self.__question_bank)

    def reset_game(self):
        self.__score = 0