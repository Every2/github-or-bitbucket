import subprocess

class GitorBitBucket:
    def __init__(self, git_user: str, git_email: str, bitbucket_user: str, bitbucket_email: str) -> None:
        try:
            remote_url_bytes = subprocess.check_output(['git', 'config', '--get', 'remote.origin.url'])
            self.remote_url = remote_url_bytes.decode().strip()
        except subprocess.CalledProcessError:
            print("Erro: Não foi possível obter a URL remota do repositório Git.")
            self.remote_url = ""

        self.git_user = git_user
        self.git_email = git_email
        self.bitbucket_user = bitbucket_user
        self.bitbucket_email = bitbucket_email

    def which_origin(self) -> None:
        if 'github.com' in self.remote_url:
            subprocess.run(['git', 'config', '--global', 'user.name', self.git_user])
            subprocess.run(['git', 'config', '--global', 'user.email', self.git_email])
            print("Configurações de usuário definidas para GitHub.")
        elif 'bitbucket.org' in self.remote_url:
            subprocess.run(['git', 'config', '--global', 'user.name', self.bitbucket_user])
            subprocess.run(['git', 'config', '--global', 'user.email', self.bitbucket_email])
            print("Configurações de usuário definidas para Bitbucket.")
        else:
            print("URL remota desconhecida, mantendo as configurações atuais.")

if __name__ == '__main__':
    g_or_b = GitorBitBucket('git_user, git_email, bitbucket_user, bitbucket_email')
    g_or_b.which_origin()