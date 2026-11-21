class Limiter:
    def __init__(self, rule, burst=0):
        self.rule, self.burst = rule, burst
