# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_15:09:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **261,657 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 15:09:10 | Baddegama (Gin Ganga) | 3.37 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:09:03 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-09-15 15:08:00 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-09-15 15:07:57 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.031 |  |
| 2026-09-15 15:07:24 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 15:07:21 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.029 |  |
| 2026-09-15 15:06:53 | Baddegama (Gin Ganga) | 3.37 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:06:49 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-09-15 15:06:11 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:05:04 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:04:40 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | -0.132 |  |
| 2026-09-15 15:04:16 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:04:10 | Magura (Kalu Ganga) | 4.58 | 🟡 Alert | -0.108 |  |
| 2026-09-15 15:03:59 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:03:54 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.021 |  |
| 2026-09-15 15:03:32 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 15:03:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 15:03:26 | Dunamale (Aththanagalu Oya) | 3.20 | 🟢 Normal | -0.041 |  |
| 2026-09-15 15:03:21 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:03:16 | Hanwella (Kelani Ganga) | 2.59 | 🟢 Normal | -0.108 |  |
| 2026-09-15 15:03:02 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-15 15:02:59 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.201 |  |
| 2026-09-15 15:02:43 | Panadugama (Nilwala Ganga) | 3.81 | 🟢 Normal | -0.134 |  |
| 2026-09-15 15:02:39 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:02:23 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.032 |  |
| 2026-09-15 15:02:22 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:02:19 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 15:01:52 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.039 |  |
| 2026-09-15 15:01:43 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:01:34 | Manampitiya (Mahaweli Ganga) | -0.45 | 🟢 Normal | -0.020 |  |
| 2026-09-15 15:01:27 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-15 15:01:26 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-09-15 15:01:10 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:01:09 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-09-15 15:00:45 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:00:37 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 15:04:10 | Magura (Kalu Ganga) | 4.58 | 🟡 Alert | -0.108 |  |
| 2026-09-15 15:01:09 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-09-15 15:09:03 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-09-15 15:06:49 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-09-15 15:01:27 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-15 15:03:02 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-15 15:03:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 15:02:19 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 15:03:32 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 15:07:24 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 15:03:59 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:02:19 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:01:43 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:02:39 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:01:00 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:05:04 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:04:16 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:09:10 | Baddegama (Gin Ganga) | 3.37 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:03:21 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:00:45 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:06:11 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:02:22 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:01:10 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:08:00 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-09-15 15:01:26 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-09-15 15:00:37 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-15 15:01:34 | Manampitiya (Mahaweli Ganga) | -0.45 | 🟢 Normal | -0.020 |  |
| 2026-09-15 15:03:54 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.021 |  |
| 2026-09-15 15:07:21 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.029 |  |
| 2026-09-15 15:07:57 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.031 |  |
| 2026-09-15 15:02:23 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.032 |  |
| 2026-09-15 15:01:52 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.039 |  |
| 2026-09-15 15:03:26 | Dunamale (Aththanagalu Oya) | 3.20 | 🟢 Normal | -0.041 |  |
| 2026-09-15 14:05:15 | Ellagawa (Kalu Ganga) | 5.87 | 🟢 Normal | -0.071 |  |
| 2026-09-15 15:03:16 | Hanwella (Kelani Ganga) | 2.59 | 🟢 Normal | -0.108 |  |
| 2026-09-15 15:04:40 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | -0.132 |  |
| 2026-09-15 15:02:43 | Panadugama (Nilwala Ganga) | 3.81 | 🟢 Normal | -0.134 |  |
| 2026-09-15 15:02:59 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.201 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)