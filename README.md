# CyberAIagent
An AI agent for cybersecurity

A Python AI agent that connects to the Airouter API (which provides free LLM access), processes a list of system events in JSON format, and then asks the LLM to detect malware or potential malicious activities, you’ll need the following:

## Overview:
1. Input: JSON file with system events.
2. Process: Send the event data as a prompt to Airouter's free LLM API.
3. Output: Inference from the LLM about malware or suspicious behavior.

## Prerequisites:
1. Python 3.x
2. requests library for HTTP requests (pip install requests)
3. An API key from Airouter (sign up at https://airouter.ai/)