import math

import matplotlib.pyplot as plt
import numpy as np
import csv
from Data import Data
from typing import Optional


def main() -> None:
    # Read data from csv
    filename = "default.csv"
    m_data = read_csv(filename)

    # Normal movement
    v = m_data["v"]
    acc = m_data["acc"]
    dec = m_data["dec"]

    # Sprinting movement
    v_s = m_data["v_s"]
    acc_s = m_data["acc_s"]
    dec_s = m_data["dec_s"]

    # Jump Movement
    gravity = m_data["gravity"]
    jump_v = m_data["jump_v"]
    jump_d_v = m_data["jump_d_v"]
    jump_t_v = m_data["jump_t_v"]
    jump_l_v = m_data["jump_l_v"]

    # Plotting

    # Velocity over time
    # velocity_over_time = []
    # walk_velocity_over_time = calc_velocity_over_time(v, acc, "Walking")
    # velocity_over_time.append(walk_velocity_over_time)
    # sprint_velocity_over_time = calc_velocity_over_time(v_s, acc_s, "Sprinting")
    # velocity_over_time.append(sprint_velocity_over_time)
    # plot_and_safe(velocity_over_time, 'time (s)', 'velocity (m/s)', "Velocity over Time")

    # Movement over time
    # movement_over_time = []
    # walk_movement_over_time = calc_movement_over_time(v, acc, dec, "Walking")
    # movement_over_time.append(walk_movement_over_time)
    # sprint_movement_over_time = calc_movement_over_time(v_s, acc_s, dec_s, "Sprinting")
    # movement_over_time.append(sprint_movement_over_time)
    # plot_and_safe(movement_over_time, 'time (s)', 'velocity (m/s)', "Movement over Time")

    # Velocity over distance
    # velocity_over_distance = []
    # walk_velocity_over_distance = calc_velocity_over_distance(v, acc, "Walking")
    # velocity_over_distance.append(walk_velocity_over_distance)
    # sprint_velocity_over_distance = calc_velocity_over_distance(v_s, acc_s, "Sprinting")
    # velocity_over_distance.append(sprint_velocity_over_distance)
    # plot_and_safe(velocity_over_distance, 'distance (m)', 'velocity (m/s)', "Velocity over Distance")

    # Movement over distance
    # movement_over_distance = []
    # walk_movement_over_distance = calc_movement_over_distance(v, acc, dec, "Walking")
    # movement_over_distance.append(walk_movement_over_distance)
    # sprint_movement_over_distance = calc_movement_over_distance(v_s, acc_s, dec_s, "Sprinting")
    # movement_over_distance.append(sprint_movement_over_distance)
    # plot_and_safe(movement_over_distance, 'distance (m)', 'velocity (m/s)', "Movement over Distance")

    # Height over Time
    # height_over_time = []
    # default_jump_height_over_time = calc_height_over_time(jump_v, gravity, "Default Jump")
    # height_over_time.append(default_jump_height_over_time)
    # double_jump_height_over_time = calc_height_over_time(jump_d_v, gravity, "Double Jump")
    # height_over_time.append(double_jump_height_over_time)
    # triple_jump_height_over_time = calc_height_over_time(jump_t_v, gravity, "Triple Jump")
    # height_over_time.append(triple_jump_height_over_time)
    # long_jump_height_over_time = calc_height_over_time(jump_l_v, gravity, "Long Jump")
    # height_over_time.append(long_jump_height_over_time)
    # plot_and_safe(height_over_time, 'time (s)', 'height (m)', "Jump Height over Time")

    # Height over Distance
    height_over_distance = []
    default_jump_height_over_distance = calc_height_over_distance(jump_v, gravity, v, "Default Jump")
    height_over_distance.append(default_jump_height_over_distance)
    double_jump_height_over_distance = calc_height_over_distance(jump_d_v, gravity, v, "Double Jump")
    height_over_distance.append(double_jump_height_over_distance)
    triple_jump_height_over_distance = calc_height_over_distance(jump_t_v, gravity, v, "Triple Jump")
    height_over_distance.append(triple_jump_height_over_distance)
    long_jump_height_over_distance = calc_height_over_distance(jump_l_v, gravity, v_s, "Long Jump")
    height_over_distance.append(long_jump_height_over_distance)
    plot_and_safe(height_over_distance, 'distance (m)', 'height (m)', "Jump Height over Distance")

    # TODO: Climbing movement -> normal, sprinting -> movement over time and distance, Climb Jump!


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
