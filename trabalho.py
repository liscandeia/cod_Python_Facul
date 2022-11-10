#cod grafico de barras com o PIB das UF
import matplotlib.pyplot as plt
import nunpy as no;
plt.rcParans.update({'font.size':7})

uf=('Roraima','Acre','Amapá', 'Tocantins', 'Sergipe',
'Rondônia', 'Piauí','Alagoas','Paraíba','Rio Grande do Norte',
'Maranhão', 'Mato Grosso do Sul','Amazonas',
'Espírito Santo', 'Mato Grosso' ,'Ceará','Pará', 'Pernanbuco','Goiás',
'Distrito Federal' ,'Bahia','Santa Catarina', 'Paraná','Rio Grande do Sul',
'Minas Gerais','Rio de Janeiro','São Paulo')

indice = y_pos = np.arange(start=len(uf),stop=0,step=-1)
pib=[14292227, 15630017, 17496661, 39355941, 44689483,
47091336, 52780785,58963729, 67986074, 71336780,97330938, 1069432406,
108181091, 137345595, 142122028, 163575327, 178376984, 197853378, 20867292, 273613711,
2293240504, 323263857, 466377036, 482464177, 651872684, 779927917,2348338000]

plt.barh(indice, pib, color='magenta')
plt.yticks(indice,uf)
plt.xlabel('PIB por Uf')
plt.title('PIB dos Estados Brasileiros')
plt.show()

#cod grafido de pizza relação do PIB por Região

import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':15})

regioes = ['Centro-Oeste','Nordeste','Sudeste','Sul']
pib = [9.90, 14.18, 5.69, 53.02, 17.22]
plt.figure(figsize=(7,7))
plt.pie(x=pib, labels=regioes, autopct='%1.1f%')
plt.show()

#Gráfico de linha representando o crscimento do PIB em relação ao ano

import matplotlib.pyplot as plt

plt.rcParans.update({'font.size':7})
anos=[2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,
2012,2013,2014,2015,2016,2017,2018,2019]
pib=[1488781276,1717950386,1957751224,2170584503,2409449916,
2720262951,3109803097,3333039339,9885847000,4376382000,4814760000,
5331618957,5778952780,5995787000,6269328000,658479000,7004141000,7389131000]

plt.plot(pib, anos, color='magenta')
plt.show()
