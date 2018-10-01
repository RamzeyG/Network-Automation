#           Makefile - Python
#
# This makefile is designed for a python program.
# Simply change the SRC variable to change the program name

COMMIT := $(shell git rev-parse HEAD)

SRC = src/ssh_automate.py

SF = src/$(sf)

all: ${SRC}

run: ${SRC}
	python ${SRC}

# Juniper program
juniper: ${SRC}
	python ${SRC} -b juniper

juniper sf: ${SRC}
	python ${SRC} -sf ${SF} -b juniper

# PAN
pan: ${SRC}
	python ${SRC} -b pan

# PAN Single file

pan sf: src/${SRC}
	python ${SRC} -sf ${SF} -b pan

# Ubuntu
ubuntu: ${SRC}
	python ${SRC} -b ubuntu


# Ubuntu
ubuntu sf: ${SRC}
	python ${SRC} -b ubuntu -sf ${SF}




# Cisco sf
cisco sf: ${SRC}
	python ${SRC} -b cisco -sf ${SF}



clean:
	rm nothing.txt

