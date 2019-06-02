class Twitter:

    def __init__(self):
        self.followed = dict()
        self.posted_tweet = dict()

    def post_tweet(self, user_id, tweet_id):
        import time
        self.posted_tweet.setdefault(user_id, []).insert(0, (tweet_id, time.time()))

    def get_news_feed(self, user_id):
        res = []
        self_published = self.posted_tweet.get(user_id, [])
        res.extend(self_published)
        
        followees = self.followed.get(user_id, set())
        for f in followees:
            res.extend(self.posted_tweet.get(f, [])[:10])
        
        res.sort(key=lambda x: x[1], reverse=True)  # sorted by publish time
        feed = list(map(lambda x: x[0], res[:10]))
        return feed

    def follow(self, follower_id, followee_id):
        if follower_id != followee_id:  # one can't follow himself
            self.followed.setdefault(follower_id, set()).add(followee_id)

    def unfollow(self, follower_id, followee_id):
        followed_ids = self.followed.get(follower_id, set())
        followed_ids.discard(followee_id)


if __name__ == '__main__':
    twitter = Twitter()

    # User 1 posts a new tweet (id = 5).
    twitter.post_tweet(1, 5)
    
    # User 1's news feed should return a list with 1 tweet id -> [5].
    feed = twitter.get_news_feed(1)
    print(feed)
    
    # User 1 follows user 2.
    twitter.follow(1, 2)
    
    # User 2 posts a new tweet (id = 6).
    twitter.post_tweet(2, 6)
    
    # User 1's news feed should return a list with 2 tweet ids -> [6, 5].
    # Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
    feed = twitter.get_news_feed(1);
    print(feed)
    
    # User 1 unfollows user 2.
    twitter.unfollow(1, 2);
    
    # User 1's news feed should return a list with 1 tweet id -> [5],
    # since user 1 is no longer following user 2.
    feed = twitter.get_news_feed(1)
    print(feed)
