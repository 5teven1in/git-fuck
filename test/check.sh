#!/bin/bash

output=$(node ./add.js 1 2 3)

[[ $output == "6" ]]
