class Instagram:
    def __init__(self, username, accounts, celebrity, reels):
        self.username = username
        self.accounts = accounts
        self.celebrity = celebrity
        self.reels = reels

    def users(self):
        print(f"my account {self.username} is this")


class Reels:
    def __init__(self, likes, comments):
        self.likes = likes
        self.comments = comments


reels = Reels("10k", "2.5k")
instagram = Instagram("whylighter", "3", "Aurthur chen", reels)
print(instagram.accounts, instagram.reels.likes, instagram.reels.comments)

reels1 = Reels("50k", "5k")
instagram1 = Instagram("whyprincess", "2", "Zhang jingyi", reels1)
instagram1.users()
print(instagram1.username, instagram1.celebrity, instagram1.reels.likes)
