#!/bin/sh -e
echo 'Hello World'
allureversion=`allure --version`
regexp="^(([1-9]|([0-4]|1\d|[1-9]|)\d)\.?\b){3}$"
[["$allureversion" =~ $regexp ]] && need_install="NO" || need_install="YES"
echo $allureversion
echo $need_install
if [[ $need_install=='YES' ]]
  case "$OSTYPE" in
    darwin*)  echo "OSX"; ;;
    linux*)   echo "LINUX"; sudo apt-get install allure;;
    msys*)    echo "WINDOWS"; scoop install allure ;;
    *)        echo "unknown: $OSTYPE" ;;
  esac
fi
pip install -r requirements.txt
pytest -p no:warnings --showlocals tests --alluredir=allurereports;
allure serve allurereports;

#  brew install allure