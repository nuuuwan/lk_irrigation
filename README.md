# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--26_01:17:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,772 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 01:17:18 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-26 01:11:24 | Rathnapura (Kalu Ganga) | 2.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-26 01:08:28 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-11-26 01:06:38 | Hanwella (Kelani Ganga) | 3.58 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-11-26 01:06:36 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-26 01:06:21 | Wellawaya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-11-26 01:05:20 | Holombuwa (Kelani Ganga) | 2.04 | 🟢 Normal | -0.267 |  |
| 2026-11-26 01:03:51 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | -0.010 |  |
| 2026-11-26 01:03:49 | Urawa (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.013 |  |
| 2026-11-26 01:03:39 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.069 |  |
| 2026-11-26 01:03:28 | Giriulla (Maha Oya) | 3.16 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2026-11-26 01:03:11 | Manampitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.031 |  |
| 2026-11-26 01:02:56 | Putupaula (Kalu Ganga) | 1.28 | 🟢 Normal | -0.032 |  |
| 2026-11-26 01:02:45 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | -0.033 |  |
| 2026-11-26 01:02:33 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-11-26 01:02:31 | Moragaswewa (Deduru Oya) | 2.28 | 🟢 Normal | 0.323 | 🔺 Rising |
| 2026-11-26 01:02:29 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-11-26 01:02:25 | Peradeniya (Mahaweli Ganga) | 4.90 | 🟢 Normal | -0.088 |  |
| 2026-11-26 01:02:24 | Dunamale (Aththanagalu Oya) | 3.70 | 🟡 Alert | 0.079 | 🔺 Rising |
| 2026-11-26 01:02:18 | Glencourse (Kelani Ganga) | 12.29 | 🟢 Normal | 0.000 |  |
| 2026-11-26 01:02:12 | Badalgama (Maha Oya) | 3.68 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-26 01:02:11 | Thanamalwila (Kirindi Oya) | 1.87 | 🟢 Normal | -0.030 |  |
| 2026-11-26 01:01:47 | Moraketiya (Walawe Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-11-26 01:01:39 | Ellagawa (Kalu Ganga) | 6.21 | 🟢 Normal | -0.035 |  |
| 2026-11-26 01:01:38 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-11-26 01:01:32 | Panadugama (Nilwala Ganga) | 4.17 | 🟢 Normal | -0.037 |  |
| 2026-11-26 01:00:31 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-11-26 01:00:23 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-26 01:00:07 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 01:02:24 | Dunamale (Aththanagalu Oya) | 3.70 | 🟡 Alert | 0.079 | 🔺 Rising |
| 2026-11-26 00:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.89 | 🟢 Normal | 254.618 | 🔺 Rising |
| 2026-11-26 00:03:55 | Yaka Wewa (Ma Oya) | 2.71 | 🟢 Normal | 79.560 | 🔺 Rising |
| 2026-11-25 20:05:34 | Magura (Kalu Ganga) | 3.40 | 🟢 Normal | 0.483 | 🔺 Rising |
| 2026-11-26 01:02:31 | Moragaswewa (Deduru Oya) | 2.28 | 🟢 Normal | 0.323 | 🔺 Rising |
| 2026-11-26 01:03:28 | Giriulla (Maha Oya) | 3.16 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2026-11-26 01:06:38 | Hanwella (Kelani Ganga) | 3.58 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-11-25 18:02:46 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-11-26 01:02:12 | Badalgama (Maha Oya) | 3.68 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-26 01:17:18 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-25 18:02:35 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-25 18:00:42 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-26 01:00:23 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-26 01:11:24 | Rathnapura (Kalu Ganga) | 2.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-26 01:00:07 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-26 01:06:36 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-26 00:02:48 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-26 01:02:18 | Glencourse (Kelani Ganga) | 12.29 | 🟢 Normal | 0.000 |  |
| 2026-11-26 01:01:38 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-11-26 01:03:51 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | -0.010 |  |
| 2026-11-26 01:06:21 | Wellawaya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-11-26 01:00:31 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-11-26 01:03:49 | Urawa (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.013 |  |
| 2026-11-26 00:18:09 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.015 |  |
| 2026-11-26 00:07:27 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | -0.019 |  |
| 2026-11-26 01:08:28 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-11-26 01:01:47 | Moraketiya (Walawe Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-11-26 01:02:29 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-11-26 01:02:33 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-26 01:02:11 | Thanamalwila (Kirindi Oya) | 1.87 | 🟢 Normal | -0.030 |  |
| 2026-11-26 01:03:11 | Manampitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.031 |  |
| 2026-11-26 01:02:56 | Putupaula (Kalu Ganga) | 1.28 | 🟢 Normal | -0.032 |  |
| 2026-11-26 01:02:45 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | -0.033 |  |
| 2026-11-26 01:01:39 | Ellagawa (Kalu Ganga) | 6.21 | 🟢 Normal | -0.035 |  |
| 2026-11-26 01:01:32 | Panadugama (Nilwala Ganga) | 4.17 | 🟢 Normal | -0.037 |  |
| 2026-11-26 01:03:39 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.069 |  |
| 2026-11-26 01:02:25 | Peradeniya (Mahaweli Ganga) | 4.90 | 🟢 Normal | -0.088 |  |
| 2026-11-26 01:05:20 | Holombuwa (Kelani Ganga) | 2.04 | 🟢 Normal | -0.267 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)