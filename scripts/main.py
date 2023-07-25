from Data import *


def main() -> None:
    # example to plot 3d all games in comparison
    filename = "All.csv"
    plot_all_comparisons_in_3d(filename, 500, '+')

    # example to plot 3d one game and those movement in comparison
    # filename = "Ours.csv"
    # plot_single_in_3d(filename, 500, '+')


def plot_all_comparisons_in_3d(filename: str, scatter_amount: int, symbol: str) -> None:
    m_data_list = read_csv_multiple(filename)

    # Velocity over Time and Distance
    plot_velocity_over_time_and_distance_multi(m_data_list, "v", "acc", "Walk Velocity over Time and Distance",
                                               scatter_amount, symbol)
    plot_velocity_over_time_and_distance_multi(m_data_list, "sprint_v", "sprint_acc",
                                               "Sprint Velocity over Time and Distance", scatter_amount, symbol)
    plot_velocity_over_time_and_distance_multi(m_data_list, "climb_v", "climb_acc",
                                               "Climbing Velocity over Time and Distance", scatter_amount, symbol)
    plot_velocity_over_time_and_distance_multi(m_data_list, "climb_sprint_v", "climb_acc",
                                               "Fast Climbing Velocity over Time and Distance", scatter_amount, symbol)

    # Movement over Time and Distance
    plot_movement_over_time_and_distance_multi(m_data_list, "v", "acc", "dec", "Walk Movement over Time and Distance",
                                               scatter_amount, symbol)
    plot_movement_over_time_and_distance_multi(m_data_list, "sprint_v", "sprint_acc", "sprint_dec",
                                               "Sprint Movement over Time and Distance", scatter_amount, symbol)
    plot_movement_over_time_and_distance_multi(m_data_list, "climb_v", "climb_acc", "climb_dec",
                                               "Climbing Movement over Time and Distance", scatter_amount, symbol)
    plot_movement_over_time_and_distance_multi(m_data_list, "climb_sprint_v", "climb_acc", "climb_dec",
                                               "Fast Climbing Movement over Time and Distance", scatter_amount, symbol)

    # Height over time and distance
    plot_height_over_time_and_distance_multi(m_data_list, "jump", "gravity", "v", "Default Jump over Time and Distance",
                                             scatter_amount, symbol)
    plot_height_over_time_and_distance_multi(m_data_list, "double_jump", "gravity", "v",
                                             "Double Jump over Time and Distance", scatter_amount, symbol)
    plot_height_over_time_and_distance_multi(m_data_list, "triple_jump", "gravity", "v",
                                             "Triple Jump over Time and Distance", scatter_amount, symbol)
    plot_height_over_time_and_distance_multi(m_data_list, "long_jump", "gravity", "sprint_v",
                                             "Long Jump over Time and Distance", scatter_amount, symbol)
    plot_height_over_time_and_distance_multi(m_data_list, "wall_jump", "gravity", "wall_jump_h",
                                             "Wall Jump over Time and Distance (No Input)", scatter_amount, symbol)
    plot_height_over_time_and_distance_multi(m_data_list, "wall_jump", "gravity", "v",
                                             "Wall Jump over Time and Distance (With Input)", scatter_amount, symbol)


def plot_single_in_2d(filename: str) -> None:
    # Read data from csv
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
    sprint_climb_movement_over_distance = calc_movement_over_distance(climb_sprint_v, climb_acc, climb_dec,
                                                                      "Fast Climbing")
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
    no_input_wall_jump_height_over_distance = calc_height_over_distance(wall_jump, gravity, wall_jump_h,
                                                                        "Wall Jump No Input")
    height_over_distance.append(no_input_wall_jump_height_over_distance)
    with_input_wall_jump_height_over_distance = \
        calc_height_over_distance(wall_jump, gravity, wall_jump_h + 0.41 * v, "Wall Jump With Input")
    # the 0.41 is rough estimation, for game balancing purpose and fighting wall hugging there is a small delay
    # after the wall jump before the player is allowed to air drift into a direction
    height_over_distance.append(with_input_wall_jump_height_over_distance)
    plot_and_safe(height_over_distance, 'distance (m)', 'height (m)', "Jump Height over Distance")


def plot_single_in_3d(filename: str, scatter_amount: int = 100, symbol: str = 'o') -> None:
    # Read data from csv
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

    # Plotting 3D
    # Velocity over time and distance
    velocity_over_time_and_distance = []
    walk_velocity_over_time_and_distance = calc_velocity_over_time_and_distance(v, acc, "Walking", scatter_amount)
    velocity_over_time_and_distance.append(walk_velocity_over_time_and_distance)
    sprint_velocity_over_time_and_distance = calc_velocity_over_time_and_distance(sprint_v, sprint_acc, "Sprinting",
                                                                                  scatter_amount)
    velocity_over_time_and_distance.append(sprint_velocity_over_time_and_distance)
    fast_climb_velocity_over_time_and_distance = calc_velocity_over_time_and_distance(climb_sprint_v, climb_acc,
                                                                                      "Fast Climbing", scatter_amount)
    velocity_over_time_and_distance.append(fast_climb_velocity_over_time_and_distance)
    climb_velocity_over_time_and_distance = calc_velocity_over_time_and_distance(climb_v, climb_acc, "Climbing",
                                                                                 scatter_amount)
    velocity_over_time_and_distance.append(climb_velocity_over_time_and_distance)
    plot_and_safe_3d(velocity_over_time_and_distance, 'time (s)', 'distance (m)', 'velocity (m/s)',
                     "Velocity over time and distance", symbol)

    # Movement over time and distance
    movement_over_time_and_distance = []
    walk_movement_over_time_and_distance = calc_movement_over_time_and_distance(v, acc, dec, "Walking", 0.5,
                                                                                scatter_amount)
    movement_over_time_and_distance.append(walk_movement_over_time_and_distance)
    sprint_movement_over_time_and_distance = calc_movement_over_time_and_distance(sprint_v, sprint_acc, sprint_dec,
                                                                                  "Sprinting", 0.5, scatter_amount)
    movement_over_time_and_distance.append(sprint_movement_over_time_and_distance)
    fast_climb_movement_over_time_and_distance = calc_movement_over_time_and_distance(climb_sprint_v, climb_acc,
                                                                                      climb_dec, "Fast Climbing",
                                                                                      0.5, scatter_amount)
    movement_over_time_and_distance.append(fast_climb_movement_over_time_and_distance)
    climb_movement_over_time_and_distance = calc_movement_over_time_and_distance(climb_v, climb_acc, climb_dec,
                                                                                 "Climbing", 0.5, scatter_amount)
    movement_over_time_and_distance.append(climb_movement_over_time_and_distance)
    plot_and_safe_3d(movement_over_time_and_distance, 'time (s)', 'distance (m)', 'velocity (m/s)',
                     "Movement over time and distance", symbol)

    # Height over time and distance
    height_over_time_and_distance = []
    jump_height_over_time_and_distance = calc_height_over_time_and_distance(jump, gravity, v, "Default Jump",
                                                                            scatter_amount)
    height_over_time_and_distance.append(jump_height_over_time_and_distance)
    double_jump_height_over_time_and_distance = calc_height_over_time_and_distance(double_jump, gravity, v,
                                                                                   "Double Jump", scatter_amount)
    height_over_time_and_distance.append(double_jump_height_over_time_and_distance)
    triple_jump_height_over_time_and_distance = calc_height_over_time_and_distance(triple_jump, gravity, v,
                                                                                   "Triple Jump", scatter_amount)
    height_over_time_and_distance.append(triple_jump_height_over_time_and_distance)
    long_jump_calc_height_over_time_and_distance = calc_height_over_time_and_distance(long_jump, gravity, sprint_v,
                                                                                      "Long Jump", scatter_amount)
    height_over_time_and_distance.append(long_jump_calc_height_over_time_and_distance)
    wall_jump_height_over_time_and_distance_no_input = calc_height_over_time_and_distance(wall_jump, gravity,
                                                                                          wall_jump_h,
                                                                                          "Wall Jump no input",
                                                                                          scatter_amount)
    height_over_time_and_distance.append(wall_jump_height_over_time_and_distance_no_input)
    # 0.41 * v is a rough estimation based on the delay in the game to fight wall hugging
    wall_jump_height_over_time_and_distance_with_input = calc_height_over_time_and_distance(wall_jump, gravity,
                                                                                            wall_jump_h + 0.41 * v,
                                                                                            "Wall Jump with input",
                                                                                            scatter_amount)
    height_over_time_and_distance.append(wall_jump_height_over_time_and_distance_with_input)
    plot_and_safe_3d(height_over_time_and_distance, 'time (s)', 'distance (m)', 'height (m)',
                     "Jump Height over Time and Distance", symbol)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
