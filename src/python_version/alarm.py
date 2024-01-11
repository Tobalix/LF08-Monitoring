from src.python_version.resources.constants import *
import datetime
import time
from datetime import datetime
from sending_emails import send_mail, send_mail_summary


def alarm():
    x = 0
    print(YELLOW, "Alarm program starts in 5 sec")
    print(RESET)
    time.sleep(5)
    now = datetime.now()
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

        time_now = now.strftime("%Y-%m-%d, %H:%M:%S")
        alarm_message = "MESSAGE: Alarm Email was sent for"
        info_message = "MESSAGE: Info Email was sent for"
        no_mail_message = "MESSAGE: No Email sent for"

        time_for_summary = datetime.now()
        is_time_for_summary = float(time_for_summary.strftime("%H.%M"))
        print("Hour of Day:", is_time_for_summary)

# Daily Summary Email
        if is_time_for_summary == 12.23:
            print("Sending Summary of today.")
            send_mail_summary(cpu_log_file_path, disk_log_file_path, ram_log_file_path)

        # Send Alarm or not?
        alarm_type = CPU
        if cpu_lines[-1].split(" ")[0] == INFO:
            send_mail(time_now, cpu_log_file_path, alarm_type)
            print(YELLOW + info_message, alarm_type)
        elif cpu_lines[-1].split(" ")[0] == WARNING:
            send_mail(time_now, cpu_log_file_path, alarm_type)
            print(RED + alarm_message, alarm_type)
        else:
            print(GREEN + no_mail_message, alarm_type)

        alarm_type = DISK
        if disk_lines[-1].split(" ")[0] == INFO:
            send_mail(time_now, disk_log_file_path, alarm_type)
            print(YELLOW + alarm_message, alarm_type)
        elif disk_lines[-1].split(" ")[0] == WARNING:
            send_mail(time_now, disk_log_file_path, alarm_type)
            print(RED + alarm_message, alarm_type)
        else:
            print(GREEN + no_mail_message, alarm_type)

        alarm_type = RAM
        if ram_lines[-1].split(" ")[0] == INFO:
            send_mail(time_now, ram_log_file_path, alarm_type)
            print(YELLOW + alarm_message, alarm_type)
        elif ram_lines[-1].split(" ")[0] == WARNING:
            send_mail(time_now, ram_log_file_path, alarm_type)
            print(RED + alarm_message, alarm_type)
        else:
            print(GREEN + no_mail_message, alarm_type)
            time.sleep(5)

        print(RESET)
