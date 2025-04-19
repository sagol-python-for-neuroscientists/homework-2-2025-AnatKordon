from collections import namedtuple
from enum import Enum
from itertools import batched

Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))

def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Notes
    -----
    The rules governing the meetings were described in the question. The outgoing
    listing may change its internal ordering relative to the incoming one.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing (tuple in this case) in which each element is of the Agent
        type, containing a 'name' field and a 'category' field, with 'category' being
        of the type Condition.

    Returns
    -------
    updated_listing : list
        A list of Agents with their 'category' field changed according to the result
        of the meeting.
    
    Anat's Note: 
    I will be using condition values instead of names (Condition.value):
        CURE 1
        HEALTHY 2
        SICK 3
        DYING 4
        DEAD 5
        """
    #calling other functions:
    healthy_dead_list, meetings_list = spliting_agents(agent_listing)
    updated_healthy_dead_list, updated_meetings_list = uneven_meetings(healthy_dead_list, meetings_list)
    updated_listing = updated_healthy_dead_list
   
    if len(updated_meetings_list) == 0:
        return updated_listing
    else:
        for agent1, agent2 in batched(updated_meetings_list, 2): #batched is a method from itertools that batches tuples
        #for agent1, agent2 in zip(agent_listing[::2], agent_listing[1::2]):
            val1, val2 = agent1.category.value, agent2.category.value #extracting values which i'll check for every condition
            ##if healthy or dead - there's no encounter so they stay the same
            if val1 == val2 == 1:
                updated_listing.extend([agent1, agent2]) #cure and cure don't affect each other
            elif val1 == 1 or val2 == 1: #if one and only one is cure - make the other the other one healthier
                if val1 == 1 and val2 > 1:
                    updated_listing.extend([
                    agent1,
                    agent2._replace(category=Condition(val2 - 1)) #replace changes the value of the agent's category
                ])
                elif val2 == 1 and val1 > 1:
                    updated_listing.extend([
                    agent1._replace(category=Condition(val1 - 1)),
                    agent2
                ]) 
            elif val1 in (3, 4) and val2 in (3,4): # i think it's end and not or though by this stage no one stays.
                    updated_listing.extend([
                    agent1._replace(category=Condition(val1 + 1)),
                    agent2._replace(category=Condition(val2 + 1))
                ])
            elif val2 == None: # if the list is uneven
                updated_listing.extend([agent1])
            else: 
                print(f"you didn't think about this case: {agent1}, {agent2}")
    return updated_listing


def spliting_agents(agent_listing: tuple):
    """splits agents to create a new meetings list that has only agents that will meet,
    also save the agents who don't meet
    Parameters
    ----------
    agent_listing : tuple
        A listing (tuple in this case) in which each element is of the Agent
        type, containing a 'name' field and a 'category' field, with 'category' being
        of the type Condition.

    Returns
    -------
    healthy_dead_list : list
        A list of agents who are healthy or dead (they don't meet).
    meetings_list : list
        A list of agents who will meet (category is cure, sick, or dying).
    """
    healthy_dead_list = []
    meetings_list = []
    for agent in agent_listing:
        val = agent.category.value
        if val in (2, 5):
            healthy_dead_list.append(agent)
        else: 
            meetings_list.append(agent)
    return healthy_dead_list, meetings_list

def uneven_meetings(healthy_dead_list, meetings_list):
    """filtering solo agents from the meetings_list to make it even

    Parameters
    ----------
    healthy_dead_list : list
    meetings_list : list

    Returns
    -------
    healthy_dead_list : list
    meetings_list : list
        returns updated versions of the two lists
    """
    for agent in meetings_list:
        if len(meetings_list) % 2 != 0:
            healthy_dead_list.append(meetings_list[-1]) #append last agent
            meetings_list.remove(meetings_list[-1])
    return healthy_dead_list, meetings_list

