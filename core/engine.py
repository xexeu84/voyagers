import os

class VoyagersEngine:
    def __init__(self):
        self.equipa = ["Marcus", "Aki", "Valentina", "Lukas"]
        self.versao = 2.0
        self.fase_actual = 2
        self.estado_sistema = True
        self.comissao_taxa = 0.15  # 15% para a plataforma

    def area_acesso(self, usuario_login):
        """Traducao da Funcao Area_Acesso()"""
        if usuario_login == "Success":
            return {"status": True, "action": "Abrir Menu_Navegacao_PWA"}
        return {"status": False, "action": "Recusar Acesso"}

    def calcular_comissao(self, peso, distancia):
        """Traducao do Procedimento Calcular_Comissao()"""
        # Taxa <- (Peso * 0.5) + (Distancia * 0.1)
        taxa_base = (peso * 0.5) + (distancia * 0.1)
        comissao_voyagers = taxa_base * self.comissao_taxa
        return round(comissao_voyagers, 2)

    def verificar_seguranca(self, riesgo_legal):
        """Traducao da Regra de Seguranca e Legalidade"""
        if riesgo_legal:
            return "BLOQUEAR_OPERACAO: Notificar Marcus CEO"
        return "OPERACAO_SEGURA"

# Instancia para uso del sistema
engine = VoyagersEngine()
