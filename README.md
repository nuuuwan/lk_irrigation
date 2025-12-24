# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--25_05:03:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,181 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 05:03:58 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:03:50 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:03:44 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-25 05:03:34 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:03:17 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.033 |  |
| 2025-12-25 05:02:22 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-25 05:02:13 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:02:12 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:02:07 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-25 05:01:55 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 05:01:38 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.033 |  |
| 2025-12-25 05:01:23 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.032 |  |
| 2025-12-25 05:01:19 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.054 |  |
| 2025-12-25 05:01:17 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2025-12-25 05:00:36 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:59:28 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:45:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | 19.286 | 🔺 Rising |
| 2025-12-25 04:45:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | 19.286 | 🔺 Rising |
| 2025-12-25 04:45:29 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2025-12-25 04:45:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | 19.286 | 🔺 Rising |
| 2025-12-25 04:29:39 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:28:16 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.054 |  |
| 2025-12-25 04:23:04 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-25 04:20:36 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.024 |  |
| 2025-12-25 04:18:18 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.041 |  |
| 2025-12-25 04:12:34 | Magura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.054 |  |
| 2025-12-25 04:10:56 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -2.323 |  |
| 2025-12-25 04:10:39 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:10:25 | Thawalama (Gin Ganga) | 2.42 | 🟢 Normal | -2.323 |  |
| 2025-12-25 04:08:07 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.033 |  |
| 2025-12-25 04:06:16 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | -6.857 |  |
| 2025-12-25 04:05:59 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:05:55 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | -6.857 |  |
| 2025-12-25 04:05:54 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-25 04:05:50 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 04:45:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | 19.286 | 🔺 Rising |
| 2025-12-25 03:30:06 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2025-12-25 04:02:18 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.336 | 🔺 Rising |
| 2025-12-25 03:07:51 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2025-12-25 04:45:29 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2025-12-25 03:02:44 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-25 04:00:49 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-25 04:05:54 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-25 04:23:04 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-25 05:03:44 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-25 05:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 05:02:12 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:03:58 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:03:50 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:01:55 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:03:01 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:07:47 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:05:25 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:00:36 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:29:39 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:08:39 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:04:58 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:03:34 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-25 03:07:08 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:10:39 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:02:13 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-25 05:02:07 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-25 05:01:17 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2025-12-25 05:02:22 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-24 18:03:33 | Weraganthota (Mahaweli Ganga) | -1.10 | 🟢 Normal | -0.020 |  |
| 2025-12-25 04:20:36 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.024 |  |
| 2025-12-25 05:01:23 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.032 |  |
| 2025-12-25 05:01:38 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.033 |  |
| 2025-12-25 05:03:17 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.033 |  |
| 2025-12-25 04:18:18 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.041 |  |
| 2025-12-24 18:01:19 | Thanthirimale (Malwathu Oya) | 2.11 | 🟢 Normal | -0.051 |  |
| 2025-12-25 05:01:19 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.054 |  |
| 2025-12-25 04:10:56 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -2.323 |  |
| 2025-12-25 04:06:16 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | -6.857 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)