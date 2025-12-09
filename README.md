# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_07:20:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,089 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 07:20:13 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:20:05 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | -0.033 |  |
| 2025-12-09 07:13:44 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:10:01 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:08:25 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2025-12-09 07:07:55 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:07:40 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-09 07:07:40 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.009 |  |
| 2025-12-09 07:06:56 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:06:41 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:05:45 | Rathnapura (Kalu Ganga) | 2.59 | 🟢 Normal | -0.092 |  |
| 2025-12-09 07:05:25 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.051 |  |
| 2025-12-09 07:04:55 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.115 |  |
| 2025-12-09 07:04:41 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:04:31 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | -0.009 |  |
| 2025-12-09 07:04:17 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:03:58 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:03:58 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-09 07:03:51 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 07:03:24 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-09 07:03:22 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:03:22 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -1.542 |  |
| 2025-12-09 07:03:13 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:03:13 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | -0.022 |  |
| 2025-12-09 07:03:10 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:03:08 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:02:39 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.011 |  |
| 2025-12-09 07:02:32 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.71 | 🟢 Normal | -0.073 |  |
| 2025-12-09 07:01:59 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:01:53 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:01:29 | Thanthirimale (Malwathu Oya) | 3.50 | 🟢 Normal | -0.054 |  |
| 2025-12-09 07:01:23 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:01:21 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-09 07:01:13 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-09 07:01:08 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:55:35 | Weraganthota (Mahaweli Ganga) | -1.23 | 🟢 Normal | -1.542 |  |
| 2025-12-09 06:46:47 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:40:57 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.026 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 07:08:25 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2025-12-09 07:07:40 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-09 07:03:24 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-09 07:03:58 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-09 07:01:13 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-09 07:03:51 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 07:01:53 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:01:59 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:07:55 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:20:13 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:13:44 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:03:08 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:04:17 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:04:41 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:10:01 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:06:41 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:03:13 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:01:08 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:03:22 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:06:56 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:01:23 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:06:27 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:03:58 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:02:32 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:03:10 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 07:07:40 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.009 |  |
| 2025-12-09 07:04:31 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | -0.009 |  |
| 2025-12-09 07:01:21 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-08 18:00:48 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-09 07:02:39 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.011 |  |
| 2025-12-09 07:03:13 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | -0.022 |  |
| 2025-12-09 07:20:05 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | -0.033 |  |
| 2025-12-09 07:05:25 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.051 |  |
| 2025-12-09 07:01:29 | Thanthirimale (Malwathu Oya) | 3.50 | 🟢 Normal | -0.054 |  |
| 2025-12-09 07:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.71 | 🟢 Normal | -0.073 |  |
| 2025-12-09 07:05:45 | Rathnapura (Kalu Ganga) | 2.59 | 🟢 Normal | -0.092 |  |
| 2025-12-09 07:04:55 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.115 |  |
| 2025-12-09 07:03:22 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -1.542 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)