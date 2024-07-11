def kidsWithCandies(self, candiesL List[int], extraCandies: int) -> List[bool]:
    most = max(candies)
    for i in range(len(candies)):
        if candies[i] + extraCandies >= most:
            candies[i] = True
        else:
            candies[i] = False
    return candies

"""
Discussion:
    This question is really poorly worded but what it means is we want to know if 
    candies[i] + extraCandies > max of candies before addition of extraCandies

    so for example:
    extraCandies=3
    [2, 3, 5, 1, 3] max=5
    if i + extraCandies >= max true else false 
"""
