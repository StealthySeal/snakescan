import sys
import psutil

# |CPU|

# get basic CPU information
def get_cpu_stats():
    physical_cpu_count = psutil.cpu_count(logical=False)
    logical_cpu_count = psutil.cpu_count(logical=True)
    cpu_frequency = psutil.cpu_freq()
    values = [physical_cpu_count, logical_cpu_count, cpu_frequency]
    return values

# Collect CPU time statistics
def get_cpu_times():
    cpu_times = psutil.cpu_times()
    user_time = round(cpu_times.user/3600, 4)
    system_time = round(cpu_times.system/3600, 4)
    idle_time = round(cpu_times.system/3600, 4)
    values = [user_time, system_time, idle_time]
    return values # return all collected cpu time statistics

# Collect CPU usage statistics
def get_cpu_usage():
    system_cpu_utilization = psutil.cpu_percent(interval=0.1)
    indiv_cpu_utilization = psutil.cpu_percent(interval=0.1, percpu=True)
    values = [system_cpu_utilization, indiv_cpu_utilization]
    return values

# Aggregate CPU info for user queries
def cpu_info():
    print(get_cpu_stats())
    print(get_cpu_times())
    print(get_cpu_usage())

# |Memory|

# Collect memory statistics
def get_memory_stats():
    total_memory = psutil.virtual_memory()[0]/1e+9
    used_memory = psutil.virtual_memory()[3]/1e+9
    available_memory = psutil.virtual_memory()[1]/1e+9
    values = [total_memory, used_memory, available_memory]
    return values

# Collect swap memory statistics
def get_swap_memory_stats():
    total_swap_memory = psutil.swap_memory()[0]/1e+9
    used_swap_memory = psutil.swap_memory()[1]/1e+9
    available_swap_memory = psutil.swap_memory()[2]/1e+9
    values = [total_swap_memory, used_swap_memory, available_swap_memory]
    return values

# Aggregate memory info for user queries
def memory_info():
    print(get_memory_stats())
    print(get_swap_memory_stats())
