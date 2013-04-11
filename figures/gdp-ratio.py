# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
data ='''
 Burma  3.0 8.0
 Turkmenistan   21.8    12.3
 Guatemala  11.3    13.7
 Cambodia   10.5    13.9
 Paraguay   11.8    14.8
 Macau  25.9    14.9
 Central African Republic   7.9 15.5
 Bangladesh 8.8 15.9
 Singapore  14.2    17.0
 Peru   16.0    17.3
 Philippines    14.1    17.3
 Guinea 14.7    17.4
 Thailand   16.0    17.7
 Uganda 11.9    17.8
 Haiti  10.3    18.2
 Laos   12.5    18.2
 Cameroon   18.5    18.5
 Madagascar 12.9    18.5
 Taiwan 12.9    18.5
 Hong Kong  13.0    18.6
 Dominican Republic 15.0    19.1
 Indonesia  13.3    19.2
 Pakistan   10.2    19.3
 Ethiopia   9.9 19.4
 Panama 10.6    19.5
 Togo   16.3    19.5
 Côte d'Ivoire  15.2    19.7
 Nepal  10.4    19.7
 El Salvador    13.0    20.0
 Gabon  9.9 20.1
 China  18.0    20.8
 Bahamas    16.8    20.9
 Costa Rica 15.6    20.9
 Sierra Leone   10.8    21.0
 Chile  18.6    21.1
 Mali   15.0    21.2
 Burkina Faso   12.1    21.6
 Armenia    16.8    21.8
 Honduras   16.3    21.8
 Chad   5.3 22.1
 Syria  10.2    22.1
 Sri Lanka  13.3    22.6
 Democratic Republic of the Congo   13.1    22.7
 Benin  17.2    23.0
 Turkey 23.5    23.4
 Mexico 8.2 23.7
 Niger  11.4    23.8
 Zambia 17.5    24.6
 Argentina  26.1    24.7
 Fiji   21.1    25.0
 Nicaragua  18.0    25.0
 Equatorial Guinea  0.9 25.5
 Tanzania   14.8    25.5
 Suriname   21.1    25.6
 Bahrain    4.8 25.7
 Mauritius  19.0    25.8
 Congo  5.3 26.0
 Gambia 19.2    26.0
 Malaysia   15.3    26.3
 United Arab Emirates   1.8 26.4
 Vanuatu    19.7    26.4
 Colombia   19.3    26.5
 Senegal    18.3    26.6
 Rwanda 13.5    26.7
 Kazakhstan 27.7    26.8
 Qatar  4.9 27.0
 Comoros    10.8    27.2
 India  18.6    27.2
 Tunisia    22.4    27.3
 South Africa   25.7    27.4
 Tajikistan 18.7    27.5
 Mozambique 14.2    28.0
 Uruguay    17.9    28.0
 Belize 22.7    28.2
 Iran   6.1 28.3
 Trinidad and Tobago    19.4    28.4
 Vietnam    23.6    28.8
 Namibia    24.8    29.0
 Morocco    26.9    29.1
 Saudi Arabia   6.6 29.1
 Kyrgyzstan 23.3    29.3
 Mauritania 13.4    29.5
 Tonga  25.7    29.9
 Nigeria    5.9 30.0
 South Korea    26.6    30.0
 Kenya  20.9    30.1
 Saint Lucia    27.5    30.9
 Azerbaijan 17.7    31.1
 Cape Verde 20.6    31.1
 Uzbekistan 19.6    31.1
 Kuwait 1.5 31.8
 Switzerland    29.4    32.0
 Albania    24.3    32.3
 Oman   3.0 32.6
 Samoa  23.0    32.7
 São Tomé and Príncipe  16.1    32.9
 Liberia    28.6    33.4
 Swaziland  36.0    33.7
 Egypt  15.4    34.0
 Venezuela  13.6    34.0
 Russia 34.1    34.1
 Saint Vincent and the Grenadines   25.6    34.1
 Lebanon    16.6    34.2
 Australia  30.8    34.3
 Jamaica    26.0    34.3
 Macedonia  28.3    34.5
 Bhutan 9.0 34.6
 Bolivia    28.5    34.8
 Slovakia   29.3    34.8
 Papua New Guinea   26.6    35.0
 Algeria    8.0 35.4
 Jordan 18.3    36.1
 Georgia    24.9    36.4
 Japan  28.3    37.1
 Luxembourg 36.5    37.2
 Bulgaria   33.3    37.3
 Lithuania  30.6    37.4
 Romania    28.5    37.6
 Malawi 16.5    38.0
 Latvia 29.1    38.5
 Guinea-Bissau  10.2    38.8
 United States  26.9    38.9
 Canada 32.2    39.7
 Seychelles 28.1    39.8
 Estonia    32.3    39.9
 Burundi    18.0    40.0
 Botswana   30.2    40.2
 Norway 42.1    40.2
 Djibouti   22.7    40.6
 Croatia    23.3    40.7
 Ecuador    16.0    40.8
 Brazil 34.4    41.0
 Mongolia   30.8    41.0
 New Zealand    34.5    41.1
 Spain  33.9    41.1
 Barbados   32.9    41.3
 Angola 6.1 41.6
 Moldova    33.4    41.6
 Ireland    30.8    42.0
 Ghana  20.6    42.4
 Dominica   30.4    42.5
 Cyprus 39.2    42.6
 Czech Republic 36.2    42.9
 Israel 33.5    42.9
 Libya  3.4 43.0
 Yemen  7.3 43.0
 Poland 34.9    43.3
 Germany    40.6    43.7
 Serbia 36.3    44.0
 Slovenia   37.6    44.3
 Malta  36.0    44.8
 Netherlands    39.8    45.9
 Portugal   37.7    46.1
 Greece 35.1    46.8
 Solomon Islands    24.1    47.3
 Ukraine    37.7    47.3
 United Kingdom 38.9    47.3
 Guyana 20.2    48.6
 Italy  43.1    48.8
 Montenegro 30.0    48.8
 Austria    42.9    49.0
 Hungary    40.5    49.2
 Finland    43.2    49.5
 Belarus    30.4    49.6
 Belgium    46.5    50.0
 Bosnia and Herzegovina 37.6    50.3
 Lesotho    63.1    51.2
 Denmark    49.0    51.8
 Sweden 47.9    52.5
 France 44.6    52.8
 Iceland    40.1    57.8
 Federated States of Micronesia 11.5    62.3
 Maldives   21.0    63.1
 Cuba   41.2    78.1
 Timor-Leste[11][12][13]    24.6    97.0
 Zimbabwe   31.7    97.8
 Kiribati[10]   39.0    114.6
'''

countries = '''\
Singapore
Turkey
South Korea
Switzerland
Australia
Slovakia
Luxembourg
Bulgaria
Lithuania
Romania
Latvia
United States
Canada
Estonia
Norway
New Zealand
Spain
Ireland
Cyprus
Czech Republic
Israel
Poland
Germany
Slovenia
Malta
Netherlands
Portugal
Greece
United Kingdom
Italy
Austria
Hungary
Finland
Belarus
Belgium
Denmark
Sweden
France
Iceland'''


lines = [ell.strip() for ell in data.split('\n') if len(ell)]
data = []
for line in lines:
    tokens = line.split()
    data.append((
    	' '.join(tokens[:-2]),
    float(tokens[-2]),
    float(tokens[-1])))


countries = set(line.strip() for line in countries.split('\n') if line)
data = [d for d in data if d[0] in countries]
countries = np.array([c for c,_,_ in data])
Taxes = np.array([t for _,t,_ in data])
Expenditures = np.array([r for _,_,r in data])

def do_plot(series, countries, name):
    order = series.argsort()
    countries = countries[order]
    series.sort()
    [USpos], = np.where(countries == 'United States')
    plt.clf()
    plt.bar(np.arange(len(series)), series)
    plt.bar(USpos,series[USpos], color='r')
    for ci,c in enumerate(countries):
        plt.text(ci, 68, c, rotation='vertical')
    plt.ylim(0,74)
    plt.savefig('{}.pdf'.format(name))

do_plot(Expenditures, countries, 'expenditures')
do_plot(Taxes, countries, 'taxes')

