# strategy.py - AI battle strategy for the Gladiator Colosseum

import random

class BattleStrategy:
    def __init__(self, config):
        """Initialize the battle strategy based on configuration."""
        self.strategy_name = config.get('strategy', 'default')
        self.attack_power = config.get('attack_power', 50)
        self.defense_power = config.get('defense_power', 30)
        self.luck_factor = config.get('luck_factor', 0.2)
        print(f"Initialized Battle Strategy: {self.strategy_name}")

    def execute_strategy(self):
        """Execute the chosen battle strategy and return the result."""
        base_outcome = self.attack_power - (self.defense_power / 2)
        luck_adjustment = random.uniform(-self.luck_factor, self.luck_factor) * base_outcome
        final_outcome = base_outcome + luck_adjustment

        # Determine result based on outcome
        if final_outcome > 50:
            return "Victory! Your AI Gladiator dominated the arena."
        elif final_outcome > 20:
            return "Draw! The battle was intense, but no clear winner emerged."
        else:
            return "Defeat! Your AI Gladiator was overpowered."

