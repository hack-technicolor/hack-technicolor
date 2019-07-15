# How to host this Documentation Locally

If you ever need to edit or use this documentation without internet, it can be a hard task.

## Windows

### Install Python

To start off you must install a Python environment. Move on to *Instal MKDocs* if you already have a Python environment installed.

If you will be using Python a lot, install Anaconda, otherwise just install standard Python.

#### Installing Anaconda

1. Go to the [Anaconda Distribution](https://www.anaconda.com/distribution/#windows) download page.
2. Under `Python 3.7 version`, hit the download button.
3. Follow the prompts during the install process.

#### Installing Standard Python

1. Go to the [Official Python Download](https://www.python.org/downloads/) site.
2. Under `Download the latest version for Windows`, click on `Download Python x.xx`.
3. Follow the installation prompts.

### Install MKDocs

1. Open a CMD Window. `Win + R` then type `cmd` + Enter.

2. If you have installed Anaconda, run `activate base` to activate the python environment.

3. Run:

```bash
pip install mkdocs mkdocs-material
```

### Download the Repository

1. Click [here](https://github.com/kevdagoat/hack-technicolor/archive/master.zip) to download a zip version of the documentation.

2. Extract the zip to the directory you want.

### Serve the Docs!

Click on `serve.bat` and it should tell you that it is serving the docs on `http://localhost:8000`

In my case:
```bash
INFO    -  Building documentation...
INFO    -  Cleaning site directory
[I 000000 17:35:02 server:296] Serving on http://127.0.0.1:8000
[I 000000 17:35:00 handlers:62] Start watching changes
[I 000000 17:35:00 handlers:64] Start detecting changes
```

Now head to http://localhost:8000 in your browser of choice.

!!! hint "What about when I unplug my Internet?"
    Don't worry as the MKDocs development server only uses the internal *network* in your PC, thats why you head to http://localhost:8000, as it is heading to your local PC.

## Linux Users

### Install Python and Git

Usually your distro has its own inbuilt package manager. In this case, we will be referring to `apt`, which is one of the more common ones out there.

1. Open up a bash shell window, if you do not know, search it up!
2. Run
```
sudo apt install -y python3 python3-pip git
```

### Install MKDocs

1. In your bash shell window, run:

```bash
pip3 install mkdocs mkdocs-material
```

### Download the Repository

1. Click [here](https://github.com/kevdagoat/hack-technicolor/archive/master.zip) to download a zip version of the documentation.

2. Extract the zip to the directory you want. This can be achieved by using the `Archive Manager` tool implemented in most Ubuntu-based distro's.

### Serve the Docs!

Click on `serve.sh` and it should tell you that it is serving the docs on `http://localhost:8000`

In my case:

```bash
INFO    -  Building documentation...
INFO    -  Cleaning site directory
[I 000000 17:35:02 server:296] Serving on http://127.0.0.1:8000
[I 000000 17:35:00 handlers:62] Start watching changes
[I 000000 17:35:00 handlers:64] Start detecting changes
```

Now head to http://localhost:8000 in your browser of choice.

!!! hint "What about when I unplug my Internet?"
    Don't worry as the MKDocs development server only uses the internal *network* in your PC, thats why you head to http://localhost:8000, as it is heading to your local PC.


