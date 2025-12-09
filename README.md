# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_11:11:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,243 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 11:11:57 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-09 11:10:49 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-09 11:09:50 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2025-12-09 11:09:19 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-09 11:07:17 | Thaldena (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2025-12-09 11:05:44 | Yaka Wewa (Ma Oya) | 1.40 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2025-12-09 11:05:39 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-09 11:05:19 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 11:04:50 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | -0.097 |  |
| 2025-12-09 11:04:41 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.079 |  |
| 2025-12-09 11:04:39 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2025-12-09 11:04:39 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.034 |  |
| 2025-12-09 11:04:19 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-09 11:04:17 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 11:04:15 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2025-12-09 11:04:03 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | 0.000 |  |
| 2025-12-09 11:03:57 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2025-12-09 11:03:57 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.032 |  |
| 2025-12-09 11:03:55 | Panadugama (Nilwala Ganga) | 3.31 | 🟢 Normal | -0.040 |  |
| 2025-12-09 11:03:29 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.084 |  |
| 2025-12-09 11:03:20 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.063 |  |
| 2025-12-09 11:03:17 | Ellagawa (Kalu Ganga) | 5.93 | 🟢 Normal | -0.021 |  |
| 2025-12-09 11:03:05 | Glencourse (Kelani Ganga) | 10.04 | 🟢 Normal | 0.000 |  |
| 2025-12-09 11:03:03 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.077 |  |
| 2025-12-09 11:03:02 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 11:03:00 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-09 11:02:57 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2025-12-09 11:02:53 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 11:02:46 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 11:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-09 11:02:41 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.040 |  |
| 2025-12-09 11:02:37 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-09 11:01:15 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 11:01:14 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.011 |  |
| 2025-12-09 11:01:13 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 11:00:41 | Nakkala (Kumbukkan Oya) | 1.52 | 🟢 Normal | 0.141 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 11:05:44 | Yaka Wewa (Ma Oya) | 1.40 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2025-12-09 11:00:41 | Nakkala (Kumbukkan Oya) | 1.52 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2025-12-09 11:07:17 | Thaldena (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2025-12-09 11:04:39 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2025-12-09 11:09:19 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-09 11:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-09 11:10:49 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-09 11:04:17 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 11:01:15 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 11:02:46 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 11:11:57 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-09 11:03:57 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2025-12-09 11:02:37 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-09 11:04:19 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-09 11:03:05 | Glencourse (Kelani Ganga) | 10.04 | 🟢 Normal | 0.000 |  |
| 2025-12-09 11:01:13 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 11:05:39 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-09 11:03:02 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 11:05:19 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 11:04:03 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | 0.000 |  |
| 2025-12-09 11:02:53 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 11:03:00 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-09 11:04:15 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2025-12-09 11:09:50 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2025-12-09 11:01:14 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.011 |  |
| 2025-12-09 10:06:28 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.020 |  |
| 2025-12-09 11:03:17 | Ellagawa (Kalu Ganga) | 5.93 | 🟢 Normal | -0.021 |  |
| 2025-12-09 11:03:57 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.032 |  |
| 2025-12-09 11:04:39 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.034 |  |
| 2025-12-09 11:02:41 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.040 |  |
| 2025-12-09 11:03:55 | Panadugama (Nilwala Ganga) | 3.31 | 🟢 Normal | -0.040 |  |
| 2025-12-09 10:17:14 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.042 |  |
| 2025-12-09 11:03:20 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.063 |  |
| 2025-12-09 11:03:03 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.077 |  |
| 2025-12-09 11:04:41 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.079 |  |
| 2025-12-09 11:03:29 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.084 |  |
| 2025-12-09 11:04:50 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | -0.097 |  |
| 2025-12-09 10:00:54 | Thanthirimale (Malwathu Oya) | 3.38 | 🟢 Normal | -0.142 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)