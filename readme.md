Hi 👋, I'm Samuel Arenas 

Backend python and Android app developer 

# Stori challenge

Read a csv file to generate a summary and send it by mail

## Installation local
## Requirements
* `python 3.8`
* `pip`
* [`virtualenv`](https://virtualenv.pypa.io/en/latest/)
## Create new virtual environment
The following command creates a new virtual environment named `venv` in the current directory, usually this will be your project's directory.
```sh
$ virtualenv venv
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.
```bash
$ pip install -r requirement.txt
```
if you want to use owner database set the enviroment vars

```bash
db_username=
db_password=
db_name=
host_db=
```

Install aws tools and set credentials

```
Set-AWSCredential `
                 -AccessKey AKIA0123456787EXAMPLE `
                 -SecretKey wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY `
                 -StoreAs MyNewProfile
``` 
## Usage

```bash
python app.py
```

## Installation lambda AWS

Create a new lambda function

Create a new S3 bucket function

Validate 2 emails to send and recipe the summary using aws SES

Create a new pipeline with a fork of this repository, I suggest use a main branch to deploy.

The code will install the dependencies and the code build is going to zip the project and deploy it on the lambda previously created 

After code is deployed create the trigger to start the function when a new csv file is upload  

## before testing 

check the lambda role has the permission full access to S3 and SES

## Usage

upload a csv file like the next to S3 bucket and wait for a email with summary transaccions

```
Id,Date,Transaction
0,7/16,+68.8
1,7/16,+48.8
2,7/16,-8.8
3,7/16,-68.8
4,7/17,+6.8
5,7/17,+54
6,8/1,-8.8
7,8/2,-68.8
8,8/3,+6.8
9,8/4,+78
```