#!/bin/bash

LOGFILE="/var/log/timeclock.log"

# Wake up console
echo -ne "\033[9;0]" >/dev/tty1

if [ "${0//\/}" != "$0" ]; then
	CWD="${0%'/'*}"
else
	CWD="."
fi

if [ -n "$LOGFILE" ]; then
	if ! [ -d "${LOGFILE%'/'*}" ]; then
		echo "Warning: couldn't find log file directory, skipping logging..." >&2
		unset LOGFILE
	else
		echo "Starting timeclock" >>$LOGFILE
		if [ -n "$(which date)" ]; then
			date >>$LOGFILE
		fi
	fi
fi

if [ "$(id -u)" == "0" ]; then 
	if [ -n "$(which ntpdate)" ]; then
		if [ -n "$LOGFILE" ]; then
			ntpdate pool.ntpdate.org &>>$LOGFILE
		else
			ntpdate pool.ntpdate.org &>>/dev/null
		fi
	fi
fi


if [ -n "$LOGFILE" ]; then
	cd "$CWD"
	"$CWD/timeclock.py" &>>$LOGFILE &
else
	cd "$CWD"
	"$CWD/timeclock.py" &>>/dev/null &
fi
