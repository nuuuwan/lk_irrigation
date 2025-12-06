# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--06_13:02:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,758 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-06 13:02:22 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2025-12-06 13:02:20 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.021 |  |
| 2025-12-06 13:02:10 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | -0.021 |  |
| 2025-12-06 13:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2025-12-06 13:01:42 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-06 13:01:32 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-06 13:01:27 | Baddegama (Gin Ganga) | 2.56 | 🟢 Normal | -0.041 |  |
| 2025-12-06 13:01:26 | Manampitiya (Mahaweli Ganga) | 2.22 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-06 13:01:14 | Giriulla (Maha Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2025-12-06 13:00:46 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.032 |  |
| 2025-12-06 13:00:33 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-06 12:15:47 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2025-12-06 12:12:03 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | -0.009 |  |
| 2025-12-06 12:09:19 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-06 12:07:35 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-06 12:06:54 | Weraganthota (Mahaweli Ganga) | -1.28 | 🟢 Normal | -0.248 |  |
| 2025-12-06 12:06:30 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-06 12:06:14 | Panadugama (Nilwala Ganga) | 3.87 | 🟢 Normal | -0.058 |  |
| 2025-12-06 12:06:07 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | -0.021 |  |
| 2025-12-06 12:06:03 | Thanthirimale (Malwathu Oya) | 6.95 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-06 12:05:52 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-06 12:05:33 | Magura (Kalu Ganga) | 3.18 | 🟢 Normal | -0.216 |  |
| 2025-12-06 12:04:59 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.021 |  |
| 2025-12-06 12:04:46 | Katharagama (Menik Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-06 12:04:26 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.032 |  |
| 2025-12-06 12:04:11 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-06 12:03:57 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-06 12:03:49 | Rathnapura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.060 |  |
| 2025-12-06 12:03:37 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.065 |  |
| 2025-12-06 12:03:36 | Moraketiya (Walawe Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2025-12-06 12:03:24 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-06 12:03:17 | Baddegama (Gin Ganga) | 2.60 | 🟢 Normal | -0.041 |  |
| 2025-12-06 12:03:15 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 12:03:13 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | -0.011 |  |
| 2025-12-06 12:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.25 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-06 12:06:03 | Thanthirimale (Malwathu Oya) | 6.95 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-06 13:01:26 | Manampitiya (Mahaweli Ganga) | 2.22 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-06 12:04:11 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-06 13:01:42 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-06 12:02:29 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-06 12:03:57 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-06 12:01:25 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-06 12:05:52 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-06 12:04:46 | Katharagama (Menik Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-06 12:03:15 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 12:09:19 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-06 13:01:32 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-06 12:15:47 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2025-12-06 12:12:03 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | -0.009 |  |
| 2025-12-06 12:07:35 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-06 12:03:24 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-06 13:00:33 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-06 12:02:10 | Galgamuwa (Mee Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-06 13:01:14 | Giriulla (Maha Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2025-12-06 12:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.25 | 🟢 Normal | -0.010 |  |
| 2025-12-06 13:02:22 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2025-12-06 12:01:03 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-06 12:03:13 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | -0.011 |  |
| 2025-12-06 13:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2025-12-06 12:03:03 | Hanwella (Kelani Ganga) | 2.95 | 🟢 Normal | -0.020 |  |
| 2025-12-06 12:02:31 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.021 |  |
| 2025-12-06 13:02:20 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.021 |  |
| 2025-12-06 13:02:10 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | -0.021 |  |
| 2025-12-06 12:00:18 | Horowpothana (Yan Oya) | 1.93 | 🟢 Normal | -0.022 |  |
| 2025-12-06 13:00:46 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.032 |  |
| 2025-12-06 13:01:27 | Baddegama (Gin Ganga) | 2.56 | 🟢 Normal | -0.041 |  |
| 2025-12-06 12:06:14 | Panadugama (Nilwala Ganga) | 3.87 | 🟢 Normal | -0.058 |  |
| 2025-12-06 12:03:49 | Rathnapura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.060 |  |
| 2025-12-06 12:03:37 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.065 |  |
| 2025-12-06 12:01:07 | Ellagawa (Kalu Ganga) | 6.15 | 🟢 Normal | -0.117 |  |
| 2025-12-06 12:05:33 | Magura (Kalu Ganga) | 3.18 | 🟢 Normal | -0.216 |  |
| 2025-12-06 12:06:54 | Weraganthota (Mahaweli Ganga) | -1.28 | 🟢 Normal | -0.248 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)