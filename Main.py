import openai
import re
import httpx
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
from openai import OpenAI

client = OpenAI()

class Agent:
    def __init__(self, system=""):
        self.system = system
        self.messages = []
        if self.system:
            self.messages.append({"role": "system", "content": system})

    def __call__(self, message):
        self.messages.append({"role": "user", "content": message})
        result = self.excecute()
        self.messages.append({"role": "assistant", "content": result})
        return result

    def excecute(self):
        completion = client.chat.completions.create(
            model="gpt-4o",
            temperature=0,
            messages=self.messages)
        return completion.choices[0].message.content


prompt = """
You run in a loop of Thought, Action, PAUSE, Observation.
At the end of the loop you output an Answer
Use Thought to describe your thoughts about the question you have been asked.
Use Action to run one of the actions available to you - then return PAUSE.
Observation will be the result of running those actions.

Your available actions are:

calculate:
e.g. calculate: 4 * 7 / 3
Runs a calculation and returns the number - uses Python so be sure to use floating point syntax if necessary

average_dog_weight:
e.g. average_dog_weight: Collie
returns average weight of a dog when given the breed

Example session:

Question: How much does a Bulldog weigh?
Thought: I should look the dogs weight using average_dog_weight
Action: average_dog_weight: Bulldog
PAUSE

You will be called again with this:

Observation: A Bulldog weights 51 lbs

You then output:

Answer: A bulldog weights 51 lbs
""".strip()

def calculate(what):
    return eval(what)

def average_dog_weight(name):
    if name in "Scottish Terrier":
        return("Scottish Terrier average 22 lbs")
    elif name in "Border Collie":
        return("Border Collie average weight is 37 lbs")
    elif name in "Toy Poodle":
        return("Toy Poodle average weight is 7 lbs")
    else:
        return f"No tengo información sobre la raza {name}"

known_actions = {
    "calculate": calculate,
    "average_dog_weight": average_dog_weight
}

abot = Agent(system=prompt)
question = """I have 2 dogs, a border collie and a scottish terrirer.\
    What is their combined weight?"""
abot(question)

next_prompt = "Observation: {}".format(average_dog_weight("Border Collie"))
abot(next_prompt)

next_prompt = "Observation: {}".format(average_dog_weight("Scottish Terrier"))
abot(next_prompt)

next_prompt = "Observation: {}".format(calculate("37 + 20"))
print(abot(next_prompt))