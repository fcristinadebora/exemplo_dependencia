from bebe import Bebe
from mae import Mae

mae = Mae("Claudete")
bebe = Bebe("Enzo", mae)

print("O bebê se chama " + bebe.get_nome())