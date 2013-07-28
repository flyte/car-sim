class Driver(object):

    def __init__(self, speed_limit, reaction_time, urgency):
        """
        :param speed_limit: Max speed the driver is legally allowed to drive
        :param reaction_time: Amount of ms it takes for the driver to react to new conditions
        :param urgency: Multiplier for speed_limit to signify more or less urgency to get to destination
        """
        self.speed_limit = speed_limit
        self.reaction_time = reaction_time
        self.urgency = urgency
        
    def top_speed(self):
        return self.speed_limit * self.urgency
