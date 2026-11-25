# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--25_10:02:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,215 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🔴 Baddegama — Major Flood; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 10:02:41 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-11-25 10:02:32 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-25 10:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-11-25 10:02:20 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-25 10:01:40 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.042 |  |
| 2026-11-25 10:01:22 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-25 10:01:22 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-25 10:01:13 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -1.150 |  |
| 2026-11-25 10:01:12 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-11-25 10:01:10 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-25 10:01:06 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-25 10:01:06 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 09:00:58 | Baddegama (Gin Ganga) | 5.90 | 🔴 Major Flood | 4.001 | 🔺 Rising |
| 2026-11-25 09:07:24 | Dunamale (Aththanagalu Oya) | 3.34 | 🟡 Alert | -0.084 |  |
| 2026-11-25 09:13:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.84 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-11-25 10:01:12 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-11-25 10:01:10 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-25 10:02:32 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-25 09:10:44 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-25 09:03:04 | Ellagawa (Kalu Ganga) | 6.76 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-25 09:03:30 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-25 09:02:55 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 10:01:22 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-25 10:01:06 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-11-25 10:01:22 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-25 10:02:20 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-25 09:19:58 | Panadugama (Nilwala Ganga) | 4.76 | 🟢 Normal | 0.000 |  |
| 2026-11-25 10:01:06 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-25 09:03:18 | Moraketiya (Walawe Ganga) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-11-25 10:02:41 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-11-25 09:06:50 | Thanamalwila (Kirindi Oya) | 1.71 | 🟢 Normal | -0.019 |  |
| 2026-11-25 09:05:15 | Katharagama (Menik Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-11-25 10:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-11-25 09:02:56 | Putupaula (Kalu Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-11-25 09:03:22 | Holombuwa (Kelani Ganga) | 1.03 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-25 09:02:58 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-11-25 10:01:40 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.042 |  |
| 2026-11-25 09:03:07 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.050 |  |
| 2026-11-25 09:03:19 | Pitabeddara (Nilwala Ganga) | 1.84 | 🟢 Normal | -0.058 |  |
| 2026-11-25 09:07:28 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.058 |  |
| 2026-11-25 09:16:44 | Urawa (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.064 |  |
| 2026-11-25 09:02:07 | Siyambalanduwa (Heda Oya) | 1.29 | 🟢 Normal | -0.073 |  |
| 2026-11-25 09:04:03 | Giriulla (Maha Oya) | 2.60 | 🟢 Normal | -0.090 |  |
| 2026-11-25 09:02:32 | Badalgama (Maha Oya) | 3.97 | 🟢 Normal | -0.119 |  |
| 2026-11-25 09:03:40 | Hanwella (Kelani Ganga) | 3.69 | 🟢 Normal | -0.128 |  |
| 2026-11-25 09:01:49 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | -0.134 |  |
| 2026-11-25 09:11:21 | Peradeniya (Mahaweli Ganga) | 3.23 | 🟢 Normal | -0.154 |  |
| 2026-11-25 09:09:32 | Rathnapura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.155 |  |
| 2026-11-25 09:01:37 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.301 |  |
| 2026-11-25 10:01:13 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -1.150 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)