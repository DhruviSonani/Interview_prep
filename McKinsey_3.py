
# Financial Services Lab - McKinsey – Front-End

def cardPackets(cardTypes):
    # Write your code here

    count2, count3, count5 = 0, 0, 0
    for i in cardTypes:
        if i % 2 != 0:
            count2 += 1
        if i % 3 != 0:
            count3 += 3
        if i % 5 != 0:
            count5 += 5

    return min(count2, count3, count5)
