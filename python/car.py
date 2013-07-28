class Car(object):

    def __init__(self, acceleration, braking):
        """
        :param acceleration: How many mph per second the car can accelerate at (ignoring wind resistance)
        :param braking: How many mph per second the car can decelerate at
        """
        self.acceleration = acceleration
        self.braking = braking

