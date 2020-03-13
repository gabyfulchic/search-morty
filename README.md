# Search & Morty :p 
![python-version](https://img.shields.io/badge/python-v3.8-brightgreen)
![ramapi-version](https://img.shields.io/badge/ramapi-v0.1.0-orange)
![flask-web-framework](https://img.shields.io/badge/Flask-web--framework-lightgrey)  
  
*Made around the Test Driven Development course.*
  
![rick & morty background](assets/rick-pq.png)
  
  
## Rules
  
```ruby
- writing tests and verifying the output expected
- executing them without function to test and the code well fail (RED)
- writing fonction to be tested
- executing tests and make sure that it success (GREEN)
- then REFACTORING the code to make it cleaner and more efficient (BLUE)
```
  
## Development Objectives   
  
- [x] Play with [ramapi](https://github.com/curiousrohan/ramapi) **@everyone**
- [x] Play with [flask](https://github.com/pallets/flask) **@everyone** 
- [x] Display web interface returning characters' info (format: link) **@Alexandre-Abruzzese**
- [x] Do the same thing but include search bar and output json object **@Alexandre-Abruzzese**
- [ ] Format all json to make a good UI 
- [ ] Include auto completion for user research
- [ ] Add features to check episodes & all character's locations into
- [ ] Search some "plus value" for our project than reach API with curl
  
## Infrastructure Objectives  
  
- [x] Automate app deployment with Ansible (Check [git submodules](https://github.com/gabyfulchic/ansible-flask)) **@gabyfulchic**
- [x] Deploy app using HTTPS and let's encrypt SSL certbot **@gabyfulchic**
- [x] Deploy app accessible everywhere and avoid installation of projet (OVH Cloud) **@gabyfulchic**
  
## Project
  
[https://weeking.tk](https://weeking.tk)
  
  
### Launch Projet in local to DEV (127.0.0.1)
  
```python
git clone https://github.com/gabyfulchic/search-morty.git && cd search-morty/
pip install -r requirements.txt
env FLASK_APP="/path/to/main.py" flask run
```

### Enable project to be worldwide (HTTP & HTTPS)
  
> HTTP  
```python
ssh your_user@your_server
cd /usr/share && git clone https://github.com/gabyfulchic/search-morty.git && cd search-morty
pip install -r requiremnts.txt
env FLASK_APP='/usr/share/search-morty/app/routes.py' flask run --host=0.0.0.0 -p 80
```
(Don't forget to open port 80)  
> HTTPS  
```python
ssh your_user@your_server
cd /usr/share && git clone https://github.com/gabyfulchic/search-morty.git && cd search-morty
pip install -r requiremnts.txt
certbot certonly --standalone
env FLASK_APP='/usr/share/search-morty/app/routes.py' flask run --host=0.0.0.0 -p 443 --cert=/path --key=/path
```
(Don't forget to open port 443)
