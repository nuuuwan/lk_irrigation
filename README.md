# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--03_21:05:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **251,039 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-03 21:05:41 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:05:25 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:05:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-09-03 21:04:49 | Thanamalwila (Kirindi Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:04:45 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:04:24 | Siyambalanduwa (Heda Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:04:15 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:03:57 | Hanwella (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-09-03 21:03:57 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:03:15 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:03:12 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.015 |  |
| 2026-09-03 21:03:02 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-09-03 21:03:00 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.110 |  |
| 2026-09-03 21:02:59 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:02:57 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-09-03 21:02:24 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:02:22 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.064 |  |
| 2026-09-03 21:02:21 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:02:18 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:02:11 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:02:06 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-09-03 21:02:00 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-09-03 21:01:53 | Ellagawa (Kalu Ganga) | 4.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-03 21:01:52 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:01:38 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:01:07 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.110 |  |
| 2026-09-03 20:31:55 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-09-03 20:23:21 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.015 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-03 20:03:38 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-09-03 20:05:49 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-09-03 21:05:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-09-03 21:02:00 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-09-03 20:01:14 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-09-03 21:01:53 | Ellagawa (Kalu Ganga) | 4.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-03 20:07:02 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 21:02:24 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:02:18 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-03 20:02:09 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:04:15 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-09-03 20:01:14 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:05:41 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:01:38 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-03 18:02:40 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-03 20:05:37 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:05:25 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-09-03 20:07:19 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:02:11 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:03:57 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:03:15 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:04:24 | Siyambalanduwa (Heda Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:02:21 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:01:52 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:04:45 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-03 18:01:11 | Thanthirimale (Malwathu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-03 20:09:04 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-03 20:31:55 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-09-03 21:04:49 | Thanamalwila (Kirindi Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:30:37 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.007 |  |
| 2026-09-03 21:03:57 | Hanwella (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-09-03 21:02:06 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-09-03 21:03:02 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-09-03 21:02:57 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-09-03 21:03:12 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.015 |  |
| 2026-09-03 18:02:27 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.060 |  |
| 2026-09-03 21:02:22 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.064 |  |
| 2026-09-03 21:03:00 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.110 |  |
| 2026-09-03 21:01:07 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)