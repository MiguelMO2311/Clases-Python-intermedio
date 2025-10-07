from dataclasses import dataclass, field

@dataclass
class DataPipeline:
    data_sources: list = field(default_factory=list) 
    transformations: list = field(default_factory=list)
    cache_activado: bool = False
    tamaño: int | None = None
    batch: int | None = None

    def run(self):
        print("Ejecutando pipeline...\n")
        for source in self.data_sources:
            print(f"Procesando fuente: {source}")
            for transform in self.transformations:
                print(f"  Aplicando transformación: {transform}")
        print("\nConfiguración tecnica:")
        print(f"Cache: {'Activada' if self.cache_activado else 'Desactivada'}")
        print(f"Tamaño total: {self.tamaño}")
        print(f"Batch size: {self.batch}")
        print("Pipeline ejecutada con éxito.")

class ConstructorDataPipeline:
    def __init__(self):
        self.reset()

    def reset(self):
        self.pipeline = DataPipeline()
        return self

    def añadir_data_source(self, source: str):
        self.pipeline.data_sources.append(source)
        return self

    def añadir(self, source: str):
        return self.añadir_data_source(source)

    def transformation(self, transformation: str):
        self.pipeline.transformations.append(transformation)
        return self

    def activar_cache(self):
        self.pipeline.cache_activado = True
        return self

    def tamaño(self, tamaño: int):
        self.pipeline.tamaño = tamaño
        return self

    def batch(self, batch_size: int):
        self.pipeline.batch = batch_size
        return self

    def construir(self) -> DataPipeline:
        return self.pipeline

constructor = ConstructorDataPipeline()
pipeline = (
    constructor
    .añadir("CSV:clientes.csv")
    .añadir("API:ventas_diarias")
    .transformation("limpieza_nulos")
    .transformation("normalizacion")
    .activar_cache()
    .tamaño(10000)
    .batch(500)
    .construir()
)

pipeline.run()
