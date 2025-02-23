class Player:
    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team


    def introduce(self):
        print(f"Hello! I am {self.name}, I play for {self.team}.")

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players=[]

    def __str__(self):
        return self.team_name

    def add_player(self, name): #Player 클래스를 직접적으로 사용하는 대신 이걸 쓸거임
        new_player = Player(name, self.team_name)
        self.players.append(new_player)

    def introduce(self):
        self.player_names = [player.name for player in self.players]
        return f"This is {self.team_name} and members are {self.player_names}!"
    
    def show_players(self):
        for player in self.players:
            player.introduce()

team_blue = Team("Team Blue")
team_blue.add_player("Boyoon Choi")
team_red = Team("Team Red")
team_red.add_player("Nico")
team_red.add_player("lynn")

team_red.show_players()
# print(team_blue.introduce())
# print(team_red.introduce())