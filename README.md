# Demo - Video Transcript using Python

## Dependencies:

```bash
pip install moviepy
pip install SpeechRecognition
```



## How to run:

> **Note:** The video file should be in the `data` folder.


### Development Environment:


#### Create a virtual environment:

```bash
python -m venv venv
```

#### Activate the virtual environment:

```bash
.\venv\Scripts\activate
```

#### Install the dependencies:

```bash
pip install -r requirements.txt
```

#### Run the script:

```bash
python .\src\main.py
```


### Docker:

#### Build the image:

```bash
docker build -t transcript-app .
```

#### Run the container:

```bash
docker run -v ./data/:/data/:rw transcript-app
```

#### Run docker-compose:

```bash
docker-compose up
```
