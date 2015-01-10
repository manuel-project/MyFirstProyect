from clientes.models import Country


class SaveDicc():
   
    def get(self,kwargs):
        fields = [i.name for i in Country._meta.fields if i.name in kwargs]
        kwargs2 = [ {k:v} for k,v  in kwargs.items() if k in fields]
        import ipdb; ipdb.set_trace()
        