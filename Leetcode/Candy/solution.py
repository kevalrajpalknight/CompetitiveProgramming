class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1]*n
        for i in range(n-1):
            if ratings[i] < ratings[i+1]:
                candies[i+1] = max(1+candies[i], candies[i+1])
        for i in range(n-2,-1,-1):
            if ratings[i+1] < ratings[i]:
                candies[i] = max(1+candies[i+1], candies[i])
        return sum(candies)