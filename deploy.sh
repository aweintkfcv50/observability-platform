#!/bin/bash
cd ~/observability-platform
git pull origin main
docker-compose down
docker-compose up -d --build

