import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import time


#Control variables

number_of_robots = 50
timesteps = 200
speed = 0.2

collision_distance = 0.8
neighbour_distance = 3.0

target_weight = 1.0
separation_weight = 2.0
alignment_weight = 0.5
cohesion_weight = 0.3
obstacle_avoidance_weight = 3.0

target_radius = 0.5

obstacle_min = np.array([4.0, 4.0])
obstacle_max = np.array([6.0, 7.0])
obstacle_avoidance_distance = 0.4


#Runs simulation function

def run_simulation(auto_complete=True):

    #Randomises starting positions for all robots
    robot_positions = np.random.uniform(0, 10, size=(number_of_robots, 2))

    #Creates array with same shape as positions array for velocities for all robots and fills with zeroes
    robot_velocities = np.zeros_like(robot_positions)

    #Tracks which robots reached the target
    #Does this by creating a list full of False values and sets them to True if that robot has reached the target
    reached_target = np.zeros(number_of_robots, dtype=bool)

    #Sets collision count to 0
    collision_count = 0

    #An empty list, which robots that have reached the target are to be added to
    robots_reached_history = []

    #Initialises target position in an array
    target_position = np.array([8.0, 7.0])


    #Animation/visuals for simulation
    #Skipped if auto complete is set to True

    if auto_complete == False:

        #Turns on interactive plotting, allowing for animation
        plt.ion()

        #Creates simulation window
        fig, ax = plt.subplots()

        #Sets the x and y axes, a 10x10 simulation
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

        #Sets title and axes labels
        ax.set_xlabel("X position")
        ax.set_ylabel("Y position")
        ax.set_title("Robot Swarm Simulation")

        #Draws the actual target as a star of size 150 and labelled target
        #Position depends on target position array intialised earlier
        ax.scatter(target_position[0], target_position[1], marker="*", s=150, label="Target")

        #A basic, rectangular obstacle placed in the middle of the map
        obstacle = Rectangle(obstacle_min, obstacle_max[0] - obstacle_min[0], obstacle_max[1] - obstacle_min[1],
        fill=False, linewidth=2)

        #Plots that obstacle onto the graph
        ax.add_patch(obstacle)

        #Plots all robots at their specified x and y positions
        robot_plot, = ax.plot(robot_positions[:, 0], robot_positions[:, 1], "o")

        ax.legend()


    #Main simulation loop
    #Must run whether auto complete is on or not

    #Runs simulation in designated number of steps
    for step in range(timesteps):

        #Creates array for new robot velocities with same shape as robot positions array and is filled with zeroes
        new_velocities = np.zeros_like(robot_positions)


        #Calculates each robot's behaviour

        #For all robots in the simulation
        for i in range(number_of_robots):

            #Path-finding to target
            #Finds direction as a vector from robot to target using vector subtraction 
            target_direction = (target_position- robot_positions[i])

            #Finds length of that direction vector
            target_distance = np.linalg.norm(target_direction)

            #To make sure no division by 0
            if target_distance > 0:
                target_direction = (target_direction / target_distance)


            #SEPARATION

            #Avoids collisions
            #Creates an initial array which will be updated to affect robot direction
            separation = np.array([0.0, 0.0])

            #ALIGNMENT
            alignment = np.array([0.0, 0.0])

            #COHESION
            cohesion = np.array([0.0, 0.0])

            neighbour_count = 0


            #Looks at other robots in the simulation 
            for j in range(number_of_robots):

                #If looking at the same robot as itself, skip the current iteration of the loop
                if i == j:
                    continue

                #Calculates vector distance from the other robot
                difference = (
                    robot_positions[i]
                    - robot_positions[j]
                )

                #Calculates scalar distance from other robot
                distance = np.linalg.norm(
                    difference
                )


                #Separation
                #Robots should avoid colliding with other robots

                #If robots breach collision distance, update separation vector which pushes robots apart
                if 0 < distance < collision_distance:
                    separation += (difference / distance)


                #Alignment
                #Robots should move together, with similar velocities, as a swarm
                if distance < neighbour_distance:
                    #Updates alignment vector
                    alignment += (robot_velocities[j])


                #Cohesion
                #Robots should stay together, with similar positions, as a swarm

                    #Updates cohesion vector
                    cohesion += (robot_positions[j])

                    #Adds to the swarm
                    neighbour_count += 1


            #Cohesion Calculation
            #Robots that are close to each other are added to the swarm


            if neighbour_count > 0:

                #Finds average position of the swarm
                average_position = (cohesion / neighbour_count)

                #Finds cohesion vector
                cohesion = (average_position - robot_positions[i])


            #Avoiding obstacles

            #Creates avoidance vector, set to 0
            obstacle_avoidance = np.array([0.0, 0.0])

            #Finds closest point to obstacle from the current robot in loop
            closest_point = np.clip(robot_positions[i], obstacle_min, obstacle_max)

            #Finds vector direction away from the closest point
            obstacle_difference = (robot_positions[i] - closest_point)

            #Finds distance away from the closest point
            obstacle_distance = np.linalg.norm(obstacle_difference)

            #If the robot is close to the obstacle, robot gets pushed away in opposite direction
            if (0 < obstacle_distance < obstacle_avoidance_distance):
                obstacle_avoidance = (obstacle_difference / obstacle_distance)


            
            #Combines all vector behaviours to calculate the overall direction for robot to move next
            #Also multiplies it by that behaviour's weight which is a measure of priority

            direction = (target_direction * target_weight+ separation * separation_weight+ alignment * alignment_weight
                        + cohesion * cohesion_weight + obstacle_avoidance * obstacle_avoidance_weight)


            #Finds length of direction
            direction_length = np.linalg.norm(direction)

            #Turns direction back into a vector
            if direction_length > 0:
                direction = (
                    direction
                    / direction_length
                )


            #Calculates velocity for the robot to move at
            new_velocities[i] = (direction * speed)


        #Updates new robot position and velocity

        robot_velocities = new_velocities

        robot_positions += robot_velocities


        #Looks for close encounters
        #Searches for each pair of robots once and only once
        for i in range(number_of_robots):
            for j in range(i + 1, number_of_robots):

                #Determines whether robots have collided
                difference = (robot_positions[i] - robot_positions[j])

                distance = np.linalg.norm(difference)

                if distance < collision_distance:
                    collision_count += 1


        #Finds distance from robot to target for all robots
        for i in range(number_of_robots):

            distance_to_target = np.linalg.norm(
                robot_positions[i]
                - target_position
            )
            #If it's close enough then robot has successfully reached the target
            if distance_to_target < target_radius:

                reached_target[i] = True

        #Records how many robots have reached the target
        robots_reached_history.append(np.sum(reached_target))

        #Animation Updating
        #Only performed if auto complete is false
        if auto_complete == False:

            #Moves robots to new positions
            robot_plot.set_data(
                robot_positions[:, 0],
                robot_positions[:, 1]
            )

            #Redraws the entire window
            fig.canvas.draw()
            fig.canvas.flush_events()

            #Brief pause 
            time.sleep(0.05)


    #Counts number of robots that reached the target after end of simulation
    robots_reached = np.sum(reached_target)

    #Calculate the success rate as a percentage
    success_rate = (robots_reached / number_of_robots * 100)


    #Close animation
    if auto_complete == False:

        plt.ioff()
        plt.show()


    #Returns results

    return {"collision_count": collision_count, "robots_reached": robots_reached, "success_rate": success_rate,
        "robots_reached_history": robots_reached_history}


#OUTSIDE SIMULATION LOOP
#Runs 1 simulation by running the run_simulation function

results = run_simulation(auto_complete=False)

#Prints results
print("Collision events:", results["collision_count"])
print("Robots reached target:", results["robots_reached"])
print("Success rate:", results["success_rate"],"%")


#GRAPH PLOTTING
#Plots a graph showing how robots reach the target over a period of timesteps
plt.figure()

plt.plot(results["robots_reached_history"])

#Labels x and y axes
plt.xlabel("Timestep")
plt.ylabel("Robots reaching target")

#Labels title
plt.title("Robots Progress Over Time")

#Shows grid
plt.grid()
plt.show()