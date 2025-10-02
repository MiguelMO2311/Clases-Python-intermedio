from typing import List, Iterator

class Cancion:
    """
    Representa una canción con título y artista.
    """

    def __init__(self, titulo: str, artista: str) -> None:
        self.titulo: str = titulo
        self.artista: str = artista

    def __str__(self) -> str:
        return f"{self.titulo} - {self.artista}"

    def __repr__(self) -> str:
        return f"Cancion(titulo='{self.titulo}', artista='{self.artista}')"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Cancion) and self.titulo == other.titulo and self.artista == other.artista


class Playlist:
    """
    Representa una lista de reproducción de canciones.
    Soporta acceso por índice, búsqueda, iteración y longitud.
    """

    def __init__(self, nombre: str) -> None:
        self.nombre: str = nombre
        self.canciones: List[Cancion] = []

    def agregar(self, cancion: Cancion) -> None:
        self.canciones.append(cancion)

    def __str__(self) -> str:
        return f"Playlist '{self.nombre}' con {len(self)} canciones"

    def __repr__(self) -> str:
        return f"Playlist(nombre='{self.nombre}', canciones={self.canciones})"

    def __len__(self) -> int:
        return len(self.canciones)

    def __getitem__(self, index: int) -> Cancion:
        return self.canciones[index]

    def __iter__(self) -> Iterator[Cancion]:
        return iter(self.canciones)

    def __contains__(self, titulo: str) -> bool:
        return any(c.titulo == titulo for c in self.canciones)


# ******** Ejemplos de uso ********

# Crear canciones
c1 = Cancion("Bohemian Rhapsody", "Queen")
c2 = Cancion("Imagine", "John Lennon")
c3 = Cancion("Stairway to Heaven", "Led Zeppelin")

# Crear playlist
rock = Playlist("Rock Clasico")
rock.agregar(c1)
rock.agregar(c2)
rock.agregar(c3)

# Imprimir playlist
print(str(rock))  # Playlist 'Rock Clasico' con 3 canciones

# Acceder por índice
print(rock[1])  # Imagine - John Lennon

# Iterar
for cancion in rock:
    print(cancion)

# Buscar por título
print("Imagine" in rock)    # True
print("Yesterday" in rock)  # False
