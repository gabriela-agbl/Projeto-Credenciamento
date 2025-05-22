import logging
import os

root_path = os.path.dirname(__file__)
log_path = os.path.join(root_path, 'Log')

os.makedirs(log_path, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_path, 'app.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S',
    encoding = 'utf-8'
)

def log_acesso(usuario, acao, status):
    logging.info(f'Usuário: {usuario} | Ação: {acao} | Status: {status}')