# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--23_01:04:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **295,341 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moragaswewa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 01:04:07 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-10-23 01:03:52 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-10-23 01:03:29 | Moragaswewa (Deduru Oya) | 5.23 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-10-23 01:03:15 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.094 |  |
| 2026-10-23 01:03:06 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-10-23 01:02:50 | Rathnapura (Kalu Ganga) | 4.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 01:02:47 | Kithulgala (Kelani Ganga) | 2.21 | 🟢 Normal | -0.021 |  |
| 2026-10-23 01:02:31 | Panadugama (Nilwala Ganga) | 4.74 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-23 01:02:09 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 0.000 |  |
| 2026-10-23 01:02:06 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-23 01:01:57 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-10-23 01:01:56 | Giriulla (Maha Oya) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-10-23 01:01:52 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-23 01:01:29 | Hanwella (Kelani Ganga) | 4.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-23 01:01:26 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-23 01:01:10 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-23 01:00:43 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.125 |  |
| 2026-10-23 01:00:34 | Horowpothana (Yan Oya) | 3.01 | 🟢 Normal | -0.010 |  |
| 2026-10-23 01:00:17 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-23 01:00:13 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 01:03:29 | Moragaswewa (Deduru Oya) | 5.23 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-10-23 00:07:50 | Putupaula (Kalu Ganga) | 1.90 | 🟢 Normal | 0.924 | 🔺 Rising |
| 2026-10-23 00:06:30 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-23 01:02:31 | Panadugama (Nilwala Ganga) | 4.74 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-23 00:07:40 | Badalgama (Maha Oya) | 3.63 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-23 00:07:11 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-23 00:00:44 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-22 18:02:23 | Thanthirimale (Malwathu Oya) | 2.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 23:08:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.84 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-23 01:00:17 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 18:02:35 | Galgamuwa (Mee Oya) | 2.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-23 00:07:42 | Baddegama (Gin Ganga) | 2.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-23 01:01:29 | Hanwella (Kelani Ganga) | 4.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-23 01:02:50 | Rathnapura (Kalu Ganga) | 4.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 00:06:05 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 01:01:26 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-23 01:02:09 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 0.000 |  |
| 2026-10-23 01:01:57 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-10-23 00:03:23 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-23 01:01:10 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-23 01:01:52 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-23 01:02:06 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-23 01:00:34 | Horowpothana (Yan Oya) | 3.01 | 🟢 Normal | -0.010 |  |
| 2026-10-23 01:01:56 | Giriulla (Maha Oya) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-10-23 01:03:06 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-10-23 01:00:13 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-10-23 01:03:52 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-10-23 01:04:07 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-10-23 01:02:47 | Kithulgala (Kelani Ganga) | 2.21 | 🟢 Normal | -0.021 |  |
| 2026-10-23 00:07:00 | Urawa (Nilwala Ganga) | 1.19 | 🟢 Normal | -0.022 |  |
| 2026-10-23 00:02:29 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.030 |  |
| 2026-10-23 00:04:29 | Glencourse (Kelani Ganga) | 12.38 | 🟢 Normal | -0.030 |  |
| 2026-10-23 00:16:07 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | -0.034 |  |
| 2026-10-23 00:07:41 | Holombuwa (Kelani Ganga) | 1.59 | 🟢 Normal | -0.037 |  |
| 2026-10-22 18:01:15 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.070 |  |
| 2026-10-23 01:03:15 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.094 |  |
| 2026-10-23 00:05:51 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.099 |  |
| 2026-10-23 01:00:43 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.125 |  |
| 2026-10-23 00:03:20 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.493 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)