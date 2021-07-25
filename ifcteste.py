import ifcopenshell
from ifc_utils.viewer import Viewer
from ifcopenshell.util.selector import Selector

ifc_file = ifcopenshell.open("./modelos_ifc/SampleHouse.ifc")

print("Arquivo ifc carregado: ",ifc_file)

selector = Selector()

elements = selector.parse(ifc_file, ".IfcWall")

print("Elementos selecionados: ",elements)

tela = Viewer(ifc_file, elements)

print("tela")

tela.display()