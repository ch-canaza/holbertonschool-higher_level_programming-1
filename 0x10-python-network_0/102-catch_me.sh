#!/bin/bash
# makes a request that causes serves to send "You got me!" as a response
curl -so /dev/null/ -w "You got me!"  0.0.0.0:5000/catch_me
