# main.py - Entry point for the AI Gladiator Colosseum agent

import yaml
from strategy import BattleStrategy

def load_config(config_file='config.yaml'):
    """Load configuration settings from the YAML file."""
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

def initialize_agent(config):
    """Initialize the AI agent with the given configuration."""
    print("Initializing AI Gladiator...")
    agent_name = config.get('agent_name', 'AI_Warrior')
    battle_strategy = BattleStrategy(config)
    print(f"Agent '{agent_name}' initialized with strategy: {battle_strategy.strategy_name}")
    return battle_strategy

def run_battle_scenario(strategy):
    """Simulate a battle scenario using the configured strategy."""
    print("Starting battle simulation...")
    result = strategy.execute_strategy()
    print(f"Battle Result: {result}")

if __name__ == "__main__":
    # Load configuration
    config = load_config()

    # Initialize AI agent
    ai_agent = initialize_agent(config)

    # Run the battle simulation
    run_battle_scenario(ai_agent)
