import menu
import archive

arq = "data.txt"

if not archive.arqExist(arq):
    archive.createArq(arq)

menu.menu()
