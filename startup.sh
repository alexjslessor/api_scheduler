#!/bin/bash

run_tests() {
    py.test -s tests/test_one.py
    # py.test -s tests/test_two.py
}
# run_tests
run_docker_local_test() {
    docker build -t fastapi_app:latest .
    docker run --name test-container -p 5000:5000 fastapi_app:latest
}
connect_to_dgo_droplet() {
    # 167.99.191.17
    # ssh -i /path/to/private/key username@203.0.113.0.
    ssh -i $HOME/.ssh/dgo_sept3 root@167.99.191.17
}
scp_dgo_droplet() {
    cd ..
    scp -i $HOME/.ssh/dgo_sept3 -r ./api-scheduler root@167.99.191.17:~/.
    # scp -i $HOME/.ssh/dgo_sept3 -r ./backend root@167.99.191.17:~/.
    # scp -i ./MyKeyPair.pem setup.sh ubuntu@167.99.191.17:~/.
}
# scp_dgo_droplet



