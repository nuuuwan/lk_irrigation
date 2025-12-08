# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--08_20:07:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,719 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-08 20:07:09 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2025-12-08 20:05:57 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:05:44 | Thawalama (Gin Ganga) | 2.38 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2025-12-08 20:04:56 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-08 20:03:47 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 20:03:35 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:03:31 | Dunamale (Aththanagalu Oya) | 1.67 | 🟢 Normal | -0.081 |  |
| 2025-12-08 20:03:24 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:03:24 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-08 20:03:16 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:03:13 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.010 |  |
| 2025-12-08 20:03:05 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:03:01 | Hanwella (Kelani Ganga) | 2.15 | 🟢 Normal | -0.050 |  |
| 2025-12-08 20:02:52 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.144 |  |
| 2025-12-08 20:02:39 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:02:38 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:02:33 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.052 |  |
| 2025-12-08 20:02:13 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-08 20:02:08 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2025-12-08 20:02:00 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:01:38 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-08 20:01:33 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:01:31 | Thanthirimale (Malwathu Oya) | 4.04 | 🟢 Normal | -0.041 |  |
| 2025-12-08 20:01:15 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:00:43 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:00:42 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 19:17:04 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:11:50 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.060 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-08 20:05:44 | Thawalama (Gin Ganga) | 2.38 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2025-12-08 19:04:37 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2025-12-08 20:04:56 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-08 20:03:24 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-08 18:02:40 | Galgamuwa (Mee Oya) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-08 18:00:08 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-08 19:04:11 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-08 20:00:42 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 20:03:47 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 17:05:58 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-08 20:00:43 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:02:00 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:03:35 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:00:24 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:17:04 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:05:57 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:03:24 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:02:39 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:03:16 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:03:05 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:01:15 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:02:38 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:07:09 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2025-12-08 20:01:38 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-08 20:03:13 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.010 |  |
| 2025-12-08 20:02:13 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-08 18:00:48 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-08 19:08:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | -0.018 |  |
| 2025-12-08 19:05:22 | Panadugama (Nilwala Ganga) | 3.37 | 🟢 Normal | -0.029 |  |
| 2025-12-08 20:02:08 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2025-12-08 20:01:31 | Thanthirimale (Malwathu Oya) | 4.04 | 🟢 Normal | -0.041 |  |
| 2025-12-08 20:03:01 | Hanwella (Kelani Ganga) | 2.15 | 🟢 Normal | -0.050 |  |
| 2025-12-08 20:02:33 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.052 |  |
| 2025-12-08 19:11:50 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.060 |  |
| 2025-12-08 20:03:31 | Dunamale (Aththanagalu Oya) | 1.67 | 🟢 Normal | -0.081 |  |
| 2025-12-08 19:04:48 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | -0.087 |  |
| 2025-12-08 20:02:52 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.144 |  |
| 2025-12-08 18:03:06 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | -0.251 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)