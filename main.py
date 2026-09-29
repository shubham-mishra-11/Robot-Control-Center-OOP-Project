class Sensor:
    """Base class for all sensors."""

    def __init__(self, sensor_id, name, type):
        self.sensor_id = sensor_id
        self.name = name
        self.type = type


class Robot:
    """Base class for all robots."""

    def __init__(self, robot_id, name, battery, status):
        self.robot_id = robot_id
        self.name = name
        self._battery = 0
        self.battery = battery
        self.status = status
        self.sensors = []
        
    def battery(self):
        """Getter: returns the internal _battery attribute."""
        return self._battery    
    
    def battery(self, value):
        """Setter: validates battery bounds whenever updated."""
        if value < 0 or value > 100:
            raise ValueError("Battery level must be between 0 and 100.")
        self._battery = value

    def add_sensor(self, sensor):
        """Adds a sensor to the robot's sensor list."""
        self.sensors.append(sensor)
        
    def check_sensor(self, sensor_id):
        """Checks if a sensor exists in the robot's sensor list by ID."""
        if len(self.sensors) == 0:
            print("No sensors are available.")
        else:
            for sensor in self.sensors:
                print(f"Sensor found: {sensor}")

    def move(self):
        """Moves the robot."""
        print(f"{self.name} is moving.")

    def __str__(self):
        """Displays the robot's current status."""
        return f"Robot: {self.name} ID: {self.robot_id} Battery: {self.battery}% Status: {self.status}"

class RoboticArm(Robot):
    """Class for robotic arms."""
    def __init__(self, robot_id, name, battery, status, joint_count):
        super().__init__(robot_id, name, battery, status)
        self.joint_count = joint_count

    def pick_up_object(self, object):
        """Picks up an object."""
        print(f"{self.name} is picking up {object}.")

    def place_object(self, object):
        """Places an object."""
        print(f"{self.name} is placing {object}.")

    def __str__(self):
        return f"super().__str__(), Joint Count: {self.joint_count}"

class DroneRobot(Robot):
    """Class for drone robots."""
    def __init__(self, robot_id, name, battery, status, max_altitude):
        super().__init__(robot_id, name, battery, status)
        self.max_altitude = max_altitude

    def fly(self):
        """Makes the drone robot fly."""
        print(f"{self.name} is flying at maximum altitude of {self.max_altitude} feet.")

    def land(self):
        """Makes the drone robot land."""
        print(f"{self.name} is landing.")

    def __str__(self):
        return f"super().__str__(), Maximum Altitude: {self.max_altitude} feet"

def main():
    pass
if __name__ == "__main__":
    main()