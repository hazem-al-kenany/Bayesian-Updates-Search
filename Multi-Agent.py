import random
import matplotlib.pyplot as plt

class MultiExplorerModel:
    def __init__(self, num_explorers):
        self.beliefs = [[0.1] * 10 for _ in range(num_explorers)]  #initialize equal probability for each of the 10 zones for all explorers
        self.observer = [0] * 10  #track the number of visits to each zone
        self.flower_finds = 0  #track the number of times the flower is found

    def simulate_independent_search(self, num_turns):  #simulate the scenario where explorers search independently
        flower_zone = random.randint(0, 9)  #randomly place the flower in one zone
        num_explorers = len(self.beliefs)

        for turn in range(num_turns):
            explorer_index = turn % num_explorers  #explorers take turns
            explorer_belief = self.beliefs[explorer_index]  #get current explorer's beliefs

            #choose a zone to search based on the current explorer's beliefs
            max_prob = max(explorer_belief)
            possible_zones = []
            for i in range(len(explorer_belief)):  #iterate over the indexes
                if explorer_belief[i] == max_prob:  #check if the probability matches the max probability
                    possible_zones.append(i)  #add the index (zone) to possible zones
            search_zone = random.choice(possible_zones)  #random choice if multiple zones have the same probability

            #track the visit to the search zone
            self.observer[search_zone] += 1

            if search_zone == flower_zone:  #if flower is found
                self.beliefs[explorer_index] = [0.1] * 10  #reset beliefs
                flower_zone = random.randint(0, 9)  #move the flower to a new zone
                self.flower_finds += 1  #increment the flower finds counter
            else:
                self.update_beliefs(explorer_belief, search_zone)  #update the current explorer's belief based on the search result

        return self.observer, self.flower_finds  #return the number of visits to each zone and flower finds

    def simulate_social_bayesian_search(self, num_turns):  #simulate the scenario where explorers use social Bayesian updates
        flower_zone = random.randint(0, 9)  #randomly place the flower in one zone
        num_explorers = len(self.beliefs)

        for turn in range(num_turns):
            explorer_index = turn % num_explorers  #explorers take turns
            explorer_belief = self.beliefs[explorer_index]  #get current explorer's beliefs

            #choose a zone to search based on the current explorer's beliefs
            max_prob = max(explorer_belief)
            possible_zones = []
            for i in range(len(explorer_belief)):  #iterate over the indexes
                if explorer_belief[i] == max_prob:  #check if the probability matches the max probability
                    possible_zones.append(i)  #add the index (zone) to possible zones
            search_zone = random.choice(possible_zones)  #random choice if multiple zones have the same probability

            #track the visit to the search zone
            self.observer[search_zone] += 1

            if search_zone == flower_zone:  #if flower is found
                self.beliefs[explorer_index] = [0.1] * 10  #reset beliefs
                flower_zone = random.randint(0, 9)  #move the flower to a new zone
                self.flower_finds += 1  #increment the flower finds counter
            else:
                self.update_beliefs(explorer_belief, search_zone)  #update the current explorer's belief based on the search result
                self.social_bayesian_update(explorer_index, search_zone)  #update all other explorers' beliefs based on observing this search

        return self.observer, self.flower_finds  #return the number of visits to each zone and flower finds

    #update the current explorer's belief
    def update_beliefs(self, belief, searched_zone):
        belief[searched_zone] = 0  #set probability of searched zone to 0
        total_prob = sum(belief)  #calculate total remaining probability
        if total_prob > 0:
            for i in range(len(belief)):
                belief[i] = belief[i] / total_prob  #redistribute the remaining probability

    #bayesian update based on the actions of others
    def social_bayesian_update(self, current_explorer_index, observed_zone):
        for index in range(len(self.beliefs)):  #iterate over the indices
            belief = self.beliefs[index]  #get the belief of the current explorer
            if index != current_explorer_index:  #exclude the current explorer
                belief[observed_zone] = 0  #set probability of searched zone to 0
                total_prob = sum(belief)  #recalculate probabilities
                if total_prob > 0:
                    for i in range(len(belief)):  #redistribute the probability
                        belief[i] = belief[i] / total_prob

#run the simulation for both methods and compare
def run_simulation():
    num_explorers = 10
    num_turns = 1000

    #run independent search
    independent_model = MultiExplorerModel(num_explorers)
    independent_visits, independent_flower_finds = independent_model.simulate_independent_search(num_turns)

    #run social bayesian update search
    bayesian_model = MultiExplorerModel(num_explorers)
    bayesian_visits, bayesian_flower_finds = bayesian_model.simulate_social_bayesian_search(num_turns)

    return independent_visits, independent_flower_finds, bayesian_visits, bayesian_flower_finds

#display the results using bar graphs and comparison
def display_results(independent_visits, independent_flower_finds, bayesian_visits, bayesian_flower_finds):
    zones = list(range(1, 11))  #zone numbers from 1 to 10

    #bar chart for search comparison
    plt.bar(zones, independent_visits, alpha=0.5, label='Independent search')
    plt.bar(zones, bayesian_visits, alpha=0.5, label='Bayesian search')
    plt.xlabel("Zones")
    plt.ylabel("Visits")
    plt.title("Comparison of zone visits between independent and bayesian search")
    plt.legend()
    plt.show()

    #print comparison of flower finds
    print("Independent Search: The flower was found", independent_flower_finds, "times in 1000 turns")
    print("Bayesian Search: The flower was found", bayesian_flower_finds, "times in 1000 turns")

if __name__ == "__main__":
    independent_visits, independent_flower_finds, bayesian_visits, bayesian_flower_finds = run_simulation()
    display_results(independent_visits, independent_flower_finds, bayesian_visits, bayesian_flower_finds)