class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        n = len(nums)
        for num in nums:
            count[num]+=1
        freq = [[] for i in range(n+1)]
        for key,v in count.items():
            freq[v].append(key)
        res = []
        for i in range(len(freq)-1,0,-1):
            curr = freq[i]
            for e in curr:
                res.append(e)
                if len(res)==k:
                    return res

    
