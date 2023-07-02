#!/bin/sh -e
case "$OSTYPE" in
  darwin*)  brew install allure;;
  linux*)   sudo apt-get install allure;;
  msys*)    scoop install allure ;;
  *)        echo "unknown: $OSTYPE" ;;
esac
pip install -r requirements.txt
pytest -p no:warnings --showlocals tests --alluredir=allurereports;
allure serve allurereports;
