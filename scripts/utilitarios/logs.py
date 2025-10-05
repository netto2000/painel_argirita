"""
logs.py
Funções genéricas e padronizadas de logging para todo o projeto.
"""

import logging
import os
from datetime import datetime

LOG_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'logs')
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, 'fiscalizacao.log')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

def log_info(msg):
    logging.info(msg)

def log_ok(msg):
    logging.info("✅ " + msg)

def log_warn(msg):
    logging.warning("⚠️ " + msg)

def log_error(msg):
    logging.error("❌ " + msg)
