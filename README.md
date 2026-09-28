# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--29_03:24:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **273,796 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 03:24:12 | Baddegama (Gin Ganga) | 3.41 | 🟢 Normal | -0.089 |  |
| 2026-09-29 03:21:35 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:13:24 | Rathnapura (Kalu Ganga) | 2.74 | 🟢 Normal | -0.077 |  |
| 2026-09-29 03:12:51 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-09-29 03:11:57 | Panadugama (Nilwala Ganga) | 3.97 | 🟢 Normal | -0.113 |  |
| 2026-09-29 03:11:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.65 | 🟢 Normal | -0.043 |  |
| 2026-09-29 03:11:20 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-29 03:10:35 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | -0.031 |  |
| 2026-09-29 03:09:55 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:07:26 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:07:24 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:06:20 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:05:54 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | -0.027 |  |
| 2026-09-29 03:05:48 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:05:09 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-29 03:05:08 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:04:43 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:04:42 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:04:35 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -36.000 |  |
| 2026-09-29 03:04:34 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | -36.000 |  |
| 2026-09-29 03:04:33 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -36.000 |  |
| 2026-09-29 03:04:29 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:04:07 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:03:57 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:03:48 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | -0.091 |  |
| 2026-09-29 03:03:37 | Siyambalanduwa (Heda Oya) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-09-29 03:02:38 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-29 03:02:34 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 03:02:27 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:02:25 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | -0.041 |  |
| 2026-09-29 03:02:11 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:02:05 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:02:04 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:02:01 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.030 |  |
| 2026-09-29 03:01:48 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:01:40 | Ellagawa (Kalu Ganga) | 5.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 03:01:24 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:01:17 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:00:49 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-29 03:00:47 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:00:41 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.032 | 🔺 Rising |
| 2026-09-29 03:00:08 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:57:14 | Baddegama (Gin Ganga) | 3.45 | 🟢 Normal | -0.089 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 03:00:41 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.032 | 🔺 Rising |
| 2026-09-28 18:02:00 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-29 03:02:38 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-29 03:00:49 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-29 03:01:40 | Ellagawa (Kalu Ganga) | 5.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 03:02:34 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 03:05:09 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-29 03:11:20 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-29 03:02:04 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:02:11 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:02:05 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:05:48 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:01:48 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:04:42 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:00:25 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-29 02:26:14 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:09:55 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:03:57 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:01:24 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:04:07 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:06:20 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:02:27 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:21:35 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:05:08 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:07:26 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:04:29 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 03:12:51 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-09-28 18:01:32 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-09-29 03:03:37 | Siyambalanduwa (Heda Oya) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-09-29 03:05:54 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | -0.027 |  |
| 2026-09-29 03:02:01 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.030 |  |
| 2026-09-29 03:10:35 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | -0.031 |  |
| 2026-09-29 03:02:25 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | -0.041 |  |
| 2026-09-29 03:11:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.65 | 🟢 Normal | -0.043 |  |
| 2026-09-29 03:13:24 | Rathnapura (Kalu Ganga) | 2.74 | 🟢 Normal | -0.077 |  |
| 2026-09-29 03:24:12 | Baddegama (Gin Ganga) | 3.41 | 🟢 Normal | -0.089 |  |
| 2026-09-29 03:03:48 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | -0.091 |  |
| 2026-09-29 03:11:57 | Panadugama (Nilwala Ganga) | 3.97 | 🟢 Normal | -0.113 |  |
| 2026-09-29 03:04:35 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)