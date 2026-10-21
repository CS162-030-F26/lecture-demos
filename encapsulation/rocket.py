from vector3 import Vector3

class Rocket:
    # This list of Vector3 objects keeps a record of the rocket's
    # flight path so far, relative to the launch pad, as sourced from
    # the rocket's GPS module. The last element
    # in the list represents the rocket's current location.
    gps_flight_path: list[Vector3]
    deployed_parachute: bool

    acceleration: Vector3
    velocity: Vector3
    position: Vector3
    
    def __init__(self) -> None:
        # Rocket is initially resting on the launch pad, so initialize
        # gps_flight_path to contain a single Vector3 object with x, y,
        # and z all equal to zero.
        self.gps_flight_path = [Vector3()]
        self.deployed_parachute = False
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

    def actuate_fins(self) -> None:
        # Get rocket's current position
        current_position = \
            self.gps_flight_path[len(self.gps_flight_path) - 1]

        # Approximate rocket's current velocity based on difference
        # between last two positions
        previous_position = \
            self.gps_flight_path[len(self.gps_flight_path) - 2]
        current_velocity = Vector3()
        current_velocity.x = current_position.x - previous_position.x
        current_velocity.y = current_position.y - previous_position.y
        current_velocity.z = current_position.z - previous_position.z

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
        current_position = \
            self.gps_flight_path[len(self.gps_flight_path) - 1]

        # Approximate rocket's current velocity based on difference
        # between last two positions
        previous_position = \
            self.gps_flight_path[len(self.gps_flight_path) - 2]
        current_velocity = Vector3()
        current_velocity.x = current_position.x - previous_position.x
        current_velocity.y = current_position.y - previous_position.y
        current_velocity.z = current_position.z - previous_position.z

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
        current_position = \
            self.gps_flight_path[len(self.gps_flight_path) - 1]
        
        # Approximate rocket's current velocity based on difference
        # between last two positions
        previous_position = \
            self.gps_flight_path[len(self.gps_flight_path) - 2]
        current_velocity = Vector3()
        current_velocity.x = current_position.x - previous_position.x
        current_velocity.y = current_position.y - previous_position.y
        current_velocity.z = current_position.z - previous_position.z

        # Here, we would somehow send current_position and
        # current_velocity to the ground receiver for monitoring.
        # Use your imagination.
        # ...
