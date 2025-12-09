# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_23:17:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,671 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 23:17:30 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-09 23:08:47 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-09 23:08:05 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.019 |  |
| 2025-12-09 23:07:45 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | -0.040 |  |
| 2025-12-09 23:07:36 | Glencourse (Kelani Ganga) | 10.17 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-09 23:06:18 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 23:05:55 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2025-12-09 23:05:35 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2025-12-09 23:05:17 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.000 |  |
| 2025-12-09 23:05:11 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 23:04:21 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-09 23:04:03 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-09 23:03:42 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | -0.011 |  |
| 2025-12-09 23:03:21 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 23:02:52 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.040 |  |
| 2025-12-09 23:02:29 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 23:02:12 | Yaka Wewa (Ma Oya) | 1.63 | 🟢 Normal | -0.020 |  |
| 2025-12-09 23:02:01 | Urawa (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.675 |  |
| 2025-12-09 23:01:59 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-09 23:01:55 | Pitabeddara (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-09 23:01:44 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-09 23:01:20 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 23:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 23:01:07 | Horowpothana (Yan Oya) | 3.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-09 23:00:35 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.022 |  |
| 2025-12-09 23:00:31 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | -0.061 |  |
| 2025-12-09 23:00:12 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:42:28 | Urawa (Nilwala Ganga) | 2.50 | 🟡 Alert | -0.675 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 22:01:54 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2025-12-09 18:00:14 | Weraganthota (Mahaweli Ganga) | -0.91 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2025-12-09 23:05:55 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2025-12-09 23:17:30 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-09 21:05:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-09 18:00:08 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-09 23:01:55 | Pitabeddara (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-09 23:07:36 | Glencourse (Kelani Ganga) | 10.17 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-09 23:01:59 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-09 23:01:07 | Horowpothana (Yan Oya) | 3.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-09 23:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 23:02:29 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 23:05:11 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 23:06:18 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 23:00:12 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-09 23:04:21 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:14:12 | Galgamuwa (Mee Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:09:27 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-09 23:04:03 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-09 23:01:44 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-09 23:01:20 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 23:03:21 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 23:05:17 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:23:40 | Thanthirimale (Malwathu Oya) | 3.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:05:02 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-09 23:03:42 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | -0.011 |  |
| 2025-12-09 23:08:05 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.019 |  |
| 2025-12-09 18:02:37 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-09 23:02:12 | Yaka Wewa (Ma Oya) | 1.63 | 🟢 Normal | -0.020 |  |
| 2025-12-09 23:05:35 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2025-12-09 22:03:37 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | -0.021 |  |
| 2025-12-09 23:00:35 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.022 |  |
| 2025-12-09 18:04:00 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.025 |  |
| 2025-12-09 23:07:45 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | -0.040 |  |
| 2025-12-09 23:02:52 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.040 |  |
| 2025-12-09 22:13:28 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.059 |  |
| 2025-12-09 23:00:31 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | -0.061 |  |
| 2025-12-09 23:02:01 | Urawa (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.675 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)