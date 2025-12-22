# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--23_03:03:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,327 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 03:03:51 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-23 03:03:30 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:03:03 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.011 |  |
| 2025-12-23 03:02:51 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:02:43 | Manampitiya (Mahaweli Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:02:34 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:02:11 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-23 03:02:10 | Horowpothana (Yan Oya) | 3.07 | 🟢 Normal | -0.030 |  |
| 2025-12-23 03:01:54 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:01:26 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | -0.098 |  |
| 2025-12-23 03:01:25 | Ellagawa (Kalu Ganga) | 4.53 | 🟢 Normal | -0.010 |  |
| 2025-12-23 03:01:20 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:01:14 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-23 03:01:11 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:01:04 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-23 03:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:00:39 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2025-12-23 02:20:49 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-23 02:19:07 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-23 02:18:25 | Peradeniya (Mahaweli Ganga) | 2.61 | 🟢 Normal | -0.098 |  |
| 2025-12-23 02:14:51 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-23 02:12:55 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-23 02:11:47 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-23 02:10:32 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2025-12-23 02:09:34 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2025-12-23 02:08:12 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -18.000 |  |
| 2025-12-23 02:08:10 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -18.000 |  |
| 2025-12-23 02:08:03 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-23 02:08:01 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-23 02:07:16 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2025-12-23 02:07:04 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-23 02:07:03 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-23 02:06:51 | Manampitiya (Mahaweli Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-23 02:06:24 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2025-12-23 02:06:16 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 22:33:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2025-12-23 00:19:54 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-23 03:01:14 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-23 01:29:10 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-23 03:00:39 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2025-12-23 03:02:11 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-23 02:14:51 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-23 02:02:27 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-23 02:12:55 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-23 03:01:20 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:02:51 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-23 02:07:04 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:02:34 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:03:30 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-23 02:10:32 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2025-12-23 02:08:03 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-23 00:00:41 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:08:23 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-23 02:03:08 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-23 02:19:07 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:01:11 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2025-12-23 02:07:03 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:02:43 | Manampitiya (Mahaweli Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-23 02:11:47 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:01:54 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-23 02:05:27 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-23 02:06:24 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2025-12-23 03:01:25 | Ellagawa (Kalu Ganga) | 4.53 | 🟢 Normal | -0.010 |  |
| 2025-12-23 03:03:51 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-23 03:01:04 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-23 03:03:03 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.011 |  |
| 2025-12-23 03:02:10 | Horowpothana (Yan Oya) | 3.07 | 🟢 Normal | -0.030 |  |
| 2025-12-23 02:05:14 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.039 |  |
| 2025-12-22 18:03:49 | Galgamuwa (Mee Oya) | 0.90 | 🟢 Normal | -0.068 |  |
| 2025-12-23 03:01:26 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | -0.098 |  |
| 2025-12-22 18:07:21 | Thanthirimale (Malwathu Oya) | 4.32 | 🟢 Normal | -0.101 |  |
| 2025-12-22 18:02:31 | Weraganthota (Mahaweli Ganga) | -1.20 | 🟢 Normal | -0.170 |  |
| 2025-12-23 02:08:12 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)