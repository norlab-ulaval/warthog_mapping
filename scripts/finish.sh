# FINISH STUFF
experimentName=$1__$(date "+%Y-%m-%d_%H:%M:%S")

echo "Stopping all processes...'"
screen -X -S sensors_all stuff "^C"
screen -X -S sensors_all stuff "exit"
screen -X -S rosbag stuff "^C"
screen -X -S mapping stuff "^C"
screen -X -S wiln stuff "^C"
echo "All processes have been stopped"

echo "Moving log files and rosbag bags in separate folder"
sleep 5
mkdir /home/robot/.ros/$experimentName
mv /home/robot/.ros/sensors_all_screen.log /home/robot/.ros/$experimentName
mv /home/robot/.ros/rosbag_screen.log /home/robot/.ros/$experimentName
mv /home/robot/.ros/mapping_screen.log /home/robot/.ros/$experimentName
mv /home/robot/.ros/wiln_screen.log /home/robot/.ros/$experimentName
mv /home/robot/.ros/rosbag.bag /home/robot/.ros/$experimentName
echo "All log files and rosbag bags have been moved in separate folder called '$experimentName' located in .ros folder."

echo "Finished. Closing..."


# exit gracefully by returning a status
exit 0
