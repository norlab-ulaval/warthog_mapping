#!/bin/bash

experimentName=$1__$(date "+%Y-%m-%d_%H:%M:%S")

echo "Starting the automatic experiment script named '$experimentName'"
echo "Killing all screens.."
killall screen
echo "All screens have been killed."




# SCREENS CREATION
echo "Creating screens..."


screen -dmS sensors_all -L -Logfile sensors_all_screen.log
echo "'sensors_all' screen created."

screen -dmS rosbag -L -Logfile rosbag_screen.log
echo "'rosbag' screen created."

screen -dmS mapping -L -Logfile mapping_screen.log
echo "'mapping' screen created."

screen -dmS wiln -L -Logfile wiln_screen.log
echo "'wiln' screen created."


echo "All new screens have been created"




# LAUNCHING STUFF
echo "Launching 'sensors_all.launch'"
screen -S sensors_all -X stuff 'roslaunch warthog_mapping sensors_all.launch'`echo -ne '\015'`
echo "'roslaunch warthog_mapping sensors_all.launch' command executed in 'sensors_all' screen"

echo "Starting a rosbag for all data"
screen -S rosbag -X stuff 'rosbag record -a -O rosbag.bag'`echo -ne '\015'`
echo "'rosbag record -a' command executed in 'rosbag' screen"

echo "Starting the mapping"
screen -S mapping -X stuff 'roslaunch warthog_mapping realtime_mapping.launch'`echo -ne '\015'`
echo "'roslaunch warthog_mapping realtime_mapping.launch' command executed in 'mapping' screen"

echo "Starting WILN"
screen -S wiln -X stuff 'roslaunch wiln warthog.launch'`echo -ne '\015'`
echo "'roslaunch wiln warthog.launch' command executed in 'wiln' screen"

echo "Everything is started. Please verify each screen to confirm proper behaviour. There is the list: "
screen -list

sleep 5


# FINISH STUFF
echo "Stopping all processes...'"
screen -X -S sensors_all stuff "^C"
screen -X -S rosbag stuff "^C"
screen -X -S mapping stuff "^C"
screen -X -S wiln stuff "^C"
echo "All processes have been stopped"

echo "Moving log files and rosbag bags in separate folder"
sleep 5
mkdir $experimentName
mv sensors_all_screen.log $experimentName
mv rosbag_screen.log $experimentName
mv mapping_screen.log $experimentName
mv wiln_screen.log $experimentName
mv rosbag.bag $experimentName
echo "All log files and rosbag bags have been moved in separate folder called '$experimentName' located in .ros folder."

echo "Finished. Closing..."


# exit gracefully by returning a status
exit 0
