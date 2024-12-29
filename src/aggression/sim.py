class Individual:
    def __init__(self):
        self.hp = 100
        #...
        pass

    def act(self, env):
        # define behavior here
        pass

class Dove(Individual):
    #...

    pass

class Hawk(Individual):
    pass


class Environment:
    def __init__(self):
        self.food = 0
        # init environment status
        pass

    def update(self):
        pass

class Simulator:
    def __init__(self):
        self.tick = 0
        self.env = Environment()
        self.population = [Individual()] * 1000
        pass

    def run(self):
        while True:
            self.step()
        pass

    def step(self):

        # update environment
        self.env.update()

        # do something here
        for individual in self.population:
            individual.act(self.env)


        self.tick += 1

    

