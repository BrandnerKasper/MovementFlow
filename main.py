import math

import matplotlib.pyplot as plt
import numpy as np
import csv
from Data import Data
from typing import Optional


def main() -> None:
    # Read data from csv
    filename = "DK64.csv"
    m_data = read_csv(filename)

    # Normal movement
    v = m_data["v"]
    acc = m_data["acc"]
    dec = m_data["dec"]

    # Sprinting movement
    sprint_v = m_data["sprint_v"]
    sprint_acc = m_data["sprint_acc"]
    sprint_dec = m_data["sprint_dec"]

    # Jump Movement
    gravity = m_data["gravity"]
    jump = m_data["jump"]
    double_jump = m_data["double_jump"]
    triple_jump = m_data["triple_jump"]
    long_jump = m_data["long_jump"]
    wall_jump = m_data["wall_jump"]
    wall_jump_h = m_data["wall_jump_h"]

    # Climbing
    climb_v = m_data["climb_v"]
    climb_acc = m_data["climb_acc"]
    climb_dec = m_data["climb_dec"]
    climb_sprint_v = m_data["climb_sprint_v"]

    # Plotting

    # Velocity over time
    velocity_over_time = []
    walk_velocity_over_time = calc_velocity_over_time(v, acc, "Walking")
    velocity_over_time.append(walk_velocity_over_time)
    sprint_velocity_over_time = calc_velocity_over_time(sprint_v, sprint_acc, "Sprinting")
    velocity_over_time.append(sprint_velocity_over_time)
    climb_velocity_over_time = calc_velocity_over_time(climb_v, climb_acc, "Climbing")
    velocity_over_time.append(climb_velocity_over_time)
    fast_climb_velocity_over_time = calc_velocity_over_time(climb_sprint_v, climb_acc, "Fast Climbing")
    velocity_over_time.append(fast_climb_velocity_over_time)
    plot_and_safe(velocity_over_time, 'time (s)', 'velocity (m/s)', "Velocity over Time")

    # Movement over time
    movement_over_time = []
    walk_movement_over_time = calc_movement_over_time(v, acc, dec, "Walking")
    movement_over_time.append(walk_movement_over_time)
    sprint_movement_over_time = calc_movement_over_time(sprint_v, sprint_acc, sprint_dec, "Sprinting")
    movement_over_time.append(sprint_movement_over_time)
    sprint_climb_movement_over_time = calc_movement_over_time(climb_sprint_v, climb_acc, climb_dec, "Fast Climbing")
    movement_over_time.append(sprint_climb_movement_over_time)
    default_climb_movement_over_time = calc_movement_over_time(climb_v, climb_acc, climb_dec, "Climbing")
    movement_over_time.append(default_climb_movement_over_time)
    plot_and_safe(movement_over_time, 'time (s)', 'velocity (m/s)', "Movement over Time")

    # Velocity over distance
    velocity_over_distance = []
    walk_velocity_over_distance = calc_velocity_over_distance(v, acc, "Walking")
    velocity_over_distance.append(walk_velocity_over_distance)
    sprint_velocity_over_distance = calc_velocity_over_distance(sprint_v, sprint_acc, "Sprinting")
    velocity_over_distance.append(sprint_velocity_over_distance)
    fast_climb_velocity_over_distance = calc_velocity_over_distance(climb_sprint_v, climb_acc, "Fast Climbing")
    velocity_over_distance.append(fast_climb_velocity_over_distance)
    climb_velocity_over_distance = calc_velocity_over_distance(climb_v, climb_acc, "Climbing")
    velocity_over_distance.append(climb_velocity_over_distance)
    plot_and_safe(velocity_over_distance, 'distance (m)', 'velocity (m/s)', "Velocity over Distance")

    # Movement over distance
    movement_over_distance = []
    walk_movement_over_distance = calc_movement_over_distance(v, acc, dec, "Walking")
    movement_over_distance.append(walk_movement_over_distance)
    sprint_movement_over_distance = calc_movement_over_distance(sprint_v, sprint_acc, sprint_dec, "Sprinting")
    movement_over_distance.append(sprint_movement_over_distance)
    sprint_climb_movement_over_distance = calc_movement_over_distance(climb_sprint_v, climb_acc, climb_dec, "Fast Climbing")
    movement_over_distance.append(sprint_climb_movement_over_distance)
    default_climb_movement_over_distance = calc_movement_over_distance(climb_v, climb_acc, climb_dec, "Climbing")
    movement_over_distance.append(default_climb_movement_over_distance)
    plot_and_safe(movement_over_distance, 'distance (m)', 'velocity (m/s)', "Movement over Distance")

    # Height over Time
    height_over_time = []
    default_jump_height_over_time = calc_height_over_time(jump, gravity, "Default Jump")
    height_over_time.append(default_jump_height_over_time)
    double_jump_height_over_time = calc_height_over_time(double_jump, gravity, "Double Jump")
    height_over_time.append(double_jump_height_over_time)
    triple_jump_height_over_time = calc_height_over_time(triple_jump, gravity, "Triple Jump")
    height_over_time.append(triple_jump_height_over_time)
    long_jump_height_over_time = calc_height_over_time(long_jump, gravity, "Long Jump")
    height_over_time.append(long_jump_height_over_time)
    wall_jump_height_over_time = calc_height_over_time(wall_jump, gravity, "Wall Jump")
    height_over_time.append(wall_jump_height_over_time)
    plot_and_safe(height_over_time, 'time (s)', 'height (m)', "Jump Height over Time")

    # Height over Distance
    height_over_distance = []
    default_jump_height_over_distance = calc_height_over_distance(jump, gravity, v, "Default Jump")
    height_over_distance.append(default_jump_height_over_distance)
    double_jump_height_over_distance = calc_height_over_distance(double_jump, gravity, v, "Double Jump")
    height_over_distance.append(double_jump_height_over_distance)
    triple_jump_height_over_distance = calc_height_over_distance(triple_jump, gravity, v, "Triple Jump")
    height_over_distance.append(triple_jump_height_over_distance)
    long_jump_height_over_distance = calc_height_over_distance(long_jump, gravity, sprint_v, "Long Jump")
    height_over_distance.append(long_jump_height_over_distance)
    no_input_wall_jump_height_over_distance = calc_height_over_distance(wall_jump, gravity, wall_jump_h, "Wall Jump No Input")
    height_over_distance.append(no_input_wall_jump_height_over_distance)
    with_input_wall_jump_height_over_distance = \
        calc_height_over_distance(wall_jump, gravity, wall_jump_h + 0.41 * v, "Wall Jump With Input")
    # the 0.41 is rough estimation, for game balancing purpose and fighting wall hugging there is a small delay
    # after the wall jump before the player is allowed to air drift into a direction
    height_over_distance.append(with_input_wall_jump_height_over_distance)
    plot_and_safe(height_over_distance, 'distance (m)', 'height (m)', "Jump Height over Distance")

    # Climb movement over time
    # climb_movement_over_time = []
    # default_climb_movement_over_time = calc_movement_over_time(v_c, acc_c, dec_c, "Default")
    # climb_movement_over_time.append(default_climb_movement_over_time)
    # sprint_climb_movement_over_time = calc_movement_over_time(v_c_s, acc_c, dec_c, "Sprinting")
    # climb_movement_over_time.append(sprint_climb_movement_over_time)
    # plot_and_safe(climb_movement_over_time, 'time (s)', 'velocity (m/s)', "Climb Movement over Time")

    # CLimb movement over distance
    # climb_movement_over_distance = []
    # default_climb_movement_over_distance = calc_movement_over_distance(v_c, acc_c, dec_c, "Default")
    # climb_movement_over_distance.append(default_climb_movement_over_distance)
    # sprint_climb_movement_over_distance = calc_movement_over_distance(v_c_s, acc_c, dec_c, "Sprinting")
    # climb_movement_over_distance.append(sprint_climb_movement_over_distance)
    # plot_and_safe(climb_movement_over_distance, 'distance (m)', 'velocity (m/s)', "Climb Movement over Distance")

    # Climb Jump Height over Time
    # climb_jump_height_over_time = []
    # default_climb_jump_height_over_time = calc_height_over_time(jump_c_vv, gravity)
    # climb_jump_height_over_time.append(default_climb_jump_height_over_time)
    # plot_and_safe(climb_jump_height_over_time, 'time (s)', 'height (m)', "Climb Jump Height over Time")

    # Climb Jump Height over Distance
    # climb_jump_height_over_distance = []
    # no_input_climb_jump_height_over_distance = calc_height_over_distance(jump_c_vv, gravity, jump_c_hv, "No Input")
    # climb_jump_height_over_distance.append(no_input_climb_jump_height_over_distance)
    # with_input_climb_jump_height_over_distance = \
    #     calc_height_over_distance(jump_c_vv, gravity, jump_c_hv + 0.41*v, "With Input")
    # # the 0.41 is rough estimation, for game balancing purpose and fighting wall hugging there is a small delay
    # # after the wall jump before the player is allowed to air drift into a direction
    # climb_jump_height_over_distance.append(with_input_climb_jump_height_over_distance)
    # plot_and_safe(climb_jump_height_over_distance, 'distance (m)', 'height (m)', "Climb Jump Height over Distance")


def read_csv(filename: str) -> dict[str, float]:
    filepath = "data/" + filename
    data = {}
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            key = line[0]
            value = line[1]
            try:
                data[key] = float(value)
            except ValueError:
                data[key] = value
    return data


def calc_velocity_over_time(v: float, acc: float, label: Optional[str] = None) -> Data:
    v = np.arange(0, v, 0.01)
    t = v / acc
    return Data(t, v, label)


def calc_movement_over_time(v: float, acc: float, dec: float, label: Optional[str] = None, offset: float = 0.5) -> Data:
    t_acc = v / acc
    t_dec = v / dec
    x = np.arange(0, t_acc + offset + t_dec, 0.0001)

    conditions = [
        (x < t_acc),
        (t_acc <= x) & (x < t_acc + offset),
        (t_acc + offset <= x)
    ]
    functions = [
        lambda n: acc * n,
        lambda n: v,
        lambda n: v - dec * (n - t_acc - offset)
    ]
    y = np.piecewise(x, conditions, functions)

    return Data(x, y, label)


def calc_velocity_over_distance(v: float, acc: float, label: Optional[str] = None) -> Data:
    v = np.arange(0, v, 0.01)
    d = (v * v) / (2 * acc)

    return Data(d, v, label)


def calc_movement_over_distance(v: float, acc: float, dec: float, label: Optional[str] = None, offset: float = 5)\
        -> Data:
    # d = (v * v) / (2 * acc) v_0 -> v_max
    d_max_v = (v * v) / (2 * acc)
    d_start_dec = d_max_v + offset
    # d = (v * v) / (2 * decc) v_max -> v_0
    d_stopp = d_start_dec + (v * v) / (2 * dec)

    x = np.arange(0, d_stopp, 0.00001)
    conditions = [
        (x < d_max_v),
        (d_max_v <= x) & (x < d_start_dec),
        (d_start_dec <= x)
    ]
    functions = [
        lambda n: np.sqrt(n * 2 * acc),
        lambda n: v,
        lambda n: v - dec * ((-v + np.sqrt(v * v + 2 * dec * (d_start_dec - n))) / (-dec))
    ]
    y = np.piecewise(x, conditions, functions)

    return Data(x, y, label)


def calc_height_over_time(jump_v: float, gravity: float, label: Optional[str] = None) -> Data:
    # Calc max jump height
    h_max = math.pow(jump_v, 2) / (gravity * -2.0)

    # Calc time in air
    t_max = math.sqrt(-2.0 * h_max / gravity) * 2.0

    t = np.arange(0, t_max, 0.0001)
    conditions = [
        (t <= t_max/2),
        (t > t_max/2)
    ]
    # h = jump_v * t + 0.5 * gravity * t**2
    functions = [
        lambda n: jump_v * n + 0.5 * gravity * n**2,
        lambda n: jump_v * n + 0.5 * gravity * (-n)**2
    ]

    h = np.piecewise(t, conditions, functions)

    return Data(t, h, label)


def calc_height_over_distance(jump_v: float, gravity: float, ground_v: float, label: Optional[str] = None) -> Data:
    # Calc max jump height
    h_max = math.pow(jump_v, 2) / (gravity * -2.0)

    # Calc time in air
    t_max = math.sqrt(-2.0 * h_max / gravity) * 2.0

    # Calc distance covered while in air
    d_max = ground_v * t_max

    d = np.arange(0, d_max, 0.0001)
    conditions = [
        (d <= d_max/2),
        (d > d_max/2)
    ]
    # h = jump_v * (d/ground_v) + 0.5 * gravity * (d/ground_v)**2
    functions = [
        lambda n: jump_v * (n / ground_v) + 0.5 * gravity * (n / ground_v)**2,
        lambda n: jump_v * (n / ground_v) + 0.5 * gravity * (-n / ground_v) ** 2,
    ]

    h = np.piecewise(d, conditions, functions)

    return Data(d, h, label)


def plot_and_safe(data: list[Data], xlabel: str, ylabel: str, title: str) -> None:
    fig, ax = plt.subplots()
    for d in data:
        x = d.x
        y = d.y

        if d.label is not None:
            label = d.label
            ax.plot(x, y, label=label)
            ax.legend()

        else:
            ax.plot(x, y)

    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.grid()

    title.replace(' ', '_')
    title.lower()
    path = "plots/" + title
    fig.savefig(path + ".png")
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
