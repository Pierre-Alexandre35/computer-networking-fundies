# Computer Networking Fundamentals 

Slides and practice labs for a networking tutorial I made with Handrien Daures in March 2021. 


## Purpose 
The purpose of this short tutorial is to provide an overview of computer networks to people with no or little knowledge on networking. There is currently two practice labs:
- HTTP / HTTPs: executing a Man-in-the-Middle attack (capture plaintext passwords from a HTTP login request)
- socket programming: talk to your friend using socket to learn more about TCP socket 


## Installation  
```
virtualenv env
source env bin activate
pip install -r requirements.txt
```

### HTTP / HTTPs lab 
```
sudo tcpdump -i any port 8000 -A | grep --line-buffered password
uvicorn main:app --reload # unsecured login 
sudo caddy reverse-proxy --from localhost --to localhost:8000 # secured login 
```

### Socket programming lab 
```
python3 server.py # shell 1
python3 client.py # shell 1
```
