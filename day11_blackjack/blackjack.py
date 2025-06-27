import random
from blackjack_art import logo
def deal_card(): # 待辦事項1: 以列表創造分牌組函數回傳隨機牌
    """從牌組中隨機分配一張牌"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card
# 待辦事項3: 創造計分函數加總牌值點數
# 待辦事項4: 判斷 2張牌並合計 21點時，回傳成績為 0
# 待辦事項5: 判斷合計點數超過 21點時，Ace為1點; 不超過 21點則 Ace為 11點
# 待辦事項6: 如果玩家或電腦有 21點(blackjack), 或玩家分數超過 21點, 則遊戲結束
def calc_score(point):
    """計算牌面分數"""
    if sum(point) == 21 and len(point) == 2:
        return 0
    if sum(point) > 21 and 11 in point:
        point.remove(11)
        point.append(1)
    return sum(point)

def compare(user, computer): #待辦事項10: 比較玩家與電腦的牌面分數大小
    if user == computer:
        return "Draw"
    elif computer == 0:
        return "Lose, opponent has Blackjack"
    elif user == 0:
        return "Win with a Blackjack"
    elif user > 21:
        return "You went over. You lose"
    elif computer > 21:
        return "Opponent went over. You win"
    elif user > computer:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_gmae_over = False

    for a in range(2): # 待辦事項2: 分配莊家與玩家每人 2 張牌，使用分牌函數與增加列表元素 append()
        """給電腦與玩家發 2張牌"""
        computer_cards.append(deal_card())
        user_cards.append(deal_card())

    while not is_gmae_over: # 待辦事項8: 當玩家加入新牌後重新確認分數直到遊戲結束
        user_score = calc_score(user_cards) 
        computer_score = calc_score(computer_cards)
        print(f"Your cards are {user_cards}, current score is {user_score}")
        print(f"Computer's first card is {computer_cards[0]}")

        if user_score > 21 or user_score == 0 or computer_score == 0:
            is_gmae_over = True
        else: #待辦事項7: 詢問玩家是否要牌. 要牌以分牌函數加入1張, 不要則結束
            add_another = input("Do you want another card? Type 'y' to get another card, type 'n' to pass. ").lower()
            if add_another == 'y':
                user_cards.append(deal_card())
            else:
                is_gmae_over = True

    while computer_score != 0 and computer_score < 17: #待辦事項9: 玩家結束要牌後，判斷電腦分數是否超過 17分，不足則補充牌面分數達 17分以上; 超過則結束補充牌並計分
        computer_cards.append(deal_card())
        computer_score = calc_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}") #展示玩家的手牌與分數
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}") #展示電腦的手牌與分數
    print(compare(user_score, computer_score)) 

while input("Do you want to play a game of Blackjack? Type 'y' to restart, type 'n' to end: ") == 'y':
    print('\n' * 20)
    play_game()