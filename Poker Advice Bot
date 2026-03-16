from treys import Card, Evaluator, Deck
import re
import sys
import os
from datetime import datetime

hero_cards = []
community_cards = []
logs = ""

def setup(street):
    villains = int(input("Total number of player? "))-1
    pot_size = int(input("Current pot size? "))
    call_cost = int(input("What is the cost to call? "))
    hole = input("Enter your hole cards: ")
    parser(hole.split(","), street)
    return villains, pot_size, call_cost
def update(street, villains, pot_size):
    print(f"========== {street} PHASE ==========")
    folded = int(input("How many players folded?"))
    villains = villains - folded
    if villains <= 0:
        return 0, pot_size, 0, folded
    new_pot_size = int(input("Current pot size? "))
    if new_pot_size < pot_size:
        sys.exit("Invalid pot size")
    else:
        pot_size = new_pot_size
    call_cost = int(input("What is the cost to call? "))
    return villains, pot_size, call_cost, folded

def get_cards(street, n):
    card = input(f"Enter {n} community cards: ")
    new_cards = card.split(",")
    parser(new_cards, street)

def parser(new_cards, street):
    global community_cards, hero_cards
    for c in new_cards:
        if re.match("^[2-9AQKJT][hdcs]$", c):
            if not street == "preflop":
                community_cards.append(Card.new(c))
                if len(community_cards) != len(set(community_cards)):
                    sys.exit("Same card dealt twice")
                else:
                    continue
            else:
                hero_cards.append(Card.new(c))
        else:
            sys.exit("Input cards in format Xy where X is the denomination and y is the suite. Use only commas between cards.")

def simulator(n, villains):
    global community_cards, hero_cards
    wins=0
    evaluator = Evaluator()

    for _ in range(1000):
        villain_cards =[]
        board = community_cards[:]
        villain_score=[]
        deck = Deck()
        deck.shuffle()
        # removing already dealt cards
        for c in (hero_cards + community_cards):
            deck.cards.remove(c)
        
        # dealing cards for rest of the board
        for i in range(5-len(board)):
            board+=deck.draw(1)
        for i in range(villains):
            villain_cards.append(deck.draw(2))

        # evaluating who wins
        hero_score = evaluator.evaluate(hero_cards, board)
        for v in villain_cards:
            villain_score.append(evaluator.evaluate(v, board))
        best_villain_score = min(villain_score)
        if hero_score < best_villain_score:
            wins+=1
    #print(wins/1000)
    return(wins/1000)

def get_advice(pot_size, call_cost, equity):
    #calculate pot odds
    pot_odds = call_cost/(call_cost + pot_size)
    if equity > pot_odds:
        return "CALL"
    else:
        return "FOLD"

def card_to_str(cards):
    str_cards = []
    if not cards:
        return ""
    for c in cards:
        str_cards.append(Card.int_to_str(c))
        
    return ", ".join(str_cards)

def init_log(game_num, street_num, players):
    global logs
    date_str = datetime.today().strftime('%d/%m/%Y')
    
    logs = f"-------------------------------------------\n"
    logs += f"{date_str}\n"
    logs += f"Game #{game_num}, round #{street_num}\n"
    logs += f"Players: {players}\n"

def logging(street, folded, pot_size, call_cost, advice, decision):
    global logs
    # Append the specific phase data to the buffer
    logs += f"\n    {street.upper()}    \n"
    logs += f"Hole cards: {card_to_str(hero_cards)}\n"
    logs += f"Community cards: {card_to_str(community_cards)}\n"
    logs += f"Players folded: {folded}\n"
    logs += f"Pot size: {pot_size}\n"
    logs += f"Call cost: {call_cost}\n"
    logs += f"Advice: {advice}\n"
    logs += f"Your decision: {decision}\n"

def final_log(result, hand_name):
    global logs
    logs += f"\n    RESULT\n"
    if result == "W":
        logs += f"You won! (Final Hand: {hand_name})\n"
    else:
        logs += f"You lost:( (Final Hand: {hand_name})\n"

    with open('pokerlogs.txt', mode='a', encoding='utf-8') as file:
        file.write(logs)

def game_number():
    if not os.path.exists('pokerlogs.txt'):
        return 1
    
    max_game = 0
    with open('pokerlogs.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        matches = re.findall(r"Game #(\d+)", content)
        if matches:
            max_game = max(int(m) for m in matches)
            
    return max_game + 1

def reset_round():
    global hero_cards, community_cards, logs
    hero_cards.clear()
    community_cards.clear()
    logs = ""

def main():
    
    game_num = game_number()
    round_num = 1
    hand_name = "High Card"
    while True:
        reset_round()
        result =""
        streets = [
            {"street" : "preflop", "n" : 0},
            {"street" : "flop", "n" : 3},
            {"street" : "turn", "n" : 1},
            {"street" : "river", "n" : 1}
        ]

        for st in streets:
            street = st["street"]
            n = st["n"]
            folded = 0

            if street == "preflop":
                villains, pot_size, call_cost = setup(street)
                init_log(game_num, round_num, villains + 1)
                equity = simulator(n, villains)
                advice = get_advice(pot_size, call_cost, equity)
                print(advice)
                decision = input("What was your decision?").upper()
                logging(street, folded, pot_size, call_cost, advice, decision)
                if decision not in ["CALL", "BET", "RAISE", "FOLD"]:
                    sys.exit("Invalid Decision")
                if decision == "FOLD":
                    result = "L"
                    break
            else:
                villains, pot_size, call_cost, folded = update(street, villains, pot_size)
                if villains == 0:
                    result = "W"
                    logging(street, folded, pot_size, call_cost, advice, decision)
                    break
                get_cards(street, n)
                equity = simulator(n, villains)
                advice = get_advice(pot_size, call_cost, equity)
                print(advice)
                decision = input("What was your decision?").upper()
                logging(street, folded, pot_size, call_cost, advice, decision)
                if decision not in ["CALL", "BET", "RAISE", "FOLD"]:
                    sys.exit("Invalid Decision")
                if decision == "FOLD":
                    result = "L"
                    break

        if result == "":
            result = input("What was the result? Enter W for win and L for loss")

        if result == "W":
            print("Congratulations! You WON")
        if result == "L":
            print("Ops! Better Luck Next Time")            

        if len(community_cards) >= 3 and len(hero_cards) == 2:
            evaluator = Evaluator()
            raw_score = evaluator.evaluate(hero_cards, community_cards)
            rank_class = evaluator.get_rank_class(raw_score)
            hand_name = evaluator.class_to_string(rank_class)
        elif len(community_cards) < 3:
            hand_name = "Preflop Hand (No Board)"
        print("Board: ", end='')
        Card.print_pretty_cards(community_cards)
        print("Hero: ", end='')
        Card.print_pretty_cards(hero_cards)
        print(f"You had a {hand_name}")

        final_log(result, hand_name)

        play_again = input("\nDo you want to play another round? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing! Closing programme.")
            break
        round_num += 1

if __name__ == "__main__":
    main()       
            
