import random

card_deck = {"ace of spade":1,
         "2 of spade":2,
         "3 of spade":3,
         "4 of spade":4,
         "5 of spade":5,
         "6 of spade":6,
         "7 of spade":7,
         "8 of spade":8,
         "9 of spade":9,
         "10 of spade":10,
         "jack of of spade":10,
         "queen of spade":10,
         "king of spade":10,
         "ace of heart":1,
         "2 of heart":2,
         "3 of heart":3,
         "4 of heart":4,
         "5 of heart":5,
         "6 of heart":6,
         "7 of heart":7,
         "8 of heart":8,
         "9 of heart":9,
         "10 of heart":10,
         "jack of heart":10,
         "queen of heart":10,
         "king of heart":10,
         "ace of diamond":1,
           "2 of diamond":2,
           "3 of diamond":3,
           "4 of diamond":4,
           "5 of diamond":5,
           "6 of diamond":6,
           "7 of diamond":7,
           "8 of diamond":8,
           "9 of diamond":9,
           "10 of diamond":10,
           "jack of diamond":10,
           "queen of diamond":10,
           "king of diamond":10,
         "ace of clubs":1,
         "2 of clubs":2,
         "3 of clubs":3,
         "4 of clubs":4,
         "5 of clubs":5,
         "6 of clubs":6,
         "7 of clubs":7,
         "8 of clubs":8,
         "9 of clubs":9,
         "10 of clubs":10,
         "jack of clubs":10,
         "queen of clubs":10,
         "king of clubs":10}




def draw_two_cards(card_deck):
    count = 0
    while count < 2:
        pick_a_card = random.choice(card_deck.keys())
        value = card_deck[pick_a_card]
        player_one_pot.append(value)
        player_one.append(pick_a_card)
        card_deck.pop(pick_a_card)
        count += 1
    return player_one


def draw_one_card(card_deck):
    pick_a_card = random.choice(card_deck.keys())
    #print pick_a_card
    player_one.append(pick_a_card)
    value = card_deck[pick_a_card]
    player_one_pot.append(value)
    card_deck.pop(pick_a_card)
    return player_one

def dealer_draw_one_card(card_deck):
    pick_a_card = random.choice(card_deck.keys())
    #print pick_a_card
    dealer.append(pick_a_card)
    card_deck.pop(pick_a_card)
    return dealer


def dealer_draw_two_cards(card_deck):
    count = 0
    while count < 2:
        pick_a_card = random.choice(card_deck.keys())
        dealer.append(pick_a_card)
        card_deck.pop(pick_a_card)
        count += 1
    return dealer

#def dealer_draws_cards(card_deck):
#    pot = []
#    total_value = 0
#    while total_value <= 15:
#        pick_a_card = random.choice(card_deck.keys())
#        value = card_deck[pick_a_card]
#        pot.append(value)
#        total_value = sum(pot)
#    return total_value
at_casino = True
while at_casino:

    is_playing = True
    while is_playing:
        player_one = []
        player_one_pot = []
        dealer = []
        your_money = 200
        table = 0
        players_request = input("WELCOME TO ROYAL CASINO! Do you want to start the Blackjack game?(yes/no)")
        if players_request == "no":
            is_playing = False
            print("Okay. You do not want to play Blackjack. See you next time!")

        elif players_request == "yes":

            set_your_money = True
            while set_your_money:
                players_second_request = int(input("Your capital is {}$ at the moment. How much do you want to bet?".format(your_money)))
                if players_second_request <= your_money:
                    tmp_table = table + players_second_request
                    tmp_your_money = your_money - players_second_request
                    print("Okay you placed {}$" .format(players_second_request))
                    print("So then let's start! This are your first two cards:")
                    set_your_money = False

                else:
                    print("Nice try! But you only have {}$." .format(your_money))

        else:
            print("Unvalid answer. Please check your answer.")

        print(draw_two_cards(card_deck))

        the_answer = True
        while the_answer:

            players_answer = raw_input("Do you want to have another card? (hit/stand)")
            if players_answer == "hit":
                print (draw_one_card(card_deck))

                if sum(player_one_pot) > 21:
                    is_playing = False
                    the_answer = False
                    print ("Bust! You are over 21!")

            elif players_answer == "stand":
                for item in player_one:
                    if item in ["ace of clubs","ace of diamond","ace of heart","ace of spade"]:
                        players_answer_1 = raw_input("Do you want to count the ace as 11 or 1? (11/1)")
                        if players_answer_1 == "11":
                            player_one_pot.append(10) #10 because ace's have the value 1 already in case of early bust.

                        elif players_answer_1 == "1":
                            player_one_pot.append(0)

                        else:
                            print ("Unvalid answer. PLease check your answer.")

                    else:
                        continue

                the_answer = False
                print ("Okay, so then its the dealers turn. Dealer has following hand:")


                def dealer_draws_cards(card_deck):
                    pot = []
                    ace_pot = []
                    total = 0
                    while total <= 15:
                        pick_a_card = random.choice(card_deck.keys())
                        print(pick_a_card)

                        if pick_a_card in ["ace of clubs", "ace of diamond", "ace of heart", "ace of spade"]:
                            ace_pot.append(pick_a_card)
                            print(ace_pot)

                            if pot <= 10:
                                pot.append(11)
                                print(pot)

                        else:
                            value = card_deck[pick_a_card]
                            pot.append(value)
                            total = sum(pot)

                    return total


                output_dealer = dealer_draws_cards(card_deck)
                print("Dealers hand is: %d " % output_dealer)
                print("Your hand is: %d" % sum(player_one_pot))
                if output_dealer > 21:
                    is_playing = False
                    print("Dealer is over 21!")

            else:
                print("Unvalid answer. Please check your answer.")

        if sum(player_one_pot) == 21:
            print("You won!")
            your_money = tmp_your_money + 2 * tmp_table
            print("Congrats! You made +{}$!".format(tmp_table))
            print("You have a total of {} Dollars now!".format(your_money))
            table = 0
            is_playing = False


        elif output_dealer == sum(player_one_pot):
            print("You won!")
            your_money = tmp_your_money + 2 * tmp_table
            print("Congrats! You made +{}$!".format(tmp_table))
            print("You have a total of {} Dollars now!".format(your_money))
            table = 0
            is_playing = False

        elif output_dealer == 21 and sum(player_one_pot) is not 21:
            print("Dealer wins!")
            is_playing = False

        elif output_dealer > sum(player_one_pot) and not output_dealer > 21:
            print("Dealer wins!")
            is_playing = False

        elif output_dealer < sum(player_one_pot):
            print("You won!")
            your_money = tmp_your_money + 2 * tmp_table
            print("Congrats! You made +{}$!".format(tmp_table))
            print("You have a total of {} Dollars now!".format(your_money))
            table = 0
            is_playing = False

        else:
            print("You won!")
            your_money = tmp_your_money + 2 * tmp_table
            print("Congrats! You made +{}$!".format(tmp_table))
            print("You have a total of {} Dollars now!".format(your_money))
            table = 0
            is_playing = False

    players_game_answer = raw_input("Do you want to play another round? (yes/no)")
    if players_game_answer == "yes":
        at_casino = True
    elif players_game_answer == "no":
        print("Okay! Hopefully you enjoyed CASINO ROYAL, see you next time!")
        at_casino = False
    else:
        print("Unvalid answer. PLease check your answer.")





#Einstellen, dass im Fall von einem Doppelbild zB jack of Heart und king of heart man splitten kann.
#Einstellen, dass man Geld setzen kann.






