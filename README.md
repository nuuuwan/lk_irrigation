# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--06_11:30:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **253,383 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-06 11:30:48 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:25:22 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:17:43 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-09-06 11:12:54 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:12:54 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | -0.027 |  |
| 2026-09-06 11:10:41 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:10:39 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:08:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.89 | 🟢 Normal | -0.068 |  |
| 2026-09-06 11:08:00 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-06 11:07:08 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-06 11:06:43 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-06 11:06:42 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:06:36 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:05:49 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.015 |  |
| 2026-09-06 11:05:43 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:04:51 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:04:51 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:04:47 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:04:34 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:04:17 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:04:05 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-06 11:03:32 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:03:13 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-06 11:02:38 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.040 |  |
| 2026-09-06 11:02:28 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:02:27 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.030 |  |
| 2026-09-06 11:02:27 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-09-06 11:02:25 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:02:21 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:02:07 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:01:50 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:01:36 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:01:26 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:01:20 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-09-06 11:01:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:00:50 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.020 |  |
| 2026-09-06 11:00:42 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-09-06 11:00:38 | Ellagawa (Kalu Ganga) | 4.59 | 🟢 Normal | -0.013 |  |
| 2026-09-06 11:00:25 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:00:23 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.040 |  |
| 2026-09-06 11:00:15 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-06 11:08:00 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-06 11:06:43 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-06 11:04:05 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-06 11:07:08 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-06 11:03:13 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-06 11:04:34 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:00:25 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:06:36 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:01:36 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:06:42 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-06 10:00:47 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:02:21 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:10:39 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:04:51 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:01:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:05:43 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:02:28 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:25:22 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:02:25 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:03:32 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:04:51 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:02:07 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:01:26 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:12:54 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:30:48 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:00:15 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:04:17 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-06 11:17:43 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-09-06 11:01:20 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-09-06 11:00:42 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-09-06 11:02:27 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-09-06 11:00:38 | Ellagawa (Kalu Ganga) | 4.59 | 🟢 Normal | -0.013 |  |
| 2026-09-06 11:05:49 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.015 |  |
| 2026-09-06 11:00:50 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.020 |  |
| 2026-09-06 11:12:54 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | -0.027 |  |
| 2026-09-06 11:02:27 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.030 |  |
| 2026-09-06 11:00:23 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.040 |  |
| 2026-09-06 11:02:38 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.040 |  |
| 2026-09-06 11:08:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.89 | 🟢 Normal | -0.068 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)