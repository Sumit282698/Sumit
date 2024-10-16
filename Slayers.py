import random


class SlayerQuest:
    def __init__(self, player_level):
        self.player_level = player_level

    def calculate_damage(self, player_level, boss_level):
        # Some hypothetical damage calculation based on player and boss level.
        return random.randint(player_level, boss_level * 2)

    def start_quest(self, boss_level):
        print(f"Starting slayer quest against level {boss_level} boss...")
        boss_health = boss_level * 100
        player_health = self.player_level * 200

        while boss_health > 0 and player_health > 0:
            player_damage = self.calculate_damage(self.player_level, boss_level)
            boss_damage = self.calculate_damage(boss_level, self.player_level)

            boss_health -= player_damage
            player_health -= boss_damage

            print(f"Player dealt {player_damage} damage to the boss.")
            print(f"Boss dealt {boss_damage} damage to the player.")
            print(f"Player health: {player_health} | Boss health: {boss_health}\n")

        if boss_health <= 0:
            print("Congratulations! You defeated the boss!")
        else:
            print("Oh no! The boss defeated you. Better luck next time!")

if __name__ == "__main__":
    player_level = int(input("Enter your player level: "))
    boss_level = int(input("Enter the level of the boss: "))

    quest = SlayerQuest(player_level)
    quest.start_quest(boss_level)
