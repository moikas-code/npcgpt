import os
from dotenv import load_dotenv
from langchain import OpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain.tools import BaseTool, StructuredTool, Tool, tool


from npc_agent import NPC_AGENT

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.environ.get('OPENAI_API_KEY')


def main(_input):

    memory = ConversationBufferMemory(memory_key="chat_history")

    llm = OpenAI(temperature=0)
    tools = [
        Tool(
            name="Status",
            func=NPC_AGENT.status,
            description="Perform Acton: Status"
        ),
        Tool(
            name="Defend",
            func=NPC_AGENT.Defend,
            description="Perform Acton: Defend"
        ),
        Tool(
            name="Attack",
            func=NPC_AGENT.Attack,
            description="Perform Acton: Attack"
        ),
        Tool(
            name="Heal",
            func=NPC_AGENT.Heal,
            description="Perform Acton: Heal"
        )
    ]

    agent_chain = initialize_agent(
        tools, llm, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True, memory=memory)

    while True:
        user_input = _input
        if user_input != 'end chat':
            agent_chain.run(user_input)
            main(input(""))


if __name__ == "__main__":
    main(input(""))
