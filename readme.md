# Docker Minecraft Server Manager (DMSM)

## Overview

DMSM is a docker-powered server management system that makes creating a new server very easy to do. This is based off of itzg's [minecraft-server](https://hub.docker.com/r/itzg/minecraft-server) docker image, but with a configuration tool and CLI based around it.

DMSM is for **Unix Systems Only**. I have compiled it for macOS (both ARM and x86) as well as for Linux (x86-64 only), as Windows users should be using Linux under WSL (with Docker) for the ideal Windows server setup.

## Installation

### Requirements

The only requirement for using this is Docker. The application is written in Python but compiled to an executible, so you don't even need Python. All you need is docker, which you can find how to set up [here](https://docs.docker.com/get-docker/).

### Install

After that, download the right executible for you in the [Releases Page](https://github.com/oitsjustjose/DMSM/releases), move it to wherever you keep things (like `/usr/local/bin` for unix-based systems)

## Building

Building this tool is straight forward. What you'll need:

- Python 3.6 -- **this version is specific**
- Pip for Python 3.6
- Pip Packages described in `requirements.txt` (you can install them via `pip install -r requirements.txt`)

All you have to do once you have the dependencies handled is to run `python3 -m nuitka --standalone --onefile dmsm.py` from within the `src` folder.

## Running

The CLI will help you do this -- give me a bit and I'll write up more docs on this!
