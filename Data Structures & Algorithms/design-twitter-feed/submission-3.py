class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.followers = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.posts[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.followers[userId] | {userId}

        maxHeap = []

        for uid in users:
            if self.posts[uid]:
                idx = len(self.posts[uid]) - 1
                time, tweetId = self.posts[uid][idx]

                heapq.heappush_max(
                    maxHeap,
                    (time, uid, idx, tweetId)
                )

        res = []

        while maxHeap and len(res) < 10:
            time, uid, idx, tweetId = heapq.heappop_max(maxHeap)
            res.append(tweetId)

            if idx > 0:
                idx -= 1
                time, tweetId = self.posts[uid][idx]

                heapq.heappush_max(
                    maxHeap,
                    (time, uid, idx, tweetId)
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)