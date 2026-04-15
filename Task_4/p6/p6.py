import platform
import datetime

def log_system_info():
    os_type = platform.system()
    current_time = datetime.datetime.now()
    log_message = f"OS: {os_type}, Timestamp: {current_time}\n"
    try:
        with open("sys_log.txt", "a") as file:
            file.write(log_message)
    except Exception as e:
        print(f"Error found: {e}")

def main():
    log_system_info()


if __name__ == "__main__":
    main()