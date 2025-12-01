# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--02_05:15:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **7,159 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-02 05:15:12 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | -0.018 |  |
| 2025-12-02 05:10:31 | Rathnapura (Kalu Ganga) | 4.20 | 🟢 Normal | -0.088 |  |
| 2025-12-02 05:10:25 | Giriulla (Maha Oya) | 2.64 | 🟢 Normal | -0.009 |  |
| 2025-12-02 05:09:45 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.018 |  |
| 2025-12-02 05:09:10 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | -0.021 |  |
| 2025-12-02 05:08:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.44 | 🟡 Alert | -0.059 |  |
| 2025-12-02 05:08:12 | Holombuwa (Kelani Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-02 05:06:53 | Hanwella (Kelani Ganga) | 7.80 | 🟡 Alert | -0.070 |  |
| 2025-12-02 05:05:50 | Nagalagam Street (Kelani Ganga) | 2.32 | 🔴 Major Flood | -0.046 |  |
| 2025-12-02 05:05:26 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-02 05:04:59 | Moraketiya (Walawe Ganga) | 1.71 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2025-12-02 05:04:39 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | -0.060 |  |
| 2025-12-02 05:04:37 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2025-12-02 05:03:47 | Ellagawa (Kalu Ganga) | 10.21 | 🟡 Alert | -0.055 |  |
| 2025-12-02 05:03:18 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-02 05:02:51 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-02 05:02:40 | Nakkala (Kumbukkan Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-02 05:02:32 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-02 05:02:26 | Putupaula (Kalu Ganga) | 3.98 | 🟡 Alert | -0.022 |  |
| 2025-12-02 05:01:56 | Thanthirimale (Malwathu Oya) | 8.89 | 🔴 Major Flood | -0.020 |  |
| 2025-12-02 05:01:33 | Badalgama (Maha Oya) | 3.71 | 🟢 Normal | -0.030 |  |
| 2025-12-02 05:00:12 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | -0.052 |  |
| 2025-12-02 04:41:06 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | -0.018 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-02 05:01:56 | Thanthirimale (Malwathu Oya) | 8.89 | 🔴 Major Flood | -0.020 |  |
| 2025-12-02 05:05:50 | Nagalagam Street (Kelani Ganga) | 2.32 | 🔴 Major Flood | -0.046 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-02 05:02:26 | Putupaula (Kalu Ganga) | 3.98 | 🟡 Alert | -0.022 |  |
| 2025-12-02 05:03:47 | Ellagawa (Kalu Ganga) | 10.21 | 🟡 Alert | -0.055 |  |
| 2025-12-02 05:08:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.44 | 🟡 Alert | -0.059 |  |
| 2025-12-02 05:06:53 | Hanwella (Kelani Ganga) | 7.80 | 🟡 Alert | -0.070 |  |
| 2025-12-02 05:04:59 | Moraketiya (Walawe Ganga) | 1.71 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2025-12-02 04:04:00 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-02 00:02:18 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | 0.003 |  |
| 2025-12-02 05:05:26 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-02 03:23:04 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-02 04:03:07 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-02 05:02:51 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-02 05:03:18 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-02 01:26:07 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-02 05:10:25 | Giriulla (Maha Oya) | 2.64 | 🟢 Normal | -0.009 |  |
| 2025-12-02 05:02:32 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-02 05:02:40 | Nakkala (Kumbukkan Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-02 05:08:12 | Holombuwa (Kelani Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-02 05:04:37 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2025-12-02 00:01:36 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | -0.011 |  |
| 2025-12-02 04:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.012 |  |
| 2025-12-02 05:15:12 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | -0.018 |  |
| 2025-12-02 05:09:45 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.018 |  |
| 2025-12-02 04:11:57 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | -0.019 |  |
| 2025-12-02 04:01:53 | Thalgahagoda (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2025-12-01 18:00:59 | Galgamuwa (Mee Oya) | 3.58 | 🟢 Normal | -0.021 |  |
| 2025-12-02 05:09:10 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | -0.021 |  |
| 2025-12-02 05:01:33 | Badalgama (Maha Oya) | 3.71 | 🟢 Normal | -0.030 |  |
| 2025-12-02 05:00:12 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | -0.052 |  |
| 2025-12-02 05:04:39 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | -0.060 |  |
| 2025-12-02 05:10:31 | Rathnapura (Kalu Ganga) | 4.20 | 🟢 Normal | -0.088 |  |
| 2025-12-01 14:07:27 | Manampitiya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.135 |  |
| 2025-12-02 00:00:49 | Horowpothana (Yan Oya) | 5.84 | 🟢 Normal | -0.144 |  |
| 2025-12-02 04:05:12 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)