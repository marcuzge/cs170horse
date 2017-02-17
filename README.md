# cs170horse
This is an Algorithm Project.
Lucos Papasan is entering a horse race! He has m horses, and he must divide them up into relay teams (of
not necessarily equal size) to enter in the competition. In the race, each team runs a total 10000 m and the
fastest team wins. Larger teams will perform better, because each horse will have to run less distance. The
goal is to find teams to maximize Lucos’s chance of winning with any team.
Lucos, being a specialist in horses, has created a model that will determine the likelihood of a given team
winning. His overall chance of winning is the sum of each individual team’s likelihood of winning. Each
horse has a performance rating pi
that models how fast the horse is. Lucos’s model has determined that the
likelihood of winning for a team of n horses is given by
 n
(∑ pi)n
 i=1

The factor of n is due to the fact that horses in larger teams have to run less distance, and so they can run
faster.
There is one more constraint. Each horse will only race if it runs directly before one of its friends in the
relay. For example, if horse A runs first and horse B runs second, then horse A must consider horse B to
be its friend. Any horse may run last in a relay team (but the second to last horse must be friends with it).
If a horse refuses to race, then all of your teams will be disqualified, making your likelihood of winning 0.
Luckily, Lucos has a list of ordered pairs of horses (h1,h2), where h1 considers h2 to be its friend (note that
friendships are not necessarily reciprocal). We can formulate this problem as a graph G = (V,E) where the
vertices are the horses, and an edge (h1,h2) exists if h1 considers h2 to be its friend, meaning that h1 can be
directly before h2 in a relay team. A relay team is represented by a path in the graph. Any path is a valid
relay team. Each node in the graph can be only used once; each horse must be assigned to exactly one team.
The goal is to find a set of relay teams that maximizes the likelihood of winning the race.

