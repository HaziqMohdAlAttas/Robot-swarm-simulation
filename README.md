# Robot-swarm-simulation

Project Description

A simple python simulation of a swarm of autonomous robots designed as a Boids-style swarm. The robots exhibit behaviours such as target seeking, obstacle avoiding as well as working together as a swarm, making sure they abide by the rules of separation, alignment and cohesion, as seen in nature in a Boids-style swarm.

In the project, 50 robots are to move towards a target. However, each of the robots initially start from different points on the map. To make sure they act as a swarm, if any 2 robots come close to each other, they get 'aligned'. This will be done by averaging out each robots position in the swarm which makes sure they are moving in the same direction. In a swarm, all the robots in it will move in the same direction, towards the target. This is alignment. However, whilst they are in the swarm, we must make sure that those 2 robots don't collide with each other. So if a robot is too close with another one, they must be able to push each other away in opposite directions. This is separation. We also want to make sure that robots stick together as a swarm. If they are too far away from each other, the robots should be lightly pulled together closer. This is referred to as cohesion. These rules also mean that control is decentralized, meaning there is no 1 leader of the swarm, mimicking the classic style of a Boids-style swarm.

As an extra addition I also decided that I would add a simple, large, rectangular shaped obstacle too. Each robot must also be pushed away from that obstacle if they get too close so they don't hit it and potentially crash.


Experiment
After finishing the project, I decided to run an experiment on it in order to fine tune the swarm into being more successful at both reaching the target, and reducing collisions with itself. To do this, the effect of separation weights on swarm performance was conducted. In my project each robot in the swarm must make sure they don't collide with each other. Separation allows for this to happen. In the program, each robot must move away from each other if they get too close. The separation weight is used to amplify that number, in order to reduce the number of collisions. However, I thought that if the separation weight was too high, this would affect the success rate of each robot in the swarm successfully reaching the target.

This is why I conducted the experiment. In order to maximize swarm performance, I came to the conclusion that swarm performance depends on the success rate, which is the percentage of robots that reached the target, but also the number of robot collisions with each other.
The optimal swarm performance would be one that had a high success rate but also a low number of collisions.

The experiment was conducted using 4 different separation weights (0.5,1.0,2.0,4.0), and also each trial was done 10 different times, so there were 40 different trials in total. Then, the mean success rate and collision count was calculated for each separation weight. Every single trial would end after 200 timesteps.

Independent variable(what changes) - Separation Weight. We will use values of 0.5,1.0,2.0 and 4.0.
Dependent variables(what we are measuring) - Success rate/percentage of robots that reach the target. Number of collisions.
Control variables(what we keep the same) - Number of robots, number of timesteps, obstacle position and size, alignment and cohesion weight, target position, etc.


Results

As seen from the graphs, there seemed to be a clear connection between separation weights and success rate + collisions count.

As separation weights increased from 0.5 to 4.0, success rates decreased from 92.6% down to 16.8%. This tells us that 0.5 is the best separation weight for maximizing success rate.
As separation weights increased from 0.5 to 4.0, collision count decreased from 28546.5 to 9640.8. This tells us that 4.0 is the best separation weight for minimizing collision count.

These results indicate that a trade-off must be made in order to find the optimal separation weight, as a low separation rate would result in high collision counts, but a high separation weight would result in low success rate. Although the weighting should be adjusted according to the situation, the most optimal separation weight out of the ones tested is 1.0. It provided the strongest balance between high target success rate and lower collision frequency as its success rate only decreases by 3.46%, and its collision counts decreases by 34.31%. This is a low decrease of success rate but also a huge decrease in collision count. As I decided an optimal swarm performance would be that which had a high success rate but also a low number of collisions, I believe the simulation with a separation weight of 1.0 fits this description the best.

