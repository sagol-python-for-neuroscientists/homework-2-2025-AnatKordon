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
    """

    """I will be using condition values instead of names (Condition.value):
        CURE 1
        HEALTHY 2
        SICK 3
        DYING 4
        DEAD 5
        """
    
    updated_listing = []

    for agent1, agent2 in batched(agent_listing, 2): #batched method from itertools groups by unique pairs
        val1, val2 = agent1.category.value, agent2.category.value #extracting values which i'll check for every condition
        ##if healthy or dead - there's no encounter so they stay the same
        if val1 in (2, 5) or val2 in (2, 5) or (val1 == val2 == 1): #check what happens when both are cure 
            updated_listing.extend([agent1, agent2])
        elif val1 == 1 ^ val2== 1: #if one and only one is cure - make the other the other one healthier
            if val1 == 1:
                updated_listing.extend([
                agent1,
                agent2._replace(category=Condition(agent2.category.value + 1))
            ])
            if val2 == 1:
                updated_listing.extend([
                agent1._replace(category=Condition(agent2.category.value + 1)),
                agent2
            ])
        elif val1 in (3, 4) and val2 in (3,4): # i think it's end and not or though by this stage no one stays.
            if val1 in (3,4):
                updated_listing.extend([
                agent1._replace(category=Condition(agent1.category.value - 1)),
                agent2._replace(category=Condition(agent2.category.value - 1))
            ])
        elif val2 == None: # if the list is uneven
            updated_listing.extend([agent1])
        else: 
            print(f"you didn't think about this case: {agent1}, {agent2}")
    return updated_listing


data0 = (
    Agent("Adam", Condition.SICK),
    Agent("Cure0", Condition.CURE),
    Agent("Cure1", Condition.CURE),
    Agent("Bob", Condition.HEALTHY),
    Agent("Alice", Condition.DEAD),
    Agent("Charlie", Condition.DYING),
    Agent("Vaccine", Condition.SICK),
    Agent("Darlene", Condition.DYING),
    Agent("Emma", Condition.SICK),
    Agent("Cure2", Condition.CURE),
)

code_list = meetup(data0)
print(code_list)
                 