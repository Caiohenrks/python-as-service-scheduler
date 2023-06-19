# Python Scheduler Service

Este script implementa um serviço do Windows chamado "Python Scheduler Service". Ele permite a execução periódica de um arquivo `arquivo.bat` em intervalos de tempo definidos usando a biblioteca `schedule`.

## Funcionalidades

- Execução periódica de um arquivo `arquivo.bat` a cada 1 minuto.
- Registro de execuções bem-sucedidas e falhas em um arquivo de log chamado `execution.log`.
- Salvar a saída do arquivo `arquivo.bat` em arquivos de log separados no diretório `logs` com o formato `timestamp.log`, onde `timestamp` é a data e hora da execução.

## Requisitos

- Python 3.x
- Bibliotecas Python: `win32serviceutil`, `win32service`, `win32event`, `servicemanager`, `socket`, `subprocess`, `datetime`, `schedule`, `time`, `traceback`

## Configuração

1. Atualize o caminho para o arquivo `arquivo.bat` no método `main()` do script.
2. Atualize o caminho completo para o arquivo de log `execution.log` no método `log_execution()`.

## Instalação e Gerenciamento como Serviço do Windows

Siga as etapas abaixo para instalar, iniciar e parar o serviço "Python Scheduler Service".

### Instalação

1. Abra o Prompt de Comando como administrador.
2. Navegue até o diretório onde o script `service.py` está localizado.
3. Execute o seguinte comando: `python service.py install`
4. O serviço "Python Scheduler Service" será instalado e pode ser gerenciado usando o utilitário `services.msc` do Windows.

### Iniciar o Serviço

1. Abra o Prompt de Comando como administrador.
2. Execute o seguinte comando: `net start PythonSchedulerService`

### Parar o Serviço

1. Abra o Prompt de Comando como administrador.
2. Execute o seguinte comando: `net stop PythonSchedulerService`

## Logs

- As execuções bem-sucedidas e falhas são registradas no arquivo `execution.log`.
- A saída do arquivo `arquivo.bat` é salva em arquivos de log separados no diretório `logs` com o formato `timestamp.log`.

Certifique-se de ajustar as informações de caminho e outras configurações de acordo com seu ambiente antes de usar o script.

**Nota**: Lembre-se de criar a pasta "logs" no mesmo diretório onde o arquivo `service.py` está localizado para que os arquivos de log sejam salvos corretamente.
