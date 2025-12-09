# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_16:14:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,434 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 16:14:45 | Galgamuwa (Mee Oya) | 1.32 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-09 16:09:14 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2025-12-09 16:08:25 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:08:08 | Thanthirimale (Malwathu Oya) | 3.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:07:59 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:06:26 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:06:20 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-09 16:06:15 | Panadugama (Nilwala Ganga) | 3.12 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:05:40 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2025-12-09 16:04:31 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-09 16:04:22 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-09 16:04:14 | Glencourse (Kelani Ganga) | 9.89 | 🟢 Normal | -0.031 |  |
| 2025-12-09 16:03:52 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-09 16:03:22 | Ellagawa (Kalu Ganga) | 5.68 | 🟢 Normal | -0.054 |  |
| 2025-12-09 16:03:17 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.051 |  |
| 2025-12-09 16:03:08 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:03:07 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:02:57 | Siyambalanduwa (Heda Oya) | 1.38 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2025-12-09 16:02:54 | Peradeniya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.048 |  |
| 2025-12-09 16:02:45 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.042 |  |
| 2025-12-09 16:02:39 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:02:34 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.65 | 🟢 Normal | -0.041 |  |
| 2025-12-09 16:02:12 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:02:12 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-09 16:01:44 | Yaka Wewa (Ma Oya) | 2.00 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2025-12-09 16:01:33 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:01:29 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:01:17 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.030 |  |
| 2025-12-09 16:01:08 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2025-12-09 16:01:02 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:00:30 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-09 16:00:26 | Weraganthota (Mahaweli Ganga) | -1.38 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-09 16:00:20 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-09 15:31:56 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.016 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 15:13:25 | Urawa (Nilwala Ganga) | 1.11 | 🟢 Normal | 0.480 | 🔺 Rising |
| 2025-12-09 16:02:57 | Siyambalanduwa (Heda Oya) | 1.38 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2025-12-09 16:05:40 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2025-12-09 16:01:44 | Yaka Wewa (Ma Oya) | 2.00 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2025-12-09 16:00:26 | Weraganthota (Mahaweli Ganga) | -1.38 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-09 16:04:22 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-09 16:06:20 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-09 16:00:30 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-09 16:04:31 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-09 16:02:12 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-09 16:09:14 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2025-12-09 15:02:15 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-09 16:14:45 | Galgamuwa (Mee Oya) | 1.32 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-09 16:01:29 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:06:26 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:01:33 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:02:34 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:03:08 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:03:07 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:06:15 | Panadugama (Nilwala Ganga) | 3.12 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:01:02 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-09 15:14:42 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:02:12 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:08:25 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:08:08 | Thanthirimale (Malwathu Oya) | 3.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:02:39 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-09 15:01:12 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2025-12-09 16:01:08 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2025-12-09 16:00:20 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-09 16:03:52 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-09 16:01:17 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.030 |  |
| 2025-12-09 16:04:14 | Glencourse (Kelani Ganga) | 9.89 | 🟢 Normal | -0.031 |  |
| 2025-12-09 15:08:21 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.036 |  |
| 2025-12-09 16:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.65 | 🟢 Normal | -0.041 |  |
| 2025-12-09 16:02:45 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.042 |  |
| 2025-12-09 16:02:54 | Peradeniya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.048 |  |
| 2025-12-09 16:03:17 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.051 |  |
| 2025-12-09 16:03:22 | Ellagawa (Kalu Ganga) | 5.68 | 🟢 Normal | -0.054 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)