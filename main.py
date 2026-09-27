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

class MobileRobot(Robot):
    """Class for mobile robots."""
    pass
    

class RoboticArm(Robot):
    """Class for robotic arms."""

    def main():
        pass

class Sensor:
    """Base class for all sensors."""

    def __init__(self, sensor_id, name, type):
        self.sensor_id = sensor_id
        self.name = name
        self.type = type