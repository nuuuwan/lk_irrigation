# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_11:16:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,451 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 11:16:20 | Urawa (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.090 |  |
| 2026-11-05 11:12:52 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.052 |  |
| 2026-11-05 11:11:54 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.036 |  |
| 2026-11-05 11:10:10 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | -0.022 |  |
| 2026-11-05 11:08:16 | Panadugama (Nilwala Ganga) | 4.55 | 🟢 Normal | -0.037 |  |
| 2026-11-05 11:07:27 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | -0.039 |  |
| 2026-11-05 11:07:14 | Rathnapura (Kalu Ganga) | 3.73 | 🟢 Normal | -0.068 |  |
| 2026-11-05 11:06:29 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-05 11:06:27 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 11:06:05 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | -0.009 |  |
| 2026-11-05 11:05:00 | Thanthirimale (Malwathu Oya) | 1.90 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-05 11:05:00 | Giriulla (Maha Oya) | 2.21 | 🟢 Normal | -0.058 |  |
| 2026-11-05 11:04:59 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.019 |  |
| 2026-11-05 11:04:57 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-11-05 11:04:30 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-05 11:04:20 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-05 11:04:15 | Badalgama (Maha Oya) | 3.47 | 🟢 Normal | -0.051 |  |
| 2026-11-05 11:03:29 | Ellagawa (Kalu Ganga) | 6.34 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-05 11:03:09 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.116 |  |
| 2026-11-05 11:02:58 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-05 11:02:53 | Hanwella (Kelani Ganga) | 2.67 | 🟢 Normal | -0.020 |  |
| 2026-11-05 11:02:39 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | -0.071 |  |
| 2026-11-05 11:02:23 | Putupaula (Kalu Ganga) | 1.34 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-05 11:02:17 | Dunamale (Aththanagalu Oya) | 2.79 | 🟢 Normal | -0.040 |  |
| 2026-11-05 11:02:16 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-11-05 11:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.18 | 🟡 Alert | -0.020 |  |
| 2026-11-05 11:02:08 | Moragaswewa (Deduru Oya) | 3.56 | 🟢 Normal | -0.042 |  |
| 2026-11-05 11:02:03 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 11:02:02 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-05 11:02:01 | Thanamalwila (Kirindi Oya) | 2.10 | 🟢 Normal | -0.040 |  |
| 2026-11-05 11:01:49 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.385 | 🔺 Rising |
| 2026-11-05 11:01:47 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.051 |  |
| 2026-11-05 11:01:29 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | -0.050 |  |
| 2026-11-05 11:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-05 11:01:05 | Kuda Oya (Kirindi Oya) | 2.42 | 🟢 Normal | -0.050 |  |
| 2026-11-05 11:00:40 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-05 11:00:16 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 11:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.18 | 🟡 Alert | -0.020 |  |
| 2026-11-05 11:01:49 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.385 | 🔺 Rising |
| 2026-11-05 11:03:29 | Ellagawa (Kalu Ganga) | 6.34 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-05 11:00:40 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-05 10:17:53 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-05 11:05:00 | Thanthirimale (Malwathu Oya) | 1.90 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-05 11:02:23 | Putupaula (Kalu Ganga) | 1.34 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-05 11:02:02 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-05 11:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-05 11:02:03 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 11:04:20 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-05 10:09:24 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 11:04:30 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-05 11:02:58 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-05 11:00:16 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-05 11:06:27 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 11:06:05 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | -0.009 |  |
| 2026-11-05 11:06:29 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-05 11:02:16 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-11-05 11:04:59 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.019 |  |
| 2026-11-05 11:04:57 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-11-05 11:02:53 | Hanwella (Kelani Ganga) | 2.67 | 🟢 Normal | -0.020 |  |
| 2026-11-05 11:10:10 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | -0.022 |  |
| 2026-11-05 11:11:54 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.036 |  |
| 2026-11-05 11:08:16 | Panadugama (Nilwala Ganga) | 4.55 | 🟢 Normal | -0.037 |  |
| 2026-11-05 11:07:27 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | -0.039 |  |
| 2026-11-05 11:02:01 | Thanamalwila (Kirindi Oya) | 2.10 | 🟢 Normal | -0.040 |  |
| 2026-11-05 11:02:17 | Dunamale (Aththanagalu Oya) | 2.79 | 🟢 Normal | -0.040 |  |
| 2026-11-05 11:02:08 | Moragaswewa (Deduru Oya) | 3.56 | 🟢 Normal | -0.042 |  |
| 2026-11-05 11:01:29 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | -0.050 |  |
| 2026-11-05 11:01:05 | Kuda Oya (Kirindi Oya) | 2.42 | 🟢 Normal | -0.050 |  |
| 2026-11-05 11:04:15 | Badalgama (Maha Oya) | 3.47 | 🟢 Normal | -0.051 |  |
| 2026-11-05 11:01:47 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.051 |  |
| 2026-11-05 11:12:52 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.052 |  |
| 2026-11-05 11:05:00 | Giriulla (Maha Oya) | 2.21 | 🟢 Normal | -0.058 |  |
| 2026-11-05 11:07:14 | Rathnapura (Kalu Ganga) | 3.73 | 🟢 Normal | -0.068 |  |
| 2026-11-05 11:02:39 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | -0.071 |  |
| 2026-11-05 11:16:20 | Urawa (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.090 |  |
| 2026-11-05 11:03:09 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.116 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)