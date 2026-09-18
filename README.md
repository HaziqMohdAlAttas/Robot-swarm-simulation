# Robot-swarm-simulation
A simple python simulation of a swarm of autonomous robots designed as a Boids-style swarm. The robots exhibit behaviours such as target seeking, obstacle avoiding as well as working together as a swarm, making sure they abide by the rules of separation, alignment and cohesion, as seen in nature in a Boids-style swarm.

Explanation of Results:
See excel spreadsheet for more info

The effect of separation weights on swarm performance was conducted. Here, swarm performance was categorized via the success rate, which is the percentage of robots that reached the target, but also the number of robot collisions with each other.
The optimal swarm performance would be one that had a high success rate but also a low number of collisions

The experiment was conducted using 4 different separation weights (0.5,1.0,2.0,4.0), and also each trial was done 10 different times, so there were 40 different trials in total. Then, the mean success rate and collision count was made for each of the 10 trials.
As seen from the graphs, there seemed to be a clear connection between separation weights and success rate + collisions count.

As separation weights increased from 0.5 to 4.0, success rates decreased from 92.6% down to 16.8%. This tells us that 0.5 is the best separation weight for maximizing success rate.
As separation weights increased from 0.5 to 4.0, collision count decreased from 28546.5 to 9640.8. This tells us that 4.0 is the best separation weight for minimizing collision count.

These results indicate that a trade-off must be made in order to find the optimal separation weight, as a low separation rate would result in high collision counts, but a high separation weight would result in low success rate. Moving forward, although the weighting should be adjusted according to the situation, the most optimal separation weight is 1.0 as its success rate only decreases by 3.46%, and its collision counts decreases by 34.31%. This is a low decrease of success rate but also and huge decrease in collision count. As I decided an optimal swarm performance would be that which had a high success rate but also a low number of collisions, I believe the simulation with a separation weight of 1.0 fits this description the best.

