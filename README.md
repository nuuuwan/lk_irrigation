# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_08:08:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **221,883 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 08:08:37 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | 0.275 | 🔺 Rising |
| 2026-08-01 08:07:25 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 08:07:02 | Rathnapura (Kalu Ganga) | 4.32 | 🟢 Normal | 0.629 | 🔺 Rising |
| 2026-08-01 08:06:56 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-01 08:06:17 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 08:05:02 | Holombuwa (Kelani Ganga) | 3.35 | 🟡 Alert | -0.516 |  |
| 2026-08-01 08:04:35 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 08:04:34 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-01 08:04:30 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 08:04:27 | Kithulgala (Kelani Ganga) | 3.00 | 🟡 Alert | -0.503 |  |
| 2026-08-01 08:04:23 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-08-01 08:04:05 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.041 |  |
| 2026-08-01 08:04:03 | Deraniyagala (Kelani Ganga) | 4.30 | 🟢 Normal | -0.906 |  |
| 2026-08-01 08:03:20 | Hanwella (Kelani Ganga) | 2.18 | 🟢 Normal | 0.632 | 🔺 Rising |
| 2026-08-01 08:03:19 | Glencourse (Kelani Ganga) | 13.85 | 🟢 Normal | 0.902 | 🔺 Rising |
| 2026-08-01 08:03:05 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-01 08:02:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.73 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-08-01 08:02:55 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-01 08:02:46 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-01 08:02:40 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 08:02:33 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.154 |  |
| 2026-08-01 08:02:15 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-01 08:02:08 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 08:02:03 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-01 08:01:59 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-01 08:01:42 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-01 08:01:36 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.022 |  |
| 2026-08-01 08:01:29 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | 0.000 |  |
| 2026-08-01 08:01:21 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-01 08:01:11 | Nawalapitiya (Mahaweli Ganga) | 4.15 | 🟡 Alert | -0.564 |  |
| 2026-08-01 08:00:08 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:57:30 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:44:03 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:21:13 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 08:04:27 | Kithulgala (Kelani Ganga) | 3.00 | 🟡 Alert | -0.503 |  |
| 2026-08-01 08:05:02 | Holombuwa (Kelani Ganga) | 3.35 | 🟡 Alert | -0.516 |  |
| 2026-08-01 08:01:11 | Nawalapitiya (Mahaweli Ganga) | 4.15 | 🟡 Alert | -0.564 |  |
| 2026-08-01 08:03:19 | Glencourse (Kelani Ganga) | 13.85 | 🟢 Normal | 0.902 | 🔺 Rising |
| 2026-08-01 08:03:20 | Hanwella (Kelani Ganga) | 2.18 | 🟢 Normal | 0.632 | 🔺 Rising |
| 2026-08-01 08:07:02 | Rathnapura (Kalu Ganga) | 4.32 | 🟢 Normal | 0.629 | 🔺 Rising |
| 2026-08-01 07:05:26 | Peradeniya (Mahaweli Ganga) | 4.72 | 🟢 Normal | 0.564 | 🔺 Rising |
| 2026-08-01 08:08:37 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | 0.275 | 🔺 Rising |
| 2026-08-01 08:02:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.73 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-08-01 07:12:17 | Magura (Kalu Ganga) | 2.98 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-08-01 08:03:05 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-01 08:02:03 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-01 08:02:46 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-01 08:04:34 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-01 08:02:15 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-01 08:04:30 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 08:02:40 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 08:01:21 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-01 08:00:08 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:00:40 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:01:51 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 08:02:08 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 08:07:25 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 08:06:56 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-01 08:01:29 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:44:03 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-08-01 08:06:17 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:06:50 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-01 08:04:35 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 08:04:23 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-08-01 08:01:59 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:14:59 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-01 08:02:55 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-01 07:05:22 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-08-01 08:01:36 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.022 |  |
| 2026-08-01 07:16:13 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.032 |  |
| 2026-08-01 08:04:05 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.041 |  |
| 2026-08-01 08:02:33 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.154 |  |
| 2026-08-01 08:04:03 | Deraniyagala (Kelani Ganga) | 4.30 | 🟢 Normal | -0.906 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)