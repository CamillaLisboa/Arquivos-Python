class RelatorioRuim:
    def __init__(self, titulo: str, conteudo: str):
        self.titulo = titulo
        self.conteudo = conteudo

    def gerar_relatorio(self) -> str:
        return f"# {self.titulo}\n\n{self.conteudo}\n"

    def salvar_em_arquivo(self, nome_arquivo: str) -> None:
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            f.write(self.gerar_relatorio())


# uso
r = RelatorioRuim("Vendas", "Total do mês: R$ 10.000")
r.salvar_em_arquivo("relatorio_srp_ruim.txt")


## refatorado

class Relatorio:
    def __init__(self, titulo: str, conteudo: str):
        self.titulo = titulo
        self.conteudo = conteudo

    def gerar(self) -> str:
        return f"# {self.titulo}\n\n{self.conteudo}\n"


# A classe separada cuida do "IO" (salvar).
class SalvarRelatorio:
    @staticmethod
    def salvar_em_arquivo(relatorio: Relatorio, nome_arquivo: str) -> None:
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            f.write(relatorio.gerar())


# uso
r = Relatorio("Vendas", "Total do mês: R$ 10.000")
SalvarRelatorio.salvar_em_arquivo(r, "relatorio_srp_ok.txt")