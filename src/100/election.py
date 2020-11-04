import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

#prompt the user to input the file name and path name to be used in the program
pathName = r"C:\\Users\\jstov\\Downloads\\indiv20\\by_date"
dataDir = Path(pathName)
filename1 = "itcont_2020_20010425_20190425.txt"
filename2 = "itcont_2020_20190426_20190628.txt"
filename3 = "itcont_2020_20190629_20190908.txt"
filename4 = "itcont_2020_20190909_20191120.txt"
fullName1 = dataDir / filename1
fullName2 = dataDir / filename2
fullName3 = dataDir / filename3
fullName4 = dataDir / filename4

data1 = pd.read_csv(fullName1, low_memory=False, sep="|", usecols=[0, 9, 14])
data1.columns = ['Filer ID', 'State', 'Donation Amount ($)']
print(data1)
data2 = pd.read_csv(fullName2, low_memory=False, sep="|", usecols=[0, 9, 14])
data2.columns = ['Filer ID', 'State', 'Donation Amount ($)']
print(data2)
data3 = pd.read_csv(fullName3, low_memory=False, sep="|", usecols=[0, 9, 14])
data3.columns = ['Filer ID', 'State', 'Donation Amount ($)']
print(data3)
data4 = pd.read_csv(fullName4, low_memory=False, sep="|", usecols=[0, 9, 14])
data4.columns = ['Filer ID', 'State', 'Donation Amount ($)']
print(data4)

data = pd.concat([data1, data2])
print(data)
data.columns = ['Filer ID', 'State', 'Donation Amount ($)']

donations_per_candidate_per_state = data['Donation Amount ($)'].groupby([data['State'], data['Filer ID']]).sum()

df = donations_per_candidate_per_state.unstack('Filer ID')
df = df.drop(['AA', 'AP', 'AE', 'ZZ', 'BC', 'AS', 'GU', 'MH', 'NU', 'SK', 'YT', 'MP', 'MB', 'QC', 'AB', 'NS', 'NT', 'FM', 'NB', 'ON', 'UK', 'VI', 'VR', 'NL'])
df = df.fillna(0)
print(df['C00401224'])

#drop all columns where the sum of donations is < $2,000,000
df = df.drop([col for col, val in df.sum().iteritems() if val < 2000000], axis=1)

df.plot(kind='bar', stacked=True)

# plt.bar(donations_per_candidate_per_state.index, donations_per_candidate_per_state[2], stacked=True, width=0.5)
# plt.ylabel('Donation Amount ($)')
# plt.xlabel('State')
# plt.title('Donations per State')

plt.show()