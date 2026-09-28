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
        if isinstance(sensor, Sensor):
            self.sensors.append(sensor)
        else:
            raise TypeError("Only Sensor instances can be added.")
    def remove_sensor(self, sensor_id):
        """Removes a sensor from the robot's sensor list by ID."""
        self.sensors = [s for s in self.sensors if s.sensor_id != sensor_id]

class RoboticArm(Robot):
    """Class for robotic arms."""
    def __init__(self, robot_id, name, battery, status, joint_count):
        super().__init__(robot_id, name, battery, status)
        self.joint_count = joint_count

class DroneRobot(Robot):
    """Class for drone robots."""
    def __init__(self, robot_id, name, battery, status, max_altitude):
        super().__init__(robot_id, name, battery, status)
        self.max_altitude = max_altitude



def main():
    pass
if __name__ == "__main__":
    main()