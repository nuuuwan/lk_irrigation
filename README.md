# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--29_01:05:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **273,712 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 01:05:04 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.039 |  |
| 2026-09-29 01:04:00 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-09-29 01:03:55 | Glencourse (Kelani Ganga) | 10.96 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-09-29 01:03:48 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-29 01:03:39 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | -0.053 |  |
| 2026-09-29 01:03:29 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 01:03:12 | Thaldena (Mahaweli Ganga) | 0.03 | 🟢 Normal | -0.038 |  |
| 2026-09-29 01:03:00 | Thalgahagoda (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-09-29 01:02:53 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-09-29 01:02:33 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 01:02:26 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 01:02:21 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-29 01:02:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | -0.097 |  |
| 2026-09-29 01:01:56 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-29 01:01:56 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-29 01:01:42 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-09-29 01:01:36 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-09-29 01:01:28 | Peradeniya (Mahaweli Ganga) | 3.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 01:01:24 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | -0.010 |  |
| 2026-09-29 01:00:57 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:59:38 | Peradeniya (Mahaweli Ganga) | 3.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:25:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.82 | 🟢 Normal | -0.097 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 00:18:32 | Baddegama (Gin Ganga) | 3.52 | 🟡 Alert | 0.000 |  |
| 2026-09-29 00:03:18 | Rathnapura (Kalu Ganga) | 2.72 | 🟢 Normal | 2.591 | 🔺 Rising |
| 2026-09-29 01:02:53 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-09-28 18:02:00 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-29 01:03:55 | Glencourse (Kelani Ganga) | 10.96 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-09-29 00:02:08 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-29 00:06:16 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-28 23:00:40 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-29 01:01:56 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:00:48 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 01:03:29 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 01:03:48 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:00:25 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-29 01:02:33 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 01:01:56 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-29 01:02:21 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-29 01:04:00 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-09-29 01:00:57 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-29 01:01:28 | Peradeniya (Mahaweli Ganga) | 3.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:11:18 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-29 00:04:24 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-29 01:02:26 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 01:03:00 | Thalgahagoda (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-09-29 01:01:36 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-09-29 01:01:24 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | -0.010 |  |
| 2026-09-28 18:01:32 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-09-29 01:01:42 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-09-28 23:13:43 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.011 |  |
| 2026-09-29 00:15:59 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.017 |  |
| 2026-09-28 23:04:30 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.025 |  |
| 2026-09-29 00:01:10 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.035 |  |
| 2026-09-29 01:03:12 | Thaldena (Mahaweli Ganga) | 0.03 | 🟢 Normal | -0.038 |  |
| 2026-09-29 01:05:04 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.039 |  |
| 2026-09-29 00:06:41 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.050 |  |
| 2026-09-29 01:03:39 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | -0.053 |  |
| 2026-09-29 00:11:12 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | -0.081 |  |
| 2026-09-29 01:02:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | -0.097 |  |
| 2026-09-29 00:04:45 | Nawalapitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.119 |  |
| 2026-09-29 00:21:32 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)