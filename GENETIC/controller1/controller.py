import controller_template as controller_template

from controller1 import genetic_algorithm


class Controller(controller_template.Controller):
    def __init__(self, track, evaluate=True, bot_type=None):
        super().__init__(track, evaluate=evaluate, bot_type=bot_type)



    #######################################################################
    ##### METHODS YOU NEED TO IMPLEMENT ###################################
    #######################################################################

    def take_action(self, parameters: list) -> int:
        """
        :param parameters: Current weights/parameters of your controller
        :return: An integer corresponding to an action:
        1 - Right
        2 - Left
        3 - Accelerate
        4 - Brake
        5 - Nothing
        """




        features = self.compute_features(self.sensors)

        

        track_distance_left = features[0]
        track_distance_center = features[1]
        track_distance_right = features[2]
        on_track = features[3]
        car_velocity = features[4]
        enemy_distance = features[5]
        enemy_detected = features[6] 
        
        R = parameters[0] + (parameters[1] * track_distance_center/(track_distance_left + 0.0001))
        L = parameters[2] + (parameters[1] * track_distance_center/(track_distance_right + 0.0001))
        A = parameters[3] + (parameters[4] * track_distance_center)
        B = parameters[5] + (parameters[6] * car_velocity) + parameters[7]*-track_distance_center
        lista = [R,L,A,B]
       
        

        maior = lista[2]
        x=2
        
        for i in range(0,len(lista)):
            if(lista[i] > maior):
                maior = lista[i]
                x = i

        return x + 1
        



    def compute_features(self, sensors):
        """
        :param sensors: Car sensors at the current state s_t of the race/game
        contains (in order):
            track_distance_left: 1-100
            track_distance_center: 1-100
            track_distance_right: 1-100
            on_track: 0 or 1
            checkpoint_distance: 0-???
            car_velocity: 10-200
            enemy_distance: -1 or 0-???
            position_angle: -180 to 180
            enemy_detected: 0 or 1
          (see the specification file/manual for more details)
        :return: A list containing the features you defined
        """
        track_distance_left = (sensors[0] - 1) /(100 - 1)
        track_distance_center = (sensors[1] - 1) /(100 - 1)
        track_distance_right = (sensors[2] - 1) /(100 - 1)
        on_track = sensors[3]
        car_velocity = (sensors[5] - 10) / (200 - 10)
        enemy_distance = sensors[6]
        enemy_detected = sensors[7]

        return [track_distance_left , track_distance_center,track_distance_right,on_track,car_velocity,enemy_distance,enemy_detected]
        




    def learn(self, weights) -> list:
        """
        IMPLEMENT YOUR LEARNING METHOD (i.e. YOUR LOCAL SEARCH ALGORITHM) HERE

        HINT: you can call self.run_episode (see controller_template.py) to evaluate a given set of weights
        :param weights: initial weights of the controller (either loaded from a file or generated randomly)
        :return: the best weights found by your learning algorithm, after the learning process is over
        """
        best_weights = genetic_algorithm.GeneticSolution(self)
        print(self.run_episode(best_weights))
        return best_weights
