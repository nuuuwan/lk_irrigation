# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--08_19:11:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,692 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-08 19:11:50 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.060 |  |
| 2025-12-08 19:08:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | -0.018 |  |
| 2025-12-08 19:07:01 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:06:32 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:06:29 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:05:34 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:05:22 | Panadugama (Nilwala Ganga) | 3.37 | 🟢 Normal | -0.029 |  |
| 2025-12-08 19:04:48 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | -0.087 |  |
| 2025-12-08 19:04:46 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.120 |  |
| 2025-12-08 19:04:37 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2025-12-08 19:04:31 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.029 |  |
| 2025-12-08 19:04:30 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2025-12-08 19:04:11 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-08 19:04:05 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:04:01 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-08 19:03:18 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.020 |  |
| 2025-12-08 19:03:05 | Thanthirimale (Malwathu Oya) | 4.08 | 🟢 Normal | -0.040 |  |
| 2025-12-08 19:03:04 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:03:02 | Hanwella (Kelani Ganga) | 2.20 | 🟢 Normal | -0.062 |  |
| 2025-12-08 19:02:47 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:02:43 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:02:40 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | 0.478 | 🔺 Rising |
| 2025-12-08 19:02:24 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2025-12-08 19:02:05 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:02:02 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.091 |  |
| 2025-12-08 19:01:45 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:01:09 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 19:00:36 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:00:24 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:00:10 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-08 18:29:45 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 18:28:39 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 18:23:46 | Panadugama (Nilwala Ganga) | 3.39 | 🟢 Normal | -0.029 |  |
| 2025-12-08 18:14:50 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | -0.120 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-08 19:02:40 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | 0.478 | 🔺 Rising |
| 2025-12-08 19:04:37 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2025-12-08 18:02:40 | Galgamuwa (Mee Oya) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-08 18:00:08 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-08 19:04:01 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-08 19:04:11 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-08 19:01:09 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 17:05:58 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-08 19:02:43 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:01:45 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:02:47 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:00:24 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-08 18:01:44 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:00:36 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:00:10 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:03:04 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:07:01 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:05:34 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:06:29 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:04:05 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:02:05 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:06:32 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-08 19:04:30 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2025-12-08 18:00:48 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-08 19:08:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | -0.018 |  |
| 2025-12-08 19:03:18 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.020 |  |
| 2025-12-08 19:02:24 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2025-12-08 19:04:31 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.029 |  |
| 2025-12-08 19:05:22 | Panadugama (Nilwala Ganga) | 3.37 | 🟢 Normal | -0.029 |  |
| 2025-12-08 19:03:05 | Thanthirimale (Malwathu Oya) | 4.08 | 🟢 Normal | -0.040 |  |
| 2025-12-08 19:11:50 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.060 |  |
| 2025-12-08 19:03:02 | Hanwella (Kelani Ganga) | 2.20 | 🟢 Normal | -0.062 |  |
| 2025-12-08 19:04:48 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | -0.087 |  |
| 2025-12-08 18:12:18 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | -0.090 |  |
| 2025-12-08 19:02:02 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.091 |  |
| 2025-12-08 19:04:46 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.120 |  |
| 2025-12-08 18:03:06 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | -0.251 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)