# Setting up Our Robot

class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0

test_bot = DriveBot()
test_bot.motor_speed = 30
test_bot.direction = 90
test_bot.sensor_range = 25

print(test_bot.motor_speed)
print(test_bot.direction)
print(test_bot.sensor_range)