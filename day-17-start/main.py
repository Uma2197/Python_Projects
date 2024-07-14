# Imagine this as instagram
# Each user will have an id and a name
# Initially, the following and followers count for any user will be 0. (default)
# Then, if someone is following somebody, then the "Following" count will be incremented for the
# first user and the "Followers" count will be incremented for the next user
class User:
    # username and id are the attributes of instagram (what it has)
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # The idea gets implemented here
    # follow is one of the methods that instagram could have. (What it does)
    def follow(self, user):
        user.followers += 1
        self.following += 1


# Here, we are defining the user ids and usernames for each user.
user_1 = User("001", "Uma")
user_2 = User("002", "Vicky")

# User 1 is deciding to follow user 2
user_1.follow(user_2)

# Now, User 2 has got 1 follower(user 1) and user 1 is now following 1 other user,(user 2)
print(user_1.followers, user_2.followers)
print(user_1.following, user_2.following)
