# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--26_05:02:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,883 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 05:02:44 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-26 05:02:22 | Dunamale (Aththanagalu Oya) | 3.92 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-11-26 05:02:20 | Glencourse (Kelani Ganga) | 11.87 | 🟢 Normal | -0.144 |  |
| 2026-11-26 05:02:17 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-11-26 05:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.674 | 🔺 Rising |
| 2026-11-26 05:02:07 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | -0.030 |  |
| 2026-11-26 05:02:07 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.097 |  |
| 2026-11-26 05:01:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-26 05:01:15 | Rathnapura (Kalu Ganga) | 2.46 | 🟢 Normal | -0.074 |  |
| 2026-11-26 05:00:55 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-26 05:00:40 | Moragaswewa (Deduru Oya) | 3.06 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-11-26 05:00:32 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.031 |  |
| 2026-11-26 05:00:28 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.040 |  |
| 2026-11-26 04:56:11 | Panadugama (Nilwala Ganga) | 4.06 | 🟢 Normal | -0.023 |  |
| 2026-11-26 04:36:12 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | -0.027 |  |
| 2026-11-26 04:20:53 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-26 04:18:19 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 05:02:22 | Dunamale (Aththanagalu Oya) | 3.92 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-11-26 04:05:36 | Baddegama (Gin Ganga) | 1.89 | 🟢 Normal | 0.704 | 🔺 Rising |
| 2026-11-26 05:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.674 | 🔺 Rising |
| 2026-11-25 20:05:34 | Magura (Kalu Ganga) | 3.40 | 🟢 Normal | 0.483 | 🔺 Rising |
| 2026-11-26 05:02:17 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-11-26 05:00:40 | Moragaswewa (Deduru Oya) | 3.06 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-11-25 18:02:46 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-11-26 04:03:06 | Badalgama (Maha Oya) | 4.02 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-11-26 04:02:24 | Giriulla (Maha Oya) | 3.70 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-25 18:02:35 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-26 05:00:55 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-25 18:00:42 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-26 04:03:31 | Hanwella (Kelani Ganga) | 3.89 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-26 04:06:05 | Katharagama (Menik Ganga) | 0.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-26 04:05:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.96 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-26 05:02:44 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-26 05:01:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-26 04:03:29 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-26 04:18:19 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.000 |  |
| 2026-11-26 04:20:53 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-26 04:04:55 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-26 04:06:30 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.009 |  |
| 2026-11-26 04:03:50 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.009 |  |
| 2026-11-26 04:02:32 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | -0.011 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-26 04:56:11 | Panadugama (Nilwala Ganga) | 4.06 | 🟢 Normal | -0.023 |  |
| 2026-11-26 04:36:12 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | -0.027 |  |
| 2026-11-26 05:02:07 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | -0.030 |  |
| 2026-11-26 05:00:32 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.031 |  |
| 2026-11-26 04:02:01 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.035 |  |
| 2026-11-26 04:03:08 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.040 |  |
| 2026-11-26 05:00:28 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.040 |  |
| 2026-11-26 04:08:49 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | -0.054 |  |
| 2026-11-26 05:01:15 | Rathnapura (Kalu Ganga) | 2.46 | 🟢 Normal | -0.074 |  |
| 2026-11-26 04:06:41 | Holombuwa (Kelani Ganga) | 1.55 | 🟢 Normal | -0.097 |  |
| 2026-11-26 05:02:07 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.097 |  |
| 2026-11-26 05:02:20 | Glencourse (Kelani Ganga) | 11.87 | 🟢 Normal | -0.144 |  |
| 2026-11-26 04:02:23 | Peradeniya (Mahaweli Ganga) | 3.54 | 🟢 Normal | -0.177 |  |
| 2026-11-26 03:08:47 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)