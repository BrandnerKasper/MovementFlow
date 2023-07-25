# Movement Flow

Movement in video games is a essential part when it comes to enjoying a game, especially while playing 3D Jump'n Runs. But what defines good movement and how can we make it feel good?


Based on Steve Swink's book [Game Feel](http://www.game-feel.com/), a [GDC talk](https://www.youtube.com/watch?v=hG9SzQxaCm8&t=461s) about designing a jump and [Game Maker's Toolkit](https://www.youtube.com/watch?v=yorTG9at90g&t=152s) analysis video about Celeste, we explore which parameters define the movement of a game.

Therefore we designed our own 3D Jump'n Run called Boss'n Run.

## Boss'n Run's Movement

In Boss'n Run it is possible to:
- walk
- run
- jump
- double jump
- triple jump
- long jump
- wall jump
- climb
- fast climb

In the follwing these movement options are briefly explained:

### Walk
This is the most basic movement option all most all games support. It consists of 3 variables:
- velocity (v) in meter per second ($m/s$), the speed in which the character traverses the game 
- accerleration (acc) in meter per $seconds^2$ ($m/s^2$) to acclerate the character to its max velocity
- deceleration (dec) in meter per $seconds^2$ ($m/s^2$) to decelerate the character back to zero velocity

We looked at how long the player character takes (time (t) in seconds ($s$)) to reach his max v from zero v, as well as how long it takes to stop from max v to zero v. As well as the distance (d) he needed to cover for that.

### Run
Same as walk, just that v, acc and dec have typically higher values so the player character traverses the game faster.

### Jump
The most essential movement mechanic in 3D Jump'n Runs. It consists of 2 variables:
- gravity in in meter per $seconds^2$ ($m/s^2$), typically negative to make the player character fall back down again.
- jump velocity (jump_v) in meter per second ($m/s$), an upward velocity to challenge briefly the gravitation force.

Here we looked at how high the character can jump (in meters), as well as how long he is in the air (in seconds), and which distance (in meters) we could cover while jumping with full speed.

### Doulbe Jump
A variation of the default jump, where only the jump_v is higher.

### Triple Jump
Another variation of the default jump, where the jump_v is at its highest.

### Long Jump
Also a variation of the default jump, where the jump_v is lower, but the character is moving with sprint velocity instead of move velocity (meaning the distance he covers is higher).

### Wall Jump
A special variation of the default jump. It is triggered when the character is already in the air and touching a wall, so he can jump of the wall with not only a upward velocity but also a sidewar velocity -> adding to the jump the variable:
- side jump velocity (wall_jump_v_h) in meter per second ($m/s$).

### Climb
Climbing is similiar to walking, but instead of performed at the ground it is performed at the wall.

### Fast Climb
Basically sprinting while climbing.

## Plots
We plotted 3 different aspects:
- the velocity over time and distance while accelerating from zero velocity to max velocity
- the overall movement over time and distance, meaning there is a acceleration part, a part where the character moves at constant max velocity and a deceleration part.
- the jump height over time and distance, meaning we look over the whole duration of the jump, how high and far the player characer goes.

### Boss'n Run Movement plots

In the following the 3 graphs are presented, that showcase all movement options in Boss'n Run.

All default movement options in form of walking, sprinting, climbing and fast climbing: With there velocity over time and distance:
![Velocity over time and distance with the movement options: walking, sprinting, climbing and fast climbing](plots/Default/3D/Velocity%20over%20time%20and%20distance.png)

With there movement over time and distance:
![Movement over time and distance with the movement options: walking, sprinting, climbing and fast climbing](plots/Default/3D/Movement%20over%20time%20and%20distance.png)

And the different jumps types: default, double, triple, long, wall jump (no input) and wall jump (with input):
![Jump height over time and distance with the jump types: default, double, triple, long, wall jump (no input), wall jump (with input)](plots/Default/3D/Jump%20Height%20over%20Time%20and%20Distance.png)