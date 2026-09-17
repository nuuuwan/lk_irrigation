# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_11:17:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **263,294 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 11:17:28 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:15:54 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-09-17 11:14:20 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:11:03 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:09:35 | Panadugama (Nilwala Ganga) | 4.67 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-09-17 11:09:26 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | -0.009 |  |
| 2026-09-17 11:08:31 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-09-17 11:08:03 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:07:31 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:06:05 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-09-17 11:05:36 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:05:35 | Baddegama (Gin Ganga) | 3.60 | 🟡 Alert | 0.000 |  |
| 2026-09-17 11:04:42 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:04:40 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | -0.010 |  |
| 2026-09-17 11:04:30 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | -0.041 |  |
| 2026-09-17 11:04:15 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:04:05 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-09-17 11:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.39 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-17 11:03:56 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.030 |  |
| 2026-09-17 11:03:43 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:03:18 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-17 11:02:55 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:02:44 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | -0.041 |  |
| 2026-09-17 11:02:40 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.005 |  |
| 2026-09-17 11:02:35 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:02:24 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.091 |  |
| 2026-09-17 11:02:21 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-17 11:02:19 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:02:18 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:02:17 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:02:09 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:02:00 | Magura (Kalu Ganga) | 3.54 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-17 11:01:59 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-09-17 11:01:46 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:01:46 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:01:41 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-17 11:01:34 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.033 |  |
| 2026-09-17 11:01:30 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:00:38 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:00:34 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:00:16 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 11:05:35 | Baddegama (Gin Ganga) | 3.60 | 🟡 Alert | 0.000 |  |
| 2026-09-17 11:02:00 | Magura (Kalu Ganga) | 3.54 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-17 11:01:41 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-17 11:09:35 | Panadugama (Nilwala Ganga) | 4.67 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-09-17 11:15:54 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-09-17 11:02:21 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-17 11:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.39 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-17 11:03:18 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-17 11:03:43 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:01:30 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:02:18 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:00:34 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:02:35 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:14:20 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:00:38 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:04:42 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:00:16 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:08:03 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:02:17 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:07:31 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:04:15 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:02:19 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:01:46 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:02:09 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:05:36 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:17:28 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:01:46 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:02:40 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.005 |  |
| 2026-09-17 11:09:26 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | -0.009 |  |
| 2026-09-17 11:04:40 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | -0.010 |  |
| 2026-09-17 11:01:59 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-09-17 11:04:05 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-09-17 11:08:31 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-09-17 11:06:05 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-09-17 11:03:56 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.030 |  |
| 2026-09-17 11:01:34 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.033 |  |
| 2026-09-17 11:04:30 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | -0.041 |  |
| 2026-09-17 11:02:44 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | -0.041 |  |
| 2026-09-17 11:02:24 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)