#!/usr/bin/env bash
my_logfile=$1
my_csvfile=$2
echo "timestamp,level,content,eventid,template" > "$my_csvfile"
lineid=0
while read -r line; do
    if [[ -z "$line" ]]; then
        continue
    fi
    ((lineid++))
    timestamp=$(echo "$line" | sed -E 's/^\[(.)\]\s\[./\1/')
    level=$(echo "$line" | sed -E 's/^\[.\]\s\[(.)\].*/\1/')
    content=$(echo "$line" | sed -E 's/^\[.\]\s\[.\]\s(.*)/\1/')
    if [[ -z "$content" ]]; then
        continue
    fi
    eventid=""
    template=""
    if [[ $content =~ jk2_init\(\)\ Found\ (.)\ in\ scoreboard\ slot\ (.) ]]; then 
        eventid="E1"
        template="jk2_init() Found child <> in scoreboard slot <>"
    elif [[ $content =~ workerENV.init\(\)\ ok\ (.*) ]]; then
        eventid="E2"
        template="workerEnv.init() ok <*>" 
    elif [[ $content =~ mod_jk\ child\ workerEnv\ in\ error\ state\ (.*) ]]; then
        eventid="E3"
        template="mod_jk child workerEnv in error state <*>"
    elif [[ $content =~ \[client\ (.)\]\ Directory\ index\ forbidden\ by\ rules:\ (.) ]]; then
        eventid="E4"
        template="[client <>] Directory index forbidden by rule: <>"
    elif [[ $content =~ jk2_init\(\)\ Can\'t\ find\ child\ (.*)\ in\ scoreboard ]]; then
    eventid="E5"
    template="jk2_init() Can't find child <*> in scoreboard"
    else 
        eventid="E6"
        template="mod_jk child init <> <>"
    fi
    if [[ -z $eventid ]];then
    eventid="0"
    fi
    echo "$timestamp,$level,$content,$eventid,$template" >> "$my_csvfile"

done < "$my_logfile"
