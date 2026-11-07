# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_08:02:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,117 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 08:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.28 | 🟡 Alert | -0.010 |  |
| 2026-11-07 08:02:33 | Putupaula (Kalu Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-11-07 08:02:33 | Moragaswewa (Deduru Oya) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-11-07 08:02:23 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 08:02:07 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.011 |  |
| 2026-11-07 08:01:59 | Thanamalwila (Kirindi Oya) | 1.63 | 🟢 Normal | -0.021 |  |
| 2026-11-07 08:01:49 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 08:01:34 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-07 08:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-11-07 08:00:08 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-11-07 07:23:24 | Panadugama (Nilwala Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-11-07 07:20:38 | Panadugama (Nilwala Ganga) | 3.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 07:02:56 | Dunamale (Aththanagalu Oya) | 3.90 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-07 08:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.28 | 🟡 Alert | -0.010 |  |
| 2026-11-07 07:04:52 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-11-07 07:03:07 | Hanwella (Kelani Ganga) | 4.28 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-07 07:06:31 | Badalgama (Maha Oya) | 4.35 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-11-07 06:06:55 | Weraganthota (Mahaweli Ganga) | -2.19 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-11-07 07:02:43 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-07 07:07:37 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 08:02:23 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 08:01:49 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 07:05:12 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-07 07:01:03 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:11:47 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-07 07:23:24 | Panadugama (Nilwala Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-11-07 08:01:34 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-07 07:03:46 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:33:22 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | -0.003 |  |
| 2026-11-07 07:02:21 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-11-07 07:02:05 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-11-07 08:00:08 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-11-07 08:02:07 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.011 |  |
| 2026-11-07 07:02:58 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.015 |  |
| 2026-11-07 08:02:33 | Putupaula (Kalu Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-11-07 08:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-11-07 07:02:21 | Moraketiya (Walawe Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-11-07 08:01:59 | Thanamalwila (Kirindi Oya) | 1.63 | 🟢 Normal | -0.021 |  |
| 2026-11-07 07:09:15 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.027 |  |
| 2026-11-07 08:02:33 | Moragaswewa (Deduru Oya) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-11-07 07:01:36 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.031 |  |
| 2026-11-07 07:03:14 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-11-07 07:02:06 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | -0.034 |  |
| 2026-11-07 07:04:26 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.042 |  |
| 2026-11-07 07:01:40 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.051 |  |
| 2026-11-07 07:03:53 | Holombuwa (Kelani Ganga) | 1.81 | 🟢 Normal | -0.070 |  |
| 2026-11-07 07:13:41 | Rathnapura (Kalu Ganga) | 2.95 | 🟢 Normal | -0.092 |  |
| 2026-11-07 07:05:38 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | -0.111 |  |
| 2026-11-07 07:05:27 | Magura (Kalu Ganga) | 3.23 | 🟢 Normal | -0.148 |  |
| 2026-11-07 07:04:07 | Glencourse (Kelani Ganga) | 12.40 | 🟢 Normal | -0.155 |  |
| 2026-11-07 07:02:53 | Giriulla (Maha Oya) | 3.41 | 🟢 Normal | -0.229 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)