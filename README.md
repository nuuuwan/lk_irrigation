# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--29_20:23:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **274,452 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 20:23:43 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:13:19 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:12:50 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-09-29 20:11:55 | Baddegama (Gin Ganga) | 2.82 | 🟢 Normal | -0.052 |  |
| 2026-09-29 20:11:07 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:08:09 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:07:35 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-09-29 20:07:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.27 | 🟢 Normal | -0.015 |  |
| 2026-09-29 20:06:00 | Rathnapura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.020 |  |
| 2026-09-29 20:05:44 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-09-29 20:05:29 | Glencourse (Kelani Ganga) | 10.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 20:05:09 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:04:54 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.087 |  |
| 2026-09-29 20:04:46 | Hanwella (Kelani Ganga) | 2.46 | 🟢 Normal | -0.060 |  |
| 2026-09-29 20:04:36 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:04:34 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-09-29 20:04:10 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.029 |  |
| 2026-09-29 20:03:42 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:03:35 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-09-29 20:03:23 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:03:22 | Ellagawa (Kalu Ganga) | 5.66 | 🟢 Normal | -0.059 |  |
| 2026-09-29 20:03:19 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-09-29 20:03:12 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:02:57 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | -0.039 |  |
| 2026-09-29 20:02:54 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:02:49 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:02:42 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 20:02:37 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-09-29 20:02:21 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:02:20 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:02:11 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-09-29 20:01:57 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:01:41 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-09-29 20:01:35 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:00:57 | Manampitiya (Mahaweli Ganga) | -0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:00:43 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 20:03:35 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-09-29 20:00:43 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-29 20:02:42 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 20:05:29 | Glencourse (Kelani Ganga) | 10.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:01:35 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:23:43 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:03:12 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:04:05 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:11:07 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:02:54 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:13:19 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:02:21 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:02:49 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:02:20 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:03:23 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:08:09 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:05:09 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:00:57 | Manampitiya (Mahaweli Ganga) | -0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:00:44 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:04:36 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:03:42 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:01:57 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:07:35 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-09-29 20:12:50 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-09-29 20:03:19 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-09-29 20:02:11 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-09-29 20:01:41 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-09-29 20:02:37 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-09-29 20:07:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.27 | 🟢 Normal | -0.015 |  |
| 2026-09-29 20:04:34 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-09-29 20:05:44 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-09-29 20:06:00 | Rathnapura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.020 |  |
| 2026-09-29 20:04:10 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.029 |  |
| 2026-09-29 20:02:57 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | -0.039 |  |
| 2026-09-29 20:11:55 | Baddegama (Gin Ganga) | 2.82 | 🟢 Normal | -0.052 |  |
| 2026-09-29 20:03:22 | Ellagawa (Kalu Ganga) | 5.66 | 🟢 Normal | -0.059 |  |
| 2026-09-29 20:04:46 | Hanwella (Kelani Ganga) | 2.46 | 🟢 Normal | -0.060 |  |
| 2026-09-29 20:04:54 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.087 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)