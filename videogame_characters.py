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
        print(f"This is {self.team_name} and members are {self.player_names}!")
    
    def show_players(self):
        for player in self.players:
            player.introduce()

    # code challenge 1: player를 삭제하는 메소드. name 베이스로 어떻게 object를 찾지??? + 해당 플레이어가 존재하지 않을 경우 에러 처리 생각!
    def rm_player(self, name):
        for player in self.players:
            if player.name == name:
                print(f"{player.name} successfully removed.")
                self.players.remove(player)
                return player
        # if not returned by this point,
        print(f"{name} doesn't exist in {self.team_name}.")
        return -1

    # code challenge 2: 팀의 xp 총합을 보여주는 메소드. xp: experience point
    def total_xp(self):
        sum_xp=0
        for player in self.players:
            sum_xp += player.xp
        return sum_xp


team_blue = Team("Team Blue")
team_blue.add_player("Boyoon Choi")
team_red = Team("Team Red")
team_red.add_player("Nico")
team_red.add_player("lynn")

print(team_red.total_xp())
print(team_blue.total_xp())
