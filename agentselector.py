class Agent:
    def __init__(self, id, is_available, avail_since, roles):
        self.id = id
        self.is_available = is_available
        self.avail_since = avail_since
        self.roles = roles

    def check_roles(self, issue, agent):
        if issue in agent.roles:
            return True

    def avail_agent(self, agents, selection_mode, issue, timestamps):
        if(selection_mode == "allavailable"):
            if self.is_available:
                if(self.check_roles(issue, self)):
                    return self
        elif(selection_mode == "leastbusy"):
            if self.is_available:
                if(len(timestamps) > 0):
                    if self.avail_since == min(timestamps):
                        if(self.check_roles(issue, self)):
                            return self
        elif(selection_mode == "random"):
            if(self.is_available):
                if(self.check_roles(issue, self)):
                    return self

    def show_matched_agents(self, free_agents):
        if(len(free_agents) != 0):
            if self in free_agents:
                return True
        else:
            return False
