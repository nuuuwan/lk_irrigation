# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_13:02:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,320 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 13:02:55 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-11-07 13:02:55 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | -0.029 |  |
| 2026-11-07 13:02:52 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-11-07 13:02:50 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-11-07 13:02:46 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-11-07 13:02:43 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-07 13:02:35 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-11-07 13:02:33 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | -0.101 |  |
| 2026-11-07 13:02:27 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 13:02:24 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-07 13:02:01 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-11-07 13:01:55 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | -0.022 |  |
| 2026-11-07 13:01:53 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-11-07 13:01:46 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.015 |  |
| 2026-11-07 13:01:24 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.049 |  |
| 2026-11-07 13:01:19 | Ellagawa (Kalu Ganga) | 6.29 | 🟢 Normal | -0.031 |  |
| 2026-11-07 13:00:44 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-11-07 13:00:39 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | -0.143 |  |
| 2026-11-07 13:00:26 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.021 |  |
| 2026-11-07 12:47:51 | Dunamale (Aththanagalu Oya) | 3.82 | 🟡 Alert | -0.025 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 12:47:51 | Dunamale (Aththanagalu Oya) | 3.82 | 🟡 Alert | -0.025 |  |
| 2026-11-07 12:04:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.21 | 🟡 Alert | -0.029 |  |
| 2026-11-07 13:00:44 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-11-07 12:05:42 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-07 13:02:43 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-07 13:02:27 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 12:05:33 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:11:24 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-07 13:02:52 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-11-07 13:02:24 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-07 11:05:29 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-07 13:02:50 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:12:18 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:06:55 | Panadugama (Nilwala Ganga) | 3.81 | 🟢 Normal | -0.009 |  |
| 2026-11-07 12:04:28 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:03:01 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-11-07 13:01:53 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-11-07 13:02:01 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-11-07 13:02:46 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:09:45 | Urawa (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-11-07 13:02:55 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-11-07 13:01:46 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.015 |  |
| 2026-11-07 13:02:35 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-11-07 13:00:26 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.021 |  |
| 2026-11-07 13:01:55 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | -0.022 |  |
| 2026-11-07 13:02:55 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | -0.029 |  |
| 2026-11-07 12:01:48 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-11-07 13:01:19 | Ellagawa (Kalu Ganga) | 6.29 | 🟢 Normal | -0.031 |  |
| 2026-11-07 12:01:17 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.031 |  |
| 2026-11-07 13:01:24 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.049 |  |
| 2026-11-07 12:02:51 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.054 |  |
| 2026-11-07 12:02:37 | Hanwella (Kelani Ganga) | 4.06 | 🟢 Normal | -0.090 |  |
| 2026-11-07 12:06:58 | Magura (Kalu Ganga) | 2.64 | 🟢 Normal | -0.099 |  |
| 2026-11-07 13:02:33 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | -0.101 |  |
| 2026-11-07 12:01:11 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.103 |  |
| 2026-11-07 12:05:25 | Badalgama (Maha Oya) | 4.01 | 🟢 Normal | -0.123 |  |
| 2026-11-07 13:00:39 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | -0.143 |  |
| 2026-11-07 12:07:44 | Glencourse (Kelani Ganga) | 11.34 | 🟢 Normal | -0.201 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)