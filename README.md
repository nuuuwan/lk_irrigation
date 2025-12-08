# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_04:42:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,979 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 04:42:14 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | -0.013 |  |
| 2025-12-09 04:39:54 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.016 |  |
| 2025-12-09 04:19:54 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:11:44 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:09:58 | Panadugama (Nilwala Ganga) | 3.21 | 🟢 Normal | -0.008 |  |
| 2025-12-09 04:07:30 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-09 04:07:24 | Rathnapura (Kalu Ganga) | 2.94 | 🟢 Normal | -0.122 |  |
| 2025-12-09 04:07:11 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:05:30 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2025-12-09 04:05:18 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-09 04:05:13 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | -0.010 |  |
| 2025-12-09 04:04:18 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.049 |  |
| 2025-12-09 04:03:48 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:03:38 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:03:19 | Ellagawa (Kalu Ganga) | 5.86 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2025-12-09 04:03:06 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:03:01 | Hanwella (Kelani Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2025-12-09 04:02:20 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:02:18 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:02:07 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-09 04:02:02 | Dunamale (Aththanagalu Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:01:14 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 04:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:01:01 | Thanthirimale (Malwathu Oya) | 3.67 | 🟢 Normal | -0.050 |  |
| 2025-12-09 04:00:31 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:00:21 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.075 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 04:03:19 | Ellagawa (Kalu Ganga) | 5.86 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2025-12-09 04:05:30 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2025-12-09 04:02:07 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-09 04:05:18 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-08 18:02:40 | Galgamuwa (Mee Oya) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-08 18:00:08 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-09 04:01:14 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 17:05:58 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-09 04:00:31 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-09 03:01:49 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:03:06 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:07:11 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:03:48 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-09 03:02:52 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:05:50 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:02:18 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:02:02 | Dunamale (Aththanagalu Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:02:20 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:03:38 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:19:54 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-09 03:06:51 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:11:44 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:09:58 | Panadugama (Nilwala Ganga) | 3.21 | 🟢 Normal | -0.008 |  |
| 2025-12-09 03:13:00 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.009 |  |
| 2025-12-09 04:07:30 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-09 04:05:13 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | -0.010 |  |
| 2025-12-08 18:00:48 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-09 04:42:14 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | -0.013 |  |
| 2025-12-09 04:39:54 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.016 |  |
| 2025-12-09 04:03:01 | Hanwella (Kelani Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2025-12-09 03:24:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.029 |  |
| 2025-12-09 04:04:18 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.049 |  |
| 2025-12-09 04:01:01 | Thanthirimale (Malwathu Oya) | 3.67 | 🟢 Normal | -0.050 |  |
| 2025-12-09 04:00:21 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.075 |  |
| 2025-12-09 04:07:24 | Rathnapura (Kalu Ganga) | 2.94 | 🟢 Normal | -0.122 |  |
| 2025-12-08 18:03:06 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | -0.251 |  |
| 2025-12-09 03:03:11 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)