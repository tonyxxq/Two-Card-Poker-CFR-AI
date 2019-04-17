import random


class Game:
    # 动作
    BET = '0'
    CALL = '1'
    CHECK = '2'
    FOLD = '3'

    # 牌力的大小排名
    RANKS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

    # 花色
    SUIT = ['h', 's', 'd', 'c']

    # 生成 52 张牌
    DECK = [rank + suit for rank in RANKS for suit in SUIT]

    @staticmethod
    def deal_cards():
        """
        随机发牌，每人两张
        """
        sample = random.sample(Game.DECK, 4)
        player_one_cards = sample[0:2]
        player_two_cards = sample[2:]

        return player_one_cards, player_two_cards

    @staticmethod
    def deal_cards_biased(player_one_favored):
        rand_hand = random.sample(Game.DECK, 2)
        strong_hand = list()

        # Strong suited ace
        if random.random() > 0.9:
            strong_hand.append('Ah')
            if random.random() > 0.5:
                strong_hand.append('Kh')
            elif random.random() > 0.5:
                strong_hand.append('Qh')
            else:
                strong_hand.append('Jh')
        # Pocket pair
        else:
            rank = random.choice(Game.RANKS)
            strong_hand.append(rank + 'h')
            strong_hand.append(rank + 's')

        if player_one_favored:
            return strong_hand, rand_hand
        else:
            return rand_hand, strong_hand

    @staticmethod
    def get_higher_rank(rank1, rank2):
        """
        比较大小
        """
        for rank in Game.RANKS:
            if rank1 == rank:
                return rank1
            if rank2 == rank:
                return rank2

        return rank1
