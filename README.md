# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--01_17:16:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,064 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 17:16:07 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | 1.200 | 🔺 Rising |
| 2026-11-01 17:12:21 | Panadugama (Nilwala Ganga) | 4.66 | 🟢 Normal | -0.010 |  |
| 2026-11-01 17:11:33 | Glencourse (Kelani Ganga) | 10.06 | 🟢 Normal | -0.092 |  |
| 2026-11-01 17:08:22 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 17:08:10 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-11-01 17:06:59 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-01 17:06:22 | Dunamale (Aththanagalu Oya) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-11-01 17:05:43 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.041 |  |
| 2026-11-01 17:05:00 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-11-01 17:04:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-01 17:04:07 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 17:04:07 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-01 17:04:01 | Ellagawa (Kalu Ganga) | 6.09 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-01 17:03:43 | Baddegama (Gin Ganga) | 2.61 | 🟢 Normal | -0.030 |  |
| 2026-11-01 17:03:37 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 1.200 | 🔺 Rising |
| 2026-11-01 17:03:36 | Deraniyagala (Kelani Ganga) | 1.17 | 🟢 Normal | 0.275 | 🔺 Rising |
| 2026-11-01 17:03:30 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 17:03:06 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-01 17:03:05 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-01 17:02:59 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-11-01 17:02:55 | Hanwella (Kelani Ganga) | 2.25 | 🟢 Normal | -0.041 |  |
| 2026-11-01 17:02:38 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-11-01 17:02:37 | Pitabeddara (Nilwala Ganga) | 1.36 | 🟢 Normal | -0.021 |  |
| 2026-11-01 17:02:36 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 17:02:15 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-01 17:02:15 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 17:01:56 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-01 17:01:54 | Galgamuwa (Mee Oya) | 0.99 | 🟢 Normal | -0.031 |  |
| 2026-11-01 17:01:42 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2026-11-01 17:01:37 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 17:00:19 | Thalgahagoda (Nilwala Ganga) | 1.51 | 🟡 Alert | -0.020 |  |
| 2026-11-01 17:16:07 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | 1.200 | 🔺 Rising |
| 2026-11-01 17:03:36 | Deraniyagala (Kelani Ganga) | 1.17 | 🟢 Normal | 0.275 | 🔺 Rising |
| 2026-11-01 17:00:09 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-11-01 17:08:10 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-11-01 17:00:46 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-01 17:05:00 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-11-01 17:01:13 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-01 17:04:01 | Ellagawa (Kalu Ganga) | 6.09 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-01 17:03:06 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-01 17:04:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-01 17:04:07 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 17:02:36 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 17:03:30 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 17:01:29 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-01 17:06:59 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-01 17:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-01 17:01:37 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 17:04:07 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-01 17:01:56 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-01 17:02:15 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 17:02:38 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-11-01 17:01:06 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 17:03:05 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-01 17:08:22 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 17:02:15 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-01 17:12:21 | Panadugama (Nilwala Ganga) | 4.66 | 🟢 Normal | -0.010 |  |
| 2026-11-01 17:00:28 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | -0.012 |  |
| 2026-11-01 17:06:22 | Dunamale (Aththanagalu Oya) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-11-01 17:02:59 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-11-01 17:02:37 | Pitabeddara (Nilwala Ganga) | 1.36 | 🟢 Normal | -0.021 |  |
| 2026-11-01 17:03:43 | Baddegama (Gin Ganga) | 2.61 | 🟢 Normal | -0.030 |  |
| 2026-11-01 17:01:29 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.030 |  |
| 2026-11-01 17:01:42 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2026-11-01 17:01:54 | Galgamuwa (Mee Oya) | 0.99 | 🟢 Normal | -0.031 |  |
| 2026-11-01 17:05:43 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.041 |  |
| 2026-11-01 17:02:55 | Hanwella (Kelani Ganga) | 2.25 | 🟢 Normal | -0.041 |  |
| 2026-11-01 17:01:19 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.045 |  |
| 2026-11-01 17:11:33 | Glencourse (Kelani Ganga) | 10.06 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)