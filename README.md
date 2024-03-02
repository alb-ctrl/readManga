## How to run 
sudo flask run --host=0.0.0.0 --port=7001

nohup flask run --reload --host=0.0.0.0 --port=7001 &


## structure 
project/
├── app.py
├── templates/
│ ├── index.html
│ ├── chapters.html
│ └── read.html
└── static/
├── css/
│ ├── style.css
│ └── reset.css
└── manga/
├── manga1/
│ ├── chapter1/
│ │ ├── page1.jpg
│ │ ├── page2.jpg
│ │ └── ...
│ ├── chapter2/
│ │ ├── page1.jpg
│ │ ├── page2.jpg
│ │ └── ...
│ └── ...
├── manga2/
│ ├── chapter1/
│ │ ├── page1.jpg
│ │ ├── page2.jpg
│ │ └── ...
│ ├── chapter2/
│ │ ├── page1.jpg
│ │ ├── page2.jpg
│ │ └── ...
│ └── ...
└── ...