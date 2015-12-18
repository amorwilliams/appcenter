#!/bin/bash

ps -efa | grep "127.0.0.1:8005" | awk '$3==1 {print "kill -9 " $2}' | sh
ps -efa | grep "127.0.0.1:8005" 
