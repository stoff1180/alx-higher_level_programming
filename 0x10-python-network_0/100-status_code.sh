#!/bin/bash
# Script that sends a request to a URL passed as an argument
# Displays only the status code of the response
curl -so /dev/null -w "%{http_code}" "$1"
