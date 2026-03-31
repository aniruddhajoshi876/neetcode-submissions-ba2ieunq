import heapq
class Twitter:

    def __init__(self):
        self.followmap = {}
        self.tweetmap = {}
        self.time = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetmap:
            self.tweetmap[userId] = []
        self.tweetmap[userId].append((self.time, tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.followmap:
            self.followmap[userId] = set()
            self.followmap[userId].add(userId)
        if not self.tweetmap:
            return []
        followees = self.followmap[userId]
        feed = []
        for user in followees:
            if user not in self.tweetmap:
                continue
            for tweet in self.tweetmap[user]:
                if len(feed) >= 10:
                    if feed[0] < tweet:
                        heapq.heappushpop(feed, tweet)
                else:
                    heapq.heappush(feed, tweet)
        feed.sort(reverse=True)
        return [tw for time,tw in feed] if feed else []  

    def follow(self, followerId, followeeId):
        if followerId not in self.followmap:
            self.followmap[followerId] = set()
            self.followmap[followerId].add(followerId)
        self.followmap[followerId].add(followeeId)
        return None

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId: return
        try:
            self.followmap[followerId].remove(followeeId)
        except KeyError:
            return
