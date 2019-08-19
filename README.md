# Proposal

### Airline Graph Project Proposal
* Shortest route from City A to City B
- The shortest route will be determined by utilizing our find_shortest_path method in our Graph class. The find_shortest_path method is an implementation of the Dijkstra Greedy Algorithm.
* The most popular airport
- We define the most popular airport as the airport that has the most planes coming in and out. To accomplish this we traverse the graph and determine which vertex has the highest degree.

* ???
- Maximal Clique

* Does a return flight possible from a given airport?
- To determine if a return flight is possible from all given airports, we will be using the eulerian and cycle detection methods in our graph class. If a


Problem: Given an airplane routing network, find the cheapest path from one city to another, find if there is there a route back to a given city, and find the cheapest route with between two cities with a single stop.

Model the problem: A network of airplane routes is represented by a graph with each vertex being a city and the weighted edges being the distance to travel between cities.
