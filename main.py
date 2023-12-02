import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deck_card():
    deck = []
    deck.append(random.choice(cards))
    deck.append(random.choice(cards))
    return deck

def current_score(s1,s2):
    return s1+s2

wanna_play = True
while wanna_play:
    ask_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if ask_to_play == 'y':
        print(logo)
        show = deck_card()
        # print(show[0])
        # print(show[1])
        answer = current_score(show[0],show[1])
        print(f"Your cards: {show}, current score = {answer}")
        code_show = deck_card()
        print(f"Computers first card is: {code_show[0]}")
        code_score = current_score(code_show[0],code_show[1])
        check = True
        i = 0
        while check:
            ask_for_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if (ask_for_card == 'y') :
                i += 1
                show.append(random.choice(cards))
                answer = current_score(answer,show[i+1])
                if (show[i + 1] == 11) and (answer > 21):
                    show[i+1] = 1
                    answer = current_score(answer, -10)
                r = 5 # This line does nothing.
                if (answer <= 21):
                    print(f"Your cards: {show}, current score ={answer}")
                    print(f"Computers first card is: {code_show[0]}")
                else:
                    check = False
                    print(f"Your cards: {show}, current score ={answer}")
                    print(f"Computer's final hand: {code_show}, final score: {code_score}")
                    print("You went over. You lose 😤")

            else:
                j = 1
                check = False
                if code_score < 17:
                    code_show.append(random.choice(cards))
                    j += 1
                    code_score = current_score(code_score, code_show[j])
                    if (code_show[j] == 11) and (code_score>21):
                        code_show[j] = 1
                        code_score = current_score(code_score, -10)


                print(f"your final hand: {show}, fianl score: {answer}")
                print(f"Computer's final hand: {code_show}, final score: {code_score}")
                if (answer > code_score) or (code_score > 21):
                    print("Opponent went over. You win 😁")
                elif answer == code_score:
                    print("It's Draw ")
                else:
                    print("You went over. You lose 😤")
    else:
        wanna_play = False




