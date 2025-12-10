# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--11_04:06:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,660 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 04:06:26 | Panadugama (Nilwala Ganga) | 3.18 | 🟢 Normal | -0.039 |  |
| 2025-12-11 04:05:59 | Horowpothana (Yan Oya) | 4.90 | 🟢 Normal | -0.114 |  |
| 2025-12-11 04:04:52 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2025-12-11 04:04:49 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 04:04:36 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-11 04:03:58 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.011 |  |
| 2025-12-11 04:03:26 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | -0.066 |  |
| 2025-12-11 04:03:18 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-11 04:03:04 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-11 04:03:02 | Hanwella (Kelani Ganga) | 1.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-11 04:02:04 | Yaka Wewa (Ma Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2025-12-11 04:01:31 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 04:01:18 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 04:01:11 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-11 04:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.017 |  |
| 2025-12-11 04:00:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2025-12-11 03:25:07 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.017 |  |
| 2025-12-11 03:19:35 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2025-12-11 03:16:08 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-11 03:15:54 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.017 |  |
| 2025-12-11 03:15:06 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | -3.600 |  |
| 2025-12-11 03:14:46 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -3.600 |  |
| 2025-12-11 03:14:36 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.018 |  |
| 2025-12-11 03:11:50 | Magura (Kalu Ganga) | 2.31 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-11 03:11:20 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.011 |  |
| 2025-12-11 03:09:06 | Glencourse (Kelani Ganga) | 9.87 | 🟢 Normal | -0.066 |  |
| 2025-12-11 03:08:55 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-11 03:07:31 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-11 04:00:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2025-12-11 04:04:52 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2025-12-11 03:02:44 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-10 18:02:01 | Thanthirimale (Malwathu Oya) | 3.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-11 03:11:50 | Magura (Kalu Ganga) | 2.31 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-11 04:03:02 | Hanwella (Kelani Ganga) | 1.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 18:04:22 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-11 04:01:11 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-11 04:01:31 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 03:00:09 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-11 04:03:18 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-11 03:06:56 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-11 03:07:09 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-11 04:03:04 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-11 03:03:58 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-11 03:16:08 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-11 03:02:05 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-11 04:04:49 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 03:01:51 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-11 03:07:31 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:09:04 | Manampitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-10 18:00:11 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-11 04:01:18 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 03:08:55 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-11 03:19:35 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2025-12-11 03:05:47 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-11 03:02:38 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2025-12-11 04:04:36 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-11 04:02:04 | Yaka Wewa (Ma Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2025-12-11 04:03:58 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.011 |  |
| 2025-12-11 04:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.017 |  |
| 2025-12-11 03:15:54 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.017 |  |
| 2025-12-11 03:14:36 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.018 |  |
| 2025-12-11 04:06:26 | Panadugama (Nilwala Ganga) | 3.18 | 🟢 Normal | -0.039 |  |
| 2025-12-11 04:03:26 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | -0.066 |  |
| 2025-12-11 04:05:59 | Horowpothana (Yan Oya) | 4.90 | 🟢 Normal | -0.114 |  |
| 2025-12-10 17:02:38 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.337 |  |
| 2025-12-11 03:15:06 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | -3.600 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)