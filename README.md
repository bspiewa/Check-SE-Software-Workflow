# Check SE Software Workflow

Extreme Networks XIQ-SE Workflow to check Switch Engine new software releases.
>:warning: Every change you do with your system is at your own risk

## Runtime preparation

- Install pip for Python 3.x in the XIQ Server

```bash
apt update
apt install python3-pip
```

>:bulb: If you find some errors with following apt install command about broken dependencies then just run `apt --fix-broken install`

- Copy `check_updates.py` and `requirements.txt` files to `/root/scripts` directory
- Install python libraries from `requirements.txt`

```bash
pip install -r requirements.txt
```

- Add executable permissions to script file

```bash
chmod +x check_updates.py
```

## Configuration

- Load Workflow file to your system, set e-mail recipients in __"Send new SE Update Notification"__ block
- Create recurring task to run this workflow
