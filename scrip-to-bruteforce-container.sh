#!/bin/bash

# Define the number of executions
NUM_EXECUTIONS=50

# Function to execute the Docker command
execute_docker_command() {
    docker exec --user root mayhem /bin/bash
}

# Main loop to execute the Docker command multiple times
for ((i=1; i<=$NUM_EXECUTIONS; i++)); do
    echo "Execution $i: Running Docker command"
    execute_docker_command &
done

# Wait for all background processes to finish
wait

