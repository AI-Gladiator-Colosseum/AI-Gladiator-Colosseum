# test_main.py - Unit tests for main.py

import unittest
from unittest.mock import patch, MagicMock
import main

class TestMain(unittest.TestCase):

    @patch('main.load_config')
    def test_load_config(self, mock_load_config):
        mock_load_config.return_value = {
            'agent_name': 'TestAgent',
            'strategy': 'test_strategy'
        }
        config = main.load_config()
        self.assertEqual(config['agent_name'], 'TestAgent')
        self.assertEqual(config['strategy'], 'test_strategy')

    @patch('main.BattleStrategy')
    def test_initialize_agent(self, mock_battle_strategy):
        mock_battle_strategy.return_value = MagicMock(strategy_name="Test Strategy")
        config = {'agent_name': 'TestAgent'}
        agent = main.initialize_agent(config)
        self.assertEqual(agent.strategy_name, "Test Strategy")

    def test_run_battle_scenario(self):
        mock_strategy = MagicMock()
        mock_strategy.execute_strategy.return_value = "Victory!"
        result = main.run_battle_scenario(mock_strategy)
        self.assertIsNone(result)  # Function does not return a value but prints output

if __name__ == "__main__":
    unittest.main()
