import pandas as pd
import numpy as np
import re

data = pd.read_csv('Biodata.csv')
# missing_values = data.isnull().sum() 
# print(missing_values)
# print(data.dropna()) 
# data.drop(["Query"],axis=1).to_csv('Biodata.csv')
# data.drop_duplicates()
# print(data.drop(["Query"],axis=1))
# data.drop(["Query"],axis=1).to_csv('Biodata.csv')
# values = {"Lowest E-value": 0}
# data.fillna(value=values)
# print(data.fillna(value=values))
# data.duplicated().sum()
# print(data.duplicated().sum())
# data.drop_duplicates()  # Remove duplicate rows
# print(data.drop(["Lowest E-value", "Greatest identity %"],  axis=1)) #fasta file formet 
# data = (data.drop(["Lowest E-value", "Greatest identity %"],  axis=1))
# data.to_csv('Biodata.csv', index=False)
# bioData = open("Biodata.csv", 'r').readlines()[1:] #if 1st line is not necessary then use .readlines()[1:], otherwise no need
# with open('out.fasta', 'w') as f:
#     for x in bioData:
#         f.write(f'>{x.split(",")[0]}\n{x.split(",")[1]}')
# print(data)

# try:
#     with open('out.fasta', mode = 'r') as protein:
#         readprotein = protein.read()
#     matches = re.findall('N[^P](S|T)[^P]', readprotein)
#     for match in matches:
#         print(match)
#         break
# except FileNotFoundError:
#     print("File not found. Please ensure that you are typing the file name exactly as it is found with the file extension.")



# # Import libraries for data visualization
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set_theme()
# data = sns.load_dataset("tips")
# data.head()


# Import libraries for data visualization
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_theme(font='sans-serif', font_scale=2)
var = pd.read_csv("Angela/MRM_GluGli_new.csv")
sns.pairplot(var, vars=["ARI", "CAD",], hue="S-poor and S-rich", height=6, palette="tab10", plot_kws={300, 200})
# plt.xlabel('ARI', fontdict={'fontsize': 20})
# plt.xlabel('CAD', fontdict={'fontsize': 20})
# plt.ylabel('ARI', fontdict={'fontsize': 20})
# plt.ylabel('CAD', fontdict={'fontsize': 20})


plt.savefig("Mitu1.png", format='png')

# sns.pairplot(var, vars=["ARI", "CAD", "LAN", "STA", "CSP",	"JAG",	"MAC", "NOR",	"WEE"], hue ="S-poor and S-rich", size= 0, palette="tab10")
# plt.savefig('ARIvsCAD_1.png', format='png')
# plt.show()
# sns.pairplot(var, hue ="Specificity",  size=3, palette=("Set1_r"))
# plt.savefig('Cultivars_log2_1.png', format='png')
# # plt.show()

# sns.pairplot(var, vars=["ARI_log2_TA", "CAD_log2_TA", "LAN_log2_TA", "STA_Log2_TA", "CSP_log2_TA", "JAG_log2_TA",	"MAC_log2_TA", "NOR_log2_TA", "WEE_log2_TA"], hue ="S-poor and S-rich", size=2, palette="tab10")
# # plt.show()
# plt.savefig('Specificity_log2.png', format='png')


# sns.pairplot(var, vars=["ARI", "CAD", "LAN", "STA", "CSP",	"JAG",	"MAC", "NOR",	"WEE"],hue ="Specificity", height= 2,  x_vars=["ARI_length_5", "ARI_depth_3", "CAD_length_5", "CAD_depth_3", "LAN_length_5", "LAN_depth_3", "STA_length_5", "STA_depth_3", "CSP_length_5", "CSP_depth_3", "JAG_depth_3", "JAG_length_5", "MAC_length_5", "MAC_depth_3", "NOR_length_5", "NOR_depth_3", "WEE_length_5", "WEE_depth_3"],
# y_vars=["WEE_length_5", "WEE_depth_3","NOR_length_5", "NOR_depth_3","MAC_length_5", "MAC_depth_3","JAG_length_5", "JAG_depth_3","CSP_length_5", "CSP_depth_3","STA_length_5", "STA_depth_3","LAN_length_5", "LAN_depth_3"], palette="icefire"), plt.xticks("ARI", "CAD",fontsize=7, fontstyle='italic'),plt.yticks(fontsize=7, fontstyle='italic')
# plt.savefig('SPECIFICITY_TEST5.png', format='png')
# plt.show()
# var.head()
# print(var.head())
# sns.pairplot(var, vars=["ARI", "CAD", "LAN", "STA", "CSP",	"JAG",	"MAC", "NOR",	"WEE"], hue ="S-poor and S-rich", palette="tab10")
#  plt.show()
# plt.savefig('cultivars.PNG', format='PNG')
# plt.savefig('cultivars.svg', format='svg', dpi=1) #for svg dpi=1
# sns.pairplot(var, hue ="ARI")
# plt.savefig('ARIvsWEE.svg', format='svg', dpi=1) #for svg dpi=1
# plt.show()
# df = pd.read_csv("Angela/Plot_3.csv")
# sns.pairplot(var, vars=["ARI", "CAD", "LAN", "STA", "CSP",	"JAG",	"MAC", "NOR",	"WEE"], hue ="Specificity",  size=5,  height=6, palette="icefire")
# sns.pairplot(var, vars=["ARI", "CAD", "LAN", "STA", "CSP",	"JAG",	"MAC", "NOR",	"WEE"],hue ="Specificity", size = 6, palette="icefire")
# plt.xlabel('5'),plt.ylabel('2'),plt.xticks([4, 5, 6, 7, 8]),plt.yticks([2, 3, 4, 5])
# plt.show()
# plt.savefig('Specificity.png', format='png')
# sns.pairplot(var, vars=["CAD","WEE"], hue ="S-poor and S-rich", palette="tab10")
# plt.savefig('CADvsWEE.png', format='png')
# plt.savefig('CADvsWEE.svg', format='svg', dpi=1)
# plt.show()
# var = pd.read_csv("Angela/MRM_GluGli_log10_specificity.csv")
# sns.pairplot(var, vars=["ARI_log10", "CAD_log10", "LAN_log10", "STA_log10", "CSP_log10",	"JAG_log10",	"MAC_log10", "NOR_log10",	"WEE_log10"], hue ="S-poor and S-rich", palette="tab10")
# plt.savefig('cultivars_log10.png', format='png')
# plt.savefig('cultivars.svg', format='svg', dpi=1)
# plt.savefig('cultivars_log10.png', format='png')
# plt.show()

# sns.pairplot(var, vars=["CAD_log10","WEE_log10"], hue ="S-poor and S-rich", palette="tab10")
# plt.savefig('CADvsWEE_log10.png', format='png')
# plt.savefig('CADvsWEE_log10.svg', format='svg', dpi=1)
# sns.pairplot(var, vars=["ARI_log10", "CAD_log10", "LAN_log10", "STA_log10", "CSP_log10",	"JAG_log10",	"MAC_log10", "NOR_log10",	"WEE_log10"], hue ="Specificity",  size=5, palette="icefire")
# plt.show()
# plt.savefig('Specificity_log10.png', format='png')
# plt.savefig('Specificity_log10.svg', format='svg', dpi=1)
# to avoid hist or line graph in pairplot
#sns.pairplot(var, hue ="S-poor and S-rich", x_var=["", ""], y_var=["", ""])