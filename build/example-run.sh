#!/usr/bin/env bash

echo "#----------------------------------------------------------------------#"
echo ""
echo "Switching back to the default nginx configuration"
echo " *            File: index.nginx-debian.html"
echo " * Salt batch size: 1"
echo " * Salt batch wait: 10s"
echo ""
echo "#----------------------------------------------------------------------#"

docker exec saltstackdocker_master_1 bash -c "salt --batch=1 --batch-wait=10 \"*\" state.sls common.nginx pillar='{\"web_index\": \"index.nginx-debian.html\"}'"
