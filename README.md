# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_16:02:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,429 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 16:02:49 | Moraketiya (Walawe Ganga) | 1.87 | 🟢 Normal | -0.029 |  |
| 2026-11-07 16:02:35 | Dunamale (Aththanagalu Oya) | 3.64 | 🟡 Alert | -0.041 |  |
| 2026-11-07 16:02:13 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-11-07 16:02:04 | Moragaswewa (Deduru Oya) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-11-07 16:01:40 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.089 |  |
| 2026-11-07 16:01:37 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-07 16:01:32 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-07 16:01:32 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-11-07 16:01:16 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-07 16:00:44 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-11-07 15:21:43 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 15:03:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | -0.029 |  |
| 2026-11-07 16:02:35 | Dunamale (Aththanagalu Oya) | 3.64 | 🟡 Alert | -0.041 |  |
| 2026-11-07 16:01:37 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-07 15:02:28 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-11-07 16:01:16 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-07 15:00:50 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-07 15:01:09 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-07 15:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 15:04:47 | Putupaula (Kalu Ganga) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 15:00:13 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-07 15:05:37 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-07 15:11:32 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-07 15:02:57 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-07 15:05:08 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-07 16:01:32 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-07 15:06:41 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-11-07 15:21:43 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-07 15:16:45 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | -0.008 |  |
| 2026-11-07 15:10:45 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.009 |  |
| 2026-11-07 16:02:13 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-11-07 16:00:44 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-11-07 16:01:32 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-11-07 15:01:36 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-11-07 15:02:58 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.013 |  |
| 2026-11-07 15:05:21 | Thanamalwila (Kirindi Oya) | 1.50 | 🟢 Normal | -0.019 |  |
| 2026-11-07 15:03:00 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-11-07 16:02:04 | Moragaswewa (Deduru Oya) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-11-07 15:07:26 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | -0.025 |  |
| 2026-11-07 16:02:49 | Moraketiya (Walawe Ganga) | 1.87 | 🟢 Normal | -0.029 |  |
| 2026-11-07 15:10:24 | Baddegama (Gin Ganga) | 1.93 | 🟢 Normal | -0.039 |  |
| 2026-11-07 15:03:07 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.039 |  |
| 2026-11-07 15:04:09 | Holombuwa (Kelani Ganga) | 1.44 | 🟢 Normal | -0.041 |  |
| 2026-11-07 15:03:48 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | -0.048 |  |
| 2026-11-07 16:01:40 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.089 |  |
| 2026-11-07 15:07:15 | Badalgama (Maha Oya) | 3.67 | 🟢 Normal | -0.107 |  |
| 2026-11-07 15:03:13 | Giriulla (Maha Oya) | 2.27 | 🟢 Normal | -0.109 |  |
| 2026-11-07 15:08:29 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.133 |  |
| 2026-11-07 15:02:56 | Hanwella (Kelani Ganga) | 3.70 | 🟢 Normal | -0.139 |  |
| 2026-11-07 15:04:25 | Glencourse (Kelani Ganga) | 10.79 | 🟢 Normal | -0.163 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)