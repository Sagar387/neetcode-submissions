class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create frequencies first
        d= {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        # python has counter built in tool, count = Counter(nums) sets dict like object mapping to freq
        
        # we can set up heap that runs k amoutn of times so we dont need to go through the full list to sort by the value

        heap=[]
        for key,val in d.items():
            if len(heap) < k:
                heapq.heappush(heap,(val,key))
            else:
                heapq.heappushpop(heap,(val,key))
        
        return [h[1] for h in heap]