from application.model.entity.periodo import Periodo
from application.model.entity.disciplina import Disciplina

class PeriodoDAO:

    def __init__(self):
        engenharia_software = Disciplina(1, "Engenharia de Software e Sistemas de Informação", None, 60, Disciplina.Credito(2,2))
        introducao_computacao_algoritmos = Disciplina(2, "Introdução à Computação e Algoritmos", None, 60, Disciplina.Credito(1,3))
        laboratorio_programacao_websites = Disciplina(3, "Laboratório de Programação de Web Sites", None, 60, Disciplina.Credito(1,3))
        fundamentos_matematica_elementar = Disciplina(4, "Fundamentos da Matemática Elementar", None, 60, Disciplina.Credito(4,0))
        psicologia_empresarial = Disciplina(5, "Psicologia Empresarial", None, 60, Disciplina.Credito(4,0))
        informatica_aplicada = Disciplina(6, "Informática Aplicada", None, 30, Disciplina.Credito(1,1))
        laboratorio_empreendedorismo_inovacao_um = Disciplina(7, "Laboratório de Empreendedorismo e Inovação I", None, 30, Disciplina.Credito(0,2))
        engenharia_requisitos_analise_sistemas = Disciplina(8, "Engenharia de Requisitos e Análise de Sistemas", engenharia_software, 60, Disciplina.Credito(2,2))
        estrutura_dados = Disciplina(9, "Estruturas de Dados", introducao_computacao_algoritmos, 60, Disciplina.Credito(2,2))
        laboratorio_programacao_orientado_objetos = Disciplina(10, "Laboratório de Programação Orientada a Objetos", introducao_computacao_algoritmos, 60, Disciplina.Credito(1,3))
        empreendedorismo_invoacao = Disciplina(11, "Empreendedorismo e Inovação", None, 60, Disciplina.Credito(2,2))
        matematica_financeira_financas = Disciplina(12, "Matemática Financeira e Finanças", fundamentos_matematica_elementar, 60, Disciplina.Credito(4,0))
        pratica_leitura_producao_textual = Disciplina(13, "Prática de Leitura e Produção Textual", informatica_aplicada, 30, Disciplina.Credito(2,0))
        laboratorio_empreendedorismo_inovacao_dois = Disciplina(14, "Laboratório de Empreendedorismo e Inovação II", laboratorio_empreendedorismo_inovacao_um, 30, Disciplina.Credito(0,2))
        self._periodo_list = []
        self._periodo_list.append(Periodo(1, "1º Período", [
            engenharia_software,
            introducao_computacao_algoritmos,
            laboratorio_programacao_websites,
            fundamentos_matematica_elementar,
            psicologia_empresarial,
            informatica_aplicada,
            laboratorio_empreendedorismo_inovacao_um
        ]))
        self._periodo_list.append(Periodo(2, "2º Período", [
            engenharia_requisitos_analise_sistemas,
            estrutura_dados,
            laboratorio_programacao_orientado_objetos,
            empreendedorismo_invoacao,
            matematica_financeira_financas,
            pratica_leitura_producao_textual,
            
        ]))

    def listar_todos(self):
        return self._periodo_list

    def buscar_por_id(self, id):
        periodo_list = list(filter(lambda periodo : periodo.get_id() == id, self._periodo_list))
        if len(periodo_list) == 0:
            return None
        return periodo_list[0] 
        #for i in range(0, len(self._periodo_list)):
        #    if self._periodo_list[i].get_id() == id:
        #        return self._periodo_list[i] 
        #return None
