'''
FINAL PROJECT: Text-Based Quiz/Trivia Game

Submitted by: PROJECT GROUP H
Mary Christen Gemel Tolentino
Dylan Isaac Vela
Ann Carleen Gaile Cuevas
Aria Carmela De Vera
Ryan Jay Buenaventura
Megan Isabel Sharpe

Submitted to:
Asst. Prof. Katrina Joy M. Abriol-Santos

Text-Based Trivia Game: Player Module
This class represents the player module of the Trivia Game
'''

import os    # Added import os for the purpose of checking saved files and deleting them.
import json  # More flexible; allows for multiple players.

class Player:
    '''
    Represents a player in the Text-Based Trivia Game.
    '''
    
    def __init__(self, player_name=""):
        '''
        Initializes a new instance of the Questions class.
        
        Parameters:
        player_name: The name of the player in the Trivia Game
        '''
        self.player_name = player_name                            # string attribute
        self.save_file = f"{self.player_name}_save.json"

    def get_name(self):
        ''' Returns the name of the player. '''
        return self.player_name

    def set_name(self, player_name):
        ''' Updates the name of the player '''
        self.player_name = player_name

# --------------------------
# Save/Load/Delete Features
# --------------------------
    
    # Added: Save current game status to a file.
    def save_game_status(self, category, subcategory, score, question_index):
        progress = {
            "player_name": self.player_name,
            "category": category,
            "subcategory": subcategory,
            "score": score,
            "question_index": question_index
        }
        with open(self.save_file, "w") as f:
            json.dump(progress, f)

    # Added: Load saved game status from file.
    def load_game_status(self):
        if os.path.exists(self.save_file):
            with open(self.save_file, "r") as f:
                return json.load(f)
        return None

    # Added: Check if a saved game exists.
    def has_saved_game(self):
        return os.path.exists(self.save_file)

    # Added: Deletes an existing player's saved game.
    def delete_saved_game(self):
        if os.path.exists(self.save_file):
            os.remove(self.save_file)

    # Added: Resume Game Function.
    def resume_game(self, quiz_questions, letters):
        if not self.has_saved_game():
            return  # No saved game found
        resume = input("You have a saved game. Do you want to resume it? (yes/no): ").lower()
        if resume != "yes":
            return

        # Load saved data
        saved = self.load_game_status()
        self.set_name(saved["player_name"])
        main_selected = saved["category"]
        sub_selected = saved["subcategory"]
        score = saved["score"]
        start_index = saved["question_index"]

        questions = quiz_questions[main_selected][sub_selected]
        print(f"\nResuming: {main_selected} -> {sub_selected} (Score: {score})\n")

        # Resume quiz from saved question
        for i in range(start_index, len(questions)):
            q = questions[i]
            print(q["question"])
            for j in range(len(q["options"])):
                print(f"{letters[j]}. {q['options'][j]}")

            answer = input("Your answer (a/b/c/d): ").lower()
            if answer in letters:
                index = letters.index(answer)
                if q["options"][index] == q["answer"]:
                    print("Correct!\n")
                    score += 1
                else:
                    print(f"Wrong! The correct answer was: {q['answer']}\n")
            else:
                print("Invalid input! Please answer a, b, c, or d.\n")

            self.save_game_status(main_selected, sub_selected, score, i + 1)

        print(f"Your final score: {score}/{len(questions)}")
        self.delete_saved_game()

        play_again = input("\nDo you want to go back to main categories? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            exit()
