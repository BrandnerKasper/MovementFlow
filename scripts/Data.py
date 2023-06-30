import csv
import math
import numpy as np
from typing import Optional

from matplotlib import pyplot as plt


class Data2D:
    def __init__(self, x: np.ndarray, y: np.ndarray, label: Optional[str] = None):
        self.x = x
        self.y = y
        self.label = label

    x: np.ndarray
    y: np.ndarray
    label: Optional[str]


# 2D movement graphs
def calc_velocity_over_time(v: float, acc: float, label: Optional[str] = None) -> Data2D:
    v = np.arange(0, v, 0.01)
    t = v / acc
    return Data2D(t, v, label)


def calc_movement_over_time(v: float, acc: float, dec: float, label: Optional[str] = None, offset: float = 0.5) -> Data2D:
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

    return Data2D(x, y, label)


def calc_velocity_over_distance(v: float, acc: float, label: Optional[str] = None) -> Data2D:
    v = np.arange(0, v, 0.01)
    d = (v * v) / (2 * acc)

    return Data2D(d, v, label)


def calc_movement_over_distance(v: float, acc: float, dec: float, label: Optional[str] = None, offset: float = 5) \
        -> Data2D:
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

    return Data2D(x, y, label)


def calc_height_over_time(jump_v: float, gravity: float, label: Optional[str] = None) -> Data2D:
    # Calc max jump height
    h_max = math.pow(jump_v, 2) / (gravity * -2.0)

    # Calc time in air
    t_max = math.sqrt(-2.0 * h_max / gravity) * 2.0

    t = np.arange(0, t_max, 0.0001)
    conditions = [
        (t <= t_max / 2),
        (t > t_max / 2)
    ]
    # h = jump_v * t + 0.5 * gravity * t**2
    functions = [
        lambda n: jump_v * n + 0.5 * gravity * n ** 2,
        lambda n: jump_v * n + 0.5 * gravity * (-n) ** 2
    ]

    h = np.piecewise(t, conditions, functions)

    return Data2D(t, h, label)


def calc_height_over_distance(jump_v: float, gravity: float, ground_v: float, label: Optional[str] = None) -> Data2D:
    # Calc max jump height
    h_max = math.pow(jump_v, 2) / (gravity * -2.0)

    # Calc time in air
    t_max = math.sqrt(-2.0 * h_max / gravity) * 2.0

    # Calc distance covered while in air
    d_max = ground_v * t_max

    d = np.arange(0, d_max, 0.0001)
    conditions = [
        (d <= d_max / 2),
        (d > d_max / 2)
    ]
    # h = jump_v * (d/ground_v) + 0.5 * gravity * (d/ground_v)**2
    functions = [
        lambda n: jump_v * (n / ground_v) + 0.5 * gravity * (n / ground_v) ** 2,
        lambda n: jump_v * (n / ground_v) + 0.5 * gravity * (-n / ground_v) ** 2,
    ]

    h = np.piecewise(d, conditions, functions)

    return Data2D(d, h, label)


# Read csv single
def read_csv(filename: str) -> dict[str, float]:
    filepath = "../data/" + filename
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


# Plotting 2D
def plot_and_safe(data: list[Data2D], xlabel: str, ylabel: str, title: str) -> None:
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
    path = "../plots/" + title
    fig.savefig(path + ".png")
    plt.show()


class Data3D:
    def __init__(self, x: np.ndarray, y: np.ndarray, z: np.ndarray,  label: Optional[str] = None):
        self.x = x
        self.y = y
        self.z = z
        self.label = label

    x: np.ndarray
    y: np.ndarray
    z: np.ndarray
    label: Optional[str]


def calc_velocity_over_time_and_distance(v: float, acc: float, label: Optional[str] = None, scatter_amount: int = 100) \
        -> Data3D:
    v = np.arange(0, v, 1 / scatter_amount)
    t = v / acc
    d = (v * v) / (2 * acc)
    return Data3D(x=t, y=d, z=v, label=label)


def calc_movement_over_time_and_distance(v_max: float, acc: float, dec: float, label: Optional[str] = None,
                                         time_offset: float = 0.5, scatter_amount: int = 100) -> Data3D:
    # over time
    t_acc = v_max / acc
    t_dec = v_max / dec
    t_max = t_acc + time_offset + t_dec
    t = np.arange(0, t_max, 1 / scatter_amount)

    conditions = [
        (t < t_acc),
        (t_acc <= t) & (t < t_acc + time_offset),
        (t_acc + time_offset <= t)
    ]
    functions = [
        lambda n: acc * n,
        lambda n: v_max,
        lambda n: v_max - dec * (n - t_acc - time_offset)
    ]
    v = np.piecewise(t, conditions, functions)

    # over distance
    d = np.cumsum(v) * (1 / scatter_amount)

    return Data3D(x=t, y=d, z=v, label=label)


def calc_height_over_time_and_distance(jump_v: float, gravity: float, ground_v: float, label: Optional[str] = None,
                                       scatter_amount: int = 100) -> Data3D:
    # Calc max jump height
    h_max = math.pow(jump_v, 2) / (gravity * -2.0)

    # Calc time in air
    t_max = math.sqrt(-2.0 * h_max / gravity) * 2.0

    t = np.arange(0, t_max, 1 / scatter_amount)
    conditions = [
        (t <= t_max / 2),
        (t > t_max / 2)
    ]
    # h = jump_v * t + 0.5 * gravity * t**2
    functions = [
        lambda n: jump_v * n + 0.5 * gravity * n ** 2,
        lambda n: jump_v * n + 0.5 * gravity * (-n) ** 2
    ]

    h = np.piecewise(t, conditions, functions)

    d = ground_v * t

    return Data3D(x=t, y=d, z=h, label=label)


# Read from csv multi
def read_csv_multiple(filename: str) -> list[dict[str, float]]:
    filepath = "../data/" + filename
    data_list = []
    for n in [1, 2, 3, 4]:
        data = {}
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            for line in reader:
                key = line[0]
                value = line[n]
                try:
                    data[key] = float(value)
                except ValueError:
                    data[key] = value
        data_list.append(data)
    return data_list


# Plotting in 3D
def plot_velocity_over_time_and_distance_multi(data: list[dict[str, float]], v_key: str, acc_key: str, title: str,
                                               scatter_amount: int, symbol: str) \
        -> None:
    velocity_over_time_and_distance = []
    for d in data:
        v = d[v_key]
        acc = d[acc_key]
        label = d["Game"]
        velocity_over_time_and_distance.append(calc_velocity_over_time_and_distance(v, acc, label, scatter_amount))
    plot_and_safe_3d(velocity_over_time_and_distance, 'time (s)', 'distance (m)', 'velocity (m/s)', title, symbol)


def plot_movement_over_time_and_distance_multi(data: list[dict[str, float]], v_key: str, acc_key: str, dec_key: str,
                                               title: str, scatter_amount: int, symbol: str) \
        -> None:
    movement_over_time_and_distance = []
    for d in data:
        v = d[v_key]
        acc = d[acc_key]
        dec = d[dec_key]
        label = d["Game"]
        movement_over_time_and_distance.append(calc_movement_over_time_and_distance(v, acc, dec, label, 0.5, scatter_amount))
    plot_and_safe_3d(movement_over_time_and_distance, 'time (s)', 'distance (m)', 'velocity (m/s)', title, symbol)


def plot_height_over_time_and_distance_multi(data: list[dict[str, float]], jump_key: str, gravity_key: str, v_key: str,
                                             title: str, scatter_amount: int, symbol: str) \
        -> None:
    height_over_time_and_distance = []

    for d in data:
        jump = d[jump_key]
        gravity = d[gravity_key]
        v = d[v_key]
        label = d["Game"]
        height_over_time_and_distance.append(
            calc_height_over_time_and_distance(jump, gravity, v, label, scatter_amount))
    plot_and_safe_3d(height_over_time_and_distance, 'time (s)', 'distance (m)', 'height (m)', title, symbol)


def plot_and_safe_3d(data: list[Data3D], xlabel: str, ylabel: str, zlabel: str, title: str, symbol: str = 'o') -> None:
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    for d in data:
        x = d.x
        y = d.y
        z = d.z

        if d.label is not None:
            label = d.label
            ax.scatter(x, y, z, marker=symbol, label=label)
            ax.legend()

        else:
            ax.scatter(x, y, z, marker=symbol)

    ax.set(xlabel=xlabel, ylabel=ylabel, zlabel=zlabel, title=title)
    ax.grid()

    title.replace(' ', '_')
    title.lower()
    path = "../plots/" + title
    fig.savefig(path + ".png")

    plt.show()


