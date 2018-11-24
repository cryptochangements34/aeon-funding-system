import logging
import socket
import collections
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET = os.environ.get('SECRET', '')
DEBUG = os.environ.get('DEBUG', None) is not None

COINCODE = os.environ.get('COINCODE', 'MSR')
PSQL_USER = os.environ.get('PSQL_USER', 'postgres')
PSQL_PASS = os.environ.get('PSQL_PASS', '')
PSQL_HOST = os.environ.get('PSQL_HOST', '127.0.0.1')
PSQL_DB = os.environ.get('PSQL_DB', 'funding')

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'postgresql://{user}:{pw}@{host}/{db}').format(user=PSQL_USER, pw=PSQL_PASS, host=PSQL_HOST, db=PSQL_DB)

SESSION_COOKIE_NAME = os.environ.get('{coincode}_SESSION_COOKIE_NAME', '{coincode}_id').format(coincode=COINCODE)
SESSION_PREFIX = os.environ.get('{coincode}_SESSION_PREFIX', 'session:').format(coincode=COINCODE)

REDIS_HOST = os.environ.get('REDIS_HOST', '127.0.0.1')
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))
REDIS_PASSWD = os.environ.get('REDIS_PASSWD', None)

BIND_HOST = os.environ.get("BIND_HOST", "0.0.0.0")
if not BIND_HOST:
    raise Exception("BIND_HOST missing")
BIND_PORT = os.environ.get("BIND_PORT", 5004)
if not BIND_PORT:
    raise Exception("BIND_PORT missing")

HOSTNAME = os.environ.get("{coincode}_HOSTNAME", socket.gethostname()).format(coincode=COINCODE)

# If using a local RPC, no need for --rpc-login credentials unless you're binding wallet-rpc to 0.0.0.0. If you are, you're bad.
# elif, remote wallet-rpc, enable --rpc-login and enter credentials below.
RPC_HOST = os.environ.get('RPC_HOST', '127.0.0.1')
RPC_PORT = os.environ.get('RPC_PORT', '11182')
RPC_LOCATION = "http://{host}:{rpc_port}/json_rpc".format(host=RPC_HOST, rpc_port=RPC_PORT)
RPC_USERNAME = os.environ.get('RPC_USERNAME', '')
RPC_PASSWORD = os.environ.get('RPC_PASSWORD', '')

FUNDING_CATEGORIES = os.environ.get('FUNDING_CATEGORIES', 'wallets|marketing|core|misc|design').split('|')

FUNDING_STATUSES = collections.OrderedDict()
FUNDING_STATUSES[0] = 'disabled'
FUNDING_STATUSES[1] = 'proposal'
FUNDING_STATUSES[2] = 'funding'
FUNDING_STATUSES[3] = 'wip'
FUNDING_STATUSES[4] = 'completed'

USER_REG_DISABLED = os.environ.get('USER_REG_DISABLED', None) is not None

PROPOSAL_CONTENT_DEFAULT = """
#### Why?

What problem(s) are you trying to solve?

#### How much?

What is the total cost in {coincode}? List expenses per item. Total hours of work and per hour rate. What exchange rates are you using?

#### What?

Describe your idea in detail.

#### Milestones?

Break down tasks into different stages. Each stage should have the estimated number of days/weeks needed and cost per stage.

#### Outcomes?

What will be delivered? What goals will be reached?

#### Why you?

What skills and experience do you have?
""".strip().format(coincode=COINCODE)
