# debugging.py

# Function to get user input
def get_daily_steps():
    """Return list of daily steps."""
    steps = input("Enter your daily steps for 7 days separated by spaces: ")
    step_list = steps.split()                    # BUG 1: faltaban los paréntesis en split()
    step_list = [int(s) for s in step_list]
    return step_list

# Function to calculate total steps
def total_steps(nums):
    """Return total steps."""
    total = sum(nums)
    return total                                 # BUG 2: faltaba el return

# Function to calculate average daily steps
def average_steps(total, days=7):
    """Return average steps as int."""
    return int(total // days)                    # BUG 3: debía retornar int, no float (/ → //)

# Function to get maximum steps
def max_steps(nums):
    """Return max steps."""
    max_val = max(nums)
    return max_val                               # BUG 4: retornaba 'maxvalue' (variable inexistente)

# Function to get minimum steps
def min_steps(nums):
    """Return min steps."""
    return min(nums)

# Function to check if each day meets the goal
def goal_check(nums, goal=10000):
    """Return list of booleans for goal."""
    result = []
    for s in nums:
        if s >= goal:
            result.append(True)
        else:
            result.append(False)
    return result

# ----------------------
# Main Program
# ----------------------
step_list = get_daily_steps()

total = total_steps(step_list)
average = average_steps(total)
highest = max_steps(step_list)
lowest = min_steps(step_list)
goal_met = goal_check(step_list)

print("Total steps:", total)
print("Average daily steps:", average)
print("Highest steps in a day:", highest)
print("Lowest steps in a day:", lowest)
print("Goal met each day:", goal_met)
