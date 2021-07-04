#!/bin/bash
sleep 10m
cd  ~/Github/vektorious.github.io/
echo "Checking Github repo"
git pull

date_time_exec=$(date '+%Y-%m-%d_%H%M%S')
log="$date_time_exec.txt"

cd  ~/Github/vektorious.github.io/rpi-script/

# create log file or overrite if already present
printf "Log File - " > $log
# append date to log file
date >> $log

echo "Taking a picture..."
echo "Taking picture $date_time_exec.jpg" >> $log
raspistill -o "$date_time_exec.jpg" >> $log  #take pic

echo "Reading temperature..."
sleep 15s
temp=$(cat /sys/bus/w1/devices/28-01145316e8aa/w1_slave | sed -n 's/^.*\(t=[^ ]*\).*/\1/p' | sed 's/t=//' | awk '{x=$1}END{print(x/1000)}')
sleep 15s

echo "The temperature is $temp"

if [ $temp == "85" ]
then
  echo "Had to remeasure the temperature" >> $log
  sleep 1s
  temp=$(cat /sys/bus/w1/devices/28-01145316e8aa/w1_slave | sed -n 's/^.*\(t=[^ ]*\).*/\1/p' | sed 's/t=//' | awk '{x=$1}END{print(x/1000)}')
  if [ $temp == "85" ]
  then
    echo "Had to remeasure the temperature again" >> $log
    sleep 1s
    temp=$(cat /sys/bus/w1/devices/28-01145316e8aa/w1_slave | sed -n 's/^.*\(t=[^ ]*\).*/\1/p' | sed 's/t=//' | awk '{x=$1}END{print(x/1000)}')
  fi
fi

echo "writing log file"
echo "$(date '+%Y-%m-%d_%T'), $temp" >> temp.log

echo "creating temperature plot"
sudo python3 temp.py >> $log

bash upload.sh $temp "$date_time_exec.jpg" >> $log # start uploading mechanism

if [ $? == 0 ]
then
  echo "upload script finished successfully" >> $log
else
  echo "something went wrong with the upload script" >> $log
fi

echo "Uploading log to zennercloud"
curl -u rpi-huette:ueberdenwolken -T $log "https://cloud.alexanderkutschera.com/remote.php/dav/files/rpi-huette/RPi_Fotos/log/$log"
# shutdown after 10 Minutes
rm $log
sleep 5m
sudo shutdown
