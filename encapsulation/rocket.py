from vector3 import Vector3

# The SensorData class provides an interface, and an implementation.
class SensorData:
    gps_flight_path: list[Vector3]
    acceleration: Vector3
    velocity: Vector3
    position: Vector3

    def __init__(self) -> None:
        self.gps_flight_path = [Vector3()]
        self.acceleration = Vector3()
        self.velocity = Vector3()
        self.position = Vector3()
        

    def query_gps(self) -> None:
        new_position = Vector3()

        # Here, we would somehow retrieve the rocket's current position
        # from the GPS hardware and update the x/y/z coordinates of
        # new_position accordingly. Of course, reading from GPS
        # hardware is beyond the scope of this course, so just use your
        # imagination here.
        # ...

        # Append new position to self.gps_flight_path
        self.gps_flight_path.append(new_position)

    def query_accelerometer(self) -> None:
        # Here, we would somehow query the rocket's current
        # acceleration from the accelerometer and update
        # self.acceleration accordingly
        # Use your imagination.
        # ...

        # Now, update velocity and position accordingly (note: this is
        # an oversimplification)
        self.velocity.x += self.acceleration.x
        self.velocity.y += self.acceleration.y
        self.velocity.z += self.acceleration.z
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
        self.position.z += self.velocity.z

    # The goal of encapsulation is to hide away brittle implementation
    # details, or design decisions. And you absorb their coupling
    # with stable interfaces in front of them.

    # YAGNI

    # This is known as a getter. A getter is just a method
    # that returns data that's somehow stored within the
    # object in question.
    def get_position(self) -> Vector3:
        return self.position

    def get_velocity(self) -> Vector3:
        return self.velocity

    def get_acceleration(self) -> Vector3:
        return self.acceleration
        

class Rocket:
    # This list of Vector3 objects keeps a record of the rocket's
    # flight path so far, relative to the launch pad, as sourced from
    # the rocket's GPS module. The last element
    # in the list represents the rocket's current location.
    deployed_parachute: bool
    
    # Composition
    sensor_data: SensorData
 
    def __init__(self) -> None:
        # Rocket is initially resting on the launch pad, so initialize
        # gps_flight_path to contain a single Vector3 object with x, y,
        # and z all equal to zero.
        self.deployed_parachute = False
        self.sensor_data = SensorData()

    def query_sensor_data(self) -> None:
        # Delegation.
        # We have delegated the responsibility of querying the individual
        # sensors to the SensorData class.
        self.sensor_data.query_gps()
        self.sensor_data.query_accelerometer()

    def actuate_fins(self) -> None:
        # Get rocket's current position
        current_velocity = self.sensor_data.get_velocity()

        # Here, we would somehow use current_position and
        # current_velocity to determine how the fins should be actuated
        # so as to guide the rocket along the target trajectory.
        # That's beyond the scope of this course, so use your
        # imagination here as well.
        # ...

    def deploy_parachute_if_ready(self) -> None:
        if self.deployed_parachute:
            # Parachute has already been deployed. Do nothing.
            return

        # Get rocket's current position
        current_velocity = self.sensor_data.get_velocity()

        # Let's say the parachute is meant to be deployed at
        # apogee (peak of trajectory). Let's say the y coordinate
        # dimension represents elevation. Then we should deploy the
        # parachute when the y coordinate of current_velocity becomes
        # non-positive (when the rocket is no longer moving upward)
        if current_velocity.y <= 0:
            # Here, we would somehow engage with the hardware to
            # deploy the parachute. Again, use your imagination.
            # ...

            self.deployed_parachute = True

    def log_data(self) -> None:
        # Get rocket's current position
        
        current_velocity = self.sensor_data.get_velocity()
        current_position = self.sensor_data.get_position()
        current_acceleration = self.sensor_data.get_acceleration()

        # Here, we would somehow send current_position and
        # current_velocity to the ground receiver for monitoring.
        # Use your imagination.
        # ...
