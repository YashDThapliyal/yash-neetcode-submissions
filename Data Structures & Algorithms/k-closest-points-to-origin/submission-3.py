class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = [[((x**2) + (y**2))**0.5, x, y] for x, y in points]
        heapq.heapify(heap)
        while k>0:
            d,x,y = heapq.heappop(heap)
            res.append([x,y])
            k -= 1

        return res