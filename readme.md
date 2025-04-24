create env

```bash
conda create -p venv python==3.11.0 -y
```

activate env

```bash
conda activate venv/.
```

created a req file


install the requirements

```bash
pip install -r requirements.txt
```

```bash
git init
```

```bash
dvc init
```

```bash
dvc add data_given/email_phishing_data.csv
```

```bash
git add .
```

```bash
git commit -m "first commit"
```

```bash
git push -u origin main
```

oneliner updates for readme

```bash
git add . && git commit -m "update Readme.md"
```

dvc commands to run all the stages after updating dvc.yaml

```bash
dvc repro
```

to check all the metrcis

```bash
dvc metrics show
```

to check the metric scores with previous 

```bash
dvc metrics diff
```