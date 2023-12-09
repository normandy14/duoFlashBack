class Session:
    def __init__(self, username, password):
        self.lingo = duolingo.Duolingo(username, password)
