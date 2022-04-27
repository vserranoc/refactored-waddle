#!/usr/bin/env bash

DIRECTORY=/home/airflow/

if [ ! -d $DIRECTORY ]
then
  apt-get -y update
  apt-get -y upgrade
  apt-get install -y \
      python3-pip \
      python3-venv

  # Create Airflow User
  echo "Creating Airflow User"
  adduser airflow --disabled-login --disabled-password --gecos "airflow system user"

  echo "Copying auth"
  mkdir -p /home/airflow/.auth
  export BUCKET_NAME={}
  sudo gsutil cp gs://bucket/.json /home/airflow/.auth

  echo "Exporting Environment variables"
  echo GOOGLE_APPLICATION_CREDENTIALS=/home/airflow/.auth/r.json >> /etc/profile
  echo BUCKET_NAME=vms-2022 >> /etc/profile
  export AIRFLOW_HOME=/home/airflow
  echo AIRFLOW_HOME=/home/airflow >> /etc/profile

  echo "Providing Airflow User Permissions"
  cd /home/airflow
  mkdir dags
  echo "Pulling Dag Files"
  gsutil -m cp -r gs://$BUCKET_NAME/dags /home/airflow
  chown airflow.airflow . -R
  chmod g+rwx . -R

  echo "Creating Virtual Env"
  python3 -m venv .
  source bin/activate
  python3 -m pip install --upgrade pip

  echo "Installing Airflow"
  AIRFLOW_VERSION=2.0.1
  PYTHON_VERSION=3.7
  CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
  python3 -m pip install "apache-airflow[gcp]==${AIRFLOW_VERSION}" --constraint "$CONSTRAINT_URL"
  python3 -m pip install tweepy

  echo "Initizialing Airflow DB"
  airflow db init
  airflow users create -r Admin -u user -p password -e email@gmail.com -f name -l lastname

  echo "Starting Airflow Scheduler & Webserver"
  nohup airflow scheduler >> scheduler.log &
  nohup airflow webserver -p 8080 >> webserver.log &

else
  echo "Setting Environment Variables"
  export AIRFLOW_HOME=/home/airflow
  echo AIRFLOW_HOME=/home/airflow >> /etc/profile
  
  echo "Pulling Dag Files"
  export BUCKET_NAME=vms-2022
  gsutil -m cp -r gs://$BUCKET_NAME/dags /home/airflow
  
  echo "Providing Airflow User Permissions"
  cd /home/airflow/
  chown airflow.airflow . -R
  chmod g+rwx . -R

  echo "Activating Virtual Environment"
  source bin/activate

  echo "Enabling Scheduler & Webserver"
  nohup airflow scheduler >> scheduler.log &
  nohup airflow webserver -p 8080 >> webserver.log &
fi