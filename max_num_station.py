# Walmart question https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/
# o(nlogn)
def countStation(arr, dept):
    arr.sort()
    dept.sort()
    j = 0
    max_req, needed = 1, 1
    for i in range(1,  len(arr)):
        # while departure time is < arrival, we will traverse next value of dept and decrement needed plateform by 1
        while dept[j] < arr[i] and max_req >= 0:
            max_req -= 1
            j += 1

        # if arrival time is less than dept time, we would require an extra plateform
        if arr[i] < dept[j]:
            max_req += 1
        # if needed is > max needed, wwe will increment max counter by 1
        if max_req > needed:
            needed += 1

    return needed


arr = [900, 905, 1200, 950, 1100, 1500]
dept = [910, 1200, 1300, 1120, 1130, 1900]
print(countStation(arr, dept))
