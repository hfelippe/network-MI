# nodes of the network
names=["index", "name", "nodeLabel", "_pos"]
df_nodes=pd.read_csv("nodes.csv", 
                     sep=',',comment='#',header=None, names=names)
df_nodes.drop(columns=["nodeLabel", "_pos"], inplace=True)

# hemisphere
names=["country", "globalSouthCountries_globalSouth"]
df_hemisphere=pd.read_csv("global-south-countries-2024.csv", 
                       sep=',', comment=None, header=0, names=names)
df_hemisphere.rename(columns={'globalSouthCountries_globalSouth': 'hemisphere'}, inplace=True)
df_hemisphere['hemisphere']=df_hemisphere['hemisphere'].replace({'Yes': 'South', 'No': 'North'})

# continents
names=["Continent", "Country"]
df_continents=pd.read_csv("Countries-Continents.csv",
                       sep=',', comment=None, header=0, names=names)

# merge base on countries (some will be NaN because of terminology inconsistency)
df_nodes = pd.merge(df_nodes, df_hemisphere[['country', 'hemisphere']], left_on='name', right_on='country', how='left')
df_nodes = pd.merge(df_nodes, df_continents[['Country', 'Continent']], left_on='name', right_on='Country', how='left')
df_nodes.drop(columns=['country', 'Country'], inplace=True)
df_nodes.rename(columns={'Continent': 'continent'}, inplace=True)

# we save only the rows with NaN and edit them *MANUALLY*, saving it as `df_nodes_manual.csv`)
#df_nodes[df_nodes.isnull().any(axis=1)].to_csv("df_nodes_nan.csv", index=False)

# loading manually modified file
names=['index', 'name', 'hemisphere', 'continent']
df_manual=pd.read_csv("df_nodes_manual.csv",sep=',',comment=None,header=0,names=names)

# updating the NaN values with those manually modified
df_nodes.set_index('name', inplace=True)
df_manual.set_index('name', inplace=True)
df_nodes.update(df_manual)
df_nodes.reset_index(inplace=True) # reset index to bring 'name' back as regular column
column_order=['index', 'name'] + [col for col in df_nodes.columns if col not in ['index', 'name']]
df_nodes = df_nodes[column_order]

# assign 0 and 1 to South and North (fillna(-1) makes sure to convert NaN into integers)
df_nodes['b_hemis'] = df_nodes['hemisphere'].replace({'South': 0, 'North': 1}).fillna(-1).astype(int)

# assign 0,...,5 to continents
df_nodes['b_cont'] = df_nodes['continent'].astype('category').cat.codes

# GDP dataset from World Bank
df_wb = pd.read_csv("ec734139-1f30-44bc-bc63-184dbe96ed00_Data.csv")
df_wb = df_wb.iloc[:217] # index 217 onwards are not countries
df_wb['index'] = df_wb.index

# list of countries manually fixed (with ChatGPT help)
names=['index_gpt', 'name_gpt']
df_gpt=pd.read_csv("countries_manual.txt",sep=' ',comment=None,header=None,names=names)
df_namematch=pd.merge(df_wb, df_gpt[['index_gpt', 'name_gpt']], left_on='index', right_on='index_gpt', how='left')
df_partition=pd.merge(df_nodes, df_namematch[['name_gpt', '2010 [YR2010]']], left_on='name', right_on='name_gpt', how='left')
df_partition.drop(columns=['name_gpt'], inplace=True)
df_partition.rename(columns={'2010 [YR2010]': 'gdp_2010'}, inplace=True)

# reorder
cols = ['index', 'name', 'hemisphere', 'continent', 'gdp_2010', 'b_hemis', 'b_cont']
df_partition = df_partition[cols]
df_partition["gdp_2010"] = pd.to_numeric(df_partition["gdp_2010"], errors='coerce')

# GDP partitioning into 50 bins
num_bins = 50
bins = np.linspace(df_partition['gdp_2010'].min(), df_partition['gdp_2010'].max(), num_bins + 1)
df_partition['b_gdp'] = pd.cut(df_partition['gdp_2010'], bins, labels=False, include_lowest=True)
df_partition.dropna(inplace=True)
df_partition['b_gdp'] = df_partition['b_gdp'].astype(int)

# save
df_partition.to_csv("df_partition.csv", index=False)
