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

git init

dvc init

dvc add data_given/email_phishing_data.csv

git add .

git commit -m "first commit"

git remote add origin https://github.com/sumit-1492/vsi_cicd.git

git branch -M main

git push -u origin main