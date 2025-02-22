![Imagem Externa](https://galaxyteamtools.neocities.org/file-Y3ewSEFzLJux5pHuLRjwoG%20(1).webp)


# Documentação da Biblioteca PyDroidHelper

`PyDroidHelper` é uma biblioteca Python projetada para fornecer uma série de ferramentas úteis para automação e gestão de pacotes, controle do sistema, monitoramento de recursos, e execução de comandos em um dispositivo Android ou ambiente similar. Ela oferece funcionalidades como instalação de pacotes, verificação de módulos, gerenciamento de armazenamento e recursos do sistema, além de execução de comandos personalizados.

## Funcionalidades
A biblioteca contém uma série de comandos que podem ser utilizados para facilitar o gerenciamento de pacotes, manipulação de arquivos, verificação de desempenho do sistema e muito mais.

### Comandos disponíveis:

#### 1. `install(package)`
Instala um pacote Python usando o `pip`.

- **Parâmetros**:
  - `package` (str): Nome do pacote a ser instalado.
  
- **Exemplo**:
  ```python
  helper = PyDroidHelper()
  helper.execute("install", "requests")
  ```

#### 2. `check(module)`
Verifica se um módulo Python está instalado no sistema.

- **Parâmetros**:
  - `module` (str): Nome do módulo a ser verificado.
  
- **Exemplo**:
  ```python
  helper = PyDroidHelper()
  helper.execute("check", "os")
  ```

#### 3. `list()`
Lista todos os pacotes Python instalados.

- **Exemplo**:
  ```python
  helper = PyDroidHelper()
  helper.execute("list")
  ```

#### 4. `clear()`
Limpa os caches locais.

- **Exemplo**:
  ```python
  helper = PyDroidHelper()
  helper.execute("clear")
  ```

#### 5. `run(command)`
Executa um comando shell/terminal.

- **Parâmetros**:
  - `command` (str): O comando a ser executado.
  
- **Exemplo**:
  ```python
  helper = PyDroidHelper()
  helper.execute("run", "ls -l")
  ```

#### 6. `update()`
Atualiza todos os pacotes instalados.

- **Exemplo**:
  ```python
  helper = PyDroidHelper()
  helper.execute("update")
  ```

#### 7. `storage()`
Exibe informações sobre o espaço de armazenamento disponível no sistema.

- **Exemplo**:
  ```python
  helper = PyDroidHelper()
  helper.execute("storage")
  ```

#### 8. `system()`
Exibe informações sobre o sistema operacional, como nome, versão e arquitetura.

- **Exemplo**:
  ```python
  helper = PyDroidHelper()
  helper.execute("system")
  ```

#### 9. `wait(seconds)`
Aguarda um determinado número de segundos.

- **Parâmetros**:
  - `seconds` (int): Tempo em segundos para aguardar.
  
- **Exemplo**:
  ```python
  helper = PyDroidHelper()
  helper.execute("wait", 5)
  ```

#### 10. `mkdir(directory_name)`
Cria um diretório.

- **Parâmetros**:
  - `directory_name` (str): Nome do diretório a ser criado.
  
- **Exemplo**:
  ```python
  helper = PyDroidHelper()
  helper.execute("mkdir", "novo_diretorio")
  ```

#### 11. `rmdir(directory_name)`
Deleta um diretório.

- **Parâmetros**:
  - `directory_name` (str): Nome do diretório a ser deletado.
  
- **Exemplo**:
  ```python
  helper = PyDroidHelper()
  helper.execute("rmdir", "diretorio_a_deletar")
  ```

#### 12. `cpu()`
Exibe a porcentagem de uso da CPU.

- **Exemplo**:
  ```python
  helper = PyDroidHelper()
  helper.execute("cpu")
  ```

#### 13. `memory()`
Exibe informações sobre o uso de memória RAM, incluindo memória total, disponível, usada e porcentagem de uso.

- **Exemplo**:
  ```python
  helper = PyDroidHelper()
  helper.execute("memory")
  ```

#### 14. `ip()`
Exibe o endereço IP local do dispositivo.

- **Exemplo**:
  ```python
  helper = PyDroidHelper()
  helper.execute("ip")
  ```

#### 15. `hash(text)`
Gera o hash SHA-256 de uma string.

- **Parâmetros**:
  - `text` (str): Texto a ser transformado em hash.
  
- **Exemplo**:
  ```python
  helper = PyDroidHelper()
  helper.execute("hash", "texto_exemplo")
  ```

#### 16. `random(start, end)`
Gera um número aleatório entre os valores `start` e `end`.

- **Parâmetros**:
  - `start` (int): O valor inicial.
  - `end` (int): O valor final.
  
- **Exemplo**:
  ```python
  helper = PyDroidHelper()
  helper.execute("random", 1, 100)
  ```

#### 17. `time()`
Exibe a data e hora atual.

- **Exemplo**:
  ```python
  helper = PyDroidHelper()
  helper.execute("time")
  ```

---

## Exemplo de Uso

```python
from PyDroidHelper import PyDroidHelper

# Cria uma instância do PyDroidHelper
helper = PyDroidHelper()

# Executa o comando 'install' para instalar um pacote
helper.execute("install", "requests")

# Executa o comando 'cpu' para verificar o uso da CPU
helper.execute("cpu")

# Executa o comando 'storage' para verificar o espaço de armazenamento
helper.execute("storage")
```

---

## Instalação

Não é necessário instalar nada além de ter o Python configurado em seu ambiente. Para utilizar, basta importar o `PyDroidHelper` em seu código Python.

---

