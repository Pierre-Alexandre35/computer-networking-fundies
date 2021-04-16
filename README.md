# Computer Networking Fundamentals 

Solutions for Computer Networking Fundamentals labs. 

## Socket Programming 

Form a group of two and build a real-time chat application using Socket TCP. 

```
virtualenv env
source env bin activate
pip install -r requirements.txt
cd socket_programming
python3 server.py # shell 1
python3 client.py # shell 1
```

## Usage

Try to capture plaintext passwords from a HTTP login request and another login request but using HTTPS

```
virtualenv env
source env bin activate
pip install -r requirements.txt
cd unsecured login
sudo vim /etc/hosts
sudo tcpdump -i any port 8000 -A | grep --line-buffered password
uvicorn main:app --reload # unsecured login 
sudo caddy reverse-proxy --from localhost --to localhost:8000 # secured login 
```
