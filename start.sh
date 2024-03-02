#!/bin/bash


/home/ibaibur/.local/bin/gunicorn --config /home/ibaibur/libot-lb/gunicorn_config.py app:app
