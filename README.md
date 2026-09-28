# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--29_00:25:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **273,691 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Baddegama — Alert; 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 00:25:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.82 | 🟢 Normal | -0.062 |  |
| 2026-09-29 00:21:32 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.180 |  |
| 2026-09-29 00:18:32 | Baddegama (Gin Ganga) | 3.52 | 🟡 Alert | 0.000 |  |
| 2026-09-29 00:15:59 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.017 |  |
| 2026-09-29 00:11:18 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:11:12 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | -0.081 |  |
| 2026-09-29 00:10:54 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:07:26 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:07:11 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | -0.038 |  |
| 2026-09-29 00:06:56 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:06:41 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.050 |  |
| 2026-09-29 00:06:16 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-29 00:06:06 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:05:51 | Baddegama (Gin Ganga) | 3.52 | 🟡 Alert | 0.000 |  |
| 2026-09-29 00:04:50 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-29 00:04:45 | Nawalapitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.119 |  |
| 2026-09-29 00:04:38 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-09-29 00:04:24 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:04:10 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.029 |  |
| 2026-09-29 00:03:41 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:03:38 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:03:32 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | -0.010 |  |
| 2026-09-29 00:03:28 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.011 |  |
| 2026-09-29 00:03:22 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:03:20 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:03:18 | Rathnapura (Kalu Ganga) | 2.72 | 🟢 Normal | 2.591 | 🔺 Rising |
| 2026-09-29 00:03:15 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:03:15 | Ellagawa (Kalu Ganga) | 5.81 | 🟢 Normal | -0.010 |  |
| 2026-09-29 00:02:58 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:02:40 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:02:08 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-29 00:01:55 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:01:24 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | -0.021 |  |
| 2026-09-29 00:01:10 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.035 |  |
| 2026-09-29 00:01:04 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:00:48 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:00:37 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.023 |  |
| 2026-09-28 23:56:49 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | 2.591 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 00:18:32 | Baddegama (Gin Ganga) | 3.52 | 🟡 Alert | 0.000 |  |
| 2026-09-29 00:01:24 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | -0.021 |  |
| 2026-09-29 00:03:18 | Rathnapura (Kalu Ganga) | 2.72 | 🟢 Normal | 2.591 | 🔺 Rising |
| 2026-09-29 00:04:38 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-09-28 18:02:00 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-29 00:02:08 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-29 00:06:16 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-29 00:04:50 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-28 23:00:40 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:01:04 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:00:48 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:01:55 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:03:38 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:00:25 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:06:56 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:03:15 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:06:06 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:03:41 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:02:40 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:07:26 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:11:18 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:04:24 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:03:22 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:03:15 | Ellagawa (Kalu Ganga) | 5.81 | 🟢 Normal | -0.010 |  |
| 2026-09-29 00:03:32 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | -0.010 |  |
| 2026-09-28 18:01:32 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-09-29 00:03:28 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.011 |  |
| 2026-09-28 23:13:43 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.011 |  |
| 2026-09-29 00:15:59 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.017 |  |
| 2026-09-29 00:00:37 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.023 |  |
| 2026-09-28 23:04:30 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.025 |  |
| 2026-09-29 00:04:10 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.029 |  |
| 2026-09-29 00:01:10 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.035 |  |
| 2026-09-29 00:07:11 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | -0.038 |  |
| 2026-09-29 00:06:41 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.050 |  |
| 2026-09-29 00:25:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.82 | 🟢 Normal | -0.062 |  |
| 2026-09-29 00:11:12 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | -0.081 |  |
| 2026-09-29 00:04:45 | Nawalapitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.119 |  |
| 2026-09-29 00:21:32 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)