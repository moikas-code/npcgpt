import os
from dotenv import load_dotenv
from langchain import OpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain.tools import BaseTool, StructuredTool, Tool, tool


from npc_agent import NPC_AGENT

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.environ.get('OPENAI_API_KEY')

tools = [Tool(
    name="NPC_AGENT",
    func=NPC_AGENT,
    description="useful for when I need to move in the world"
)]

memory = ConversationBufferMemory(memory_key="chat_history")

llm = OpenAI(temperature=0)

agent_chain = initialize_agent(
    tools, llm, agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory)


def main(_input):
    while True:
        user_input = _input
        if user_input == 'end chat':
            break
        else:
            agent_chain.run(input=_input)
            main(input("User: "))


if __name__ == "__main__":
    main(input("User: "))
