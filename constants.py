class Constants():

    __instance = None

    def __new__(cls):
        if not Constants.__instance:
            Constants.__instance = object.__new__(cls)
        return Constants.__instance

    def __init__(self):
        self.ytmLoginLink: str = "https://www.ytmonster.net/login"
        self.ytmDashboardLink: str = "https://www.ytmonster.net/dashboard"
        self.ytLoginLink: str = "https://www.youtube.com/account"
        self.ytmCookies: str = "ytm_cookies.pkl"
        self.ytCookies: str = "yt_cookies.pkl"