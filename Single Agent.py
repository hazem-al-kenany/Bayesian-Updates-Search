import random
import matplotlib.pyplot as plt

class Explorer: #for single explorer search behavior
    def __init__(self):
        self.beliefs = [0.1] * 10 #initialize equal probability for each of the 10 zones

    def choose_zone(self): #chooses a zone to search based on current beliefs
        max_prob = max(self.beliefs)  #find the highest probability
        possible_zones = []  #store zones with highest probability
        for i in range(len(self.beliefs)):
            if self.beliefs[i] == max_prob:
                possible_zones.append(i)  #add zones with max probability
        return random.choice(possible_zones)  #choose randomly if multiple zones have same probability

    def update_beliefs(self, searched_zone, found_flower): #update beliefs after searching a zone
        if found_flower:
            return  #do nothing if flower is found
        self.beliefs[searched_zone] = 0  #set probability of searched zone to 0
        total_prob = sum(self.beliefs)  #calculate total remaining probability
        if total_prob > 0:
            for i in range(len(self.beliefs)):
                self.beliefs[i] = self.beliefs[i] / total_prob  #redistribute the remaining probability across the unvisited zones

class Observer: #track the number of visits to each zone
    def __init__(self):
        self.visits = [0] * 10  #initialize visit counter for each zone to 0
        self.flower_finds = 0 #initialize counter for finding the rare flower

    def track_visit(self, zone):
        self.visits[zone] += 1

    def track_flower_find(self):  #track when the flower is found
        self.flower_finds += 1

def simulate(): #run simulation for 1000 turns
    observer = Observer()  #initialize the observer
    flower_zone = random.randint(0, 9)  #rare flower is randomly placed in one zone
    explorer = Explorer()  #initialize a single explorer for the entire simulation
    turns = 1000
    
    for _ in range(turns):

        search_zone = explorer.choose_zone()  #explorer chooses a zone to search
        observer.track_visit(search_zone)  #observer tracks the visit

        if search_zone == flower_zone:
            observer.track_flower_find()  #track the flower found
            flower_zone = random.randint(0, 9)  #reset flower location after it is found
            explorer = Explorer()  #reset the explorer's beliefs once the flower is found

        else:
            explorer.update_beliefs(search_zone, False)  #update explorer's beliefs if flower not found

    return observer.visits, observer.flower_finds  #return the number of visits to each zone

#display the results using a bar graph
def display_results(visits, flower_finds):
    zones = list(range(1, 11))  #zone numbers from 1 to 10
    plt.bar(zones, visits)
    plt.xlabel("Zones")
    plt.ylabel("Number of Visits")
    plt.title("Number of Visits to Each Zone After 1000 Turns")
    plt.show()
    print("In 1000 turns, the flower was found", flower_finds,  "times.")

if __name__ == "__main__":
    visits, flower_finds = simulate()  #run the simulation
    display_results(visits, flower_finds)  #display the results as a bar graph