import os
from crewai import Agent, Task, Crew, Process

from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks


# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py




class CustomCrew:
    def __init__(self,call):
        self.call = call
        pass

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        custom_agent_1 = agents.Call_Analyser()
        custom_agent_2 = agents.Department_Decider()
        custom_agent_3 = agents.Department_messenger()
        custom_agent_4 = agents.Cilivian_communicator()
        

        # Custom tasks include agent name and variables as input
        custom_task_1 = tasks.Identify_emergency(
            custom_agent_1,self.call
        )
        custom_task_2 = tasks.Decide_Department(
            custom_agent_2
        )
        custom_task_3 = tasks.Email_Department(
            custom_agent_3
        )
        custom_task_4 = tasks.Civilian_communication(
            custom_agent_4
        )

        # Define your custom crew here
        crew = Crew(
            agents=[custom_agent_1,custom_agent_2,custom_agent_3,custom_agent_4,],
            tasks=[custom_task_1,custom_task_2,custom_task_3,custom_task_4,],
            verbose=True,
        )
        try:
            result = crew.kickoff()
        except:
            result = """Crew is having diifuctly reaching Gemini, please try again 
                        And stay safe while doing so
                        YOUR SAFETY SHOULD BE YOUR FIRST PRIORITY"""


        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    call = input("enter distress call: ")
    

    custom_crew = CustomCrew(call)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result: ")
    print("########################\n")
    print(result)
