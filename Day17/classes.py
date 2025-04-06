class User:
    def __init__(self, self_id, user_username):
        self.id = self_id
        self.username = user_username
        self.followers = 0
        self.following = 0

    def follow(self, user):
         self.following += 1
         user.followers += 1
    
    def __hash__(self):
        return hash((self.id, self.username))
    
    def __eq__(self, other):
        return self.id == other.id and self.username == other.username

user_1 = User("123", "Ognyan")
user_2 = User("123", "Ognyan")

print(f"{hash(user_1)=}")
print(f"{hash(user_2)=}")

user_1.follow(user_2)
