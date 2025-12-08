# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_02:17:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,918 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 02:17:17 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-09 02:13:04 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:11:19 | Panadugama (Nilwala Ganga) | 3.23 | 🟢 Normal | -0.005 |  |
| 2025-12-09 02:08:28 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-09 02:07:28 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:07:26 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:06:20 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2025-12-09 02:05:50 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:05:10 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:04:38 | Rathnapura (Kalu Ganga) | 3.20 | 🟢 Normal | -0.116 |  |
| 2025-12-09 02:03:42 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.031 |  |
| 2025-12-09 02:03:33 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.010 |  |
| 2025-12-09 02:02:51 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:02:39 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-09 02:02:37 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-09 02:02:29 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:02:19 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2025-12-09 02:02:13 | Glencourse (Kelani Ganga) | 10.08 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-09 02:02:06 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:02:01 | Thanthirimale (Malwathu Oya) | 3.77 | 🟢 Normal | -0.040 |  |
| 2025-12-09 02:01:55 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:01:51 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2025-12-09 02:01:42 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:01:40 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:00:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | -0.128 |  |
| 2025-12-09 02:00:50 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | -0.020 |  |
| 2025-12-09 02:00:24 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:00:22 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 02:01:51 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2025-12-09 02:02:19 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2025-12-09 02:06:20 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2025-12-09 01:10:54 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-09 02:17:17 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-09 02:08:28 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-09 02:02:13 | Glencourse (Kelani Ganga) | 10.08 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-08 18:02:40 | Galgamuwa (Mee Oya) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-08 18:00:08 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-09 02:02:37 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-08 17:05:58 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-09 00:21:20 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.004 |  |
| 2025-12-09 02:00:22 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:02:06 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:01:42 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:01:55 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:02:51 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:01:40 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:05:10 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:00:24 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:05:50 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:13:04 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:07:28 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:02:29 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-09 01:11:47 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:11:19 | Panadugama (Nilwala Ganga) | 3.23 | 🟢 Normal | -0.005 |  |
| 2025-12-09 00:08:54 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2025-12-09 02:03:33 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.010 |  |
| 2025-12-09 02:02:39 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-08 18:00:48 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-09 01:03:08 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2025-12-09 02:00:50 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | -0.020 |  |
| 2025-12-09 02:03:42 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.031 |  |
| 2025-12-09 02:02:01 | Thanthirimale (Malwathu Oya) | 3.77 | 🟢 Normal | -0.040 |  |
| 2025-12-09 01:04:44 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.087 |  |
| 2025-12-09 02:04:38 | Rathnapura (Kalu Ganga) | 3.20 | 🟢 Normal | -0.116 |  |
| 2025-12-09 02:00:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | -0.128 |  |
| 2025-12-08 18:03:06 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | -0.251 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)