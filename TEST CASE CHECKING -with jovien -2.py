from jovian.pythondsa import evaluate_test_case # type: ignore

test = {
    'input':{
        'a':2,
        'b':10
        },
    'output':200
    }
def ma(a,b):
    return a*b

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


evaluate_test_case(ma, test)
# print(locate_card(test['input']['cards'],test['input']['query']) == test['output'])


