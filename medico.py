from pessoa import Pessoa

class Medico(Pessoa):
    def __init__(self, nome, email, dt_nasc, crm, espec):
        super().__init__(nome, email, dt_nasc)
        self.crm = crm
        self.especialidade = espec

    def __str__(self):
        return f'''
        {super().__str__()},
        especialidade: {self.especialidade},
        Número do CRM {self.crm}'''