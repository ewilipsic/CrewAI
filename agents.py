from crewai import Agent,LLM
from textwrap import dedent

import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

from tools import file_writer_tool
# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py

class CustomAgents:
    def __init__(self):
        self.llm = LLM(model= "gemini/gemini-pro",temperature=0.5,api_key=os.environ["GOOGLE_API_KEY"])

    def Call_Analyser(self):
        return Agent(
            role="Expert Emergency Identifier",
            backstory=dedent(f"""You a smart Identifier that has always been able to remove useless info and deliver a consise summary of the issues at hand"""),
            goal=dedent(f"""Given a distress call to the emergency services
                            Extract the Nature of the issue and key insights
                        """),
            #tools=[],
            allow_delegation=False,
            verbose=False,
            llm=self.llm,
        )

    def Department_Decider(self):
        return Agent(
            role="Expert Emergency response co-ordinator",
            backstory=dedent(f"""You a experienced emergency response Co-ordinator who has a history of making correct emergency responses"""),
            goal=dedent(f"""Given information about a emergency
                            You will output which response services
                            And key details they would need to know to take effective action
                        """),
            tools=[],
            allow_delegation=False,
            verbose=False,
            llm=self.llm,
        )

    def Department_messenger(self):
        return Agent(
            role="Expert interdepartment Communicator",
            backstory=dedent(f"""You Great at writing emails to deprtments ordering them to organise a response and providing needed info"""),
            goal=dedent(f"""given a list of departments to be contacted 
                            you will draft a email to each of them individualy,giving them relavent info on the emergency happening currently
                            and informing them about the other departments that wil be on the scene
                        
                            
                        """),
            #tools=[file_writer_tool],
            allow_delegation=False,
            verbose=False,
            llm=self.llm,
        )
    def Cilivian_communicator(self):
        return Agent(
            role="Expert Civilian Communicator",
            backstory=dedent(f"""You have years of experience informing cilivians about what to do in the current situation while keeping them calm"""),
            goal=dedent(f"""
                            Given information about the response to the current issue
                            1)Give the civilian instructions on: How to stay safe until help arrives
                            2)Try to calm them with your response

                            
                        """),
            #tools=[file_writer_tool],
            allow_delegation=False,
            verbose=False,
            llm=self.llm,
        )

