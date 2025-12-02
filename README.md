# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--03_05:03:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **7,970 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-03 05:03:25 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.054 |  |
| 2025-12-03 05:03:25 | Putupaula (Kalu Ganga) | 3.17 | 🟡 Alert | -0.122 |  |
| 2025-12-03 05:03:02 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | -0.011 |  |
| 2025-12-03 05:03:01 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-03 05:02:56 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-03 05:01:51 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2025-12-03 05:01:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.17 | 🟡 Alert | -0.101 |  |
| 2025-12-03 05:01:23 | Badalgama (Maha Oya) | 3.34 | 🟢 Normal | -0.033 |  |
| 2025-12-03 05:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-03 05:00:30 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.040 |  |
| 2025-12-03 05:00:26 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-03 04:41:08 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.054 |  |
| 2025-12-03 04:37:55 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-03 04:34:01 | Putupaula (Kalu Ganga) | 3.23 | 🟡 Alert | -0.122 |  |
| 2025-12-03 04:14:30 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.018 |  |
| 2025-12-03 04:12:34 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-03 04:11:13 | Panadugama (Nilwala Ganga) | 3.05 | 🟢 Normal | -0.012 |  |
| 2025-12-03 04:09:33 | Hanwella (Kelani Ganga) | 5.91 | 🟢 Normal | -0.040 |  |
| 2025-12-03 04:08:22 | Nagalagam Street (Kelani Ganga) | 1.68 | 🟠 Minor Flood | -0.060 |  |
| 2025-12-03 04:07:03 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.014 |  |
| 2025-12-03 04:06:25 | Giriulla (Maha Oya) | 2.21 | 🟢 Normal | -0.011 |  |
| 2025-12-03 04:06:25 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-03 04:06:00 | Badalgama (Maha Oya) | 3.37 | 🟢 Normal | -0.033 |  |
| 2025-12-03 04:05:48 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.013 |  |
| 2025-12-03 04:05:18 | Rathnapura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.069 |  |
| 2025-12-03 04:05:10 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2025-12-03 04:04:35 | Glencourse (Kelani Ganga) | 11.04 | 🟢 Normal | -0.031 |  |
| 2025-12-03 04:04:24 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.031 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-03 04:00:40 | Thanthirimale (Malwathu Oya) | 7.62 | 🟠 Minor Flood | -0.045 |  |
| 2025-12-03 04:08:22 | Nagalagam Street (Kelani Ganga) | 1.68 | 🟠 Minor Flood | -0.060 |  |
| 2025-12-03 05:01:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.17 | 🟡 Alert | -0.101 |  |
| 2025-12-03 05:03:25 | Putupaula (Kalu Ganga) | 3.17 | 🟡 Alert | -0.122 |  |
| 2025-12-03 05:01:51 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2025-12-03 05:02:56 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-03 05:00:26 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-03 04:06:25 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-03 05:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-03 04:01:59 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-03 05:03:01 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:02:23 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-03 04:03:56 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2025-12-03 04:01:17 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-03 04:37:55 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-03 04:12:34 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-03 04:05:10 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2025-12-03 04:01:22 | Nakkala (Kumbukkan Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-03 04:01:49 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-03 05:03:02 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | -0.011 |  |
| 2025-12-03 04:11:13 | Panadugama (Nilwala Ganga) | 3.05 | 🟢 Normal | -0.012 |  |
| 2025-12-03 04:05:48 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.013 |  |
| 2025-12-03 04:07:03 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.014 |  |
| 2025-12-02 18:12:00 | Manampitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.018 |  |
| 2025-12-03 04:14:30 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.018 |  |
| 2025-12-03 03:04:13 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | -0.025 |  |
| 2025-12-03 04:04:35 | Glencourse (Kelani Ganga) | 11.04 | 🟢 Normal | -0.031 |  |
| 2025-12-03 05:01:23 | Badalgama (Maha Oya) | 3.34 | 🟢 Normal | -0.033 |  |
| 2025-12-03 05:00:30 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.040 |  |
| 2025-12-03 04:09:33 | Hanwella (Kelani Ganga) | 5.91 | 🟢 Normal | -0.040 |  |
| 2025-12-03 05:03:25 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.054 |  |
| 2025-12-03 04:01:50 | Horowpothana (Yan Oya) | 3.34 | 🟢 Normal | -0.063 |  |
| 2025-12-03 04:05:18 | Rathnapura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.069 |  |
| 2025-12-02 18:07:24 | Galgamuwa (Mee Oya) | 2.52 | 🟢 Normal | -0.120 |  |
| 2025-12-03 04:03:26 | Ellagawa (Kalu Ganga) | 3.18 | 🟢 Normal | -5.408 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)