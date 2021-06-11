#!/bin/sh

if [ ! $(whoami) = "root" ]
then
    echo "Please run this script as root";
    exit 1;
fi

export url="https://github.com/oitsjustjose/DMSM/releases/download/1.1.0/dmsm_x86-64"

if [ ! $(command -v docker) ]
then
    echo "docker is not installed. Please install it via https://docs.docker.com/get-docker/"
    exit 1
fi

echo "Downloading DMSM.."

if [ $(command -v curl) ]
then
    curl -L $url > dmsm;
else
    if [ $(command -v wget) ]
    then
        wget $url dmsm;
    else
        echo "You don't seem to have curl or wget. Please install one of your choice!"
        exit 1
    fi
fi

echo "Installing DMSM..";

chmod +x dmsm;

if [ -d "/usr/local/bin" ]
then
    mv ./dmsm /usr/local/bin/dmsm
else
    if [ -d "/usr/bin" ]
    then
        mv ./dmsm /usr/bin/dmsm
    else
        echo "/usr/local/bin nor /usr/bin could not be found. Are you on a Unix Device??"
    fi
fi

echo "Installed! Use via dmsm (create|start|stop|restart|delete) SERVERNAME"