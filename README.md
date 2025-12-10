# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--10_11:28:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,090 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-10 11:28:06 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:09:43 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.049 |  |
| 2025-12-10 11:08:54 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.021 |  |
| 2025-12-10 11:08:19 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2025-12-10 11:06:42 | Yaka Wewa (Ma Oya) | 2.40 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2025-12-10 11:06:36 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:05:51 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.086 |  |
| 2025-12-10 11:05:12 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-10 11:05:01 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:04:49 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:04:44 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-10 11:04:43 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 11:04:12 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:04:07 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | -0.040 |  |
| 2025-12-10 11:03:50 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | -0.050 |  |
| 2025-12-10 11:03:42 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.089 |  |
| 2025-12-10 11:03:40 | Thanthirimale (Malwathu Oya) | 3.57 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-10 11:03:40 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:03:40 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | -0.030 |  |
| 2025-12-10 11:03:39 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:03:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:03:26 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:03:11 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | -0.010 |  |
| 2025-12-10 11:02:48 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 11:02:36 | Manampitiya (Mahaweli Ganga) | 2.71 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-10 11:02:25 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-10 11:02:22 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:02:21 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-10 11:02:07 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:02:02 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:01:38 | Panadugama (Nilwala Ganga) | 3.99 | 🟢 Normal | -0.114 |  |
| 2025-12-10 11:01:14 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:01:10 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.011 |  |
| 2025-12-10 11:01:08 | Siyambalanduwa (Heda Oya) | 0.90 | 🟢 Normal | -0.030 |  |
| 2025-12-10 11:00:55 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.038 |  |
| 2025-12-10 11:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-10 11:00:46 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | -1.104 |  |
| 2025-12-10 11:00:19 | Horowpothana (Yan Oya) | 5.06 | 🟢 Normal | 0.094 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-10 11:06:42 | Yaka Wewa (Ma Oya) | 2.40 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2025-12-10 11:05:12 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-10 11:00:19 | Horowpothana (Yan Oya) | 5.06 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2025-12-10 11:02:21 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-10 11:03:40 | Thanthirimale (Malwathu Oya) | 3.57 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-10 11:02:36 | Manampitiya (Mahaweli Ganga) | 2.71 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-10 11:04:43 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 11:02:48 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 11:02:02 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:01:14 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:03:39 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:28:06 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:03:40 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:03:26 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:02:22 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:04:12 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:04:49 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:05:01 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:06:36 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:02:07 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:03:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2025-12-10 11:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-10 11:03:11 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | -0.010 |  |
| 2025-12-10 11:02:25 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-10 11:04:44 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-10 11:01:10 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.011 |  |
| 2025-12-10 11:08:19 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2025-12-10 11:08:54 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.021 |  |
| 2025-12-10 11:01:08 | Siyambalanduwa (Heda Oya) | 0.90 | 🟢 Normal | -0.030 |  |
| 2025-12-10 11:03:40 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | -0.030 |  |
| 2025-12-10 11:00:55 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.038 |  |
| 2025-12-10 11:04:07 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | -0.040 |  |
| 2025-12-10 11:09:43 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.049 |  |
| 2025-12-10 11:03:50 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | -0.050 |  |
| 2025-12-10 11:05:51 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.086 |  |
| 2025-12-10 11:03:42 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.089 |  |
| 2025-12-10 11:01:38 | Panadugama (Nilwala Ganga) | 3.99 | 🟢 Normal | -0.114 |  |
| 2025-12-10 11:00:46 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | -1.104 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)