# Librería Legacy 
class LegacyImageLib:
    def load(self, path: str):
        width = len(path) + 1
        height = max(1, len(path) // 2)
        return {"width": width, "height": height, "path": path}

# Librería New
class NewImageLib:
    class S3_picture:
        def __init__(self, name):
            self.name = name

        def get_info(self):
            return {"width": len(self.name) + 2, "height": 10}

    def query_image(self, name):
        return self.S3_picture(name)

# Clase Imagen (estructura común)
class Imagen:
    def __init__(self, width: int, height: int, path: str):
        self.width = width
        self.height = height
        self.path = path

# Adaptador 
class ImageAdapter:
    def __init__(self, lib):
        self.lib = lib

    def load(self, path: str) -> Imagen:
        if isinstance(self.lib, LegacyImageLib):
            info = self.lib.load(path)
            return Imagen(info["width"], info["height"], info["path"])

        elif isinstance(self.lib, NewImageLib):
            picture = self.lib.query_image(path)
            info = picture.get_info()
            return Imagen(info["width"], info["height"], path)

        else:
            raise TypeError("Librería no compatible")


# *** Ejemplo de uso ***

if __name__ == "__main__":
    legacy = LegacyImageLib()
    new = NewImageLib()

    loader1 = ImageAdapter(legacy)
    img1 = loader1.load("foto_legacy.png")
    print(f"Legacy -> width: {img1.width}, height: {img1.height}, path: {img1.path}")

    loader2 = ImageAdapter(new)
    img2 = loader2.load("foto_new.png")
    print(f"New -> width: {img2.width}, height: {img2.height}, path: {img2.path}")

