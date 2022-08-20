#!/bin/bash

num=5
val=7

if [ ${num} -eq ${val} ]; then
  echo "${num} gather than ${val}"
else
  echo "${num} litter than ${val}"
fi

# same as next:
[ ${num} -eq ${val} ] && echo "${num} gather than ${val}" || echo "${num} litter than ${val}"
