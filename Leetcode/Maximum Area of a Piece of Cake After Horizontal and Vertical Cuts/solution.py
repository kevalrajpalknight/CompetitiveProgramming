class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        maximumArea, maxHorizontal, maxVertical = 0,0,0
        horizontalCuts = sorted([0] + horizontalCuts + [h])
        verticalCuts = sorted([0] + verticalCuts + [w])
        horizontalWidths, verticalWidths = [], []
        
        for i in range(len(horizontalCuts)-1):
            horizontalDistance = abs(horizontalCuts[i] - horizontalCuts[i+1])
            if maxHorizontal < horizontalDistance:
                maxHorizontal = horizontalDistance
                
        for i in range(len(verticalCuts)-1):
            verticalDistance = abs(verticalCuts[i] - verticalCuts[i+1])
            if maxVertical < verticalDistance:
                maxVertical = verticalDistance
                
        maximumArea = maxVertical * maxHorizontal
        return maximumArea % (10**9 + 7)