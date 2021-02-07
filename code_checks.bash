coverage run --branch --include=$PWD/*.py -m pytest; coverage html; coverage xml -o coverage/coverage.xml
tests="$(printf "%s," test*)"
bandit *.py -x ${tests::-1}
pylint -j 0 --ignore-patterns=test* --disable=W0312,C0114,C0303 *.py
