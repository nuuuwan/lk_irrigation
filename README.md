# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--13_20:12:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **287,028 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Urawa — Alert; 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 20:12:39 | Thalgahagoda (Nilwala Ganga) | 1.62 | 🟡 Alert | 0.000 |  |
| 2026-10-13 20:09:57 | Baddegama (Gin Ganga) | 2.52 | 🟢 Normal | -0.038 |  |
| 2026-10-13 20:09:50 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.019 |  |
| 2026-10-13 20:08:40 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-13 20:08:29 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-13 20:07:39 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-13 20:06:52 | Magura (Kalu Ganga) | 3.94 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-10-13 20:06:43 | Urawa (Nilwala Ganga) | 2.76 | 🟡 Alert | 0.153 | 🔺 Rising |
| 2026-10-13 20:06:23 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.118 |  |
| 2026-10-13 20:05:21 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-13 20:05:08 | Ellagawa (Kalu Ganga) | 7.30 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-13 20:04:59 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-13 20:04:39 | Rathnapura (Kalu Ganga) | 3.61 | 🟢 Normal | 0.337 | 🔺 Rising |
| 2026-10-13 20:04:24 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.068 |  |
| 2026-10-13 20:03:38 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 20:03:30 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 20:03:17 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-10-13 20:03:14 | Glencourse (Kelani Ganga) | 10.72 | 🟢 Normal | -0.058 |  |
| 2026-10-13 20:03:11 | Thawalama (Gin Ganga) | 2.92 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-10-13 20:02:52 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 20:02:45 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | 0.418 | 🔺 Rising |
| 2026-10-13 20:02:24 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 20:02:23 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-10-13 20:02:22 | Hanwella (Kelani Ganga) | 3.19 | 🟢 Normal | -0.030 |  |
| 2026-10-13 20:02:14 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-10-13 20:02:11 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-10-13 20:02:11 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-10-13 20:02:09 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-13 20:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-13 20:01:29 | Panadugama (Nilwala Ganga) | 5.66 | 🟡 Alert | -0.020 |  |
| 2026-10-13 20:01:06 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-13 20:01:06 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-13 20:00:52 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-13 20:00:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.02 | 🟡 Alert | -0.015 |  |
| 2026-10-13 19:37:26 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | 0.169 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 20:06:43 | Urawa (Nilwala Ganga) | 2.76 | 🟡 Alert | 0.153 | 🔺 Rising |
| 2026-10-13 20:12:39 | Thalgahagoda (Nilwala Ganga) | 1.62 | 🟡 Alert | 0.000 |  |
| 2026-10-13 20:00:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.02 | 🟡 Alert | -0.015 |  |
| 2026-10-13 20:01:29 | Panadugama (Nilwala Ganga) | 5.66 | 🟡 Alert | -0.020 |  |
| 2026-10-13 20:02:45 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | 0.418 | 🔺 Rising |
| 2026-10-13 20:04:39 | Rathnapura (Kalu Ganga) | 3.61 | 🟢 Normal | 0.337 | 🔺 Rising |
| 2026-10-13 20:06:52 | Magura (Kalu Ganga) | 3.94 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-10-13 20:02:14 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-10-13 20:03:11 | Thawalama (Gin Ganga) | 2.92 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-10-13 20:08:40 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-13 20:01:06 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-13 20:05:08 | Ellagawa (Kalu Ganga) | 7.30 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-13 20:02:09 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-13 20:05:21 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-13 20:02:52 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 20:03:38 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 20:02:24 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 20:04:59 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-13 20:07:39 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-13 20:03:30 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 20:02:11 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-10-13 20:01:06 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:05:16 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-13 20:00:52 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-13 20:08:29 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-13 19:03:17 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:04:16 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-13 20:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-13 20:02:23 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-10-13 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.010 |  |
| 2026-10-13 20:02:11 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-10-13 19:12:24 | Putupaula (Kalu Ganga) | 1.76 | 🟢 Normal | -0.017 |  |
| 2026-10-13 20:09:50 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.019 |  |
| 2026-10-13 20:03:17 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-10-13 20:02:22 | Hanwella (Kelani Ganga) | 3.19 | 🟢 Normal | -0.030 |  |
| 2026-10-13 20:09:57 | Baddegama (Gin Ganga) | 2.52 | 🟢 Normal | -0.038 |  |
| 2026-10-13 20:03:14 | Glencourse (Kelani Ganga) | 10.72 | 🟢 Normal | -0.058 |  |
| 2026-10-13 20:04:24 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.068 |  |
| 2026-10-13 20:06:23 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.118 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)