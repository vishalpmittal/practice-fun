rm -rf ../06_json-server/public/*
gulp
cp ../06_json-server/db.json.bck ../06_json-server/db.json
cp -R dist/* ../06_json-server/public/.
