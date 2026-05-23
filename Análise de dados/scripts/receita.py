preco_cenoura = 11.27
preco_oleo = 12
preco_fermento = 4.25
preco_leite = 4.65
preco_acucar = 2.48
preco_ovos = 18

def soma_ingredientes(tem_cenoura, tem_oleo, tem_fermento, tem_leite, tem_acucar, tem_ovos):

	total_compra = 0

	if tem_cenoura:
		total_compra = total_compra + preco_cenoura
	if tem_oleo:
		total_compra = total_compra + preco_oleo
	if tem_fermento:
		total_compra = total_compra + preco_fermento
	if tem_leite:
		total_compra = total_compra + preco_leite
	if tem_acucar:
		total_compra = total_compra + preco_acucar
	if tem_ovos:
		total_compra = total_compra + preco_ovos
	return total_compra

total = soma_ingredientes(True, True, True, True, True, True)

print(total)