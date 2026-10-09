# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--09_14:26:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,227 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 14:26:04 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-09 14:12:20 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-09 14:11:21 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.083 |  |
| 2026-10-09 14:10:51 | Urawa (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.520 | 🔺 Rising |
| 2026-10-09 14:09:15 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.057 |  |
| 2026-10-09 14:07:00 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.077 |  |
| 2026-10-09 14:06:25 | Panadugama (Nilwala Ganga) | 3.88 | 🟢 Normal | -0.059 |  |
| 2026-10-09 14:06:08 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.040 |  |
| 2026-10-09 14:05:49 | Baddegama (Gin Ganga) | 2.74 | 🟢 Normal | -0.031 |  |
| 2026-10-09 14:05:46 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.019 |  |
| 2026-10-09 14:05:33 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-09 14:05:11 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-10-09 14:04:47 | Badalgama (Maha Oya) | 4.14 | 🟢 Normal | -0.063 |  |
| 2026-10-09 14:04:38 | Dunamale (Aththanagalu Oya) | 2.64 | 🟢 Normal | -0.120 |  |
| 2026-10-09 14:04:36 | Hanwella (Kelani Ganga) | 3.43 | 🟢 Normal | -0.089 |  |
| 2026-10-09 14:04:27 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-09 14:04:26 | Putupaula (Kalu Ganga) | 1.46 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-09 14:04:16 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.019 |  |
| 2026-10-09 14:04:16 | Glencourse (Kelani Ganga) | 11.31 | 🟢 Normal | 0.000 |  |
| 2026-10-09 14:04:02 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-09 14:03:24 | Giriulla (Maha Oya) | 3.10 | 🟢 Normal | -0.076 |  |
| 2026-10-09 14:03:00 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-09 14:02:59 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-10-09 14:02:58 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-09 14:02:46 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-09 14:02:30 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-09 14:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.81 | 🟢 Normal | -0.050 |  |
| 2026-10-09 14:02:21 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 14:02:19 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.021 |  |
| 2026-10-09 14:02:17 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-09 14:02:17 | Ellagawa (Kalu Ganga) | 6.51 | 🟢 Normal | -0.040 |  |
| 2026-10-09 14:02:04 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 14:01:37 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 14:01:12 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | -0.081 |  |
| 2026-10-09 14:01:10 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-09 14:01:04 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | -0.020 |  |
| 2026-10-09 14:00:47 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.032 |  |
| 2026-10-09 14:00:39 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-10-09 14:00:28 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 14:10:51 | Urawa (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.520 | 🔺 Rising |
| 2026-10-09 14:00:39 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-10-09 14:05:11 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-10-09 14:04:26 | Putupaula (Kalu Ganga) | 1.46 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-09 14:02:30 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-09 14:26:04 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-09 14:01:37 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 14:02:04 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 13:01:02 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-09 14:12:20 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-09 14:02:17 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-09 14:02:58 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-09 14:02:21 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 14:04:02 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-09 14:04:16 | Glencourse (Kelani Ganga) | 11.31 | 🟢 Normal | 0.000 |  |
| 2026-10-09 14:01:10 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-09 14:03:00 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-09 14:02:46 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-09 14:05:33 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-09 14:02:59 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-10-09 14:04:16 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.019 |  |
| 2026-10-09 14:05:46 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.019 |  |
| 2026-10-09 14:01:04 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | -0.020 |  |
| 2026-10-09 14:00:28 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.020 |  |
| 2026-10-09 14:02:19 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.021 |  |
| 2026-10-09 14:05:49 | Baddegama (Gin Ganga) | 2.74 | 🟢 Normal | -0.031 |  |
| 2026-10-09 14:00:47 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.032 |  |
| 2026-10-09 14:06:08 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.040 |  |
| 2026-10-09 14:02:17 | Ellagawa (Kalu Ganga) | 6.51 | 🟢 Normal | -0.040 |  |
| 2026-10-09 14:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.81 | 🟢 Normal | -0.050 |  |
| 2026-10-09 14:09:15 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.057 |  |
| 2026-10-09 14:06:25 | Panadugama (Nilwala Ganga) | 3.88 | 🟢 Normal | -0.059 |  |
| 2026-10-09 14:04:47 | Badalgama (Maha Oya) | 4.14 | 🟢 Normal | -0.063 |  |
| 2026-10-09 14:03:24 | Giriulla (Maha Oya) | 3.10 | 🟢 Normal | -0.076 |  |
| 2026-10-09 14:07:00 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.077 |  |
| 2026-10-09 14:01:12 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | -0.081 |  |
| 2026-10-09 14:11:21 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.083 |  |
| 2026-10-09 14:04:36 | Hanwella (Kelani Ganga) | 3.43 | 🟢 Normal | -0.089 |  |
| 2026-10-09 14:04:38 | Dunamale (Aththanagalu Oya) | 2.64 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)