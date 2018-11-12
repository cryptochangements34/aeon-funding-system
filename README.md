# Masari Funding System 

## Description

A forum style funding system for Masari currency

Written in Python using Flask originally by dsc (skftn) with contributions from camthegeek

## Features
- Simplistic user system
- Proposal system
- Accounting system
- Stats per proposal
-- Coins received
-- Coins paid out
-- Coins available
- Comment system per proposal
- More in development

## Installation (locally)

### Install dependancies

```sudo apt install python-virtualenv python3 redis-server postgresql-server-dev-* postgresql postgresql-client python-pip virtualenv git```

Run a masari node
`./masarid`

Create a view-only masari wallet for this project
`./masari-wallet-cli -- generate-from-view-key funding`
Standard address: `5me2m9HZgrr38Tn9JgSee84nuzf6sS2ms29yqWXLXDQQ4A1QYzZs1BjPhXi4X2HcCgLXQrc2sZuML6A4ihmWAvQ7BXCnaaQ`
View-key: `a7bcbaf962cda3dac09db13b1679107a29a45b5973d9dfcbed0eaa7bf3f91e0c`

If necessary, create a new postgres user for this project
Create a database for the funding system in postgres
`CREATE DATABASE funding;`

Run an RPC wallet using this view-only wallet
`./masari-wallet-rpc --rpc-bind-port 11182 --disable-rpc-login --wallet-file funding --password "your_wallet_password"`

```
git clone https://github.com/masari-project/masari-funding-system.git
cd masari-funding-system
virtualenv -p /usr/bin/python3 env
source env/bin/activate
pip install -r requirements.txt
cp settings.py_example settings.py
- change settings.py accordingly
python run_dev.py
```
