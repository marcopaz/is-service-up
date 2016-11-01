#!/bin/bash
cd ./frontend
npm run build
rm -rf ../isserviceup/static
cp -R dist/ ../isserviceup/static/
cd -
