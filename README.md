# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--21_02:02:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **321,417 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Urawa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 02:02:11 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-21 02:02:07 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 02:01:58 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-21 02:01:56 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-21 02:01:41 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-21 02:01:37 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 02:01:28 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-11-21 02:01:04 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-21 02:00:42 | Peradeniya (Mahaweli Ganga) | 3.52 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-21 02:00:30 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-11-21 01:53:40 | Nawalapitiya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -0.152 |  |
| 2026-11-21 01:36:02 | Horowpothana (Yan Oya) | 1.91 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-11-21 01:29:29 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-21 01:23:08 | Panadugama (Nilwala Ganga) | 3.92 | 🟢 Normal | 0.144 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 01:05:09 | Urawa (Nilwala Ganga) | 2.85 | 🟡 Alert | 0.627 | 🔺 Rising |
| 2026-11-21 02:00:30 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-11-21 01:03:52 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-11-21 01:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-11-21 01:23:08 | Panadugama (Nilwala Ganga) | 3.92 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-11-21 01:05:15 | Glencourse (Kelani Ganga) | 9.73 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-21 01:04:11 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-11-21 01:03:22 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-11-21 01:29:29 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-21 02:00:42 | Peradeniya (Mahaweli Ganga) | 3.52 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-21 01:07:18 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-21 00:15:47 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-21 02:01:58 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-21 01:03:51 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-21 01:04:18 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-21 00:09:50 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-21 02:02:07 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 01:36:02 | Horowpothana (Yan Oya) | 1.91 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-11-21 02:01:41 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-21 02:01:37 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:00:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-21 01:04:39 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-21 01:06:23 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-21 01:03:03 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-21 02:02:11 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-21 01:04:45 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-21 01:04:00 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-11-21 01:11:04 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-21 02:01:04 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-21 02:01:56 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-21 01:03:14 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-21 01:02:57 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-11-21 02:01:28 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-11-21 01:00:27 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-11-20 18:01:40 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-11-20 18:00:21 | Weraganthota (Mahaweli Ganga) | -2.17 | 🟢 Normal | -0.020 |  |
| 2026-11-21 01:05:21 | Thawalama (Gin Ganga) | 3.04 | 🟢 Normal | -0.071 |  |
| 2026-11-21 01:53:40 | Nawalapitiya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -0.152 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)