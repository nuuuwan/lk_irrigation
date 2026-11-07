# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_17:03:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,475 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 17:03:25 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:03:25 | Rathnapura (Kalu Ganga) | 2.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 17:03:23 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.040 |  |
| 2026-11-07 17:03:16 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-11-07 17:02:47 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:02:38 | Dunamale (Aththanagalu Oya) | 3.58 | 🟡 Alert | -0.060 |  |
| 2026-11-07 17:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | -0.020 |  |
| 2026-11-07 17:02:26 | Putupaula (Kalu Ganga) | 1.53 | 🟢 Normal | -0.031 |  |
| 2026-11-07 17:02:11 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-11-07 17:02:07 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-11-07 17:02:04 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-07 17:02:04 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:02:03 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.079 |  |
| 2026-11-07 17:01:49 | Pitabeddara (Nilwala Ganga) | 1.56 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-11-07 17:01:19 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-11-07 17:01:14 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-07 17:01:05 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.165 |  |
| 2026-11-07 16:25:02 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-07 16:20:14 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.016 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 17:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | -0.020 |  |
| 2026-11-07 17:02:38 | Dunamale (Aththanagalu Oya) | 3.58 | 🟡 Alert | -0.060 |  |
| 2026-11-07 17:02:11 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-11-07 16:07:37 | Panadugama (Nilwala Ganga) | 3.97 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-11-07 17:03:16 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-11-07 17:01:49 | Pitabeddara (Nilwala Ganga) | 1.56 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-11-07 16:07:25 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-07 17:02:04 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-07 17:03:25 | Rathnapura (Kalu Ganga) | 2.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 16:04:45 | Giriulla (Maha Oya) | 2.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 16:20:14 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-07 16:05:54 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-07 17:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-07 16:08:36 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 16:04:15 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-07 16:04:33 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:02:47 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-07 16:10:02 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:02:04 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:03:25 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-07 16:01:32 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:01:14 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-11-07 16:25:02 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-07 16:08:16 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-11-07 17:01:19 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-11-07 16:00:44 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-11-07 17:02:07 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-11-07 15:05:21 | Thanamalwila (Kirindi Oya) | 1.50 | 🟢 Normal | -0.019 |  |
| 2026-11-07 16:03:53 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | -0.020 |  |
| 2026-11-07 16:02:04 | Moragaswewa (Deduru Oya) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-11-07 16:06:19 | Holombuwa (Kelani Ganga) | 1.41 | 🟢 Normal | -0.029 |  |
| 2026-11-07 16:09:24 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | -0.031 |  |
| 2026-11-07 17:02:26 | Putupaula (Kalu Ganga) | 1.53 | 🟢 Normal | -0.031 |  |
| 2026-11-07 17:03:23 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.040 |  |
| 2026-11-07 16:16:09 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.071 |  |
| 2026-11-07 17:02:03 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.079 |  |
| 2026-11-07 16:04:06 | Badalgama (Maha Oya) | 3.57 | 🟢 Normal | -0.106 |  |
| 2026-11-07 16:05:12 | Hanwella (Kelani Ganga) | 3.57 | 🟢 Normal | -0.125 |  |
| 2026-11-07 17:01:05 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.165 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)