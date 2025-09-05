import time

class Robot:
    potulation =0

    def __init__(self, name):
        self.name =name
        print("initializing {}".format(self.name))
        # when the robort is crated add it to the population
        Robot.potulation += 1


    def die(self):
        print("(robot being destroyed{}: )".format(self.name))
        Robot.potulation -=1

        if Robot.potulation ==0:
            print("{} was the last one ".format(self.name))
        else:
            print("there is still {} robot working.".format(Robot.potulation))

    def say_hi(self):
        print(" greetings my master calls me {}.".format(self.name))


    @classmethod
    def how_many(cls):
        print("we have {} robots ".format(cls.potulation))

print()
d1 = Robot("mark1")
time.sleep(3)
d1.say_hi()
time.sleep(1)
Robot.how_many()

print()
time.sleep(1)
d2 = Robot("mark2")
time.sleep(3)
d2.say_hi()
time.sleep(1)
Robot.how_many()
print("\n Robots can now work here.\n")
print("\nRoborts are done working . Time to dstroy them.\n")
time.sleep(2)
d1.die()
time.sleep(2)
d2.die()
time .sleep(2)
Robot.how_many()