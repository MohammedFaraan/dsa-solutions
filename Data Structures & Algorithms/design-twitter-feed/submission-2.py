class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.followers = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.posts[userId].append([self.time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []

        maxHeap.extend(self.posts[userId])

        for fId in self.followers[userId]:
            if fId != userId:
                maxHeap.extend(self.posts[fId])
        
        heapq.heapify_max(maxHeap)
        
        k = 10
        res = []
        while maxHeap and k > 0:
            res.append(heapq.heappop_max(maxHeap)[1])
            k -= 1

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
