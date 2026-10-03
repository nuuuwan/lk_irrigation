# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--03_08:12:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **277,581 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🔴 Padiyathalawa — Major Flood
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 08:12:05 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | -0.019 |  |
| 2026-10-03 08:11:50 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.044 |  |
| 2026-10-03 08:10:28 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-03 08:09:50 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-03 08:09:39 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | -0.018 |  |
| 2026-10-03 08:09:35 | Glencourse (Kelani Ganga) | 10.69 | 🟢 Normal | -0.019 |  |
| 2026-10-03 08:09:31 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-03 08:08:18 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.009 |  |
| 2026-10-03 08:08:15 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-10-03 08:06:21 | Ellagawa (Kalu Ganga) | 6.54 | 🟢 Normal | -0.010 |  |
| 2026-10-03 08:06:18 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-03 08:05:48 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-03 08:05:47 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-03 08:05:27 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 08:05:10 | Pitabeddara (Nilwala Ganga) | 1.36 | 🟢 Normal | -0.031 |  |
| 2026-10-03 08:05:01 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.088 |  |
| 2026-10-03 08:04:44 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 08:02:27 | Padiyathalawa (Maduru Oya) | 8.00 | 🔴 Major Flood | 8.091 | 🔺 Rising |
| 2026-10-03 08:01:42 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-03 08:01:04 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-03 08:03:23 | Putupaula (Kalu Ganga) | 1.07 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-03 08:10:28 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-03 08:02:00 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 08:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 08:05:27 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 08:05:48 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-03 08:02:24 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-03 08:04:44 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-03 08:01:40 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-03 08:01:35 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 08:01:09 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-03 08:01:17 | Panadugama (Nilwala Ganga) | 4.48 | 🟢 Normal | 0.000 |  |
| 2026-10-03 08:05:47 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-03 08:09:31 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-03 08:06:18 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-03 08:09:50 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-03 08:08:18 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.009 |  |
| 2026-10-03 08:02:56 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | -0.010 |  |
| 2026-10-03 08:08:15 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-10-03 08:06:21 | Ellagawa (Kalu Ganga) | 6.54 | 🟢 Normal | -0.010 |  |
| 2026-10-03 08:01:37 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | -0.011 |  |
| 2026-10-03 08:00:58 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.012 |  |
| 2026-10-03 08:09:39 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | -0.018 |  |
| 2026-10-03 08:12:05 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | -0.019 |  |
| 2026-10-03 08:09:35 | Glencourse (Kelani Ganga) | 10.69 | 🟢 Normal | -0.019 |  |
| 2026-10-03 08:02:39 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-10-03 08:03:27 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.024 |  |
| 2026-10-03 08:05:10 | Pitabeddara (Nilwala Ganga) | 1.36 | 🟢 Normal | -0.031 |  |
| 2026-10-03 08:03:39 | Hanwella (Kelani Ganga) | 2.47 | 🟢 Normal | -0.040 |  |
| 2026-10-03 08:03:32 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.041 |  |
| 2026-10-03 08:11:50 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.044 |  |
| 2026-10-03 08:03:50 | Thawalama (Gin Ganga) | 2.36 | 🟢 Normal | -0.051 |  |
| 2026-10-03 08:01:38 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.054 |  |
| 2026-10-03 08:04:03 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.079 |  |
| 2026-10-03 08:05:01 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.088 |  |
| 2026-10-03 08:01:11 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)