# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--27_03:13:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **28,915 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 03:13:47 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:11:08 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-27 03:09:58 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:09:04 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:08:31 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-27 03:07:38 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-27 03:06:51 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:06:35 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 03:05:40 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:05:30 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -2.504 |  |
| 2025-12-27 03:05:17 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-27 03:04:56 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:04:51 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.024 |  |
| 2025-12-27 03:04:28 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:04:14 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2025-12-27 03:03:35 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.019 |  |
| 2025-12-27 03:03:35 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -2.504 |  |
| 2025-12-27 03:03:27 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.108 |  |
| 2025-12-27 03:03:23 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:02:56 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | -0.021 |  |
| 2025-12-27 03:02:51 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:02:42 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:02:26 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:02:25 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 03:02:24 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:02:16 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:02:10 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-27 03:02:00 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2025-12-27 03:01:12 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-27 03:00:59 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:00:13 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-27 02:49:26 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-27 02:37:55 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2025-12-27 02:29:58 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.108 |  |
| 2025-12-27 02:19:02 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.008 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 03:04:14 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2025-12-27 03:07:38 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-27 01:00:33 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-27 02:00:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-27 03:11:08 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-27 03:01:12 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-27 03:06:35 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 03:02:25 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 03:05:17 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-27 03:02:16 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:06:51 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:02:42 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-27 02:07:56 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:02:24 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:02:51 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-26 18:15:02 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:03:23 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:02:26 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:04:28 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-26 23:03:48 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:00:59 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:05:40 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:04:56 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:09:04 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:13:47 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-27 02:00:43 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-27 00:04:02 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:00:13 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-27 02:19:02 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.008 |  |
| 2025-12-27 03:08:31 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-26 18:01:40 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2025-12-27 03:02:00 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2025-12-27 03:02:10 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-27 03:03:35 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.019 |  |
| 2025-12-27 03:02:56 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | -0.021 |  |
| 2025-12-27 03:04:51 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.024 |  |
| 2025-12-26 18:05:51 | Weraganthota (Mahaweli Ganga) | -1.72 | 🟢 Normal | -0.029 |  |
| 2025-12-27 03:03:27 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.108 |  |
| 2025-12-27 03:05:30 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -2.504 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)