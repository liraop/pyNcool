#!/usr/bin/env bash

#####
#
# Script written to automatically adjust nvidia's GPU fan speed.
# Temperature is checked every $checkTime seconds.
#
# Script meant to start on user login
#
# Requirements:
# Nvidia GPU and 'coolbits 4' option enabled on xorg.conf
#
# Written by liraop - lirapdo@gmail.com
#
#####

## settings
set -o errexit
set -o pipefail
set -o nounset

## time to rerun temperature check
checkTime=10

while true; do
   ## get GPU core temperature
   gputemp=$(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits)
   ## enable fan control
   nsReturn=$(nvidia-settings -a [gpu:0]/GPUFanControlState=1)
   ## get current fan speed
   startSpeed=$(nvidia-smi --query-gpu=fan.speed --format=csv,noheader,nounits)

   printf %b "GPU Temperature: ${gputemp}c\n"

   ## check temperature, set target speed, set fan speed
   case $gputemp in
      [0-4][0-9])
      targetSpeed=40
      nsReturn=$(nvidia-settings -a [fan:0]/GPUTargetFanSpeed=${targetSpeed})
      ;;
      5[0-9])
      targetSpeed=50
      nsReturn=$(nvidia-settings -a [fan:0]/GPUTargetFanSpeed=${targetSpeed})
      ;;
      6[0-9])
      targetSpeed=60
      nsReturn=$(nvidia-settings -a [fan:0]/GPUTargetFanSpeed=${targetSpeed})
      ;;
      [7-9][0-9])
      targetSpeed=100
      nsReturn=$(nvidia-settings -a [fan:0]/GPUTargetFanSpeed=${targetSpeed})
      ;;
      *)
      msg="We can certainly say something is wrong"
      ;;
   esac

   ## where the magic happens to fix fan speed status
   nsReturn=$(nvidia-settings -a [gpu:0]/GPUFanControlState=1)
   ## gets fan final speed
   finalSpeed=$(nvidia-smi --query-gpu=fan.speed --format=csv,noheader,nounits)

   msg="Fan speed was ${startSpeed}%\nFan speed is ${finalSpeed}%\n"
   printf %b "${msg}"
   sleep ${checkTime}
done
