h_T1 = int(input('Vertrek thuis (uren): '))
m_T1 = (int(input('Vertrek thuis (minuten): '))) + (h_T1 * 60)
h_V1 = int(input('aankomst vriendin (uren): '))
m_V1 = (int(input('aankomst vriendin (minuten): '))) + (h_V1 * 60)
h_V2 = int(input('Vertrek vriendin (uren): '))
m_V2 = (int(input('Vertrek vriendin (minuten): '))) + (h_V2 * 60)
h_T2 = int(input('aankomst thuis (uren): '))
m_T2 = (int(input('aankomst thuis (minuten): '))) + (h_T2 * 60)

############### VAN XANDER #################

verschil_thuis = m_T2 - m_T1
if verschil_thuis < 0:
    verschil_thuis = 1440 + verschil_thuis
verschil_vriendin = m_V2 - m_V1
if verschil_vriendin < 0:
    verschil_vriendin = 1440 + verschil_vriendin

achterstand = (verschil_thuis - verschil_vriendin) / 2

m_V2 += achterstand

minuten_klok = int(m_V2 % 60)
uren_klok = int(m_V2 // 60)
if uren_klok > 24:
    uren_klok -= 24

print(uren_klok)
print(minuten_klok)