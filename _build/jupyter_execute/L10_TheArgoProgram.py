#!/usr/bin/env python
# coding: utf-8

# #  The Argo data
# 
# <img src="https://raw.githubusercontent.com/euroargodev/argoonlineschool/master/images/logoArgo.png" alt="Argo status" width="100"/>

# Argo is a  broad-scale global array of profiling floats that measure temperature and salinity versus pressure. Argo is the major component of the ocean observing system. This is the actual distribution o the Argo array
# 
# <img src="http://sio-argo.ucsd.edu/statusbig.gif" alt="Argo status" width="800"/>
# 

# The objectives of Argo are:
# 
# - Provide a quantitative description of the changing state of the upper ocean and the patterns of ocean climate variability from months to decades, including heat and freshwater storage and transport.
# - Enhance the value of the Jason altimeter through measurement of subsurface temperature, salinity, and velocity, with sufficient coverage and resolution to permit interpretation of altimetric sea surface height variability.
# - Allow the initializing of ocean and coupled ocean-atmosphere forecast models, for data assimilation and for model testing.
# - Document seasonal to decadal climate variability and to aid our understanding of its predictability. A wide range of applications for high-quality global ocean analyses is anticipated.

# **Why is it called Argo?**
# 
# This questions is always in the mind of anyone than hears for the first time about the Argo program, therefore it is important to explain it. In Greek mythology, Argo was the ship in which Jason and the Argonauts sail to search for the golden fleece. In an analogus way, Argo floats sail the sea and complement the observations from the satellite called JASON-1, that measures the shape of the ocean surface.  Data from Argo and JASON-1 together will monitor the ocean currents, the oceans' transport of heat and freshwater around the globe and sea-level rise. 
# 
# Additionally, at the developing phase of the Argo network in 1998, a document prepared by Dean Roemmich of Scripps Institution of Oceanography, and entitled "A Proposal for Global Ocean Observations for Climate: the Array for Real-time Geostrophic Oceanography" explored the potential of using profiling floats to monitor the ocean, ... 
# 
# More information in the web page of the [Argo Steering Team](http://www.argo.ucsd.edu/index.html)

# **The WMO: a unique identifiers for each float**
# 
# Each one of the Argo floats have a unique indentifier, kwnon as the World Meteorological Organization (WMO). The WMO is assigned at the moment of the deployment of the float, but it is not hard-coded in the float.

# **The basis of the Argo Data System**
# 
# When an Argo float surfaces, the data are received by one of the *Data Assembly Centers* (DAC). At the DACs, they are subjected to initial scrutiny using a set of real time quality control tests where erroneous data are flagged or corrected, then the data are passed to one of the two Argo *Global Data Assembly Center* (GDAC), the Coriolis GDAC (Brest, France, Europe) or the US-Godae GDAC (Mobterey, California, USA). 
# 
# The GDACs are the first stage at which the freely available data can be obtained via the internet. The GDACs synchronize their data holdings to ensure consistent data is available on both sites. The target is for these *real-time* data to be available within 24 hours of their transmission from the float.

# Additionally Argo data can be accesed by several other ways:
# 
# - via the Global Telecomunication System for operational centers. 
# - via interactive Data selection tools on the GDACs
# - via gridded fields and velocity products based on Argo NetCDF files from the GDACs
# - via data viewers that incorporate Argo data
# - via the [Global Argo Data Repository (GADR)](https://www.nodc.noaa.gov/argo/) for archived and offline data
# - via monthly copies of the GDACs https://www.seanoe.org/data/00311/42182/
# 
# See the [Argo data sources](https://argo.ucsd.edu/data/) to read a full description, with links, to this other ways of accesing the data
# 
# **However, in this book we focus in the accesss to the primary source of the Argo data, the GDACs**

# **The netCDF format**
# 
# At the early stage of the Argo program, and due to the huge ammount of data that was foressen  Argo would create, it was decided that netCDF would be the offical file format for the Argo data. In the next section we give an introduction to the properties of this data format, and how to read files in netCDF.
