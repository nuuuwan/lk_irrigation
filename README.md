# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--03_03:23:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **7,928 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-03 03:23:25 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:20:11 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:19:59 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:15:53 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.009 |  |
| 2025-12-03 03:12:36 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:09:35 | Hanwella (Kelani Ganga) | 5.95 | 🟢 Normal | -0.068 |  |
| 2025-12-03 03:07:54 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:07:48 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | -0.019 |  |
| 2025-12-03 03:07:34 | Nagalagam Street (Kelani Ganga) | 1.74 | 🟠 Minor Flood | -0.089 |  |
| 2025-12-03 03:07:32 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2025-12-03 03:07:29 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | -0.009 |  |
| 2025-12-03 03:07:18 | Thanthirimale (Malwathu Oya) | 7.66 | 🟠 Minor Flood | -0.610 |  |
| 2025-12-03 03:06:15 | Putupaula (Kalu Ganga) | 3.27 | 🟡 Alert | -0.090 |  |
| 2025-12-03 03:06:12 | Glencourse (Kelani Ganga) | 11.07 | 🟢 Normal | -0.011 |  |
| 2025-12-03 03:05:55 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:05:01 | Horowpothana (Yan Oya) | 3.40 | 🟢 Normal | -0.048 |  |
| 2025-12-03 03:04:58 | Ellagawa (Kalu Ganga) | 8.45 | 🟢 Normal | -0.134 |  |
| 2025-12-03 03:04:41 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2025-12-03 03:04:13 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | -0.025 |  |
| 2025-12-03 03:04:02 | Rathnapura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.061 |  |
| 2025-12-03 03:03:55 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-03 03:03:31 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:03:29 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:03:22 | Thanthirimale (Malwathu Oya) | 7.70 | 🟠 Minor Flood | -0.610 |  |
| 2025-12-03 03:03:16 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.121 |  |
| 2025-12-03 03:03:09 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.32 | 🟡 Alert | -0.128 |  |
| 2025-12-03 03:02:41 | Giriulla (Maha Oya) | 2.22 | 🟢 Normal | -0.030 |  |
| 2025-12-03 03:02:23 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:02:22 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:02:12 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:01:55 | Badalgama (Maha Oya) | 3.39 | 🟢 Normal | -0.010 |  |
| 2025-12-03 03:01:12 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:01:03 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:00:19 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.060 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-03 03:07:34 | Nagalagam Street (Kelani Ganga) | 1.74 | 🟠 Minor Flood | -0.089 |  |
| 2025-12-03 03:07:18 | Thanthirimale (Malwathu Oya) | 7.66 | 🟠 Minor Flood | -0.610 |  |
| 2025-12-03 03:06:15 | Putupaula (Kalu Ganga) | 3.27 | 🟡 Alert | -0.090 |  |
| 2025-12-03 03:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.32 | 🟡 Alert | -0.128 |  |
| 2025-12-03 03:00:19 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-03 03:03:55 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-03 03:02:12 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:01:03 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:19:59 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:02:22 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:20:11 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:02:23 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:03:09 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:03:31 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:05:55 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:23:25 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:07:54 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:01:12 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:03:29 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:15:53 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.009 |  |
| 2025-12-03 03:07:29 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | -0.009 |  |
| 2025-12-03 03:01:55 | Badalgama (Maha Oya) | 3.39 | 🟢 Normal | -0.010 |  |
| 2025-12-03 03:07:32 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2025-12-03 03:06:12 | Glencourse (Kelani Ganga) | 11.07 | 🟢 Normal | -0.011 |  |
| 2025-12-02 18:12:00 | Manampitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.018 |  |
| 2025-12-03 03:07:48 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | -0.019 |  |
| 2025-12-03 03:04:41 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2025-12-03 03:04:13 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | -0.025 |  |
| 2025-12-03 03:02:41 | Giriulla (Maha Oya) | 2.22 | 🟢 Normal | -0.030 |  |
| 2025-12-03 03:05:01 | Horowpothana (Yan Oya) | 3.40 | 🟢 Normal | -0.048 |  |
| 2025-12-03 03:04:02 | Rathnapura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.061 |  |
| 2025-12-03 03:09:35 | Hanwella (Kelani Ganga) | 5.95 | 🟢 Normal | -0.068 |  |
| 2025-12-02 18:07:24 | Galgamuwa (Mee Oya) | 2.52 | 🟢 Normal | -0.120 |  |
| 2025-12-03 03:03:16 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.121 |  |
| 2025-12-03 03:04:58 | Ellagawa (Kalu Ganga) | 8.45 | 🟢 Normal | -0.134 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)