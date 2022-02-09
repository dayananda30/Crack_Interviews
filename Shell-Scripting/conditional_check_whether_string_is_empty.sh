#!/bin/bash

if [[ $input_var ]]
then
  echo "input_var is not empty!!!"
else
  echo "input_var is empty"
  exit 1
fi