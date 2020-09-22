# https://leetcode.com/problems/design-twitter/

# Design Twitter

# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

# postTweet(userId, tweetId): Compose a new tweet.
# getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
# follow(followerId, followeeId): Follower follows a followee.
# unfollow(followerId, followeeId): Follower unfollows a followee.
# Example:

# Twitter twitter = new Twitter();

# // User 1 posts a new tweet (id = 5).
# twitter.postTweet(1, 5);

# // User 1's news feed should return a list with 1 tweet id -> [5].
# twitter.getNewsFeed(1);

# // User 1 follows user 2.
# twitter.follow(1, 2);

# // User 2 posts a new tweet (id = 6).
# twitter.postTweet(2, 6);

# // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# // Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.getNewsFeed(1);

# // User 1 unfollows user 2.
# twitter.unfollow(1, 2);

# // User 1's news feed should return a list with 1 tweet id -> [5],
# // since user 1 is no longer following user 2.
# twitter.getNewsFeed(1);


import heapq
from typing import List
class Twitter:

    def __init__(self):

        self.followers = {}
        self.following = {}
        self.tweetMap = {}
        self.globalcount = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.globalcount -= 1
        if userId in self.tweetMap:
            self.tweetMap[userId].append((self.globalcount,tweetId))
        else:
            self.tweetMap[userId] = [(self.globalcount, tweetId)]

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        if userId in self.tweetMap:
            heap.extend(self.tweetMap[userId])
        for id in self.following.get(userId,[]):
            if id != userId:
                heap.extend(self.tweetMap.get(id,[]))

        heapq.heapify(heap)
        res = []
        while heap and len(res) < 10:
            item = heapq.heappop(heap)
            res.append(item[1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:

        followeeSet = set()
        if followerId in self.following:
            self.following[followerId].add(followeeId)
        else:
            self.following[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId in self.following:
            if followeeId in self.following[followerId]:
                self.following[followerId].remove(followeeId)

t = Twitter()
t.postTweet(11,220)
t.postTweet(11,221)
t.postTweet(2,12)
t.follow(11, 2)
t.follow(2, 11)
print("followers: {0}".format(t.followers))
print("following: {0}".format(t.following))
print("tweetMap: {0}".format(t.tweetMap))
print("globalcount: {0}".format(t.globalcount))
print(t.getNewsFeed(11))
