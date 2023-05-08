from enum import Enum
from typing import Optional, Type
from langchain.tools import BaseTool, StructuredTool, Tool, tool
from langchain.callbacks.manager import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun

from lib.attack import attack_tool


class Actions(Enum):
    MOVE = "MOVE"
    ATTACK = "ATTACK"
    DEFEND = "DEFEND"
    TALK = "TALK"


entities = {
    "user": {
        "name": "USER",
        "health": 100,
        "attack": 30,
        "defend": 42,
    },

    "ai": {
        "name": "AI",
        "health": 100,
        "attack": 25,
        "defend": 30,
    },

    "monster": {
        "name": "Goblin",
        "health": 100,
        "attack": 25,
        "defend": 25,
    }}


class NPC_AGENT():
    def status(query):
        """Perform Acton: Status"""
        print("Stats: Name:", str(entities[query]["name"]), "Health:", str(entities[query]["health"]), "Attack:", str(
            entities[query]["attack"]), "Defense:", str(entities[query]["defend"]))
        return "Stats:", "Name:", str(entities[query]["name"]), "Health:", str(entities[query]["health"]), "Attack:", str(
            entities[query]["attack"]), "Defense:", str(entities[query]["defend"])

    def Attack(query):
        attack_tool(query,entities)

    def Defend(query):
        """Perform Acton: Defend"""

        print("Defend." + str(entities[query]["defend"]))
        # str(AI['health'] - User['attack'])
        return "Defend." + str(entities[query]["defend"])

    def Heal(query):
        """Perform Acton: Heal"""
        print("Healing " + str(entities[query]['name']) + ", " +
              str(entities[query]['health'] + 10))
        return "Healing " + str(entities[query]['name']) + ", " + str(entities[query]['health'] + 10)
