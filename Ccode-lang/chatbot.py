#!/usr/bin/env python

running = True
while running:
    inp = raw_input(">> ")
    if inp == "hello" or inp == "hi":
        print("hello")
    elif inp == "stop" or inp == "exit" or inp == "quit":
        print("stopping program")
        running = False
    else:
        print("I don't understand")