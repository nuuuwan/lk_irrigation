# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--07_11:08:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **39,019 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 11:08:45 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.009 |  |
| 2026-01-07 11:07:44 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.012 |  |
| 2026-01-07 11:07:42 | Peradeniya (Mahaweli Ganga) | 2.17 | 🟢 Normal | -0.028 |  |
| 2026-01-07 11:06:41 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-01-07 11:06:38 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-07 11:05:52 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.010 |  |
| 2026-01-07 11:05:13 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | -0.011 |  |
| 2026-01-07 11:05:03 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-01-07 11:04:47 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-01-07 11:04:45 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-07 11:04:44 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-07 11:04:21 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-01-07 11:03:26 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-07 11:03:14 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-01-07 11:03:06 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.041 |  |
| 2026-01-07 11:02:52 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.011 |  |
| 2026-01-07 11:02:34 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 11:02:30 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.023 |  |
| 2026-01-07 11:02:25 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-07 11:02:22 | Katharagama (Menik Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-07 11:02:19 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.091 |  |
| 2026-01-07 11:02:17 | Manampitiya (Mahaweli Ganga) | 2.84 | 🟢 Normal | -0.030 |  |
| 2026-01-07 11:02:09 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-07 11:02:07 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 11:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.030 |  |
| 2026-01-07 11:01:55 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-07 11:01:54 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.101 |  |
| 2026-01-07 11:01:49 | Siyambalanduwa (Heda Oya) | 1.76 | 🟢 Normal | -0.059 |  |
| 2026-01-07 11:01:32 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-07 11:01:21 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-01-07 11:01:16 | Weraganthota (Mahaweli Ganga) | -1.04 | 🟢 Normal | -0.010 |  |
| 2026-01-07 11:01:15 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-01-07 11:00:56 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-07 11:00:52 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-07 11:00:39 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-01-07 11:00:08 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-01-07 10:23:29 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-07 10:18:58 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.012 |  |
| 2026-01-07 10:14:11 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:13:33 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 11:04:47 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-01-07 11:03:26 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-07 11:04:44 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-07 11:02:34 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 11:04:45 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-07 11:02:07 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 10:01:13 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-07 11:01:55 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-07 11:02:09 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:04:57 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-07 11:00:56 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-07 11:02:25 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:04:08 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-07 11:06:38 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-07 11:00:52 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-07 11:01:32 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-07 11:08:45 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.009 |  |
| 2026-01-07 11:05:52 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.010 |  |
| 2026-01-07 11:02:22 | Katharagama (Menik Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-07 11:01:21 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-01-07 11:01:16 | Weraganthota (Mahaweli Ganga) | -1.04 | 🟢 Normal | -0.010 |  |
| 2026-01-07 11:00:08 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-01-07 11:00:39 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-01-07 11:03:14 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-01-07 11:05:03 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-01-07 11:01:15 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-01-07 11:05:13 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | -0.011 |  |
| 2026-01-07 11:02:52 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.011 |  |
| 2026-01-07 11:07:44 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.012 |  |
| 2026-01-07 11:04:21 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-01-07 11:02:30 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.023 |  |
| 2026-01-07 11:07:42 | Peradeniya (Mahaweli Ganga) | 2.17 | 🟢 Normal | -0.028 |  |
| 2026-01-07 11:02:17 | Manampitiya (Mahaweli Ganga) | 2.84 | 🟢 Normal | -0.030 |  |
| 2026-01-07 11:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.030 |  |
| 2026-01-07 11:06:41 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-01-07 11:03:06 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.041 |  |
| 2026-01-07 11:01:49 | Siyambalanduwa (Heda Oya) | 1.76 | 🟢 Normal | -0.059 |  |
| 2026-01-07 11:02:19 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.091 |  |
| 2026-01-07 11:01:54 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)