# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--25_09:04:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,191 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🔴 Baddegama — Major Flood; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 09:04:09 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-11-25 09:04:03 | Giriulla (Maha Oya) | 2.60 | 🟢 Normal | -0.090 |  |
| 2026-11-25 09:03:40 | Hanwella (Kelani Ganga) | 3.69 | 🟢 Normal | -0.128 |  |
| 2026-11-25 09:03:38 | Panadugama (Nilwala Ganga) | 4.76 | 🟢 Normal | 2736.000 | 🔺 Rising |
| 2026-11-25 09:03:37 | Panadugama (Nilwala Ganga) | 4.00 | 🟢 Normal | 2736.000 | 🔺 Rising |
| 2026-11-25 09:03:35 | Panadugama (Nilwala Ganga) | 4.05 | 🟢 Normal | 2736.000 | 🔺 Rising |
| 2026-11-25 09:03:34 | Panadugama (Nilwala Ganga) | 4.05 | 🟢 Normal | 2736.000 | 🔺 Rising |
| 2026-11-25 09:03:30 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-25 09:03:22 | Holombuwa (Kelani Ganga) | 1.03 | 🟢 Normal | -0.021 |  |
| 2026-11-25 09:03:19 | Pitabeddara (Nilwala Ganga) | 1.84 | 🟢 Normal | -0.058 |  |
| 2026-11-25 09:03:18 | Moraketiya (Walawe Ganga) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-11-25 09:03:07 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.050 |  |
| 2026-11-25 09:03:04 | Ellagawa (Kalu Ganga) | 6.76 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-25 09:02:58 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-11-25 09:02:56 | Putupaula (Kalu Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-11-25 09:02:56 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-11-25 09:02:55 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 09:02:32 | Badalgama (Maha Oya) | 3.97 | 🟢 Normal | -0.119 |  |
| 2026-11-25 09:02:07 | Siyambalanduwa (Heda Oya) | 1.29 | 🟢 Normal | -0.073 |  |
| 2026-11-25 09:01:52 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2026-11-25 09:01:49 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | -0.134 |  |
| 2026-11-25 09:01:45 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-25 09:01:37 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.301 |  |
| 2026-11-25 09:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-11-25 09:01:18 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-25 09:01:14 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-25 09:01:12 | Magura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.255 |  |
| 2026-11-25 09:00:58 | Baddegama (Gin Ganga) | 5.90 | 🔴 Major Flood | 4.001 | 🔺 Rising |
| 2026-11-25 09:00:24 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | -0.033 |  |
| 2026-11-25 09:00:14 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | -0.031 |  |
| 2026-11-25 08:30:13 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.036 |  |
| 2026-11-25 08:19:39 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.023 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 09:00:58 | Baddegama (Gin Ganga) | 5.90 | 🔴 Major Flood | 4.001 | 🔺 Rising |
| 2026-11-25 08:03:12 | Dunamale (Aththanagalu Oya) | 3.43 | 🟡 Alert | -0.108 |  |
| 2026-11-25 09:03:38 | Panadugama (Nilwala Ganga) | 4.76 | 🟢 Normal | 2736.000 | 🔺 Rising |
| 2026-11-25 08:11:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.54 | 🟢 Normal | 0.383 | 🔺 Rising |
| 2026-11-25 09:01:52 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2026-11-25 09:01:14 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-25 08:19:39 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-25 09:03:04 | Ellagawa (Kalu Ganga) | 6.76 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-25 09:03:30 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-25 08:02:42 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 09:02:55 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 09:01:45 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-25 09:01:18 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-25 09:03:18 | Moraketiya (Walawe Ganga) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-11-25 09:04:09 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-11-25 09:02:56 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-11-25 08:01:55 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-11-25 08:03:55 | Katharagama (Menik Ganga) | 0.23 | 🟢 Normal | -0.012 |  |
| 2026-11-25 09:02:56 | Putupaula (Kalu Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-11-25 09:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-11-25 09:03:22 | Holombuwa (Kelani Ganga) | 1.03 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-25 09:02:58 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-11-25 09:00:14 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | -0.031 |  |
| 2026-11-25 09:00:24 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | -0.033 |  |
| 2026-11-25 08:30:13 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.036 |  |
| 2026-11-25 08:02:30 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.040 |  |
| 2026-11-25 08:04:57 | Peradeniya (Mahaweli Ganga) | 3.40 | 🟢 Normal | -0.050 |  |
| 2026-11-25 09:03:07 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.050 |  |
| 2026-11-25 08:05:40 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.052 |  |
| 2026-11-25 09:03:19 | Pitabeddara (Nilwala Ganga) | 1.84 | 🟢 Normal | -0.058 |  |
| 2026-11-25 09:02:07 | Siyambalanduwa (Heda Oya) | 1.29 | 🟢 Normal | -0.073 |  |
| 2026-11-25 09:04:03 | Giriulla (Maha Oya) | 2.60 | 🟢 Normal | -0.090 |  |
| 2026-11-25 09:02:32 | Badalgama (Maha Oya) | 3.97 | 🟢 Normal | -0.119 |  |
| 2026-11-25 08:07:35 | Rathnapura (Kalu Ganga) | 3.66 | 🟢 Normal | -0.120 |  |
| 2026-11-25 09:03:40 | Hanwella (Kelani Ganga) | 3.69 | 🟢 Normal | -0.128 |  |
| 2026-11-25 09:01:49 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | -0.134 |  |
| 2026-11-25 09:01:12 | Magura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.255 |  |
| 2026-11-25 09:01:37 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.301 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)