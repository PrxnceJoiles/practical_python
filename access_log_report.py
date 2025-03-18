#!/usr/bin/env python3

import argparse
from collections import Counter
import re

def log_generator(filename):
    """
    Reads the log file and extracts statistics on User-Agent counts.
    """
    user_agents = []
    #the r designates a raw string literal, ensuring that backslashes are treated correctly
    #The "[^"]*" matches a quoted string 
    #The \s* matches any whitespac characters that separste fields
    #The "([^"]*)" captures the user agent string inside the last pair of double quotes
    #The $ ensures the match happens at the end of the line

    pattern = r'"[^"]*"\s*"([^"]*)"$'  # Regex to capture User-Agent
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                match = re.search(pattern, line)
                if match:
                    user_agents.append(match.group(1))
        
        agent_counts = Counter(user_agents)
        print(f"Total unique User-Agents: {len(agent_counts)}")
        for agent, count in agent_counts.most_common():
            print(f"{agent}: {count}")
    
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Accepts a log file and processes its details")
    parser.add_argument("filename", help="The name of the log file for processing")
    args = parser.parse_args()
    log_generator(args.filename)
