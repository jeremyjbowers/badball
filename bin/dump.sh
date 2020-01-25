#!/bin/bash
cd /home/ubuntu/apps/badball; sudo su -c "source ~/.bashrc && workon badball && django-admin dumpdata badball > /tmp/badball.json" ubuntu