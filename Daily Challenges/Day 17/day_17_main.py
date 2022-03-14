
# Classes should be PascalCased
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.follower_count = 0
        self.following_names = []
        self.follower_names = []
        print(f"User {id} created. Welcome {name}.")

    def follow(self, user_to_follow):
        self.following_names.append(user_to_follow.name)
        user_to_follow.follower_names.append(self.name)
        user_to_follow.follower_count += 1

user_1 = User("001", "Seth")
user_2 = User("002", "Josh")
user_2.follow(user_1)
print(user_2.following_names)
print(user_1.follower_names)
print(user_1.follower_count)





class Car:
    def __init__(self, car_type, seats, horsepower):
        self.car_type = car_type
        self.seats = seats
        self.horsepower = horsepower

    def enter_race_mode(self):
        self.seats = 2


race_car = Car("racecar", "4", "300")



