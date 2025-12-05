# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--06_01:21:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,356 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-06 01:21:03 | Katharagama (Menik Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-06 01:19:04 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2025-12-06 01:10:01 | Rathnapura (Kalu Ganga) | 2.75 | 🟢 Normal | -0.019 |  |
| 2025-12-06 01:09:32 | Ellagawa (Kalu Ganga) | 6.39 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-06 01:08:32 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-06 01:07:16 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-06 01:06:49 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.038 |  |
| 2025-12-06 01:06:26 | Katharagama (Menik Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-06 01:05:17 | Baddegama (Gin Ganga) | 2.44 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2025-12-06 01:04:41 | Hanwella (Kelani Ganga) | 3.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-06 01:03:45 | Glencourse (Kelani Ganga) | 10.62 | 🟢 Normal | -0.066 |  |
| 2025-12-06 01:03:20 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | -0.010 |  |
| 2025-12-06 01:03:17 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-06 01:03:13 | Thanthirimale (Malwathu Oya) | 6.73 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2025-12-06 01:02:23 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-06 01:02:05 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-06 01:01:40 | Nakkala (Kumbukkan Oya) | 1.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 01:01:33 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 01:01:24 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.024 |  |
| 2025-12-06 01:01:15 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-06 01:01:15 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-06 01:01:04 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.010 |  |
| 2025-12-06 01:00:25 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-06 00:11:12 | Magura (Kalu Ganga) | 4.16 | 🟡 Alert | 0.453 | 🔺 Rising |
| 2025-12-06 01:03:13 | Thanthirimale (Malwathu Oya) | 6.73 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2025-12-06 01:05:17 | Baddegama (Gin Ganga) | 2.44 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2025-12-06 01:09:32 | Ellagawa (Kalu Ganga) | 6.39 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-06 01:03:17 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-05 18:01:43 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-05 18:04:31 | Galgamuwa (Mee Oya) | 0.79 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-06 01:07:16 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-06 01:08:32 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-05 16:03:28 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-06 00:16:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2025-12-06 01:04:41 | Hanwella (Kelani Ganga) | 3.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-06 01:01:15 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-06 01:19:04 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2025-12-06 01:01:40 | Nakkala (Kumbukkan Oya) | 1.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 01:01:33 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 01:00:25 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-06 01:02:05 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:09:31 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:06:05 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:10:53 | Panadugama (Nilwala Ganga) | 4.33 | 🟢 Normal | 0.000 |  |
| 2025-12-06 01:02:23 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-06 01:21:03 | Katharagama (Menik Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:06:18 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:09:53 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:12:14 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:15:20 | Urawa (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.008 |  |
| 2025-12-06 01:03:20 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | -0.010 |  |
| 2025-12-06 01:01:04 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.010 |  |
| 2025-12-06 01:01:15 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-06 01:10:01 | Rathnapura (Kalu Ganga) | 2.75 | 🟢 Normal | -0.019 |  |
| 2025-12-06 01:01:24 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.024 |  |
| 2025-12-06 01:06:49 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.038 |  |
| 2025-12-06 00:03:14 | Holombuwa (Kelani Ganga) | 1.06 | 🟢 Normal | -0.054 |  |
| 2025-12-06 01:03:45 | Glencourse (Kelani Ganga) | 10.62 | 🟢 Normal | -0.066 |  |
| 2025-12-06 00:15:50 | Thawalama (Gin Ganga) | 3.30 | 🟢 Normal | -0.077 |  |
| 2025-12-05 18:05:43 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.177 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)