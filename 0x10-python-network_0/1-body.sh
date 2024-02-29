#!/bin/bash
# A script that takes in a URL, sends a GETrequest and displays the  body of a 200 status code response
curl -Ls "$1"
