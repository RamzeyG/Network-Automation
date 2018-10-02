#           Makefile - Python
#
# This makefile is designed for a python program.
# Simply change the SRC variable to change the program name

COMMIT := $(shell git rev-parse HEAD)

SRC = src/ssh_automate.py


all: ${SRC}

ifndef
run: ${SRC}
	python ${SRC}
endif

# Juniper program
ifndef SF
juniper: ${SRC}
	python ${SRC} -b juniper
endif

junipersf: ${SRC}
	python ${SRC} -sf ${SF} -b juniper

# PAN
ifndef SF
pan: ${SRC}
	python ${SRC} -b pan
endif

# PAN Single file

pansf: ${SRC}
	python ${SRC} -sf $(sf) -b pan

# Ubuntu
ifndef SF
ubuntu: ${SRC}
	python ${SRC} -b ubuntu
endif

# Ubuntu
ubuntusf: ${SRC}
	python ${SRC} -b ubuntu -sf $(sf)




# Cisco sf
ciscosf: ${SRC}
	python ${SRC} -b cisco -sf $(sf)



clean:
	rm nothing.txt

