# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--10_12:20:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,129 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-10 12:20:38 | Galgamuwa (Mee Oya) | 0.77 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-10 12:08:39 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-10 12:08:39 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.020 |  |
| 2025-12-10 12:08:05 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-10 12:07:44 | Weraganthota (Mahaweli Ganga) | -0.50 | 🟢 Normal | 1.299 | 🔺 Rising |
| 2025-12-10 12:07:36 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.015 |  |
| 2025-12-10 12:07:02 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-10 12:06:37 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-10 12:05:51 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.032 |  |
| 2025-12-10 12:05:48 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.019 |  |
| 2025-12-10 12:05:23 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-10 12:05:07 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-10 12:05:04 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | -0.010 |  |
| 2025-12-10 12:04:41 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-10 12:04:21 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-10 12:04:11 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2025-12-10 12:03:58 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2025-12-10 12:03:38 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2025-12-10 12:03:17 | Glencourse (Kelani Ganga) | 9.83 | 🟢 Normal | -0.010 |  |
| 2025-12-10 12:03:10 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.019 |  |
| 2025-12-10 12:03:08 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | -0.041 |  |
| 2025-12-10 12:03:05 | Thanthirimale (Malwathu Oya) | 3.65 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2025-12-10 12:03:04 | Panadugama (Nilwala Ganga) | 3.91 | 🟢 Normal | -0.078 |  |
| 2025-12-10 12:03:00 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.084 |  |
| 2025-12-10 12:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-10 12:02:42 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-10 12:02:40 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 12:02:30 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-10 12:02:21 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.010 |  |
| 2025-12-10 12:02:18 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 12:02:09 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-10 12:02:08 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 12:01:55 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.031 |  |
| 2025-12-10 12:01:40 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.052 |  |
| 2025-12-10 12:01:24 | Manampitiya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-10 12:01:22 | Yaka Wewa (Ma Oya) | 2.52 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2025-12-10 12:00:44 | Horowpothana (Yan Oya) | 5.13 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-10 12:00:22 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-10 12:00:13 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | -0.055 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-10 12:07:44 | Weraganthota (Mahaweli Ganga) | -0.50 | 🟢 Normal | 1.299 | 🔺 Rising |
| 2025-12-10 12:01:22 | Yaka Wewa (Ma Oya) | 2.52 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2025-12-10 12:03:05 | Thanthirimale (Malwathu Oya) | 3.65 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2025-12-10 12:01:24 | Manampitiya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-10 12:00:44 | Horowpothana (Yan Oya) | 5.13 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-10 12:02:30 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-10 12:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-10 12:02:18 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 12:02:08 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 12:02:40 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 12:20:38 | Galgamuwa (Mee Oya) | 0.77 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-10 12:06:37 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-10 12:02:42 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-10 12:04:21 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-10 12:08:05 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-10 12:08:39 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-10 12:03:38 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2025-12-10 12:05:23 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-10 12:02:09 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-10 12:05:04 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | -0.010 |  |
| 2025-12-10 12:04:41 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-10 12:03:17 | Glencourse (Kelani Ganga) | 9.83 | 🟢 Normal | -0.010 |  |
| 2025-12-10 12:03:58 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2025-12-10 12:00:22 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-10 12:02:21 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.010 |  |
| 2025-12-10 12:07:36 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.015 |  |
| 2025-12-10 12:03:10 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.019 |  |
| 2025-12-10 12:05:48 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.019 |  |
| 2025-12-10 12:05:07 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-10 12:08:39 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.020 |  |
| 2025-12-10 12:04:11 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2025-12-10 12:01:55 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.031 |  |
| 2025-12-10 12:05:51 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.032 |  |
| 2025-12-10 12:03:08 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | -0.041 |  |
| 2025-12-10 12:01:40 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.052 |  |
| 2025-12-10 12:00:13 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | -0.055 |  |
| 2025-12-10 12:03:04 | Panadugama (Nilwala Ganga) | 3.91 | 🟢 Normal | -0.078 |  |
| 2025-12-10 12:03:00 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)