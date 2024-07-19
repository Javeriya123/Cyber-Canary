#!/usr/bin/python3

import sys
import re
import subprocess
from collections import Counter

def detect_brute_force(command, threshold):
    command_pattern = re.compile(re.escape(command))
    command_counter = Counter()

    for line in sys.stdin:
        line = line.strip()
        print(f"Received log line: {line}")  # For debugging
        if command_pattern.search(line):
            command_counter[command] += 1
            if command_counter[command] > threshold:
                message = f"Brute force attack detected: '{command}' executed {command_counter[command]} times"
                print(message)
                # Send the log message to syslog for forwarding
                subprocess.run(['logger', '-t', 'bruteforce_detector', message])
                sys.stderr.write(message + '\n')
                return

if __name__ == "__main__":
    command_to_detect = 'Running Docker command'  # Part of the log output to match
    execution_threshold = 3  # Set the threshold for brute-force detection
    detect_brute_force(command_to_detect, execution_threshold)

