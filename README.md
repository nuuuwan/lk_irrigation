# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--03_08:02:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,065 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-03 08:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.79 | 🟢 Normal | -0.110 |  |
| 2025-12-03 08:02:01 | Badalgama (Maha Oya) | 3.30 | 🟢 Normal | -0.011 |  |
| 2025-12-03 08:01:24 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | -0.024 |  |
| 2025-12-03 08:01:23 | Ellagawa (Kalu Ganga) | 7.81 | 🟢 Normal | -0.151 |  |
| 2025-12-03 08:01:20 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:01:16 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:01:04 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-03 08:00:20 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.011 |  |
| 2025-12-03 07:43:57 | Panadugama (Nilwala Ganga) | 3.05 | 🟢 Normal | 0.000 |  |
| 2025-12-03 07:36:11 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-03 07:34:34 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-03 07:24:19 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.046 |  |
| 2025-12-03 07:11:52 | Nagalagam Street (Kelani Ganga) | 1.48 | 🟡 Alert | -0.044 |  |
| 2025-12-03 07:11:41 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-03 07:11:22 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.009 |  |
| 2025-12-03 07:11:10 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | -0.024 |  |
| 2025-12-03 07:11:04 | Kuda Oya (Kirindi Oya) | 1.72 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-03 07:08:05 | Giriulla (Maha Oya) | 2.19 | 🟢 Normal | -0.009 |  |
| 2025-12-03 07:07:32 | Badalgama (Maha Oya) | 3.31 | 🟢 Normal | -0.011 |  |
| 2025-12-03 07:07:11 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2025-12-03 07:06:50 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.084 |  |
| 2025-12-03 07:06:31 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | -0.009 |  |
| 2025-12-03 07:06:04 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-03 07:05:57 | Katharagama (Menik Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-03 07:05:24 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-03 07:05:14 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | -0.009 |  |
| 2025-12-03 07:04:44 | Hanwella (Kelani Ganga) | 5.68 | 🟢 Normal | -0.077 |  |
| 2025-12-03 07:04:41 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.011 |  |
| 2025-12-03 07:04:32 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-03 07:04:30 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-03 07:04:24 | Yaka Wewa (Ma Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-03 07:04:18 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-03 07:03:58 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-03 07:03:55 | Putupaula (Kalu Ganga) | 3.12 | 🟡 Alert | -0.019 |  |
| 2025-12-03 07:03:42 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-03 07:02:37 | Thanthirimale (Malwathu Oya) | 7.50 | 🟠 Minor Flood | -0.040 |  |
| 2025-12-03 07:03:55 | Putupaula (Kalu Ganga) | 3.12 | 🟡 Alert | -0.019 |  |
| 2025-12-03 07:11:52 | Nagalagam Street (Kelani Ganga) | 1.48 | 🟡 Alert | -0.044 |  |
| 2025-12-03 07:01:49 | Nakkala (Kumbukkan Oya) | 1.46 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-03 07:01:15 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-03 07:03:42 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-03 08:01:04 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-03 07:04:32 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-03 07:11:41 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-03 07:11:04 | Kuda Oya (Kirindi Oya) | 1.72 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-03 07:04:30 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-03 07:04:24 | Yaka Wewa (Ma Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:01:20 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-03 07:43:57 | Panadugama (Nilwala Ganga) | 3.05 | 🟢 Normal | 0.000 |  |
| 2025-12-03 07:04:18 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:01:16 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-03 07:07:11 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2025-12-03 07:36:11 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-03 07:05:57 | Katharagama (Menik Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-03 07:01:44 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-03 07:11:22 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.009 |  |
| 2025-12-03 07:06:31 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | -0.009 |  |
| 2025-12-03 07:08:05 | Giriulla (Maha Oya) | 2.19 | 🟢 Normal | -0.009 |  |
| 2025-12-03 07:05:14 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | -0.009 |  |
| 2025-12-03 07:06:04 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-03 08:00:20 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.011 |  |
| 2025-12-03 08:02:01 | Badalgama (Maha Oya) | 3.30 | 🟢 Normal | -0.011 |  |
| 2025-12-02 18:12:00 | Manampitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.018 |  |
| 2025-12-03 08:01:24 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | -0.024 |  |
| 2025-12-03 07:24:19 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.046 |  |
| 2025-12-03 07:04:44 | Hanwella (Kelani Ganga) | 5.68 | 🟢 Normal | -0.077 |  |
| 2025-12-03 07:06:50 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.084 |  |
| 2025-12-03 07:00:10 | Horowpothana (Yan Oya) | 3.16 | 🟢 Normal | -0.103 |  |
| 2025-12-03 08:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.79 | 🟢 Normal | -0.110 |  |
| 2025-12-02 18:07:24 | Galgamuwa (Mee Oya) | 2.52 | 🟢 Normal | -0.120 |  |
| 2025-12-03 08:01:23 | Ellagawa (Kalu Ganga) | 7.81 | 🟢 Normal | -0.151 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)