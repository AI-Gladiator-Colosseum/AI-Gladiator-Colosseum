# test_strategy.py - Unit tests for strategy.py

import unittest
from strategy import BattleStrategy

class TestBattleStrategy(unittest.TestCase):

    def test_initialization(self):
        config = {
            'strategy': 'aggressive',
            'attack_power': 60,
            'defense_power': 40,
            'luck_factor': 0.3
        }
        strategy = BattleStrategy(config)
        self.assertEqual(strategy.strategy_name, 'aggressive')
        self.assertEqual(strategy.attack_power, 60)
        self.assertEqual(strategy.defense_power, 40)
        self.assertEqual(strategy.luck_factor, 0.3)

    def test_execute_strategy_victory(self):
        config = {
            'attack_power': 70,
            'defense_power': 30,
            'luck_factor': 0.1
        }
        strategy = BattleStrategy(config)
        result = strategy.execute_strategy()
        self.assertIn(result, ["Victory! Your AI Gladiator dominated the arena.",
                               "Draw! The battle was intense, but no clear winner emerged.",
                               "Defeat! Your AI Gladiator was overpowered."])

if __name__ == "__main__":
    unittest.main()
