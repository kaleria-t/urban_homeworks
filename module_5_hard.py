from time import sleep
class User:
    userdict = {}
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        User.userdict[self.nickname]=self.password

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration # продолжительность, секунды
        self.time_now = time_now # секунда остановки (изначально 0)
        self.adult_mode = adult_mode

class UrTube:
    videos = []
    users = []
    current_user = None

    def log_in(self, nickname, password):
        if nickname in User.userdict:
            if hash(password) == User.userdict[nickname]:
                UrTube.current_user = nickname

    def register(self, nickname, password, age):
        if nickname not in UrTube.users:
            UrTube.users.append(nickname)
        else:
            print(f"Пользователь {nickname} уже существует")

ur = UrTube()
ur.register('user_1', 1212, 34)
ur.log_in('user_1', 1212)
print(ur.current_user)
print(User.userdict)
print(UrTube.current_user)