# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--05_11:22:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **252,468 measurements** from **39** stations.
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
| 2026-09-05 11:22:21 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:21:33 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | -0.007 |  |
| 2026-09-05 11:10:38 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-09-05 11:09:46 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | -0.009 |  |
| 2026-09-05 11:06:49 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-09-05 11:06:30 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:05:57 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:05:55 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:05:40 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:05:36 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-09-05 11:05:25 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:05:11 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.014 |  |
| 2026-09-05 11:04:46 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | -0.019 |  |
| 2026-09-05 11:04:43 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:04:14 | Galgamuwa (Mee Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:04:09 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:04:08 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-09-05 11:03:45 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-09-05 11:03:35 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.192 |  |
| 2026-09-05 11:03:29 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-05 11:03:18 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-09-05 11:02:57 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:02:54 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.059 |  |
| 2026-09-05 11:02:42 | Ellagawa (Kalu Ganga) | 4.51 | 🟢 Normal | -0.010 |  |
| 2026-09-05 11:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-09-05 11:02:13 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.031 |  |
| 2026-09-05 11:02:12 | Glencourse (Kelani Ganga) | 9.34 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-09-05 11:02:10 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-09-05 11:02:00 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:01:29 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.020 |  |
| 2026-09-05 11:01:25 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:01:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:01:15 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:01:09 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:01:02 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:00:47 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:00:09 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:00:07 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-05 10:59:45 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-05 11:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-09-05 11:02:12 | Glencourse (Kelani Ganga) | 9.34 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-09-05 11:10:38 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-09-05 11:00:07 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-05 11:03:29 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-05 11:00:09 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:05:55 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:05:57 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:01:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:02:57 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:04:14 | Galgamuwa (Mee Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:01:15 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:01:25 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:01:09 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:02:00 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:05:25 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:04:09 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:02:59 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:04:43 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:00:47 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:06:30 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:22:21 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:05:40 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:01:02 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-05 11:21:33 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | -0.007 |  |
| 2026-09-05 11:09:46 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | -0.009 |  |
| 2026-09-05 11:03:18 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-09-05 11:03:45 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-09-05 11:02:10 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-09-05 11:02:42 | Ellagawa (Kalu Ganga) | 4.51 | 🟢 Normal | -0.010 |  |
| 2026-09-05 11:06:49 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-09-05 11:05:36 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-09-05 11:05:11 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.014 |  |
| 2026-09-05 11:04:46 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | -0.019 |  |
| 2026-09-05 11:01:29 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.020 |  |
| 2026-09-05 11:02:13 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.031 |  |
| 2026-09-05 11:04:08 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-09-05 11:02:54 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.059 |  |
| 2026-09-05 11:03:35 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.192 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)