#!/usr/bin/env python3

# Externqal api

def send(command, plane):
    if command == "changealt":
        command = command.split(' ')
        raise(command[1])

def changealt(change):
    if change < 0:
        plane.altitude -= change
    else:
        plane.altitude += change
