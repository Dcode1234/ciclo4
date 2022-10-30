from Repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa

class ControladorMesa():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()
    def index(self):
        return self.repositorioMesa.findAll()
    def create(self,infoMesa):
        nuevoMesa=Mesa(infoMesa)
        return self.repositorioMesa.save(nuevoMesa)
    def show(self,numero):
        elMesa=Mesa(self.repositorioMesa.findById(numero))
        return elMesa.__dict__
    def update(self,numero,infoMesa):
        MesaActual=Mesa(self.repositorioMesa.findById(numero))
        MesaActual.numero=infoMesa["numero"]
        MesaActual.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        return self.repositorioMesa.save(MesaActual)
    def delete(self,id):
        return self.repositorioMesa.delete(id)