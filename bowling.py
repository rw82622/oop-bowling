class Game:
    all_scores = {}
    player_id_key = 0
    
    def __init__(self):
        self.scores = []
        self.current_score = 0
        self.frame_number = 0
        self.player_id = Game.player_id_key + 1
        Game.player_id_key += 1
        
    def play(self, first_roll):
        if self.frame_number < 10:
            frame = []
            if first_roll == 10:
                frame += [10, -2]
                self.current_score += 10
            else:
                second_roll = input('How many pins did you knock down on the second roll for the current frame? ')
                if first_roll + second_roll == 10:
                    frame = [10, -1]
                    self.current_score += 10
                else:
                    frame_points = first_roll + second_roll
                    frame = [frame_points, 0]
                    self.current_score += frame_points
            self.scores += frame
            Game.all_scores.update({self.player_id : self.scores})
            if ((len(self.scores) > 1) and (self.scores[self.frame_number - 1][1] == -1)):
                self.current_score += first_roll
            if ((len(self.scores) > 2) and (self.scores[self.frame_number - 2][1] == -2)):
                if self.scores[self.frame_number -1][1] != -2:
                    self.current_score += (self.scores[self.frame_number -1][0])
                else:
                    self.current_score += ((self.scores[self.frame_number -1][0]) + first_roll)
            self.frame_number += 1
        else:
            print('Sorry, The Game is Over!')
            
    def get_current_score(self):
        return self.current_score
        
    