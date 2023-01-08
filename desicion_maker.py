print("To let me choice the best and *right* or *subitable* anime for you based on yr mood, pls fill below questions patiently, THanks!\n")

def normal_animes():
    normal_animes.psychological = """
        1. Monster
        2. Erased
        3. The promised Neverland
        4. Psycho pass 
        5. Id invaded
        6. 7 seeds
        7. Terror in resonance
        8. Parasyte the maxim
        9. Classroom of elite 
        10. kakegurui
        11. Akuma no Riddle
        12. When they cry
        13. Death Parade
"""
    
    normal_animes.Supernatural = """
        1. kyokou suiri
        2. Mob psycho 100
        3. Ousama game
        4. Fairy gone
        5. Devils line
        6. Hinamatsuri
        7. B the Beginning 
        8. Tokyo Ghoul 
        9. Devilman crybaby
        10. kekkai sensen
"""
    
    normal_animes.Magic = """
        1. Black clover 
        2. A Certain Magical: All series
        3. Dorohedoro
        4. Rising of the shield hero
        5. That time i reincarnated as a slime 
        6. kenja no mago
        7. Radiant
        8. Overlord
        9. Arifureta
        10. Fate series
"""
    
    normal_animes.Slice_of_life = """
        1. Fruits Basket
        2. Smile down the Runway
        3. Asteroid in love
        4. Teasing master Takagi san
        5. Violet Evergarden
        6. Somali and the forest spirit
        7. Love chuunibyou and other delusions
        8. March comes like a Lion
        9. Beastars
        10. Ascendance of a Book worm
        11. The Pet Girl Of Sakurasou
        12. Anohanna
"""
    
    normal_animes.Mystery = """
        1. Death note
        2. Trigun
        3. kanata no Astra
        4. Hyouka 
        5. Monster
        6. Black buttler
        7. Durarara
        8. kabukichou sherlock
        9. Darker than black
        10. Future diary
"""
    
    normal_animes.Comedy = """
        1. Konosuba
        2. My teen romantic comedy
        3. Disasterous life of Saiki k
        4. Devil is a part timer
        5. School rumble
        6. Haven't you heard I'm Sakamoto
        7. Bakuman
        8. Cautious Hero: Noragami
        9. Rikekoi
        10. Grand Blue (Must try)
        11. Nichijou
        12. Rent A Girlfriend
        13. Prison School(Ecchi)
        14. One Punch Man
"""
    
    normal_animes.Romance = """
        1. As the moon, so beautiful
        2. Your Lie in April
        3. A lull in the sea
        4. Clannad
        5. Toradora!
        6. 3d girlfriend
        7. Golden time
        8. Darling in the franxx
        9. Relife
        10. Tsuredure Children
        11. Kaguya Sama: Love is War
        12. Rent A Girlfriend
"""
    
    normal_animes.ACTION = """
        1. My hero academia
        2. Bleach
        3. Dragon ball
        4. Attack on titan
        5. One punch man
        6. Hunter X Hunter 
        7. Demon slayer
        8. Junni Taisen
        9. Assasinss classroom
        10. High School Dxd(Ecchi)
        11. Hellsing series
"""
    
    normal_animes.Horror = """
        1. Angels of Death
        2. kabaneri of the iron fortress
        3. Happy sugar life
        4. Berserk
        5. Sirius the jaeger
        6. Another
        7. Ajin
        8. Blood series
        9. Danganronpa
        10. Elfen Lied
"""
    
    normal_animes.Fantasy = """
        1. The seven deadly sins!
        2. Sword art online 
        3. Fairy tail
        4. Re:Zero Starting life in Another world
        5. No game No life
        6. Log horizon
        7. How not to summon a demon lord 
        8. Made in Abyss
        9. Akame ga kill
        10. Is it wrong to pick girls in dungeon?
"""
    
    normal_animes.ADVENTURE = """
        1. One piece
        2. Naruto
        3. Hunter x hunter
        4. Fullmetal alchemist Brotherhood
        5. Jojo's bizzare adventure
        6. Samurai champloo
        7. Bungou stray dogs
        8. Castlevania
        9. Claymore
        10. Goblin slayer
"""
    

def happy_animes():
    happy_animes.love = """
        1. Toradora!
        2. Horimiya 
        3. Nodame Cantabile
        4. Kids on the Slope
        5. Anohana: The Flower We Saw That Day
        6. Clannad & Clannad: After Story
        7. Fruits Basket
        8. Nana
        9. Kaguya-sama: Love Is War
        10. Your Lie in April 
        11. Sasaki & Miyano (Special)
"""
    
    happy_animes.action = """
        1. Naruto
        2. One Piece
        3. One-Punch Man
        4. Dragon Ball
        5. Hunter X Hunter
        6. Attack on titan
        7. Demon slayer
        8. Junni Taisen
        9. Bleach
        10. Tokyo Revengers
"""
    



def sad_anmies():
    sad_anmies.for_choice_1 = """
        1. A Silent Voice
        2. The Grave
        3. your name
        4. millennium actress
        5. Hotarubi no Mori e 
        6. Whisper of the Heart
        7. The Girl Who left Through Time
        8. Wolf children
        9. Stand By Me Dota Mon
        10. The Wind rises
"""
        
    sad_anmies.for_choice_2 = """
        1. Given
        2. Violet Evergarden
        3. Barakamon
        4. Haikyuu
        5. Run With the Wind
        6. One Piece
        7. Naruto
        8. Assassination Classroom
        9. Demon Slayer
        10. My Hero Academia
"""
    return


def messages():
    messages.message_for_sad = "\nOh, you having a hard time, i guess :(\n"
    messages.message_for_happy = "\nGreat to hear that you happy!\n" 
    messages.message_for_normal =  "\nYou are balanced :)\n"
    return

def mood_questions():
    print("1.sad\n2.happy\n3.normal\n")
    mood_questions.mood = input("What mood are you in right now in above: ")
    return

def mood_messages():
    messages()
    mood_questions()
    if mood_questions.mood == "1":
        print(messages.message_for_sad)
    elif mood_questions.mood == "2":
        print(messages.message_for_happy)
    elif mood_questions.mood == "3":
        print(messages.message_for_normal)
    else:
        print("\nPls, only answer with 1,2,3\n")
        mood_messages()

def Choices():
    mood_messages()
    normal_animes()
    sad_anmies()
    happy_animes()
    if mood_questions.mood == "1":
        def sad_1():
            print("1.The animes that would make me cry more :( [Not recommended if you really sad]\n2.Escape the hard time by watching them\n")
            movie_type = input("What type would you like to watch: ")
            if movie_type == "1":
                print(sad_anmies.for_choice_1)
                print("Select one or two of these above anime as your wish and go watch!\n")
            elif movie_type == "2":
                print(sad_anmies.for_choice_2)
                print("Select one or two of these above anime as your wish and go watch!\n")
            else:
                print("\nPls answer with only numbers like 1 or 2\n")
                sad_1()
        sad_1()
    if mood_questions.mood == "2":
        def happy_1():
            print("1.Love and Romatic\n2.Actions\n")
            movie_type = input("What type would you like to watch: ")
            if movie_type == "1":
                print(happy_animes.love)
                print("Select one or two of these above anime as your wish and go watch!\n")
            elif movie_type == "2":
                print(happy_animes.action)
                print("Select one or two of these above anime as your wish and go watch!\n")
            else:
                print("\nPls answer with only numbers like 1 or 2\n")
                happy_1()
        happy_1()
    if mood_questions.mood == "3":
        def normal_1():
            print("Since you are normal, you can watch any kind of anime of your choice!\n")
            print("1.ADVENTURE\n2.Psychological\n3.Magic\n4.ACTION\n5.Romance\n6.Slice_of_life\n7.Mystery\n8.Horror\n9.Fantasy\n10.Supernatural")
            movie_type = input("What type would you like to watch: ")
            if movie_type == "1":
                print(normal_animes.ADVENTURE)
                print("Select one or two of these above anime as your wish and go watch!\n")
            elif movie_type == "2":
                print(normal_animes.psychological)
                print("Select one or two of these above anime as your wish and go watch!\n")
            elif movie_type == "3":
                print(normal_animes.Magic)
                print("Select one or two of these above anime as your wish and go watch!\n")
            elif movie_type == "4":
                print(normal_animes.ACTION)
                print("Select one or two of these above anime as your wish and go watch!\n")
            elif movie_type == "5":
                print(normal_animes.Romance)
                print("Select one or two of these above anime as your wish and go watch!\n")
            elif movie_type == "6":
                print(normal_animes.Slice_of_life)
                print("Select one or two of these above anime as your wish and go watch!\n")
            elif movie_type == "7":
                print(normal_animes.Mystery)
                print("Select one or two of these above anime as your wish and go watch!\n")
            elif movie_type == "8":
                print(normal_animes.Horror)
                print("Select one or two of these above anime as your wish and go watch!\n")
            elif movie_type == "9":
                print(normal_animes.Fantasy)
                print("Select one or two of these above anime as your wish and go watch!\n")
            elif movie_type == "10":
                print(normal_animes.Supernatural)
                print("Select one or two of these above anime as your wish and go watch!\n")
            else:
                print("\nPls answer with only numbers like 1 or 2\n")
                normal_1()
        normal_1()

Choices()
