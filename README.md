# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--26_13:29:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **28,411 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 13:29:27 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:28:08 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2025-12-26 13:28:07 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2025-12-26 13:21:57 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:18:00 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:10:54 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.026 |  |
| 2025-12-26 13:09:32 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2025-12-26 13:09:07 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2025-12-26 13:06:57 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:06:17 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 13:05:59 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-26 13:05:28 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:05:19 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 13:05:17 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:04:54 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | -0.010 |  |
| 2025-12-26 13:04:52 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:04:45 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:04:32 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:04:00 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:03:15 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2025-12-26 13:03:12 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.051 |  |
| 2025-12-26 13:03:05 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:02:59 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | -0.020 |  |
| 2025-12-26 13:02:53 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2025-12-26 13:02:48 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:02:47 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:02:43 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:02:34 | Horowpothana (Yan Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2025-12-26 13:02:21 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2025-12-26 13:02:17 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.091 |  |
| 2025-12-26 13:01:44 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.011 |  |
| 2025-12-26 13:01:34 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:01:25 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:01:21 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-26 13:01:06 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2025-12-26 13:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:00:45 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.030 |  |
| 2025-12-26 13:00:29 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.040 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 13:28:08 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2025-12-26 13:00:29 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-26 13:01:21 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-26 13:06:17 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 13:05:19 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 13:01:25 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:21:57 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:02:43 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:04:00 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:01:34 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:02:47 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:04:52 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:04:32 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:02:17 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:05:28 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:05:17 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:02:48 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:04:45 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:06:57 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:18:00 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:29:27 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:09:07 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2025-12-26 13:09:32 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2025-12-26 13:02:34 | Horowpothana (Yan Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2025-12-26 13:03:15 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2025-12-26 13:04:54 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | -0.010 |  |
| 2025-12-26 13:05:59 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-26 13:01:06 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2025-12-26 13:01:44 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.011 |  |
| 2025-12-26 13:02:59 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | -0.020 |  |
| 2025-12-26 13:02:53 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2025-12-26 13:02:21 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2025-12-26 13:10:54 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.026 |  |
| 2025-12-26 13:00:45 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.030 |  |
| 2025-12-26 13:28:07 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2025-12-26 12:02:53 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | -0.032 |  |
| 2025-12-26 13:03:12 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.051 |  |
| 2025-12-26 13:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)