#!/bin/bash

# Check if version argument is passed
if [ -z "$1" ]; then
    echo "Error: No version provided. Pass the version as an argument."
    exit 1
fi

new_version=$1

# Inject the new version into library.properties
sed -i "s/^version=.*/version=$new_version/" library.properties

echo "Updated library.properties with version $new_version"
