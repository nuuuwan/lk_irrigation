# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_01:14:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,889 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 01:14:49 | Hanwella (Kelani Ganga) | 2.06 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-09 01:11:47 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 01:10:54 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-09 01:06:00 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2025-12-09 01:05:23 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-09 01:04:44 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.087 |  |
| 2025-12-09 01:04:29 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-09 01:03:29 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-09 01:03:28 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2025-12-09 01:03:16 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-09 01:03:08 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2025-12-09 01:03:05 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-09 01:02:45 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-09 01:02:39 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.017 |  |
| 2025-12-09 01:02:30 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-09 01:02:20 | Rathnapura (Kalu Ganga) | 3.32 | 🟢 Normal | -0.075 |  |
| 2025-12-09 01:02:13 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-09 01:01:52 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-09 01:01:52 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-09 01:01:51 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-09 01:01:50 | Ellagawa (Kalu Ganga) | 5.63 | 🟢 Normal | -0.020 |  |
| 2025-12-09 01:01:30 | Thanthirimale (Malwathu Oya) | 3.81 | 🟢 Normal | -0.051 |  |
| 2025-12-09 01:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 01:01:10 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-09 01:00:40 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.269 |  |
| 2025-12-09 01:00:20 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.102 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 01:03:16 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-09 01:10:54 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-09 01:14:49 | Hanwella (Kelani Ganga) | 2.06 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-08 18:02:40 | Galgamuwa (Mee Oya) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-08 18:00:08 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-09 01:05:23 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-09 01:01:52 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-09 01:01:52 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-08 17:05:58 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-09 00:21:20 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.004 |  |
| 2025-12-09 01:04:29 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-09 01:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 01:01:51 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-09 01:01:10 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-09 01:06:00 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:03:46 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-09 01:03:05 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-09 01:02:13 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-09 01:02:45 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-09 01:03:29 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:01:23 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-09 01:11:47 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:17:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.17 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:10:03 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2025-12-09 00:19:49 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | -0.010 |  |
| 2025-12-09 01:03:28 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2025-12-09 00:08:54 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2025-12-08 18:00:48 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-09 01:03:08 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2025-12-09 01:02:39 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.017 |  |
| 2025-12-09 01:01:50 | Ellagawa (Kalu Ganga) | 5.63 | 🟢 Normal | -0.020 |  |
| 2025-12-09 01:01:30 | Thanthirimale (Malwathu Oya) | 3.81 | 🟢 Normal | -0.051 |  |
| 2025-12-09 01:02:20 | Rathnapura (Kalu Ganga) | 3.32 | 🟢 Normal | -0.075 |  |
| 2025-12-09 01:04:44 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.087 |  |
| 2025-12-09 00:07:03 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.087 |  |
| 2025-12-09 01:00:20 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.102 |  |
| 2025-12-08 18:03:06 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | -0.251 |  |
| 2025-12-09 01:00:40 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.269 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)