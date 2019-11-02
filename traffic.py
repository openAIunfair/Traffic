class rail:
    def __init__(self):
        self.speed_limit = 1
        self.length = 100
        self.carriers = {}
        self.previous = None
        self.next = None


class carrier:
    def __init__(self, rail, pos):
        self.rail = rail
        self.speed = 0
        self.pos = pos
        self.acceleration = 0
        self.max_acc = 0.1
        self.max_break = 0.2

    def step(self):
        self.pos += self.speed
        self.speed += self.acceleration
