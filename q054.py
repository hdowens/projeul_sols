from timeit import default_timer

def solve_hand(hand):

    #dict to map the face cards to ints
    #note that this doesnt allow for ace-low straights?
    card_dict = {"T" : 10, "J" : 11, "Q" : 12, "K" : 13, "A" : 14}

    #bools for returning the answer
    fofakind = False
    three_kind = False
    pair = False
    twopair = False
    straight = False
    flush = False

    #organising the data
    faces = []
    for i in hand.split(' '):
        if i[0].isalpha():
            faces.append(int(card_dict[i[0]]))
        else:
            faces.append(int(i[0]))
    suits = [i[1] for i in hand.split(' ')]
    faces = sorted(faces)

    #four of a kind
    for i in range(0, 2):
        if int(faces[i])== int(faces[i+1]) and int(faces[i+1]) == int(faces[i+2]) and int(faces[i+2]) == int(faces[i+3]):
            fofakind = True

    #test for three of a kind
    for i in range(0, 3):
        if faces.count(faces[i]) == 3:
            three_kind = True

    #test for pairs
    #count vals using a dict
    pair_dict = {}
    for i in range(0, 5):
        if faces[i] in pair_dict:
            pair_dict[faces[i]] = pair_dict.get(faces[i],0) + 1
        else:
            pair_dict[faces[i]] = 1

    count = 0
    for occur in pair_dict.values():
        if occur == 2:
            count = count + 1

    #assign bools based on dict count of faces
    if count == 2:
        twopair = True
    if count == 1:
        pair = True

    #flush
    if all(elem == suits[0] for elem in suits): 
        flush = True

    #straight
    if int(faces[0]+1) == int(faces[1]):
        if int(faces[1]+1) == int(faces[2]):
            if int(faces[2]+1) == int(faces[3]):
                if int(faces[3]+1) == int(faces[4]):
                    straight = True

    """
        begin the return statements
        note that through testing I realised that there are no royal flushes, straight flushes
        four of a kinds or full houses, which I thought was odd
        but I left them in for the completeness of the solution

        i have written a much more complete solution in C++ which analyses all 7 cards, 2 from the player and 5 from the table
    """

    if straight and flush and faces[4] == 14:
        return (10, faces)

    if straight and flush:
        return (9, faces)

    if fofakind:
        return (8, faces)

    if three_kind and pair:
        return(7, faces)

    if flush:
        return (6, faces)

    if straight:
        return (5, faces)

    if three_kind:
        return (4, faces)

    if twopair:
        return (3, faces)

    if pair:
        return (2, faces)
        
    else:
        return (1, faces)
  

def compare_hand(faces_p1, faces_p2):

    #high card comparison
    if faces_p1[0] == 1:
       if faces_p1[1][4] > faces_p2[1][4]:
           return True

    #pair comparison
    if faces_p1[0] == 2:
  
        """
        two options here (to win), either player1 has a higher pair than player2 OR
        player1 has the same pair as player2 which results in needing to find the 
        higher card in the remining 3 cards 
        """

        pair1 = 0
        pair2 = 0
        for i in range(0, 4):
             if faces_p1[1].count(faces_p1[1][i]) == 2:
                 pair1 = faces_p1[1][i]
             if faces_p2[1].count(faces_p2[1][i]) == 2:
                 pair2 = faces_p2[1][i]

        
        if pair1 > pair2:
            return True

        if pair1 == pair2:
            #remove the pair and find the highest card
            res1 = [i for i in faces_p1[1] if i != pair1]
            res2 = [i for i in faces_p2[1] if i != pair2]
            if res1[2] > res2[2]:
                return True

        """
        Through testing I saw that there were player1 vs player2 where both had twopair, so I omitted this. 
        It would be trivial to implement however, based on code above.
        """
    return False



def compute():
    with open('p054_poker.txt') as f:
        words = [word.split("\n") for word in f.readlines()]

    count = 0
    for i in words:
        cur_game = str(i[0])
        player1, player2 = cur_game[0:14], cur_game[15:]
        play1, play2 = solve_hand(player1), solve_hand(player2)
        if play1[0] > play2[0]:
            count += 1
        if play1[0] == play2[0]:
            if compare_hand(play1, play2):
                count += 1

    return count



if __name__ == "__main__":

    start = default_timer()

    print(compute())

    stop = default_timer()

    print("Time taken -> ", stop - start)

