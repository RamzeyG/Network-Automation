#           Makefile - Python
#
# This makefile is designed for a python program.
# Simply change the SRC variable to change the program name

COMMIT := $(shell git rev-parse HEAD)

SRC = src/ssh_automate.py


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

pan sf: ${SRC}
	python ${SRC} -sf $(sf) -b pan

# Ubuntu
ubuntu: ${SRC}
	python ${SRC} -b ubuntu


# Ubuntu
ubuntu sf: ${SRC}
	python ${SRC} -b ubuntu -sf $(sf)




# Cisco sf
cisco sf: ${SRC}
	python ${SRC} -b cisco -sf $(sf)



clean:
	rm nothing.txt

