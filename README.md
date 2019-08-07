Airline Graph Project Proposal
Cheapest path from City A to City B
The most popular airport
Cheapest cycle
Cheapest path with stops, ie City A, City B, City C


Problem: Given an airplane routing network, find the cheapest path from one city to another, find if there is there a route back to a given city, and find the cheapest route with between two cities with a single stop.

Model the problem: A network of airplane routes is represented by a graph with each vertex being a city and the weighted edges being the distance to travel between cities.




--------------------------------------
Given a network of friends, find the biggest influencer, the largest group of friends who all know each other, and the longest time it would take for a message to pass from person A to person B via friends.

Example: The network of friends is modeled with each person being a vertex in a graph and an edge between any two people if they are friends.
The biggest influencer is the maximum degree of the graph.
The largest group of friends is the maximal clique number in the graph. This can be approximated by Turán's theorem.
The time to send a message is the shortest path which can be found via Dijkstra's Algorithm.
