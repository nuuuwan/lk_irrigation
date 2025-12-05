# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--05_06:33:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,687 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-05 06:33:31 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.004 |  |
| 2025-12-05 06:21:07 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2025-12-05 06:13:10 | Hanwella (Kelani Ganga) | 3.55 | 🟢 Normal | -0.018 |  |
| 2025-12-05 06:09:52 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | -0.009 |  |
| 2025-12-05 06:09:45 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-05 06:08:26 | Thanthirimale (Malwathu Oya) | 5.66 | 🟡 Alert | 1.050 | 🔺 Rising |
| 2025-12-05 06:08:18 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.114 |  |
| 2025-12-05 06:07:44 | Badalgama (Maha Oya) | 3.01 | 🟢 Normal | 0.000 |  |
| 2025-12-05 06:06:07 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-05 06:05:53 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-05 06:05:00 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.009 |  |
| 2025-12-05 06:04:34 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 06:04:20 | Rathnapura (Kalu Ganga) | 2.74 | 🟢 Normal | -0.110 |  |
| 2025-12-05 06:03:59 | Panadugama (Nilwala Ganga) | 4.74 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2025-12-05 06:03:44 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-05 06:03:38 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 06:03:10 | Magura (Kalu Ganga) | 2.67 | 🟢 Normal | -648.000 |  |
| 2025-12-05 06:03:09 | Magura (Kalu Ganga) | 2.85 | 🟢 Normal | -648.000 |  |
| 2025-12-05 06:03:07 | Magura (Kalu Ganga) | 3.02 | 🟢 Normal | -648.000 |  |
| 2025-12-05 06:03:04 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | -0.075 |  |
| 2025-12-05 06:02:58 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.059 |  |
| 2025-12-05 06:02:57 | Giriulla (Maha Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2025-12-05 06:02:54 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-05 06:02:39 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | -0.051 |  |
| 2025-12-05 06:02:31 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2025-12-05 06:01:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | 1.088 | 🔺 Rising |
| 2025-12-05 06:01:42 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | -0.061 |  |
| 2025-12-05 06:01:30 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.025 |  |
| 2025-12-05 06:01:28 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2025-12-05 06:01:27 | Pitabeddara (Nilwala Ganga) | 2.16 | 🟢 Normal | -0.142 |  |
| 2025-12-05 06:01:22 | Urawa (Nilwala Ganga) | 1.51 | 🟢 Normal | -0.799 |  |
| 2025-12-05 06:01:20 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2025-12-05 06:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-05 06:00:15 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-05 06:00:09 | Siyambalanduwa (Heda Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-05 05:43:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | 1.088 | 🔺 Rising |
| 2025-12-05 05:41:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.21 | 🟢 Normal | 1.088 | 🔺 Rising |
| 2025-12-05 05:39:22 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-05 06:08:26 | Thanthirimale (Malwathu Oya) | 5.66 | 🟡 Alert | 1.050 | 🔺 Rising |
| 2025-12-05 06:01:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | 1.088 | 🔺 Rising |
| 2025-12-05 06:03:59 | Panadugama (Nilwala Ganga) | 4.74 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2025-12-05 06:01:28 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2025-12-05 06:09:45 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-05 06:01:20 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2025-12-05 06:05:53 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-05 06:04:34 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 06:33:31 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.004 |  |
| 2025-12-05 06:02:31 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2025-12-05 06:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-05 06:06:07 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-05 06:21:07 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:01:47 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-05 06:00:09 | Siyambalanduwa (Heda Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:04:32 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 06:03:38 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 06:07:44 | Badalgama (Maha Oya) | 3.01 | 🟢 Normal | 0.000 |  |
| 2025-12-05 06:02:54 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-05 06:09:52 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | -0.009 |  |
| 2025-12-05 06:05:00 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.009 |  |
| 2025-12-05 06:02:57 | Giriulla (Maha Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2025-12-05 06:03:44 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-05 06:00:15 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-05 06:13:10 | Hanwella (Kelani Ganga) | 3.55 | 🟢 Normal | -0.018 |  |
| 2025-12-05 06:01:30 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.025 |  |
| 2025-12-04 19:33:02 | Manampitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.027 |  |
| 2025-12-04 18:08:34 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | -0.047 |  |
| 2025-12-05 06:02:39 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | -0.051 |  |
| 2025-12-05 06:02:58 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.059 |  |
| 2025-12-05 06:01:42 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | -0.061 |  |
| 2025-12-05 06:03:04 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | -0.075 |  |
| 2025-12-05 06:04:20 | Rathnapura (Kalu Ganga) | 2.74 | 🟢 Normal | -0.110 |  |
| 2025-12-05 06:08:18 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.114 |  |
| 2025-12-05 06:01:27 | Pitabeddara (Nilwala Ganga) | 2.16 | 🟢 Normal | -0.142 |  |
| 2025-12-05 06:01:22 | Urawa (Nilwala Ganga) | 1.51 | 🟢 Normal | -0.799 |  |
| 2025-12-05 06:03:10 | Magura (Kalu Ganga) | 2.67 | 🟢 Normal | -648.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)