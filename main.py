# -------------------------------
# Quiz Game - Pang pamili
# -------------------------------

import os  # Added: Required for file handling in save/resume features. Feel free to remove in case it breaks anything.
           # ~ Dylan
from player import *
from questions import *
from quizgame import *

# Dataset for the Questions, Answers (Options), Correct Answer

quiz_questions = {
    "Pop Culture Trivia": {
        "Celebrity Culture": [
            PopCultureQuestions(
                question_text="Who was the first Black woman to win the Academy Award for Best Actress in 2002?",
                answer=["Halle Berry", "Viola Davis", "Whoopi Goldberg", "Angela Bassett"],
                correct_answers="Halle Berry",
                subcategory="Celebrity Culture"
            ),
            PopCultureQuestions(
                question_text="Which rap song holds the record for winning the most Grammy Awards?",
                answer=["Lose Yourself – Eminem", "God’s Plan – Drake", "Alright – Kendrick Lamar", "Not Like Us – Kendrick Lamar"],
                correct_answers="Alright – Kendrick Lamar",
                subcategory="Celebrity Culture"
            ),
            PopCultureQuestions(
                question_text="What was the name of the 2019 YouTube video in which Tati Westbrook ended her friendship with James Charles?",
                answer=["Breaking My Silence", "Bye James", "Bye Sister", "Sisters No More"],
                correct_answers="Bye Sister",
                subcategory="Celebrity Culture"
            ),
        ],
        "Movies": [
            PopCultureQuestions(
                question_text="What is the highest-grossing film of all time?",
                answer=["Avengers: Endgame", "Titanic", "Avatar", "Star Wars: The Force Awakens"],
                correct_answers="Avatar",
                subcategory="Movies"
            ),
            PopCultureQuestions(
                question_text="Which historical document does Nicholas Cage’s character steal in National Treasure?",
                answer=["The Declaration of Independence", "The U.S. Constitution", "The Bill of Rights", "The Articles of Confederation"],
                correct_answers="The Declaration of Independence",
                subcategory="Movies"
            ),
            PopCultureQuestions(
                question_text="Which of the following is the longest non-experimental narrative film ever made?",
                answer=["Logistics", "Amra Ekta Cinema Banabo", "The Cure for Insomnia", "Out 1"],
                correct_answers="Amra Ekta Cinema Banabo",
                subcategory="Movies"
            ),
        ],
        "TV": [
            PopCultureQuestions(
                question_text="Which TV show ends by suddenly cutting to black?",
                answer=["True Detective", "The Sopranos", "Breaking Bad", "Lost"],
                correct_answers="The Sopranos",
                subcategory="TV"
            ),
            PopCultureQuestions(
                question_text="Game of Thrones is based on which book series by George R.R. Martin?",
                answer=["A Song of Ice and Fire", "A Clash of Kings", "A Dance with Dragons", "The Witcher"],
                correct_answers="A Song of Ice and Fire",
                subcategory="TV"
            ),
            PopCultureQuestions(
                question_text="What was the name of the coffee shop in Friends?",
                answer=["Brewster’s", "The Daily Grind", "Bean There", "Central Perk"],
                correct_answers="Central Perk",
                subcategory="TV"
            ),
            PopCultureQuestions(
                question_text="Which morning TV show was involved in a scandal when two anchors were revealed to be in an extramarital relationship?",
                answer=["CBS This Morning", "Morning Joe", "Good Morning America", "Today"],
                correct_answers="Good Morning America",
                subcategory="TV"
            ),
        ]
    },
    "Game Trivia": {
        "Video Games": [
            GameQuestions(
                question_text="Which game features the character Link?",
                answer=["Super Mario", "Zelda", "Halo", "Minecraft"],
                correct_answers="Zelda",
                subcategory="Video Games"
            ),
            GameQuestions(
                question_text="Which video game series has creatures called 'Pokémon'?",
                answer=["Digimon", "Pokémon", "Yu-Gi-Oh!", "Dragon Ball Z"],
                correct_answers="Pokémon",
                subcategory="Video Games"
            ),
            GameQuestions(
                question_text="What is the best-selling video game of all time?",
                answer=["Minecraft", "Tetris", "Grand Theft Auto V", "Wii Sports"],
                correct_answers="Minecraft",
                subcategory="Video Games"
            ),
        ]
    },
    "Anime Trivia": {
        "Popular Anime": [
            AnimeQuestions(
                question_text="Who is the main character of Naruto?",
                answer=["Sasuke Uchiha", "Naruto Uzumaki", "Kakashi Hatake", "Sakura Haruno"],
                correct_answers="Naruto Uzumaki",
                subcategory="Popular Anime"
            ),
            AnimeQuestions(
                question_text="Which anime features a giant humanoid creature called a Titan?",
                answer=["One Piece", "Attack on Titan", "Dragon Ball Z", "Bleach"],
                correct_answers="Attack on Titan",
                subcategory="Popular Anime"
            ),
            AnimeQuestions(
                question_text="In One Piece, what is the name of the main pirate crew?",
                answer=["Blackbeard Pirates", "Straw Hat Pirates", "Red Hair Pirates", "Whitebeard Pirates"],
                correct_answers="Straw Hat Pirates",
                subcategory="Popular Anime"
            ),
        ]
    }
}

letters = ["a", "b", "c", "d"]

# Load all questions
quiz.load_from_nested_dict(quiz_questions)

quiz.shuffle_question_bank()
quiz.reset_game()

# -------------------------------
# Start of Game
# -------------------------------

name = input("Enter your name: ")
player = Player(name)
print(f"Welcome, {player.get_name()}! Are you ready to play?\n")

# Added: Resume game if save file exists. 
# Basically, if the game is interupted before the end, 
# you will given the choice to continue from where you left off. 
# Please remove if it breaks anything. ~ Dylan
resume_saved_game(player, quiz_questions, letters)

# -------------------------------
# Main game loop
# -------------------------------

while True:
    # Choose main category
    main_categories = list(quiz_questions.keys())
    print("\nMain Categories:")
    for i in range(len(main_categories)):
        print(str(i + 1) + ". " + main_categories[i])
    print("0. Quit")

    main_choice = input("Choose a main category (number): ")
    
    if main_choice == "0":
        print("Thanks for playing!")
        break

    if not main_choice.isdigit() or int(main_choice) < 1 or int(main_choice) > len(main_categories):
        print("Invalid choice. Try again.")
        continue

    main_selected = main_categories[int(main_choice) - 1]

    # Choose sub-category
    sub_categories = list(quiz_questions[main_selected].keys())
    print("\nSub-Categories in " + main_selected + ":")
    for i in range(len(sub_categories)):
        print(str(i + 1) + ". " + sub_categories[i])
    print("0. Go back")

    sub_choice = input("Choose a sub-category (number): ")
    
    if sub_choice == "0":
        continue  # back to main category

    if not sub_choice.isdigit() or int(sub_choice) < 1 or int(sub_choice) > len(sub_categories):
        print("Invalid choice. Try again.")
        continue

    sub_selected = sub_categories[int(sub_choice) - 1]

    # Start quiz
    score = 0
    questions = quiz_questions[main_selected][sub_selected]
    print("\nYou chose: " + main_selected + " -> " + sub_selected + "\n")

    for i in range(len(questions)):
        q = questions[i]
        print(q["question"])
        for j in range(len(q["options"])):
            print(letters[j] + ". " + q["options"][j])
        
        answer = input("Your answer (a/b/c/d): ").lower()
        if answer in letters:
            index = letters.index(answer)
            if q["options"][index] == q["answer"]:
                print("Correct!\n")
                score += 1
            else:
                print("Wrong! The correct answer was: " + q["answer"] + "\n")
        else:
            print("Invalid input! Please answer a, b, c, or d.\n")

        # Added: Save progress after each question. Please Remove if it breaks anything. ~Dylan
        player.save_game_status(main_selected, sub_selected, score, i + 1)

    print("Your final score: " + str(score) + "/" + str(len(questions)))

    # Added: Clear saved game after quiz ends. Again, please remove if it breaks anything. ~ Dylan
    player.delete_saved_game()

    # Ask if they want to play again
    play_again = input("\nDo you want to go back to main categories? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
