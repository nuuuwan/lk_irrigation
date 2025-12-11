# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--11_11:06:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,928 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 11:06:50 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:05:41 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:05:33 | Dunamale (Aththanagalu Oya) | 1.29 | 🟢 Normal | -0.021 |  |
| 2025-12-11 11:04:40 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | -0.020 |  |
| 2025-12-11 11:04:28 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2025-12-11 11:04:18 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:04:16 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 11:04:14 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.041 |  |
| 2025-12-11 11:03:56 | Ellagawa (Kalu Ganga) | 5.12 | 🟢 Normal | -0.010 |  |
| 2025-12-11 11:03:39 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:03:34 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | -0.011 |  |
| 2025-12-11 11:03:34 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:03:26 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-11 11:03:20 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:03:17 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | -0.041 |  |
| 2025-12-11 11:03:10 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.050 |  |
| 2025-12-11 11:02:49 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.005 |  |
| 2025-12-11 11:02:48 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2025-12-11 11:02:41 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:02:23 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.090 |  |
| 2025-12-11 11:02:18 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.013 |  |
| 2025-12-11 11:02:10 | Yaka Wewa (Ma Oya) | 1.36 | 🟢 Normal | -0.021 |  |
| 2025-12-11 11:02:10 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | -0.040 |  |
| 2025-12-11 11:02:06 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:01:54 | Horowpothana (Yan Oya) | 4.61 | 🟢 Normal | -0.019 |  |
| 2025-12-11 11:01:17 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:01:16 | Thanthirimale (Malwathu Oya) | 4.15 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-11 11:01:12 | Weraganthota (Mahaweli Ganga) | -1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:01:10 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.092 |  |
| 2025-12-11 11:01:06 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:00:50 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-11 11:00:17 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.031 |  |
| 2025-12-11 10:15:18 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-11 10:14:54 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-11 11:03:26 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-11 11:01:16 | Thanthirimale (Malwathu Oya) | 4.15 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-11 11:04:16 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 11:01:12 | Weraganthota (Mahaweli Ganga) | -1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:02:06 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:06:50 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:02:49 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:01:06 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:01:47 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:03:39 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:05:41 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:02:41 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:02:55 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:03:34 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:01:17 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:03:20 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:02:10 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:04:18 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:02:49 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.005 |  |
| 2025-12-11 10:04:16 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-11 11:00:50 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-11 11:03:56 | Ellagawa (Kalu Ganga) | 5.12 | 🟢 Normal | -0.010 |  |
| 2025-12-11 11:03:34 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | -0.011 |  |
| 2025-12-11 11:02:18 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.013 |  |
| 2025-12-11 11:01:54 | Horowpothana (Yan Oya) | 4.61 | 🟢 Normal | -0.019 |  |
| 2025-12-11 11:04:28 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2025-12-11 11:04:40 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | -0.020 |  |
| 2025-12-11 11:05:33 | Dunamale (Aththanagalu Oya) | 1.29 | 🟢 Normal | -0.021 |  |
| 2025-12-11 11:02:10 | Yaka Wewa (Ma Oya) | 1.36 | 🟢 Normal | -0.021 |  |
| 2025-12-11 11:02:48 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2025-12-11 11:00:17 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.031 |  |
| 2025-12-11 11:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | -0.040 |  |
| 2025-12-11 11:03:17 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | -0.041 |  |
| 2025-12-11 11:04:14 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.041 |  |
| 2025-12-11 11:03:10 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.050 |  |
| 2025-12-11 11:02:23 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.090 |  |
| 2025-12-11 11:01:10 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.092 |  |
| 2025-12-11 10:04:51 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)