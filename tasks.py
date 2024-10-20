from crewai import Task
from textwrap import dedent
from tools import file_writer_tool

# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def Identify_emergency(self, agent,call):
        return Task(
            description=dedent(
                f"""
                Task: To extact usefull data from distress call
                Description: Extact the nature of the issue,Key insights related to it and address of the location 
                Example Natures: It is a fire,It is a wild animal,It is a crimal etc
                Example Key Insights: If as wild animal is loose ,which animal is it . If a crime is happening is somone armed with a gun,For most emergencies is someone injured etc

                Address of where the incident is happening is also very important

                Paramenters:
                distress call : {call}
                {self.__tip_section()}
                
                
                """
            ),
            #tools=[file_read_tool],
            expected_output=dedent(f""" text containing three lines
                                   nature of issue:
                                   key insights:
                                   address:"""),
            agent=agent,
        )
    
    def Decide_Department(self, agent):
        return Task(
            description=dedent(
                f"""
                Task: List departments needed to respond to the situation
                Description: Given information about a emergency
                            You will output which response services (like - abulance,police,firefighters,zoo authority etc) are needed to apropriately handle a issue
                            And provide them information that will help them
                            from the information provided
                            NOT ALL DEPARTMENTS WILL BE NEEDED BE CAREFUL TO CALL ONLY NEEDED DEPARTMENTS

                {self.__tip_section()}
                            
                """
            ),
            #tools=[file_read_tool],
            expected_output=dedent(f"""lines of text of format
                                    department1: information helpful to dept1
                                    department2: information helpful to dept2
                                    """),
            agent=agent,
        )

    def Email_Department(self, agent):
        return Task(
            description=dedent(
                f"""
                Task: Write emails to departments
                Description:given a list of departments to be contacted and information to be provided to them
                            you will draft a email to each of them individualy,giving them relavent information from what is provided on the emergency happening currently
                            and informing them about the other departments that wil be on the scene
                {self.__tip_section()}
                            
                """
            ),
            #tools=[file_writer_tool],
            expected_output=dedent(f"""the emails that will be sent to each department one after the other seperated by one empty line
                                    """),
            agent=agent,
        )
    
    def Civilian_communication(self, agent):
        return Task(
            description=dedent(
                f"""
                Task: 
                Description:Given information about the response to the current issue
                            1)Give the civilian instructions on: How to stay safe until help arrives
                            2)Try to calm them with your response
                {self.__tip_section()}
                            
                """
            ),
            #tools=[file_writer_tool],
            expected_output=dedent(f"""text response to the civilian"""),
            agent=agent,
        )