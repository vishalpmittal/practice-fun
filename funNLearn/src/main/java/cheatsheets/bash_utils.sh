#!/bin/bash

export CMD_SEPARATOR="----------------------------------------------"
export OSM_REPO_DIR="/desk/git-vmware/osstpmgt"
export DEV_ENV_DIR="/desk/notes/BDMittals/notes_vm/0_vmware/dev_envs"

function print_separator(){
    echo $CMD_SEPARATOR
}

function print_task(){
    echo ""
    echo "--> $1"
}

function wait_for_user_apprvl(){
    read -p "$1" -n 1 -r
    return $REPLY
}

function timer_start(){
    SECONDS=0
}

function timer_stop(){
    duration=$SECONDS
    echo "-> $1 took: $(($duration / 60)) min. $(($duration % 60)) sec."
}

function file_is_present(){
    if [ -f "$1" ]; then
        return 1
    else
        return 0
    fi
}

function file_is_not_present(){
    if [ ! -f "$1" ]; then
        return 1
    else
        return 0
    fi
}