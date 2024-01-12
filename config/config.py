
class Config(object):
    __instance = None
    user_city = "Moscow"
    __user_role = "default"


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Config, cls).__new__(cls)
        return cls.instance

    def __repr__(self):
        return f"This is config file for user settings"

    def set_city(self, city):
        self.user_city = city

if __name__ == "__main__":
    a = Config()
