# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--05_05:14:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,649 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-05 05:14:48 | Urawa (Nilwala Ganga) | 2.13 | 🟢 Normal | -5.538 |  |
| 2025-12-05 05:12:38 | Urawa (Nilwala Ganga) | 2.33 | 🟢 Normal | -5.538 |  |
| 2025-12-05 05:12:35 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.083 |  |
| 2025-12-05 05:10:46 | Pitabeddara (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.067 |  |
| 2025-12-05 05:07:45 | Panadugama (Nilwala Ganga) | 4.63 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2025-12-05 05:06:42 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | -0.409 |  |
| 2025-12-05 05:06:39 | Badalgama (Maha Oya) | 3.01 | 🟢 Normal | 0.000 |  |
| 2025-12-05 05:06:35 | Hanwella (Kelani Ganga) | 3.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-05 05:05:29 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2025-12-05 05:05:25 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-05 05:05:17 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2025-12-05 05:05:04 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-05 05:04:43 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2025-12-05 05:04:22 | Rathnapura (Kalu Ganga) | 2.85 | 🟢 Normal | -1.489 |  |
| 2025-12-05 05:04:19 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-05 05:03:28 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-05 05:03:26 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-05 05:03:22 | Moraketiya (Walawe Ganga) | 1.41 | 🟢 Normal | 0.335 | 🔺 Rising |
| 2025-12-05 05:03:10 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2025-12-05 05:03:02 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.021 |  |
| 2025-12-05 05:02:51 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 05:02:37 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-05 05:02:36 | Dunamale (Aththanagalu Oya) | 2.68 | 🟢 Normal | -0.062 |  |
| 2025-12-05 05:02:26 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-05 05:02:19 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-05 05:01:59 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-05 05:01:43 | Siyambalanduwa (Heda Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-05 05:01:37 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-05 05:01:35 | Thanthirimale (Malwathu Oya) | 4.49 | 🟢 Normal | -1.064 |  |
| 2025-12-05 05:01:18 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.050 |  |
| 2025-12-05 04:59:56 | Rathnapura (Kalu Ganga) | 2.96 | 🟢 Normal | -1.489 |  |
| 2025-12-05 04:59:22 | Glencourse (Kelani Ganga) | 10.87 | 🟢 Normal | -0.409 |  |
| 2025-12-05 04:52:52 | Pitabeddara (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.067 |  |
| 2025-12-05 04:25:00 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2025-12-05 04:21:20 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-05 03:14:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.11 | 🟢 Normal | 6.353 | 🔺 Rising |
| 2025-12-05 05:03:22 | Moraketiya (Walawe Ganga) | 1.41 | 🟢 Normal | 0.335 | 🔺 Rising |
| 2025-12-05 05:05:29 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2025-12-05 05:07:45 | Panadugama (Nilwala Ganga) | 4.63 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2025-12-05 05:03:28 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-05 05:04:43 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2025-12-05 05:02:19 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-05 05:04:19 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-05 05:05:25 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-05 05:02:26 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-05 05:06:35 | Hanwella (Kelani Ganga) | 3.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-05 04:21:20 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-05 05:02:37 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-05 05:03:26 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:01:47 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-05 05:01:43 | Siyambalanduwa (Heda Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:04:32 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 05:02:51 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 05:06:39 | Badalgama (Maha Oya) | 3.01 | 🟢 Normal | 0.000 |  |
| 2025-12-05 05:05:04 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-05 05:01:37 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-05 05:05:17 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2025-12-05 05:01:59 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-05 05:03:10 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2025-12-04 18:04:34 | Galgamuwa (Mee Oya) | 0.53 | 🟢 Normal | -0.020 |  |
| 2025-12-05 05:03:02 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.021 |  |
| 2025-12-04 19:33:02 | Manampitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.027 |  |
| 2025-12-04 18:08:34 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | -0.047 |  |
| 2025-12-05 05:01:18 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.050 |  |
| 2025-12-05 05:02:36 | Dunamale (Aththanagalu Oya) | 2.68 | 🟢 Normal | -0.062 |  |
| 2025-12-05 05:10:46 | Pitabeddara (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.067 |  |
| 2025-12-05 05:12:35 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.083 |  |
| 2025-12-05 04:08:41 | Magura (Kalu Ganga) | 3.02 | 🟢 Normal | -0.222 |  |
| 2025-12-05 05:06:42 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | -0.409 |  |
| 2025-12-05 05:01:35 | Thanthirimale (Malwathu Oya) | 4.49 | 🟢 Normal | -1.064 |  |
| 2025-12-05 05:04:22 | Rathnapura (Kalu Ganga) | 2.85 | 🟢 Normal | -1.489 |  |
| 2025-12-05 05:14:48 | Urawa (Nilwala Ganga) | 2.13 | 🟢 Normal | -5.538 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)