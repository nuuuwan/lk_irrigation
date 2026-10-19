# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_18:15:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,396 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 18:15:34 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | -0.018 |  |
| 2026-10-19 18:08:39 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:08:34 | Baddegama (Gin Ganga) | 2.39 | 🟢 Normal | -0.031 |  |
| 2026-10-19 18:08:00 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-19 18:06:23 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.010 |  |
| 2026-10-19 18:06:02 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:05:55 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-19 18:05:29 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-19 18:05:27 | Ellagawa (Kalu Ganga) | 6.74 | 🟢 Normal | -0.069 |  |
| 2026-10-19 18:05:05 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.019 |  |
| 2026-10-19 18:04:45 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 18:04:22 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:04:21 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.070 |  |
| 2026-10-19 18:03:58 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-10-19 18:03:43 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-10-19 18:03:27 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:03:20 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:03:06 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-19 18:02:55 | Urawa (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-10-19 18:02:54 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | -0.011 |  |
| 2026-10-19 18:02:46 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | -0.021 |  |
| 2026-10-19 18:02:35 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-19 18:02:33 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | -0.070 |  |
| 2026-10-19 18:02:30 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-10-19 18:02:22 | Pitabeddara (Nilwala Ganga) | 1.61 | 🟢 Normal | -0.030 |  |
| 2026-10-19 18:02:22 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | -0.021 |  |
| 2026-10-19 18:02:17 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.040 |  |
| 2026-10-19 18:02:15 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-19 18:01:58 | Putupaula (Kalu Ganga) | 1.32 | 🟢 Normal | -0.032 |  |
| 2026-10-19 18:01:56 | Moragaswewa (Deduru Oya) | 1.44 | 🟢 Normal | -0.031 |  |
| 2026-10-19 18:01:39 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:01:36 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-10-19 18:01:33 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:01:32 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-19 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.070 |  |
| 2026-10-19 18:01:20 | Rathnapura (Kalu Ganga) | 2.66 | 🟢 Normal | -0.021 |  |
| 2026-10-19 18:00:13 | Thalgahagoda (Nilwala Ganga) | 1.88 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 18:00:13 | Thalgahagoda (Nilwala Ganga) | 1.88 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-19 17:14:58 | Panadugama (Nilwala Ganga) | 5.15 | 🟡 Alert | -0.026 |  |
| 2026-10-19 18:01:32 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-19 18:05:55 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-19 18:08:00 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-19 18:02:15 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-19 18:04:45 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 18:05:29 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-19 18:01:36 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-10-19 18:02:54 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:06:02 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:04:22 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:08:39 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:03:20 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:01:39 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:03:27 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:01:33 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:03:58 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-10-19 18:06:23 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.010 |  |
| 2026-10-19 18:02:30 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-10-19 18:03:06 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-19 18:03:43 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-10-19 18:02:35 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-19 18:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | -0.011 |  |
| 2026-10-19 18:02:55 | Urawa (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-10-19 18:15:34 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | -0.018 |  |
| 2026-10-19 18:05:05 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.019 |  |
| 2026-10-19 18:02:46 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | -0.021 |  |
| 2026-10-19 18:02:22 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | -0.021 |  |
| 2026-10-19 18:01:20 | Rathnapura (Kalu Ganga) | 2.66 | 🟢 Normal | -0.021 |  |
| 2026-10-19 18:02:22 | Pitabeddara (Nilwala Ganga) | 1.61 | 🟢 Normal | -0.030 |  |
| 2026-10-19 18:08:34 | Baddegama (Gin Ganga) | 2.39 | 🟢 Normal | -0.031 |  |
| 2026-10-19 18:01:56 | Moragaswewa (Deduru Oya) | 1.44 | 🟢 Normal | -0.031 |  |
| 2026-10-19 18:01:58 | Putupaula (Kalu Ganga) | 1.32 | 🟢 Normal | -0.032 |  |
| 2026-10-19 18:02:17 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.040 |  |
| 2026-10-19 18:05:27 | Ellagawa (Kalu Ganga) | 6.74 | 🟢 Normal | -0.069 |  |
| 2026-10-19 18:02:33 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | -0.070 |  |
| 2026-10-19 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.070 |  |
| 2026-10-19 18:04:21 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)