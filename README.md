# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--05_11:18:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,873 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-05 11:18:30 | Rathnapura (Kalu Ganga) | 2.25 | 🟢 Normal | -0.070 |  |
| 2025-12-05 11:16:27 | Moraketiya (Walawe Ganga) | 1.31 | 🟢 Normal | -0.009 |  |
| 2025-12-05 11:15:52 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2025-12-05 11:15:15 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.056 |  |
| 2025-12-05 11:14:11 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | -0.085 |  |
| 2025-12-05 11:13:39 | Thanthirimale (Malwathu Oya) | 6.25 | 🟡 Alert | 0.085 | 🔺 Rising |
| 2025-12-05 11:06:59 | Pitabeddara (Nilwala Ganga) | 1.71 | 🟢 Normal | -0.040 |  |
| 2025-12-05 11:06:41 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:06:29 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.019 |  |
| 2025-12-05 11:06:00 | Giriulla (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:05:59 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:05:48 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:05:44 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.039 |  |
| 2025-12-05 11:04:50 | Ellagawa (Kalu Ganga) | 6.28 | 🟢 Normal | -0.030 |  |
| 2025-12-05 11:04:30 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.021 |  |
| 2025-12-05 11:03:58 | Glencourse (Kelani Ganga) | 10.52 | 🟢 Normal | -0.064 |  |
| 2025-12-05 11:03:51 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | -0.044 |  |
| 2025-12-05 11:03:48 | Hanwella (Kelani Ganga) | 3.36 | 🟢 Normal | -0.040 |  |
| 2025-12-05 11:03:38 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:03:35 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:02:49 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.055 |  |
| 2025-12-05 11:02:47 | Weraganthota (Mahaweli Ganga) | -0.35 | 🟢 Normal | -0.273 |  |
| 2025-12-05 11:02:27 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:02:20 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:02:19 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2025-12-05 11:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | -0.059 |  |
| 2025-12-05 11:02:14 | Galgamuwa (Mee Oya) | 0.57 | 🟢 Normal | -0.011 |  |
| 2025-12-05 11:02:07 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:01:50 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-05 11:01:38 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-05 11:01:31 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:01:14 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.155 |  |
| 2025-12-05 11:00:39 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:00:30 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-05 11:00:29 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-05 11:13:39 | Thanthirimale (Malwathu Oya) | 6.25 | 🟡 Alert | 0.085 | 🔺 Rising |
| 2025-12-05 11:01:50 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-05 11:02:19 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2025-12-05 11:02:07 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:00:29 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:06:41 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:06:00 | Giriulla (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:05:33 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:03:35 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:05:48 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:03:23 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:01:31 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:02:20 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:03:38 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:05:59 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:02:27 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:00:39 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-05 11:15:52 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2025-12-05 11:16:27 | Moraketiya (Walawe Ganga) | 1.31 | 🟢 Normal | -0.009 |  |
| 2025-12-05 11:00:30 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-05 11:01:38 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-05 11:02:14 | Galgamuwa (Mee Oya) | 0.57 | 🟢 Normal | -0.011 |  |
| 2025-12-05 11:06:29 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.019 |  |
| 2025-12-05 11:04:30 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.021 |  |
| 2025-12-05 11:04:50 | Ellagawa (Kalu Ganga) | 6.28 | 🟢 Normal | -0.030 |  |
| 2025-12-05 11:05:44 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.039 |  |
| 2025-12-05 11:03:48 | Hanwella (Kelani Ganga) | 3.36 | 🟢 Normal | -0.040 |  |
| 2025-12-05 11:06:59 | Pitabeddara (Nilwala Ganga) | 1.71 | 🟢 Normal | -0.040 |  |
| 2025-12-05 11:03:51 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | -0.044 |  |
| 2025-12-05 11:02:49 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.055 |  |
| 2025-12-05 11:15:15 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.056 |  |
| 2025-12-05 11:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | -0.059 |  |
| 2025-12-05 11:03:58 | Glencourse (Kelani Ganga) | 10.52 | 🟢 Normal | -0.064 |  |
| 2025-12-05 11:18:30 | Rathnapura (Kalu Ganga) | 2.25 | 🟢 Normal | -0.070 |  |
| 2025-12-05 11:14:11 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | -0.085 |  |
| 2025-12-05 11:01:14 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.155 |  |
| 2025-12-05 11:02:47 | Weraganthota (Mahaweli Ganga) | -0.35 | 🟢 Normal | -0.273 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)