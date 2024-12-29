## Projet Python pour la Data Science 

Authors : Audrey BOVET and Eve SAMANI

# Table of contents
1. [Subject](#subject)
2. [Motivations](#motivations)
3. [Data used](#sources)
4. [Présentation du dépôt](#pres)
5. [Licence](#licence)



# Subject <a name="subject">

Predicting the evolution of the 'Atlantic puffin' population in time and space according to different global warming scenarios. 
![puffin](https://islande24.fr/wp-content/uploads/2018/11/shutterstock_403375483.jpg)

# Motivations <a name="motivations">

The 'Atlantic puffin' ('macareux moine' in French) is a small seabird from North Atlantic Ocean which breeds in large colonies on costal cliffs or offshore islands, especially in Russia, Iceland, Ireland, British, Norway and the Faore Islands. Climate change and the increase of the sea surface temperature (SST) lead to difficulties to feed themselves during the breeding season. Today, puffins are declared a vulnerable species (IUCN RedList) because of the decreasing of the population. 
We have therefore attempted to predict the evolution of this species' population according to the different climate scenarios envisaged by the CMIP6 (Coupled model intercomparison project) : 
- SSP 5.8-5 (most pessimistic)
- SSP 2.4-5 (intermediate scenario)
- SSP 1.2-6 (most optimistic)

# Data used <a name="sources">
* [CMIP6 climate projections](https://cds.climate.copernicus.eu/datasets/projections-cmip6?tab=overview), database available with Copernicus, composed of historical and predictive data, for several scenarios, several models and several variables (we will focus on the 'SST' (sea surface temperature) variable only).
* [Atlantic puffin data](https://onlinelibrary.wiley.com/doi/10.1111/gcb.15665), based on _"Centennial relationships between ocean temperature and Atlantic puffin production reveal shifting decennial trends", Erpur S. Hansen and ali, Global Change Biology, August 2021_.
* [eBird](https://ebird.org/data/download), online database providing scientists and birdwatchers with real-time information on bird abundance and distribution. 

### Chick Production in Seabirds and Its Estimation

Chick production refers to the number of chicks that are successfully fledged (raised to independence) by a given seabird population in a specific year. This metric is vital for understanding how environmental changes, such as global warming, affect population dynamics in seabirds like the Atlantic puffin (*Fratercula arctica*). Factors such as climate variability, food availability, and the survival rates of adult birds all influence chick production (Hansen et al., 2021).

#### Formula for Estimating Chick Production

In their study, Hansen et al. (2021) estimate chick production $P_t$ in year $t$ using the following formula:

$
P_t = C \times \sum_{a} \left( p_a \times H_t \times \frac{1}{\phi^a} \right)
$

Where:
- $P_t$ is the chick production in year $t$.
- $C$ is a constant scaling factor to normalize the data.
- $p_a$ is the proportion of harvested birds in age class $a$.
- $H_t$ is the total harvest in year $t$.
- $\phi$ represents the annual survival rate of adults, which accounts for mortality over time.
- $a$ refers to the age class of the harvested birds.

This formula is a function of both the harvest data and the age structure of the harvested birds, which is inferred from long-term ringed bird data collected from harvested puffins (Hansen et al., 2021). The values of $p_a$ are based on the age distribution of harvested birds, with most being between 2 and 6 years old.

#### Steps in Calculation:
1. **Age Structure of Harvested Birds:** The proportion of birds in each age class $p_a$ is determined from ringed bird data. The majority of harvested birds are between 2 and 6 years old (Hansen et al., 2021).
2. **Adjusting for Survival:** The formula adjusts for adult mortality using the survival rate $phi$ to ensure the calculation reflects the true number of fledged chicks, not overrepresenting younger or less-surviving age classes.
3. **Scaling the Index:** The chick production index is scaled by the constant $C = 22,147^{-1}$, which ensures the index is normalized between 1 and 10 for consistency over time.

#### Harvesting Puffins history

The harvesting of puffins, particularly on the Westman Islands, has been a long-standing tradition, with records dating back to the 9th century. Historically, puffins were hunted for their meat and feathers, with the harvest reaching significant levels, especially during the 19th and 20th centuries. According to Hansen et al. (2021), harvesting on these islands continued until 2010, with the method of capture evolving over time. In the early years, hunters used pole nets, which became the primary method of harvesting from 1876 onwards. The harvest took place in a limited number of locations within each colony, and harvest effort was determined by the number of days the hunt occurred within the legal harvest season, which typically spanned around 30 to 45 days per year.

The data on puffin harvests from this region, covering more than a century, have been crucial for estimating chick production, as they allow researchers to infer the number of offspring produced each year based on the number of harvested birds. Since most of the birds harvested were immature, the harvest records serve as a proxy for estimating the relative production of chicks within the population. However, it is important to note that the harvest data do not provide an exact measure of population size, and they must be adjusted for variations in harvest effort and changes in the harvest season over time (Hansen et al., 2021). The use of these harvest records, alongside survival rates and age structure data, allows for the construction of a chick production index, which tracks long-term demographic trends in puffin populations.

#### Interpretation of the Chick Production Index:

The chick production index is a proxy for the relative number of chicks successfully fledged in a given year. While it does not provide the absolute cohort size, it is a useful tool for tracking long-term trends in chick production. It helps researchers assess the influence of environmental factors, such as temperature changes, on puffin reproduction (Hansen et al., 2021). 

#### Log Transformation:

For statistical analysis, the chick production index is typically log-transformed to normalize the data, especially for long-term trends. However, the untransformed index is often presented in graphs for easier interpretation. On the untransformed scale, an index value of 0 indicates no chick production, and higher values correspond to greater fledgling success.

### Conclusion:

The chick production index, as described by Hansen et al. (2021), provides a valuable measure of reproductive success in seabird populations like the Atlantic puffin. It enables researchers to analyze the long-term demographic trends of these populations, helping to assess the impact of climate change and other environmental factors on species that may be difficult to monitor through direct population estimates.

### Sources:
Hansen, E.S., Sandvik, H., Erikstad, K.E., Yoccoz, N.G., Anker-Nilssen, T., Bader, J., Descamps, S., Hodges, K., Mesquita, M.d.S., Reiertsen, T.K. & Varpe, Ø. (2021). Centennial relationships between ocean temperature and Atlantic puffin production reveal shifting decennial trends. *Global Change Biology*, 27, 3753-3764. [https://doi.org/10.1111/gcb.15665](https://doi.org/10.1111/gcb.15665)



