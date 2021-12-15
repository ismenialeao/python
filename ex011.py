#Pintando parede


#CAlcule largura e altura e  area da parece em metros


larg = float(input('largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt


print('Sua parede tem a dimensão de {}x{} e sua area é de {}m². '.format(larg, alt, area))

tinta = area / 2
print('Para pintar essa parede vc precisaria de {}' .format(tinta))