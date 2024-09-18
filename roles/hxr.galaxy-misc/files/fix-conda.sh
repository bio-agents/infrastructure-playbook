#!/bin/bash
. /opt/galaxy/.bashrc
for i in `find /usr/local/agents/_conda/envs/ -mindepth 1 -maxdepth 1 -type d`;
do
    if [ ! -f $i/bin/conda ]; then
        /usr/local/agents/_conda/bin/conda ..checkenv bash $i
    fi
done
