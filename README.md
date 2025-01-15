# Multi-Agent Search Simulation with Independent and Bayesian Updates

This project simulates multi-agent search behaviors to locate a rare flower across ten zones. Two approaches are implemented:
1. **Independent Search**: Agents search independently, updating their own beliefs.
2. **Social Bayesian Search**: Agents incorporate observed actions of others into their belief updates.

The simulation compares the effectiveness of these methods based on zone visits and flower finds over 1,000 turns.

---

## Features

### Task 1: Single Explorer Search
- **Belief System**:
  - Each explorer starts with equal probabilities for all zones.
  - Probabilities are updated based on unsuccessful searches.
- **Zone Selection**:
  - Zones with the highest probability are prioritized.
- **Rare Flower**:
  - The flower is randomly placed and relocates upon being found.

### Task 2: Multi-Agent Search with Bayesian Updates
- **Independent Search**:
  - Each agent searches independently, updating their own beliefs.
- **Social Bayesian Search**:
  - Agents update their beliefs based on their own searches and the observed actions of others.
- **Comparison Metrics**:
  - Tracks the number of visits to each zone.
  - Records the total number of flower finds for both methods.

---

## Simulation Process

### Task 1: Single Explorer Search
1. **Initialization**:
   - A single explorer and an observer are created.
   - The flower is randomly placed in one of the ten zones.
2. **Turns**:
   - Over 1,000 turns:
     - The explorer selects a zone based on their beliefs.
     - The observer tracks visits and flower finds.
     - Beliefs are updated if the flower is not found.
     - The flower relocates upon being found.
3. **Results**:
   - Zone visit counts and flower finds are recorded.

### Task 2: Multi-Agent Search
1. **Initialization**:
   - Ten explorers are initialized with equal probabilities for all zones.
   - The flower is randomly placed.
2. **Search Methods**:
   - **Independent Search**:
     - Each agent updates its own beliefs independently.
   - **Social Bayesian Search**:
     - Agents update beliefs based on their own searches and observed searches of others.
3. **Results**:
   - Zone visit counts and flower finds are compared for both methods.

---

## Code Structure

### Key Classes and Functions

#### **Explorer (Task 1)**
- Maintains a probabilistic belief system for the ten zones.
- Updates beliefs based on search outcomes.

#### **MultiExplorerModel (Task 2)**
- Manages beliefs for multiple agents.
- Implements independent and Bayesian search methods.

#### **Simulation Functions**
- `simulate_independent_search`: Executes independent search for Task 2.
- `simulate_social_bayesian_search`: Executes Bayesian search for Task 2.
- `run_simulation`: Runs both search methods and compares results.

#### **Visualization**
- Bar charts compare zone visits for both search methods.
- Console output summarizes flower finds.

---

## How to Run

### Prerequisites
- Python 3.7 or higher.
- Required libraries:
  ```bash
  pip install matplotlib
