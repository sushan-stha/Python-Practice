import qrcode  # type: ignore[reportMissingModuleSource]

name = input("Enter your name: ")
img = qrcode.make(name)
img.save(f"{name}.png")