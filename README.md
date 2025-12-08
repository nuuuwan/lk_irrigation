# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--08_21:06:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,753 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-08 21:06:36 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | -0.044 |  |
| 2025-12-08 21:05:37 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.029 |  |
| 2025-12-08 21:05:01 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.046 |  |
| 2025-12-08 21:04:52 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-08 21:04:35 | Putupaula (Kalu Ganga) | 1.14 | 🟢 Normal | -0.032 |  |
| 2025-12-08 21:04:33 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-08 21:04:31 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-08 21:04:31 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-08 21:04:29 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2025-12-08 21:03:51 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-08 21:03:31 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.089 |  |
| 2025-12-08 21:03:21 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-08 21:03:12 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | -0.050 |  |
| 2025-12-08 21:03:01 | Thanthirimale (Malwathu Oya) | 3.99 | 🟢 Normal | -0.049 |  |
| 2025-12-08 21:02:55 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-08 21:02:55 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-08 21:02:28 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 21:02:26 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-08 21:02:09 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2025-12-08 21:01:56 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2025-12-08 21:01:53 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-08 21:01:37 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-08 21:01:22 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 21:01:20 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-08 21:00:57 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-08 21:00:10 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:21:45 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-08 20:17:34 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | -0.058 |  |
| 2025-12-08 20:16:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.018 |  |
| 2025-12-08 20:14:04 | Rathnapura (Kalu Ganga) | 2.20 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2025-12-08 20:12:17 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.046 |  |
| 2025-12-08 20:12:11 | Ellagawa (Kalu Ganga) | 5.79 | 🟢 Normal | -0.044 |  |
| 2025-12-08 20:09:31 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:08:23 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-08 20:14:04 | Rathnapura (Kalu Ganga) | 2.20 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2025-12-08 21:02:55 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-08 21:01:56 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2025-12-08 18:02:40 | Galgamuwa (Mee Oya) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-08 21:04:31 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-08 18:00:08 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-08 17:05:58 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-08 20:21:45 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-08 21:00:57 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-08 21:00:10 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-08 21:01:22 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 21:01:53 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-08 21:04:52 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-08 21:02:28 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 21:02:55 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-08 21:03:51 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:03:16 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-08 20:03:05 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-08 21:01:20 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-08 21:04:33 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-08 21:02:26 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-08 21:01:37 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-08 21:03:21 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-08 21:04:29 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2025-12-08 18:00:48 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-08 20:16:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.018 |  |
| 2025-12-08 21:02:09 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2025-12-08 21:05:37 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.029 |  |
| 2025-12-08 21:04:35 | Putupaula (Kalu Ganga) | 1.14 | 🟢 Normal | -0.032 |  |
| 2025-12-08 21:06:36 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | -0.044 |  |
| 2025-12-08 21:05:01 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.046 |  |
| 2025-12-08 21:03:01 | Thanthirimale (Malwathu Oya) | 3.99 | 🟢 Normal | -0.049 |  |
| 2025-12-08 21:03:12 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | -0.050 |  |
| 2025-12-08 20:02:33 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.052 |  |
| 2025-12-08 20:17:34 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | -0.058 |  |
| 2025-12-08 20:03:31 | Dunamale (Aththanagalu Oya) | 1.67 | 🟢 Normal | -0.081 |  |
| 2025-12-08 21:03:31 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.089 |  |
| 2025-12-08 18:03:06 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | -0.251 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)