from enum import Enum
from typing import Optional, Type
from langchain.tools import BaseTool, StructuredTool, Tool, tool
from langchain.callbacks.manager import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun


class Actions(Enum):
    MOVE = "MOVE"
    ATTACK = "ATTACK"
    DEFEND = "DEFEND"
    TALK = "TALK"


# @tool("NPC_AGENT", return_direct=True)
def NPC_AGENT(query: str, action: str = "Talk") -> str:
    """Use the tool."""
    try:
        action = Actions(action.upper())
        match action.name:
            case "TALK":
                return "I was able to perform Speak: " + action.name + " with query: " + query
            case "MOVE":
                return "I was able to perform Move: " + action.name + " with query: " + query
            case "ATTACK":
                return "I was able to perform Attack: " + action.name + " with query: " + query
            case "DEFEND":
                return "I was able to perform Defend: " + action.name + " with query: " + query
            case _:
                action-default

    except ValueError:
        raise ValueError(f"Action {action} is not a valid action.")
