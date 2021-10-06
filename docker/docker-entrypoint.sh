#!/bin/sh

if [ ! -d "/tmp/check" ]; then
  mkdir /tmp/check

#  python3 manage.py migrate
#  echo `date` > /tmp/check/first_`date +%Y%m%d_%H%M%S`
else
#  echo `date` > /tmp/check/second_`date +%Y%m%d_%H%M%S`
fi

exec "$@"
