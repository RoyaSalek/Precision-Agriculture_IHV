# YOLO Setup Guide

## Create Virtual Environment

```bash
python3 -m venv venv
```

## Activate Virtual Environment

### macOS/Linux

```bash
source venv/bin/activate
```

### Windows (PowerShell)

```powershell
venv\Scripts\Activate.ps1
```

### Windows (Command Prompt)

```cmd
venv\Scripts\activate.bat
```

Verify:

```bash
which python
python --version
```

Windows:

```powershell
where python
python --version
```

---

## Upgrade pip

```bash
pip install -U pip
```

---

## Install Ultralytics

```bash
pip install -U ultralytics
```

Verify installation:

```bash
yolo version
pip show ultralytics
```

---

## Test YOLO Inference

```bash
yolo predict model=yolo11n.pt source='https://ultralytics.com/images/bus.jpg'
```

Expected result:

```text
4 persons, 1 bus
```

Output location:

```text
runs/detect/predict
```

---

## Status

- [x] Virtual environment created
- [x] Ultralytics installed
- [x] YOLO CLI verified
- [x] Pretrained model downloaded
- [x] Successful inference completed
