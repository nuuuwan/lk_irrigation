# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--28_23:04:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **30,551 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 23:04:47 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-28 23:04:35 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-28 23:04:18 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-28 23:03:47 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-28 23:03:35 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-28 23:03:22 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.005 |  |
| 2025-12-28 23:03:11 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-28 23:03:07 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-28 23:02:55 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-28 23:02:30 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-28 23:02:26 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-28 23:02:22 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | -0.010 |  |
| 2025-12-28 23:01:46 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-28 23:01:41 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | -0.011 |  |
| 2025-12-28 23:01:36 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-28 23:01:29 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-28 23:01:18 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 23:01:10 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-28 23:00:36 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 23:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-28 23:00:24 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2025-12-28 23:00:06 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-28 22:20:42 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-28 22:16:42 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-28 22:14:16 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 22:09:31 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-28 22:09:21 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-28 22:07:30 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 22:07:26 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 21:07:39 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2025-12-28 23:01:10 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-28 22:20:42 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-28 22:09:21 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-28 23:01:18 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 23:04:18 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-28 22:05:35 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-28 22:14:16 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 23:01:29 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-28 18:12:51 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-28 22:03:24 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 23:03:47 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-28 23:02:26 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-28 23:02:30 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-28 23:01:46 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-28 21:03:57 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.000 |  |
| 2025-12-28 22:04:15 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-28 23:00:06 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-28 23:03:35 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-28 22:04:45 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-28 22:05:27 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 18:09:20 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-28 23:00:36 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 22:01:11 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 23:04:35 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-28 23:03:22 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.005 |  |
| 2025-12-28 23:03:07 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-28 23:03:11 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-28 23:02:22 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | -0.010 |  |
| 2025-12-28 23:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-28 18:02:15 | Weraganthota (Mahaweli Ganga) | -1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-28 23:04:47 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-28 23:01:36 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-28 22:05:44 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.011 |  |
| 2025-12-28 23:01:41 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | -0.011 |  |
| 2025-12-28 23:00:24 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2025-12-28 21:13:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.020 |  |
| 2025-12-28 22:06:00 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.056 |  |
| 2025-12-28 22:05:42 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.108 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)