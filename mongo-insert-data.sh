#!/bin/bash

mongoimport --db='clients' --collection='clients' --file='./clients.json' --jsonArray