"""
Leia um arquivo que contenha dados de log de treinamento de modelos de Machine Learning.
Calcule a média e o desvio padrão do tempo de exercução constantes.
"""
import pandas as pd
def calcular_estatisticas_tempo_execucao(arquivo_log):
    """
    Lê um arquivo de log e calcula a média e o desvio padrão do tempo de execução.

    Args:
        arquivo_log (str): Caminho para o arquivo de log.

    Returns:
        tuple: Média e desvio padrão do tempo de execução.
    """
    # Lê o arquivo de log
    df = pd.read_csv(arquivo_log)

    # Verifica se a coluna 'tempo_execucao' existe
    if 'tempo_execucao' not in df.columns:
        raise ValueError("O arquivo de log deve conter uma coluna 'tempo_execucao'.")

    # Calcula a média e o desvio padrão
    media = df['tempo_execucao'].mean()
    desvio_padrao = df['tempo_execucao'].std()

    return media, desvio_padrao
# Exemplo de uso
if __name__ == "__main__":          
    arquivo = 'caminho/para/seu/arquivo_log.csv'
    try:
        media, desvio_padrao = calcular_estatisticas_tempo_execucao(arquivo)
        print(f"Média do tempo de execução: {media:.2f} segundos")
        print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f} segundos")
    except Exception as e:
        print(f"Erro ao processar o arquivo de log: {e}")       
import pandas as pd
import numpy as np
def calcular_estatisticas_tempo_execucao(arquivo_log):

    """
    Lê um arquivo de log e calcula a média e o desvio padrão do tempo de execução.

    Args:
        arquivo_log (str): Caminho para o arquivo de log.

    Returns:
        tuple: Média e desvio padrão do tempo de execução.
    """
    # Lê o arquivo de log
    df = pd.read_csv(arquivo_log)

    # Verifica se a coluna 'tempo_execucao' existe
    if 'tempo_execucao' not in df.columns:
        raise ValueError("O arquivo de log deve conter uma coluna 'tempo_execucao'.")

    # Calcula a média e o desvio padrão
    media = np.mean(df['tempo_execucao'])
    desvio_padrao = np.std(df['tempo_execucao'])

    return media, desvio_padrao     
# Exemplo de uso
if __name__ == "__main__":        
    arquivo = 'caminho/para/seu/arquivo_log.csv'
    try:
        media, desvio_padrao = calcular_estatisticas_tempo_execucao(arquivo)
        print(f"Média do tempo de execução: {media:.2f} segundos")
        print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f} segundos")
    except Exception as e:
        print(f"Erro ao processar o arquivo de log: {e}")           
import pandas as pd
import numpy as np
def calcular_estatisticas_tempo_execucao(arquivo_log):
    """
    Lê um arquivo de log e calcula a média e o desvio padrão do tempo de execução.

    Args:
        arquivo_log (str): Caminho para o arquivo de log.

    Returns:
        tuple: Média e desvio padrão do tempo de execução.
    """
    # Lê o arquivo de log
    df = pd.read_csv(arquivo_log)

    # Verifica se a coluna 'tempo_execucao' existe
    if 'tempo_execucao' not in df.columns:
        raise ValueError("O arquivo de log deve conter uma coluna 'tempo_execucao'.")

    # Calcula a média e o desvio padrão
    media = np.mean(df['tempo_execucao'])
    desvio_padrao = np.std(df['tempo_execucao'])

    return media, desvio_padrao     
# Exemplo de uso
if __name__ == "__main__":        
    arquivo = 'caminho/para/seu/arquivo_log.csv'
    try:
        media, desvio_padrao = calcular_estatisticas_tempo_execucao(arquivo)
        print(f"Média do tempo de execução: {media:.2f} segundos")
        print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f} segundos")
    except Exception as e:
        print(f"Erro ao processar o arquivo de log: {e}")       
import pandas as pd
import numpy as np
def calcular_estatisticas_tempo_execucao(arquivo_log):
    """
    Lê um arquivo de log e calcula a média e o desvio padrão do tempo de execução.

    Args:
        arquivo_log (str): Caminho para o arquivo de log.

    Returns:
        tuple: Média e desvio padrão do tempo de execução.
    """
    # Lê o arquivo de log
    df = pd.read_csv(arquivo_log)

    # Verifica se a coluna 'tempo_execucao' existe
    if 'tempo_execucao' not in df.columns:
        raise ValueError("O arquivo de log deve conter uma coluna 'tempo_execucao'.")

    # Calcula a média e o desvio padrão
    media = np.mean(df['tempo_execucao'])
    desvio_padrao = np.std(df['tempo_execucao'])

    return media, desvio_padrao     
# Exemplo de uso
if __name__ == "__main__":        
    arquivo = 'caminho/para/seu/arquivo_log.csv'
    try:
        media, desvio_padrao = calcular_estatisticas_tempo_execucao(arquivo)
        print(f"Média do tempo de execução: {media:.2f} segundos")
        print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f} segundos")
    except Exception as e:
        print(f"Erro ao processar o arquivo de log: {e}")       
import pandas as pd
import numpy as np
def calcular_estatisticas_tempo_execucao(arquivo_log):
    """
    Lê um arquivo de log e calcula a média e o desvio padrão do tempo de execução.

    Args:
        arquivo_log (str): Caminho para o arquivo de log.

    Returns:
        tuple: Média e desvio padrão do tempo de execução.
    """
    # Lê o arquivo de log
    df = pd.read_csv(arquivo_log)

    # Verifica se a coluna 'tempo_execucao' existe
    if 'tempo_execucao' not in df.columns:
        raise ValueError("O arquivo de log deve conter uma coluna 'tempo_execucao'.")

    # Calcula a média e o desvio padrão
    media = np.mean(df['tempo_execucao'])
    desvio_padrao = np.std(df['tempo_execucao'])

    return media, desvio_padrao
# Exemplo de uso
if __name__ == "__main__":        
    arquivo = 'caminho/para/seu/arquivo_log.csv'
    try:
        media, desvio_padrao = calcular_estatisticas_tempo_execucao(arquivo)
        print(f"Média do tempo de execução: {media:.2f} segundos")
        print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f} segundos")
    except Exception as e:
        print(f"Erro ao processar o arquivo de log: {e}")       
import pandas as pd
import numpy as np  
def calcular_estatisticas_tempo_execucao(arquivo_log):
    """
    Lê um arquivo de log e calcula a média e o desvio padrão do tempo de execução.

    Args:
        arquivo_log (str): Caminho para o arquivo de log.

    Returns:
        tuple: Média e desvio padrão do tempo de execução.
    """
    # Lê o arquivo de log
    df = pd.read_csv(arquivo_log)

    # Verifica se a coluna 'tempo_execucao' existe
    if 'tempo_execucao' not in df.columns:
        raise ValueError("O arquivo de log deve conter uma coluna 'tempo_execucao'.")

    # Calcula a média e o desvio padrão
    media = np.mean(df['tempo_execucao'])
    desvio_padrao = np.std(df['tempo_execucao'])

    return media, desvio_padrao
# Exemplo de uso
if __name__ == "__main__":        
    arquivo = 'caminho/para/seu/arquivo_log.csv'
    try:
        media, desvio_padrao = calcular_estatisticas_tempo_execucao(arquivo)
        print(f"Média do tempo de execução: {media:.2f} segundos")
        print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f} segundos")
    except Exception as e:
        print(f"Erro ao processar o arquivo de log: {e}")

import pandas as pd
import numpy as np  
def calcular_estatisticas_tempo_execucao(arquivo_log):
    """
    Lê um arquivo de log e calcula a média e o desvio padrão do tempo de execução.

    Args:
        arquivo_log (str): Caminho para o arquivo de log.

    Returns:
        tuple: Média e desvio padrão do tempo de execução.
    """
    # Lê o arquivo de log
    df = pd.read_csv(arquivo_log)

    # Verifica se a coluna 'tempo_execucao' existe
    if 'tempo_execucao' not in df.columns:
        raise ValueError("O arquivo de log deve conter uma coluna 'tempo_execucao'.")

    # Calcula a média e o desvio padrão
    media = np.mean(df['tempo_execucao'])
    desvio_padrao = np.std(df['tempo_execucao'])

    return media, desvio_padrao

# Exemplo de uso
if __name__ == "__main__":      
    arquivo = 'caminho/para/seu/arquivo_log.csv'
    try:
        media, desvio_padrao = calcular_estatisticas_tempo_execucao(arquivo)
        print(f"Média do tempo de execução: {media:.2f} segundos")
        print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f} segundos")
    except Exception as e:
        print(f"Erro ao processar o arquivo de log: {e}")       
import pandas as pd
import numpy as np    
def calcular_estatisticas_tempo_execucao(arquivo_log):
    """
    Lê um arquivo de log e calcula a média e o desvio padrão do tempo de execução.

    Args:
        arquivo_log (str): Caminho para o arquivo de log.

    Returns:
        tuple: Média e desvio padrão do tempo de execução.
    """
    # Lê o arquivo de log
    df = pd.read_csv(arquivo_log)

    # Verifica se a coluna 'tempo_execucao' existe
    if 'tempo_execucao' not in df.columns:
        raise ValueError("O arquivo de log deve conter uma coluna 'tempo_execucao'.")

    # Calcula a média e o desvio padrão
    media = np.mean(df['tempo_execucao'])
    desvio_padrao = np.std(df['tempo_execucao'])

    return media, desvio_padrao
# Exemplo de uso
if __name__ == "__main__":        
    arquivo = 'caminho/para/seu/arquivo_log.csv'
    try:
        media, desvio_padrao = calcular_estatisticas_tempo_execucao(arquivo)
        print(f"Média do tempo de execução: {media:.2f} segundos")
        print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f} segundos")
    except Exception as e:
        print(f"Erro ao processar o arquivo de log: {e}")
import pandas as pd
import numpy as np
def calcular_estatisticas_tempo_execucao(arquivo_log):
    """
    Lê um arquivo de log e calcula a média e o desvio padrão do tempo de execução.

    Args:
        arquivo_log (str): Caminho para o arquivo de log.

    Returns:
        tuple: Média e desvio padrão do tempo de execução.
    """
    # Lê o arquivo de log
    df = pd.read_csv(arquivo_log)

    # Verifica se a coluna 'tempo_execucao' existe
    if 'tempo_execucao' not in df.columns:
        raise ValueError("O arquivo de log deve conter uma coluna 'tempo_execucao'.")

    # Calcula a média e o desvio padrão
    media = np.mean(df['tempo_execucao'])
    desvio_padrao = np.std(df['tempo_execucao'])


    return media, desvio_padrao
# Exemplo de uso
if __name__ == "__main__":
    arquivo = 'caminho/para/seu/arquivo_log.csv'
    try:
        media, desvio_padrao = calcular_estatisticas_tempo_execucao(arquivo)
        print(f"Média do tempo de execução: {media:.2f} segundos")
        print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f} segundos")
    except Exception as e:
        print(f"Erro ao processar o arquivo de log: {e}")
import pandas as pd
import numpy as np
def calcular_estatisticas_tempo_execucao(arquivo_log):
    """
    Lê um arquivo de log e calcula a média e o desvio padrão do tempo de execução.

    Args:
        arquivo_log (str): Caminho para o arquivo de log.

    Returns:
        tuple: Média e desvio padrão do tempo de execução.
    """
    # Lê o arquivo de log
    df = pd.read_csv(arquivo_log)

    # Verifica se a coluna 'tempo_execucao' existe
    if 'tempo_execucao' not in df.columns:
        raise ValueError("O arquivo de log deve conter uma coluna 'tempo_execucao'.")

    # Calcula a média e o desvio padrão
    media = np.mean(df['tempo_execucao'])
    desvio_padrao = np.std(df['tempo_execucao'])
    return media, desvio_padrao
# Exemplo de uso
if __name__ == "__main__":
    arquivo = 'caminho/para/seu/arquivo_log.csv'
    try:
        media, desvio_padrao = calcular_estatisticas_tempo_execucao(arquivo)
        print(f"Média do tempo de execução: {media:.2f} segundos")
        print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f} segundos")
    except Exception as e:
        print(f"Erro ao processar o arquivo de log: {e}")
import pandas as pd
import numpy as np

def calcular_estatisticas_tempo_execucao(arquivo_log):
    """
    Lê um arquivo de log e calcula a média e o desvio padrão do tempo de execução.

    Args:
        arquivo_log (str): Caminho para o arquivo de log.

    Returns:
        tuple: Média e desvio padrão do tempo de execução.
    """
    # Lê o arquivo de log
    df = pd.read_csv(arquivo_log)

    # Verifica se a coluna 'tempo_execucao' existe
    if 'tempo_execucao' not in df.columns:
        raise ValueError("O arquivo de log deve conter uma coluna 'tempo_execucao'.")

    # Calcula a média e o desvio padrão
    media = np.mean(df['tempo_execucao'])   
    desvio_padrao = np.std(df['tempo_execucao'])
    return media, desvio_padrao
# Exemplo de uso
if __name__ == "__main__":
    arquivo = 'caminho/para/seu/arquivo_log.csv'
    try:
        media, desvio_padrao = calcular_estatisticas_tempo_execucao(arquivo)
        print(f"Média do tempo de execução: {media:.2f} segundos")
        print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f} segundos")
    except Exception as e:
        print(f"Erro ao processar o arquivo de log: {e}")
import pandas as pd
import numpy as np
def calcular_estatisticas_tempo_execucao(arquivo_log):
    """
    Lê um arquivo de log e calcula a média e o desvio padrão do tempo de execução.

    Args:
        arquivo_log (str): Caminho para o arquivo de log.

    Returns:
        tuple: Média e desvio padrão do tempo de execução.
    """
    # Lê o arquivo de log
    df = pd.read_csv(arquivo_log)

    # Verifica se a coluna 'tempo_execucao' existe
    if 'tempo_execucao' not in df.columns:
        raise ValueError("O arquivo de log deve conter uma coluna 'tempo_execucao'.")

    # Calcula a média e o desvio padrão
    media = np.mean(df['tempo_execucao'])

    desvio_padrao = np.std(df['tempo_execucao'])
    return media, desvio_padrao
# Exemplo de uso
if __name__ == "__main__":
    arquivo = 'caminho/para/seu/arquivo_log.csv'
    try:
        media, desvio_padrao = calcular_estatisticas_tempo_execucao(arquivo)
        print(f"Média do tempo de execução: {media:.2f} segundos")
        print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f} segundos")
    except Exception as e:
        print(f"Erro ao processar o arquivo de log: {e}")
import pandas as pd
import numpy as np
def calcular_estatisticas_tempo_execucao(arquivo_log):
    """
    Lê um arquivo de log e calcula a média e o desvio padrão do tempo de execução.

    Args:
        arquivo_log (str): Caminho para o arquivo de log.

    Returns:
        tuple: Média e desvio padrão do tempo de execução.
    """
    # Lê o arquivo de log
    df = pd.read_csv(arquivo_log)

    # Verifica se a coluna 'tempo_execucao' existe
    if 'tempo_execucao' not in df.columns:
        raise ValueError("O arquivo de log deve conter uma coluna 'tempo_execucao'.")

    # Calcula a média e o desvio padrão
    media = np.mean(df['tempo_execucao'])   