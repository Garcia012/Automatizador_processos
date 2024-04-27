import os

def renomear_arquivos(diretorio, novo_nome):
    # Lista todos os arquivos no diretório
    arquivos = os.listdir(diretorio)
    
    # Loop pelos arquivos
    for arquivo in arquivos:
        # Monta o caminho completo do arquivo
        caminho_completo = os.path.join(diretorio, arquivo)
        
        # Verifica se é um arquivo (e não uma pasta)
        if os.path.isfile(caminho_completo):
            # Separa o nome e a extensão do arquivo
            nome_arquivo, extensao = os.path.splitext(arquivo)
            
            # Renomeia o arquivo
            novo_nome_arquivo = novo_nome + extensao
            novo_caminho_completo = os.path.join(diretorio, novo_nome_arquivo)
            os.rename(caminho_completo, novo_caminho_completo)
            print(f"Arquivo {arquivo} renomeado para {novo_nome_arquivo}")
    # Teste do script
    if __name__ == "__main__":
    diretorio_teste = "caminho/do/seu/diretorio"  # Altere para o caminho do seu diretório
    novo_nome_arquivo = "novo_nome"
    renomear_arquivos(diretorio_teste, novo_nome_arquivo)

