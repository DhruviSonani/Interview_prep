def solution(queries, diff):
    numbers, length, result = [], 0, []
    for q in queries:
        number = int(q[1:])
        if q[0] == "+":
            numbers.append(number)
            length += 1
        else:
            while number in numbers:
                numbers.remove(number)
                length -= 1
                count = 0

        numbers.sort()
        count = 0
        l = 0
        r = 1

        while r < length:        
            if numbers[r]-numbers[l] == diff:
                count += numbers.count(numbers[l])
                l += 1
                r += 1
            elif numbers[r]-numbers[l] > diff:
                l += 1
            else:
                r += 1
        result.append(count)
    return result

queries = ["+5","+5", "+4", "+2", "-4"]
print(solution(queries, 1))

