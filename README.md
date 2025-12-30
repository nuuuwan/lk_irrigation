# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--30_17:12:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **32,118 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 17:12:49 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:12:33 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:11:56 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:10:01 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:09:37 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:08:36 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.027 |  |
| 2025-12-30 17:08:02 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:06:41 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2025-12-30 17:05:49 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:05:35 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-30 17:05:26 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:05:13 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2025-12-30 17:04:48 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:04:47 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:04:26 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:04:24 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:03:54 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:03:52 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:03:42 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.011 |  |
| 2025-12-30 17:03:14 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-30 17:03:09 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:02:56 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:02:50 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:02:35 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:02:28 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:02:21 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-30 17:02:20 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2025-12-30 17:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.020 |  |
| 2025-12-30 17:02:03 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:01:56 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:01:49 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-30 17:01:26 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:01:08 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:01:02 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:01:01 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2025-12-30 17:00:58 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:00:51 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:00:29 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-30 16:26:17 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-30 16:20:20 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 17:02:21 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-30 17:01:49 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-30 17:03:14 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-30 16:17:45 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-30 17:02:20 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2025-12-30 17:04:24 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:04:48 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:01:56 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:02:03 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:00:29 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:00:51 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:11:56 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:10:01 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:01:08 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:04:53 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:05:49 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:02:35 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:03:54 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:02:56 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:12:33 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:12:49 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:01:26 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:03:52 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:02:50 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:04:47 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:08:02 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:04:26 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:09:37 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:01:02 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:05:26 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:02:28 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:03:09 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-30 17:05:13 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2025-12-30 17:05:35 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-30 17:01:01 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2025-12-30 17:06:41 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2025-12-30 17:03:42 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.011 |  |
| 2025-12-30 17:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.020 |  |
| 2025-12-30 17:08:36 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.027 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)