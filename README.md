# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_10:07:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **263,243 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 10:07:11 | Baddegama (Gin Ganga) | 3.60 | 🟡 Alert | 0.024 | 🔺 Rising |
| 2026-09-17 10:07:06 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-09-17 10:07:01 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-09-17 10:06:53 | Glencourse (Kelani Ganga) | 9.64 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-17 10:06:33 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-09-17 10:06:08 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-17 10:05:45 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-09-17 10:05:36 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-17 10:05:35 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | -0.011 |  |
| 2026-09-17 10:05:23 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | -0.048 |  |
| 2026-09-17 10:05:17 | Magura (Kalu Ganga) | 3.47 | 🟢 Normal | 0.000 |  |
| 2026-09-17 10:05:02 | Panadugama (Nilwala Ganga) | 4.60 | 🟢 Normal | 0.423 | 🔺 Rising |
| 2026-09-17 10:04:53 | Ellagawa (Kalu Ganga) | 4.91 | 🟢 Normal | -0.020 |  |
| 2026-09-17 10:04:49 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-09-17 10:04:19 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-09-17 10:04:17 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.040 |  |
| 2026-09-17 10:03:44 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-17 10:03:34 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.060 |  |
| 2026-09-17 10:03:17 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-09-17 10:03:17 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.031 |  |
| 2026-09-17 10:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 10:02:37 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-09-17 10:02:33 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-17 10:02:21 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-17 10:02:16 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 10:01:46 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-09-17 10:01:40 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-17 10:01:33 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-17 10:01:08 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 10:00:05 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 10:07:11 | Baddegama (Gin Ganga) | 3.60 | 🟡 Alert | 0.024 | 🔺 Rising |
| 2026-09-17 10:05:02 | Panadugama (Nilwala Ganga) | 4.60 | 🟢 Normal | 0.423 | 🔺 Rising |
| 2026-09-17 10:06:33 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-09-17 10:04:49 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-09-17 10:01:33 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-17 10:07:06 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-09-17 10:06:53 | Glencourse (Kelani Ganga) | 9.64 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-17 10:00:05 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-17 09:09:31 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 10:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 10:01:46 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-09-17 09:03:56 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-17 10:01:08 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 09:03:45 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-17 10:02:16 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 10:01:40 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-17 10:05:17 | Magura (Kalu Ganga) | 3.47 | 🟢 Normal | 0.000 |  |
| 2026-09-17 10:02:21 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-17 10:06:08 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-17 09:00:10 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-17 10:07:01 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-09-17 10:05:36 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-17 10:02:37 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-09-17 10:03:44 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-17 09:00:44 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-17 09:04:51 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-17 10:02:33 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-17 10:03:17 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-09-17 10:04:19 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-09-17 10:05:45 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-09-17 10:05:35 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | -0.011 |  |
| 2026-09-17 09:13:26 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.012 |  |
| 2026-09-17 10:04:53 | Ellagawa (Kalu Ganga) | 4.91 | 🟢 Normal | -0.020 |  |
| 2026-09-17 10:03:17 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.031 |  |
| 2026-09-17 09:01:55 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.032 |  |
| 2026-09-17 10:04:17 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.040 |  |
| 2026-09-17 10:05:23 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | -0.048 |  |
| 2026-09-17 10:03:34 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.060 |  |
| 2026-09-17 09:03:35 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)