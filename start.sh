#!/bin/bash

/usr/bin/nohup gunicorn --config /home/ibaibur/libot-lb/gunicorn_config.py app:app >> /home/ibaibur/libot-lb/app.log &
