# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--22_03:03:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,328 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 03:03:04 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | -0.032 |  |
| 2026-11-22 03:02:49 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.000 |  |
| 2026-11-22 03:02:25 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 03:02:23 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-22 03:02:20 | Giriulla (Maha Oya) | 1.99 | 🟢 Normal | -0.040 |  |
| 2026-11-22 03:02:10 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-22 03:02:04 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 03:02:03 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-22 03:01:53 | Moragaswewa (Deduru Oya) | 1.76 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-22 03:01:47 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | -1.715 |  |
| 2026-11-22 03:01:46 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-22 03:01:45 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-22 03:01:21 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.020 |  |
| 2026-11-22 03:01:12 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-11-22 03:00:59 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.152 |  |
| 2026-11-22 03:00:36 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.041 |  |
| 2026-11-22 03:00:23 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-22 02:48:00 | Rathnapura (Kalu Ganga) | 2.24 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-11-22 02:33:00 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -36.000 |  |
| 2026-11-22 02:32:58 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -36.000 |  |
| 2026-11-22 02:22:48 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 02:48:00 | Rathnapura (Kalu Ganga) | 2.24 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-11-22 02:04:10 | Panadugama (Nilwala Ganga) | 4.71 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-22 03:01:53 | Moragaswewa (Deduru Oya) | 1.76 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-22 02:07:57 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-22 00:04:39 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-22 03:00:23 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-22 02:02:22 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 03:02:25 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 18:00:46 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-22 02:01:07 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-22 03:02:23 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-22 03:02:04 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 02:22:48 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:00:19 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-11-22 01:01:46 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-11-22 02:04:27 | Hanwella (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-22 03:02:49 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.000 |  |
| 2026-11-22 02:02:18 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-22 02:07:29 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-22 03:02:10 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:02:22 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-22 02:05:15 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-22 02:07:22 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-11-22 02:20:29 | Urawa (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.016 |  |
| 2026-11-22 01:05:32 | Dunamale (Aththanagalu Oya) | 1.39 | 🟢 Normal | -0.019 |  |
| 2026-11-22 03:01:21 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.020 |  |
| 2026-11-22 03:01:12 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-11-22 03:03:04 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | -0.032 |  |
| 2026-11-22 01:07:54 | Thanamalwila (Kirindi Oya) | 1.68 | 🟢 Normal | -0.039 |  |
| 2026-11-22 03:02:20 | Giriulla (Maha Oya) | 1.99 | 🟢 Normal | -0.040 |  |
| 2026-11-22 03:00:36 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.041 |  |
| 2026-11-22 02:03:06 | Badalgama (Maha Oya) | 3.44 | 🟢 Normal | -0.079 |  |
| 2026-11-22 02:12:23 | Ellagawa (Kalu Ganga) | 5.38 | 🟢 Normal | -0.111 |  |
| 2026-11-22 02:12:22 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.118 |  |
| 2026-11-22 03:00:59 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.152 |  |
| 2026-11-22 03:01:47 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | -1.715 |  |
| 2026-11-22 02:05:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | -2.441 |  |
| 2026-11-22 02:33:00 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)