import os
import subprocess

class GitorBitBucket:
    def __init__(self) -> None:
        try:
            remote_url_bytes = subprocess.check_output(['git', 'config', '--get', 'remote.origin.url'])
            self.remote_url = remote_url_bytes.decode().strip()
        except subprocess.CalledProcessError:
            print("Erro: Não foi possível obter a URL remota do repositório Git.")
            self.remote_url = ""
             
    def which_origin(self) -> None:
        file_name = "user_data.txt"
        user_data = {}
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    key, value = line.strip().split(': ')
                    user_data[key] = value
        else:
            user_data['github_user'] = input("Digite seu nome de usuário do GitHub: ")
            user_data['github_email'] = input("Digite seu email do GitHub: ")
            user_data['bitbucket_user'] = input("Digite seu nome de usuário do Bitbucket: ")
            user_data['bitbucket_email'] = input("Digite seu email do Bitbucket: ")
            with open(file_name, 'w') as file:
                file.write(f"github_user: {user_data['github_user']}\n")
                file.write(f"github_email: {user_data['github_email']}\n")
                file.write(f"bitbucket_user: {user_data['bitbucket_user']}\n")
                file.write(f"bitbucket_email: {user_data['bitbucket_email']}\n")

        if 'github.com' in self.remote_url:
            subprocess.run(['git', 'config', 'user.name', user_data['github_user']])
            subprocess.run(['git', 'config', 'user.email', user_data['github_email']])
            print("Configurações de usuário definidas para GitHub.")
        elif 'bitbucket.org' in self.remote_url:
            subprocess.run(['git', 'config', 'user.name', user_data['bitbucket_user']])
            subprocess.run(['git', 'config', 'user.email', user_data['bitbucket_email']])
            print("Configurações de usuário definidas para Bitbucket.")
        else:
            print("URL remota desconhecida, mantendo as configurações atuais.")

if __name__ == '__main__':
    g_or_b = GitorBitBucket()
    g_or_b.which_origin()