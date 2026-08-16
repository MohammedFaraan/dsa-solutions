class Twitter:

    def __init__(self):
        self.tweets_by_user = defaultdict(list)
        self.user_followers = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets_by_user[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.user_followers[userId] | {userId}

        maxHeap = []
        for uid in users:
            if self.tweets_by_user[uid]:
                idx = len(self.tweets_by_user[uid]) - 1
                time, tweetId = self.tweets_by_user[uid][idx]

                heapq.heappush_max(maxHeap, (time, uid, idx, tweetId))
        
        res = []
        while maxHeap and len(res) < 10:
            time, uid, idx, tweetId = heapq.heappop_max(maxHeap)
            res.append(tweetId)
        
            if idx > 0:
                idx -= 1
                time, tweetId = self.tweets_by_user[uid][idx]
                heapq.heappush_max(maxHeap, (time, uid, idx, tweetId))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.user_followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_followers[followerId].discard(followeeId)

        
