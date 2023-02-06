#!/bin/bash

# Define a function to display the remote connection information
display_info() {
  # Get the list of established connections
  connections=$(netstat -tpn | grep ESTABLISHED)
  
  # Display the header
  echo "##################################################################"
  echo "# Remote Connection Information:                                 #"
  echo "##################################################################"
  echo ""
  
  # Iterate through the list of connections and display the relevant information
  i=0
  while read -r line; do
    # Extract the protocol, local IP and port, and remote IP and port
    protocol=$(echo $line | awk '{print $1}')
    local_ip=$(echo $line | awk '{print $4}' | awk -F: '{print $1}')
    local_port=$(echo $line | awk '{print $4}' | awk -F: '{print $2}')
    remote_ip=$(echo $line | awk '{print $5}' | awk -F: '{print $1}')
    remote_port=$(echo $line | awk '{print $5}' | awk -F: '{print $2}')
    
    # Display the information
    echo "Connection $i:"
    echo "Protocol: $protocol"
    echo "Local IP: $local_ip"
    echo "Local Port: $local_port"
    echo "Remote IP: $remote_ip"
    echo "Remote Port: $remote_port"
    echo ""
    
    # Increment the connection counter
    ((i++))
  done <<< "$connections"
  
  # Prompt the user for action
  read -p "Enter the number of the connection to stop, or 'p' to ping a remote connection: " input
  
  # Check if the user wants to stop a connection
  if [[ $input =~ ^[0-9]+$ ]]; then
    # Get the PID of the process associated with the connection
    pid=$(lsof -n -i :$remote_port | awk '{print $2}' | tail -n +2)
    
    # Kill the process
    kill -9 $pid
    
    # Confirm that the process has been stopped
    echo "Process $pid has been stopped."
  elif [ "$input" == "p" ]; then
    # Prompt the user for the remote IP
    read -p "Enter the remote IP: " remote_ip
    
    # Ping the remote IP
    ping $remote_ip
  else
    # Invalid input
    echo "Invalid input."
  fi
}

# Call the display_info function
display_info
