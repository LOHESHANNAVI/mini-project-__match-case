# cards = [13,11,10,7,4,3,1,0]
# query = 7
# output = 3


test = {
    'input':{
        'cards':[13,11,10,7,4,3,1,0],
        'query':7
    },
    'output':3
    }

def locate_card(cards, query):
    low = 0
    high = len(cards) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_card = cards[mid]

        if mid_card == query:
            return mid
        elif mid_card < query:
            high = mid - 1
        else:
            low = mid + 1

    return -1  # Return -1 if the card is not found



print(locate_card(test['input']['cards'],test['input']['query']) == test['output'])


