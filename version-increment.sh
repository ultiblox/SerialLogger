#!/bin/bash

echo "Incrementing version..."

# Function to parse and increment version
increment_version() {
    local version=$1
    local IFS='.'
    local -a parts=($version)

    # Always increment the patch number
    parts[2]=$((parts[2]+1))

    echo "${parts[0]}.${parts[1]}.${parts[2]}"
}

echo "Fetching all tags..."
# Fetch all tags
git fetch --tags

# Determine the base version
if [ -f "VERSION" ]; then
    base_version=$(cat VERSION)
    echo "Base version from VERSION file: $base_version"
elif [ -f "version.txt" ]; then
    base_version=$(cat version.txt)
    echo "Base version from version.txt file: $base_version"
else
    base_version="0.0.0"
    echo "Default base version: $base_version"
fi

sorted_tags=$(git tag --sort=-version:refname)
echo "Sorted tags: $sorted_tags"

# Get the latest tag sorted by version
latest_tag=$(git tag --sort=-version:refname | head -n 1)
echo "Latest tag found: $latest_tag"

# Check if the latest tag is just a pipeline ID (old format)
if [[ "$latest_tag" =~ ^v[0-9]+$ ]]; then
    echo "Latest tag is in old format (pipeline ID)."
    # Start new versioning from version.txt and pipeline ID
    new_version="${base_version%.*}.$CI_PIPELINE_ID"
    echo "Initial new version from base and pipeline ID: $new_version"
    new_version=$(increment_version $new_version)
    echo "Incremented new version: $new_version"
else
    echo "Latest tag is in new format."
    # Determine version bump type based on commit messages
    version_bump="patch" # default to patch
    echo "Analyzing commit messages for version bump..."
    for commit in $(git log $latest_tag..HEAD --pretty=format:%s);
    do
        if [[ $commit == *"BREAKING CHANGE"* ]]; then
            version_bump="major"
            echo "Found breaking change, setting version bump to major."
            break
        elif [[ $commit == *"feat"* ]]; then
            version_bump="minor"
            echo "Found feature, setting version bump to minor."
        fi
    done

    # Increment version based on the determined bump type
    new_version=$(increment_version $latest_tag $version_bump)
    echo "Incremented new version based on commit analysis: $new_version"
fi

echo "Writing new version to VERSION file..."
echo $new_version > VERSION
echo "New version: $new_version"
