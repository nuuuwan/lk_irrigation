# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--04_17:21:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **251,799 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-04 17:21:14 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-04 17:17:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | -0.088 |  |
| 2026-09-04 17:16:55 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:09:19 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-04 17:09:00 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.018 |  |
| 2026-09-04 17:08:19 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-04 17:07:35 | Glencourse (Kelani Ganga) | 9.23 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:06:07 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:05:30 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:05:10 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | -0.018 |  |
| 2026-09-04 17:05:09 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:05:03 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:05:00 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:04:38 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:04:20 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:03:59 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.019 |  |
| 2026-09-04 17:03:59 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | -0.029 |  |
| 2026-09-04 17:03:44 | Thanthirimale (Malwathu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:03:39 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:03:14 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | -475.200 |  |
| 2026-09-04 17:03:13 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | -475.200 |  |
| 2026-09-04 17:03:10 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:02:55 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:02:54 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:02:53 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:02:49 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:02:35 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | -0.041 |  |
| 2026-09-04 17:02:17 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:02:14 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-04 17:02:13 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:02:03 | Thanamalwila (Kirindi Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:01:56 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:01:53 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:01:49 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:01:43 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-09-04 17:01:30 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:00:51 | Nagalagam Street (Kelani Ganga) | 0.50 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-04 17:00:42 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 17:00:30 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.060 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-04 17:09:19 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-04 17:02:14 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-04 17:00:51 | Nagalagam Street (Kelani Ganga) | 0.50 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-04 17:00:42 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 17:08:19 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-04 17:21:14 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-04 17:02:53 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:01:56 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:01:30 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:01:43 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:02:17 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:05:09 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:16:55 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:03:10 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:02:54 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:02:13 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:01:53 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:07:35 | Glencourse (Kelani Ganga) | 9.23 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:04:20 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:02:49 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:02:55 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:05:30 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:05:00 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:03:39 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:03:44 | Thanthirimale (Malwathu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:06:07 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:05:03 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:01:49 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-04 17:02:03 | Thanamalwila (Kirindi Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-04 16:44:32 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.007 |  |
| 2026-09-04 17:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-09-04 17:05:10 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | -0.018 |  |
| 2026-09-04 17:09:00 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.018 |  |
| 2026-09-04 17:03:59 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.019 |  |
| 2026-09-04 17:03:59 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | -0.029 |  |
| 2026-09-04 17:02:35 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | -0.041 |  |
| 2026-09-04 17:00:30 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.060 |  |
| 2026-09-04 17:17:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | -0.088 |  |
| 2026-09-04 17:03:14 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | -475.200 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)