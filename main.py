from agentselector import Agent
from datetime import datetime
import random


def given_agents():
    agents = []
    agents.append(Agent(0, True, datetime.now(), [
        "sales", "support", "tech"]))
    agents.append(Agent(1, True, datetime.now(),
                        ["sales", "support", "language", "custom"]))
    agents.append(Agent(2, True, datetime.now(),
                        ["sales", "tech", "language"]))
    agents.append(Agent(3, True, datetime.now(), ["tech", "language"]))
    agents.append(Agent(4, True, datetime.now(), [
        "sales", "general"]))
    agents.append(Agent(5, True, datetime.now(), [
                  "language", "general", "custom"]))
    return agents


def choose_mode():
    selection_modes = ["allavailable", "leastbusy", "random"]
    selection_mode = random.choice(selection_modes)
    print("\nRandomly selected mode :", selection_mode)
    return selection_mode


def get_issues(agents):
    print("Support Available for following issues :")
    avail_issues = []
    for agent in agents:
        for role in agent.roles:
            avail_issues.append(role)
    avail_issues = list(set(avail_issues))
    for a_iss in avail_issues:
        print(a_iss)
    selection_mode = choose_mode()
    issues = input(
        "\nEnter the Issue You Seek Support for Separated by Space : ")
    issues = issues.split()
    return issues, selection_mode


def set_timestamps(agents, issue):
    timestamps = []
    for agent in agents:
        if issue in agent.roles:
            timestamps.append(agent.avail_since)
    return timestamps


def check_for_random(agents, issue):
    for agent in agents:
        if(agent.is_available):
            if issue in agent.roles:
                return True
    return False


def get_random_free_agent(agents, selection_mode, issue, timestamps):
    selected = False
    free_agents = []
    while not selected:
        i = random.randint(0, len(agents)-1)
        k = agents[i].avail_agent(
            agents, selection_mode, issue, timestamps)
        if(k != None):
            free_agents.append(agents[i])
        if(len(free_agents) > 0):
            selected = True
    return free_agents


def get_free_agent(agents, selection_mode, issue, timestamps):
    free_agents = []
    for agent in agents:
        k = agent.avail_agent(
            agents, selection_mode, issue, timestamps)
        if(k != None):
            free_agents.append(agent)
    return free_agents


def print_result(agents, free_agents, issue, output):
    for agent in agents:
        if(agent.show_matched_agents(free_agents)):
            print(f"Agent {agent.id} available for issue : {issue}")
            output = True
    if(not output):
        print(f"No agent available for issue : {issue}")


agents = given_agents()
issues, selection_mode = get_issues(agents)
for issue in issues:
    output = False
    timestamps = []
    free_agents = []
    timestamps = set_timestamps(agents, issue)
    if(selection_mode == 'random'):
        if check_for_random(agents, issue):
            free_agents = get_random_free_agent(
                agents, selection_mode, issue, timestamps)
    else:
        free_agents = get_free_agent(agents, selection_mode, issue, timestamps)
    print_result(agents, free_agents, issue, output)
