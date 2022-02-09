#!/bin/bash

# shellcheck disable=SC1046
# shellcheck disable=SC1073
if touch "/home/$USER/test.txt"; then
  echo "test.txt file got created successfully"
fi