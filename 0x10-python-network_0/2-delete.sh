#!/bin/bash
# Sends a DELETE request to the URL passed as first argument and display the body of the response
curl -s -X DELETE "${1}"


