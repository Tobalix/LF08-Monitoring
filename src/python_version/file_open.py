from datetime import datetime
def file_open(now):
    x = 0

    date_today = now.strftime("%Y-%m-%d_")
    while x == x:
        cpu_log_file_path = f"../../logs/{date_today}CPU.log"
        cpu_log = open(f'{cpu_log_file_path}', 'r')
        cpu_lines = cpu_log.readlines()

        count = 0
        for line in cpu_lines:
            count += 1
            print("CPU L{}: {}".format(count, line.strip()))
        print("\n")

        disk_log_file_path = f"../../logs/{date_today}DISK.log"
        disk_log = open(f'{disk_log_file_path}', 'r')
        disk_lines = disk_log.readlines()
        count = 0
        for line in disk_lines:
            count += 1
            print("DISK L{}: {}".format(count, line.strip()))
        print("\n")

        ram_log_file_path = f"../../logs/{date_today}RAM.log"
        ram_log = open(f'{ram_log_file_path}', 'r')
        ram_lines = ram_log.readlines()
        count = 0
        for line in ram_lines:
            count += 1
            print("RAM L{}: {}".format(count, line.strip()))
        print("\n")