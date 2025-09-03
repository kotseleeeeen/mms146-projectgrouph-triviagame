# Dataset for the Questions, Answers (Options, Correct Answer

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
