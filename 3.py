class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def move(self):
        if self.battery < 20:
            print(f"{self.name}: Battery too low to move ({self.battery}%)")
            return False
        return True

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"{self.name}: Charging complete. Battery now at {self.battery}%")


class DeliveryRobot(Robot):
    def move(self):
        if not super().move():
            return
        print(f"{self.name}: Moving to delivery location")


class SecurityRobot(Robot):
    def move(self):
        if not super().move():
            return
        print(f"{self.name}: Patrolling the assigned area")


class RescueRobot(Robot):
    def move(self):
        if not super().move():
            return
        print(f"{self.name}: Moving toward disaster location")


if __name__ == "__main__":
    robot_units = [
        DeliveryRobot("DeliBot-1", 50),
        SecurityRobot("GuardBot-2", 15),
        RescueRobot("RescueBot-3", 80)
    ]

    for unit in robot_units:
        unit.move()
        unit.charge(30)
        unit.move()
        print("-" * 30)
