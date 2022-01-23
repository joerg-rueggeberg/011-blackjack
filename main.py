# REPLIT VERSION
from replit import clear
from art import logo
from random import choice

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = []
cpu = []


def deal(deal_who):
    """ Gibt eine zufällige Karte aus 'cards' an 'player' oder 'cpu' """
    deal_who.append(choice(cards))


def score(score_who):
    """ Berechnet den aktuellen Punktestand von 'player' oder 'cpu', erfasst einen Blackjack oder wandelt bei mehr
    als 2 Karten eine 11 in eine 1 um."""
    global player
    # Blackjack
    if sum(score_who) == 21 and len(score_who) == 2:
        return 0
    # Ass = 1 bei mehr als 2 Karten
    elif sum(score_who) > 21 and len(score_who) > 2 and 11 in score_who:
        score_who[score_who.index(11)] = 1
        return sum(score_who)
    # Summe
    else:
        return sum(score_who)

def compare(score_player, score_cpu):
    """Vergleicht die Punktestände nach Siegbedingungen und gibt einen Gewinner aus."""
    global player
    global cpu
    if score(player) == score(cpu):
        return f"*********************************************\n" \
               f"Unentschieden! {score(player)}:{score(cpu)}\n" \
               f"*********************************************"
    elif score(player) == 0:
        return f"*********************************************\n" \
               f"BLACKJACK für Spieler - Du gewinnst!\n" \
               f"*********************************************"
    elif score(cpu) == 0:
        return f"*********************************************\n" \
               f"BLACKJACK für Computer - Du verlierst!\n" \
               f"*********************************************"
    elif score(player) > 21:
        return f"*********************************************\n" \
               f"Spieler hat überzogen - Der Computer gewinnt! {score(player)}:{score(cpu)}\n" \
               f"*********************************************\n"
    elif score(cpu) > 21:
        return f"*********************************************\n" \
               f"Computer hat überzogen - Du gewinnst! {score(player)}:{score(cpu)}\n" \
               f"*********************************************"
    elif score(player) > score(cpu):
        return f"*********************************************\n" \
               f"Du gewinnst! {score(player)}:{score(cpu)}\n" \
               f"*********************************************"
    else:
        return f"*********************************************\n" \
               f"Der Computer gewinnt! {score(cpu)}:{score(player)}\n" \
               f"*********************************************"


def blackjack():
    """Definiert das komplette Programm zur erneuten Ausführung"""
    global player
    global cpu
    end = False
    end_player = False

    # Ausgabe Starthände
    deal(player)
    deal(player)
    deal(cpu)
    deal(cpu)

    print(logo)
    print(f"\nKarten Spieler: {player} - Summe: {score(player)}\nStartkarte Computer: {cpu[0]}")

    # Berechnung Spielstatus
    while not end:
        if score(player) == 0 or score(cpu) > 21:
            end = True
        elif score(cpu) == 0 or score(player) > 21:
            end = True
        else:
            # Spieler zieht Karten
            if not end_player:
                deal_more = input("\nMöchtest du eine weitere Karte ziehen? j/n: ").lower()
                print()
                if deal_more == "j":
                    deal(player)
                    score(player)
                    print(f"Deine Karten: {player} - Summe: {score(player)}")
                else:
                    print(f"Deine finalen Karten: {player} - Summe: {score(player)}")
                    end_player = True
            # CPU zieht Karten
            if end_player:
                if sum(cpu) <= 17:
                    deal(cpu)
                    # print(f"Karten Computer: {cpu} - Summe: {score(cpu)}\n")
                else:
                    end = True
    print(f"Computers finale Karten: {cpu} - Summe: {score(cpu)}\n")
    print(compare(player, cpu))

    print()
    con = input("Möchtest du eine weitere Runde spielen? j/n: ").lower()
    if con == "j":
        end = False
        clear()
        player = []
        cpu = []
        blackjack()

# Ruft das Programm auf
blackjack()