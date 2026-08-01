# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_11:23:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **222,007 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 11:23:53 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-01 11:13:10 | Magura (Kalu Ganga) | 3.12 | 🟢 Normal | -0.009 |  |
| 2026-08-01 11:11:32 | Giriulla (Maha Oya) | 2.60 | 🟢 Normal | 1.242 | 🔺 Rising |
| 2026-08-01 11:10:23 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:09:36 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-08-01 11:08:22 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:07:36 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:06:37 | Glencourse (Kelani Ganga) | 14.90 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-08-01 11:06:29 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-08-01 11:06:27 | Rathnapura (Kalu Ganga) | 4.55 | 🟢 Normal | -0.095 |  |
| 2026-08-01 11:06:15 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:06:11 | Peradeniya (Mahaweli Ganga) | 5.90 | 🟡 Alert | -0.102 |  |
| 2026-08-01 11:05:50 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-01 11:04:47 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:04:06 | Holombuwa (Kelani Ganga) | 1.90 | 🟢 Normal | -0.442 |  |
| 2026-08-01 11:04:03 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:04:01 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-01 11:03:47 | Hanwella (Kelani Ganga) | 4.34 | 🟢 Normal | 0.539 | 🔺 Rising |
| 2026-08-01 11:03:41 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.032 |  |
| 2026-08-01 11:03:37 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-01 11:03:18 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:03:05 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:02:57 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.05 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-08-01 11:02:33 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:02:28 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:02:28 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:02:27 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.005 |  |
| 2026-08-01 11:02:20 | Nawalapitiya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.416 |  |
| 2026-08-01 11:02:11 | Deraniyagala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.458 |  |
| 2026-08-01 11:02:09 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:01:55 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-08-01 11:01:34 | Thanthirimale (Malwathu Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:01:17 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | 0.433 | 🔺 Rising |
| 2026-08-01 11:01:14 | Kithulgala (Kelani Ganga) | 2.38 | 🟢 Normal | -0.173 |  |
| 2026-08-01 11:00:55 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:00:51 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:00:18 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 11:06:11 | Peradeniya (Mahaweli Ganga) | 5.90 | 🟡 Alert | -0.102 |  |
| 2026-08-01 11:11:32 | Giriulla (Maha Oya) | 2.60 | 🟢 Normal | 1.242 | 🔺 Rising |
| 2026-08-01 11:03:47 | Hanwella (Kelani Ganga) | 4.34 | 🟢 Normal | 0.539 | 🔺 Rising |
| 2026-08-01 11:01:17 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | 0.433 | 🔺 Rising |
| 2026-08-01 11:06:37 | Glencourse (Kelani Ganga) | 14.90 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-08-01 11:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.05 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-08-01 11:04:01 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-01 11:23:53 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-01 11:05:50 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-01 11:03:37 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-01 11:00:51 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-01 10:01:54 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:02:09 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:00:55 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:02:33 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:03:05 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:08:22 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:02:57 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:06:15 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:02:28 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:02:28 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:03:18 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:04:03 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:04:47 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:10:23 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:01:34 | Thanthirimale (Malwathu Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:00:18 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:07:36 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 11:02:27 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.005 |  |
| 2026-08-01 11:13:10 | Magura (Kalu Ganga) | 3.12 | 🟢 Normal | -0.009 |  |
| 2026-08-01 11:09:36 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-08-01 11:01:55 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-08-01 11:06:29 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-08-01 11:03:41 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.032 |  |
| 2026-08-01 11:06:27 | Rathnapura (Kalu Ganga) | 4.55 | 🟢 Normal | -0.095 |  |
| 2026-08-01 11:01:14 | Kithulgala (Kelani Ganga) | 2.38 | 🟢 Normal | -0.173 |  |
| 2026-08-01 11:02:20 | Nawalapitiya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.416 |  |
| 2026-08-01 11:04:06 | Holombuwa (Kelani Ganga) | 1.90 | 🟢 Normal | -0.442 |  |
| 2026-08-01 11:02:11 | Deraniyagala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.458 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)