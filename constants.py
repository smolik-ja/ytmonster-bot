class Constants():

    __instance = None

    def __new__(cls):
        if not Constants.__instance:
            Constants.__instance = object.__new__(cls)
        return Constants.__instance

    def __init__(self):
        self.ytmLoginLink: str = "https://www.ytmonster.net/login"
        self.ytmDashboardLink: str = "https://www.ytmonster.net/dashboard"
        self.cookiesName: str = "cookies.pkl"