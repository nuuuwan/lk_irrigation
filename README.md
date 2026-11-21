# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--22_02:33:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,310 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 02:33:00 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -36.000 |  |
| 2026-11-22 02:32:58 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -36.000 |  |
| 2026-11-22 02:22:48 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-11-22 02:20:29 | Urawa (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.016 |  |
| 2026-11-22 02:12:23 | Ellagawa (Kalu Ganga) | 5.38 | 🟢 Normal | -0.111 |  |
| 2026-11-22 02:12:22 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.118 |  |
| 2026-11-22 02:07:57 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-22 02:07:29 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-22 02:07:22 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-11-22 02:06:46 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | -0.028 |  |
| 2026-11-22 02:05:33 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.168 |  |
| 2026-11-22 02:05:29 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-22 02:05:15 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-22 02:05:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | -2.441 |  |
| 2026-11-22 02:04:27 | Hanwella (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-22 02:04:10 | Panadugama (Nilwala Ganga) | 4.71 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-22 02:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.34 | 🟢 Normal | -2.441 |  |
| 2026-11-22 02:03:34 | Moraketiya (Walawe Ganga) | 2.96 | 🟢 Normal | 0.000 |  |
| 2026-11-22 02:03:20 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 02:03:06 | Badalgama (Maha Oya) | 3.44 | 🟢 Normal | -0.079 |  |
| 2026-11-22 02:02:32 | Moragaswewa (Deduru Oya) | 1.72 | 🟢 Normal | 0.377 | 🔺 Rising |
| 2026-11-22 02:02:22 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 02:02:18 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-22 02:01:51 | Giriulla (Maha Oya) | 2.03 | 🟢 Normal | -0.050 |  |
| 2026-11-22 02:01:38 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | -0.020 |  |
| 2026-11-22 02:01:36 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.040 |  |
| 2026-11-22 02:01:07 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-22 02:01:07 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.021 |  |
| 2026-11-22 02:00:37 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-22 02:00:12 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 02:02:32 | Moragaswewa (Deduru Oya) | 1.72 | 🟢 Normal | 0.377 | 🔺 Rising |
| 2026-11-22 01:35:56 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-11-22 02:05:29 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-22 02:04:10 | Panadugama (Nilwala Ganga) | 4.71 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-22 02:07:57 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-22 00:04:39 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-22 02:02:22 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 02:03:20 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 18:00:46 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-22 02:00:37 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-22 02:01:07 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-22 01:01:27 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 02:22:48 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:00:19 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-11-22 01:01:46 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-11-22 02:04:27 | Hanwella (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-22 02:03:34 | Moraketiya (Walawe Ganga) | 2.96 | 🟢 Normal | 0.000 |  |
| 2026-11-22 02:02:18 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-22 02:07:29 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-22 00:02:55 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:02:22 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-22 01:20:28 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.008 |  |
| 2026-11-22 02:05:15 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-22 02:07:22 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-11-22 02:20:29 | Urawa (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.016 |  |
| 2026-11-22 01:05:32 | Dunamale (Aththanagalu Oya) | 1.39 | 🟢 Normal | -0.019 |  |
| 2026-11-22 02:01:38 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | -0.020 |  |
| 2026-11-22 02:01:07 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.021 |  |
| 2026-11-22 02:06:46 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | -0.028 |  |
| 2026-11-22 01:07:54 | Thanamalwila (Kirindi Oya) | 1.68 | 🟢 Normal | -0.039 |  |
| 2026-11-22 02:01:36 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.040 |  |
| 2026-11-22 02:01:51 | Giriulla (Maha Oya) | 2.03 | 🟢 Normal | -0.050 |  |
| 2026-11-22 02:03:06 | Badalgama (Maha Oya) | 3.44 | 🟢 Normal | -0.079 |  |
| 2026-11-22 02:12:23 | Ellagawa (Kalu Ganga) | 5.38 | 🟢 Normal | -0.111 |  |
| 2026-11-22 02:12:22 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.118 |  |
| 2026-11-22 02:05:33 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.168 |  |
| 2026-11-22 02:05:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | -2.441 |  |
| 2026-11-22 02:33:00 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)