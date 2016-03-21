# Creating know.json

import ujson


# Schema for know.json
# uid, integer
# title, string
# agency, string
# rank, integer
# url, string
# describe, string
# problem, list of strings
# delivery, list of string
# geography, list of strings
# time, list of strings
# refresh, list of string

def add_dataset(title, 
                agency, 
                url, 
                describe, 
                problem, 
                delivery, 
                geography, 
                time, 
                refresh,
                uid,
                rank
                ):
    return {
        'uid': uid,
        'title': title,
        'agency': agency,
        'rank': rank,
        'url': url,
        'describe': describe,
        'problem': problem,
        'delivery': delivery,
        'geography': geography,
        'time': time,
        'refresh': refresh
    }

# with open('know.json', 'rb') as f:
#     know = ujson.load(f)
know = []

# Commodity Flow Survey
title = 'Commodity Flow Survey'
agency = 'census'
url = 'http://www.census.gov/econ/cfs/pums.html'
describe = u'The first generation 2012 Commodity Flow Survey (CFS) Public Use Microdata (PUM) file is now available. This new, experimental data product contains information for approximately 4.5 million shipments obtained from businesses included in the 2012 CFS. The PUM file provides access to shipment-level characteristics while continuing to protect the confidentiality of individual business information. PUM file users can create customized tables and build models to track and analyze the movement of commodities.'
problem = ['network analysis']
delivery = ['bulk']
geography = ['tabulation areas']
time = ['quarter']
refresh = ['cross section']
know.append(add_dataset(title, agency, url, describe, problem, delivery, geography, time, refresh, uid = 1, rank = 1))

# ACS
title = 'American Community Survey'
agency = 'census'
url = 'https://www.census.gov/data/developers/data-sets/acs-survey-5-year-data.html'
describe = u'The American Community Survey (ACS) is an ongoing survey that provides data every year -- giving communities the current information they need to plan investments and services. The ACS covers a broad range of topics about social, economic, demographic, and housing characteristics of the U.S. population. Much of the ACS data provided on the Census Bureau\'s Web site are available separately by age group, race, Hispanic origin, and sex. The 5-year estimates from the ACS are "period" estimates that represent data collected over a period of time. The primary advantage of using multiyear estimates is the increased statistical reliability of the data for less populated areas and small population subgroups.'
problem = ['time series', 'classification', 'prediction', 'resolution']
delivery = ['bulk', 'api']
geography = ['block group', 'tract', 'county', 'msa', ' state', 'national']
time = ['five year averages']
refresh = ['annual']
know.append(add_dataset(title, agency, url, describe, problem, delivery, geography, time, refresh, uid = 2, rank = 2))

# Business Dynamics
title = 'Business Dynamics'
agency = 'census'
url = 'https://www.census.gov/data/developers/data-sets/business-dynamics.html'
describe = u'The Business Dynamics Statistics (BDS) includes measures of establishment openings and closings, firm startups, job creation and destruction by firm size, age, and industrial sector, and several other statistics on business dynamics. The U.S. economy is comprised of over 6 million establishments with paid employees. The population of these businesses is constantly churning - some businesses grow, others decline and yet others close. New businesses are constantly replenishing this pool. The BDS series provide annual statistics on gross job gains and losses for the entire economy and by industrial sector and state. This data track changes in employment at the establishment level, and thus provide a picture of the dynamics underlying aggregate net employment growth.'
problem = ['time series', 'prediction', 'classification']
delivery = ['api']
geography = ['msa', 'state', 'national']
time = ['annual']
refresh = ['annual']
know.append(add_dataset(title, agency, url, describe, problem, delivery, geography, time, refresh, uid = 3, rank = 3))

# Economic Indicators
title = 'Economic Indicators'
agency = 'census'
url = 'https://www.census.gov/data/developers/data-sets/economic-indicators.html'
describe = u'The U.S. Census Bureau\'s economic indicator surveys provide monthly and quarterly data that are timely, reliable, and offer comprehensive measures of the U.S. economy. These surveys produce a variety of statistics covering construction, housing, international trade, retail trade, wholesale trade, services and manufacturing. The survey data provide measures of economic activity that allow analysis of economic performance and inform business investment and policy decisions.'
problem = ['time series', 'prediction', 'resolution']
delivery = ['api']
geography = ['msa', 'state', 'national']
time = ['monthly', 'quarterly']
refresh = ['monthly', 'quarterly']
know.append(add_dataset(title, agency, url, describe, problem, delivery, geography, time, refresh, uid = 4, rank = 4))

# Climate Data Online
title = 'Climate Data Online'
agency = 'noaa'
url = 'https://www.ncdc.noaa.gov/cdo-web/webservices'
describe = u'Climate Data Online (CDO) provides free access to NCDC\'s archive of global historical weather and climate data in addition to station history information. These data include quality controlled daily, monthly, seasonal, and yearly measurements of temperature, precipitation, wind, and degree days as well as radar data and 30-year Climate Normals.'
problem = ['prediction', 'resolution']
delivery = ['api']
geography = ['point']
time = ['minute','hourly','daily','monthly','annual']
refresh = ['minute','hourly','daily','monthly','annual']
know.append(add_dataset(title, agency, url, describe, problem, delivery, geography, time, refresh, uid = 5, rank = 5))

# Severe Weather Data Inventory
title = 'Severe Weather Data Inventory'
agency = 'noaa'
url = 'https://www.ncdc.noaa.gov/swdi/'
describe = u'The Severe Weather Data Inventory (SWDI) is an integrated database of severe weather records, such as hail and tornados. SWDI enables a user to search through a variety of source data sets in the NCDC (now NCEI) archive in order to find records covering a particular time period and geographic region, and then to download the results of the search in a variety of formats. The formats currently supported are Shapefile (for GIS), KMZ (for Google Earth), CSV (comma-separated), and XML. The current data layers in SWDI are: Storm Cells from NEXRAD (Level-III Storm Structure Product); Hail Signatures from NEXRAD (Level-III Hail Product); Mesocyclone Signatures from NEXRAD (Level-III Meso Product); Digital Mesocyclone Detection Algorithm from NEXRAD (Level-III MDA Product); Tornado Signature from NEXRAD (Level-III TVS Product); Preliminary Local Storm Reports from the NOAA National Weather Service; Lightning Strikes from Vaisala NLDN.'
problem = ['risk', 'climatology']
delivery = ['api', 'bulk']
geography = ['point']
time = ['minute']
refresh = ['monthly']
know.append(add_dataset(title, agency, url, describe, problem, delivery, geography, time, refresh, uid = 6, rank = 6))

# VIIRS Monthly Imagery Composites
title = 'VIIRS Monthly Imagery Composites'
agency = 'noaa'
url = 'http://ngdc.noaa.gov/eog/viirs/download_monthly.html'
describe = u'VIIRS, a scanning radiometer, collects visible and infrared imagery and radiometric measurements of the land, atmosphere, cryosphere, and oceans. VIIRS data is used to measure cloud and aerosol properties, ocean color, sea and land surface temperature, ice motion and temperature, fires, and Earth\'s albedo. Climatologists use VIIRS data to improve our understanding of global climate change.'
problem = ['processing', 'prediction']
delivery = ['bulk']
geography = ['pixel']
time = ['daily','monthly']
refresh = ['quarterly']
know.append(add_dataset(title, agency, url, describe, problem, delivery, geography, time, refresh, uid = 7, rank = 7))

# VIIRS Combustion Sources
title = 'VIIRS Combustion Sources'
agency = 'noaa'
url = 'http://ngdc.noaa.gov/eog/viirs/download_viirs_fire.html'
describe = u'VIIRS is unique in the recording of near-infrared and short-wave infrared data at night. This includes the M7, M8, and M10 spectral bands. With sunlight eliminated, combustion sources are readily detected, particularly in the M10 band. The recorded signal can be fully attributed to the combustion source. In our analysis we use data from all of the VIIRS bands collecting data at night. The M10 band data are used to detect combustion sources. To eliminate noise, confirmation is sought in the Day/Night Band (DNB), M7, M8 and M12. Plank curve fitting is performed to estimate the temperature of background and heat source. Results are distributed in form of CSV files and KMZ files. The KMZ has data from the local maxima detected in the M10 band. Filtering is used to eliminate the bow tie effects from the identification of local maxima. The CSV has data from all of the pixels with radiances above background noise in the M10 band. Atmospheric correction is performed with MODTRAN parameterized with temperature and moisture profiles processed from the simultaneously acquired CrIS and ATMS sensors. Readme file is also available in case of situations out of BAU. Note that the processing algorithms have been evolving over time. Once the processing algorithms are stabilized we will reprocess the 2012 archive. '
problem = ['processing', 'prediction', 'detection']
delivery = ['bulk']
geography = ['point']
time = ['monthly']
refresh = ['monthly']
know.append(add_dataset(title, agency, url, describe, problem, delivery, geography, time, refresh, uid = 8, rank = 8))

# Market Research Library
title = 'Market Research Library'
agency = 'ita'
url = 'http://developer.trade.gov/market-research-library.html'
describe = u'The Market Research Library API provides metadata for country and industry reports that are produced by ITA\'s trade experts and are available in ITA\'s online market research library. ITA commercial officers that are stationed around the world, publish these authoritative reports in conjunction with Foreign Service officers from the State Department.'
problem = ['metadata', 'prediction', 'detection']
delivery = ['api']
geography = ['country']
time = ['unspecified']
refresh = ['unspecified']
know.append(add_dataset(title, agency, url, describe, problem, delivery, geography, time, refresh, uid = 9, rank = 9))

# Consolidated Screening List for Export Controls
title = 'Consolidated Screening List for Export Controls'
agency = 'ita'
url = 'http://developer.trade.gov/consolidated-screening-list.html'
describe = u'The Consolidated Screening List API consolidates eleven export screening lists of the Departments of Commerce, State and the Treasury into a single data feed as an aid to industry in conducting electronic screens of potential parties to regulated transactions.'
problem = ['risk', 'detection']
delivery = ['api']
geography = ['entity']
time = ['sporadic']
refresh = ['unspecified']
know.append(add_dataset(title, agency, url, describe, problem, delivery, geography, time, refresh, uid = 10, rank = 10))

# Current Population Survey
title = 'Current Population Survey'
agency = 'census'
url = 'http://thedataweb.rm.census.gov/ftp/cps_ftp.html'
describe = u'The Current Population Survey (CPS) is one of the oldest, largest, and most well-recognized surveys in the United States. It is immensely important, providing information on many of the things that define us as individuals and as a society - our work, our earnings, and our education. In addition to being the primary source of monthly labor force statistics, the CPS is used to collect data for a variety of other studies that keep the nation informed of the economic and social well-being of its people. This is done by adding a set of supplemental questions to the monthly basic CPS questions. Supplemental inquiries vary month to month and cover a wide variety of topics such as child support, volunteerism, health insurance coverage, and school enrollment. Supplements are usually conducted annually or biannually, but the frequency and recurrence of a supplement depend completely on what best meets the needs of the supplement\'s sponsor.'
problem = ['prediction', 'resolution']
delivery = ['bulk']
geography = ['tabulation areas']
time = ['monthly']
refresh = ['monthly']
know.append(add_dataset(title, agency, url, describe, problem, delivery, geography, time, refresh, uid = 11, rank = 11))

# Foreign Trade Balance by Country
title = 'Foreign Trade Balance by Country'
agency = 'census'
url = 'http://www.census.gov/foreign-trade/balance/index.html'
describe = u'To provide detailed statistics on goods and estimates of services shipped from the U.S. to foreign countries. The United States Code, Title 13, requires this program. Participation is mandatory. The Treasury Department assists in the conduct of this program. The export statistics consist of goods valued at more than $2,500 per commodity shipped by individuals and organizations (including exporters, freight forwarders, and carriers) from the U.S. to other countries. Data is compiled in terms of commodity classification, quantities, values, shipping weights, method of transportation (air or vessel), state of (movement) origin, customs district, customs port, country of destination, and whether contents are domestic goods or re-exports. Since January 1989, commodities have been compiled under Schedule B harmonized classifications of domestic and foreign commodity exports. These transactions are classified under approximately 8,000 different products leaving the United States. Statistics are also complied under the Standard International Trade Classification (SITC), North American Industry Classification System (NAICS), End-Use Commodity Classification, and Advanced Technology Products. These statistics include data about all 240 U.S. trading partners, 400 U.S. ports, and 45 districts. Among these statistics it total of import and export value by month by US trade partners for 20+ years.'
problem = ['network analysis', 'resolution']
delivery = ['bulk']
geography = ['country']
time = ['monthly']
refresh = ['panel']
know.append(add_dataset(title, agency, url, describe, problem, delivery, geography, time, refresh, uid = 12, rank = 12))

# BEA API
title = 'BEA API'
agency = 'bea'
url = 'http://www.bea.gov/API/signup/index.cfm'
describe = u'API provides programmatic access to BEA published economic statistics using industry-standard methods and procedures. BEA\'s data API includes methods for retrieving a subset of our statistical data and the metadata that describes it. Data series include GDP, Personal Income, Employment, Interest Rates, among other key economic indicators across county, state, and national levels.'
problem = ['prediction', 'resolution', 'classification']
delivery = ['api', 'bulk']
geography = ['state', 'msa', 'national']
time = ['monthly', 'quarterly', 'annual']
refresh = ['panel']
know.append(add_dataset(title, agency, url, describe, problem, delivery, geography, time, refresh, uid = 13, rank = 13))

# Survey of Business Owners
title = 'Survey of Business Owners'
agency = 'census'
url = 'http://www.census.gov/econ/sbo/getdata.html'
describe = u'The Survey of Business Owners (SBO) provides the only comprehensive, regularly collected source of information on selected economic and demographic characteristics for businesses and business owners by gender, ethnicity, race, and veteran status. Title 13 of the United States Code authorizes this survey and provides for mandatory responses. Included are all nonfarm businesses filing Internal Revenue Service tax forms as individual proprietorships, partnerships, or any type of corporation, and with receipts of $1,000 or more. The SBO covers both firms with paid employees and firms with no paid employees. The SBO is conducted on a company or firm basis rather than an establishment basis. A company or firm is a business consisting of one or more domestic establishments that the reporting firm specified under its ownership or control. Estimates include the number of employer and nonemployer firms, sales and receipts, annual payroll, and employment. Data aggregates are presented by gender, ethnicity, race, and veteran status for the United States by 2012 North American Industry Classification System (NAICS), states, metropolitan and micropolitan statistical areas, counties, places, and employment and receipts size. The first-ever Survey of Business Owners Public Use Microdata Sample is now available. The SBO PUMS was created using responses from the 2007 SBO and provides access to survey data at a level of detail below that of the currently published SBO results. The SBO PUMS will allow researchers to create customized tables and models and to study entrepreneurial activity and the relationships between business characteristics such as access to capital, firm size, employer-paid benefits, minority- and women-ownership, and firm age.'
problem = ['prediction', 'resolution']
delivery = ['bulk']
geography = ['tabulation areas']
time = ['annual']
refresh = ['annual']
know.append(add_dataset(title, agency, url, describe, problem, delivery, geography, time, refresh, uid = 14, rank = 14))

# Survey of Income and Program Participation
title = 'Survey of Income and Program Participation'
agency = 'census'
url = 'http://thedataweb.rm.census.gov/ftp/sipp_ftp.html'
describe = u'The Survey of Income and Program Participation (SIPP) is a household-based survey designed as a continuous series of national panels. Each panel features a nationally representative sample interviewed over a multi-year period lasting approximately four years. SIPP is a source of data for a variety of topics and provides for the integration of information for separate topics to form a single, unified database. This allows for the examination of the interaction between tax, transfer, and other government and private policies. Government policy formulators depend heavily upon SIPP for information on the distribution of income and the success of government assistance programs. SIPP collects information for assistance received either directly as money or indirectly as in-kind benefits. SIPP data provide the most extensive information available on how the nation\'s economic well-being changes over time, which has been SIPP\'s defining characteristic since its inception in 1983.'
problem = ['prediction', 'resolution']
delivery = ['bulk']
geography = ['state']
time = ['quarterly']
refresh = ['panel']
know.append(add_dataset(title, agency, url, describe, problem, delivery, geography, time, refresh, uid = 15, rank = 15))

with open('know.json', 'wb') as f:
    ujson.dump({ 'data': know }, f)
