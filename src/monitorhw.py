import psutil


# function to get the cpu usage
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

print(get_cpu_usage(), psutil.cpu_stats())