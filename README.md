# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--02_01:26:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **7,053 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-02 01:26:07 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-02 01:19:46 | Putupaula (Kalu Ganga) | 4.02 | 🟠 Minor Flood | -0.016 |  |
| 2025-12-02 01:11:55 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -36.000 |  |
| 2025-12-02 01:11:54 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -36.000 |  |
| 2025-12-02 01:10:24 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-02 01:08:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.64 | 🟠 Minor Flood | -0.036 |  |
| 2025-12-02 01:08:04 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-02 01:07:32 | Glencourse (Kelani Ganga) | 11.81 | 🟢 Normal | 0.000 |  |
| 2025-12-02 01:07:31 | Glencourse (Kelani Ganga) | 11.81 | 🟢 Normal | 0.000 |  |
| 2025-12-02 01:06:28 | Hanwella (Kelani Ganga) | 8.07 | 🟠 Minor Flood | -0.070 |  |
| 2025-12-02 01:05:55 | Rathnapura (Kalu Ganga) | 4.47 | 🟢 Normal | -0.081 |  |
| 2025-12-02 01:05:03 | Dunamale (Aththanagalu Oya) | 3.20 | 🟢 Normal | -0.049 |  |
| 2025-12-02 01:04:54 | Ellagawa (Kalu Ganga) | 10.45 | 🟡 Alert | -0.047 |  |
| 2025-12-02 01:04:27 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-02 01:04:23 | Moraketiya (Walawe Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2025-12-02 01:03:51 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-02 01:03:49 | Nagalagam Street (Kelani Ganga) | 2.47 | 🔴 Major Flood | 0.000 |  |
| 2025-12-02 01:03:21 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-02 01:03:18 | Nakkala (Kumbukkan Oya) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-02 01:03:16 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | -0.011 |  |
| 2025-12-02 01:03:09 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-02 01:02:42 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-02 01:02:34 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.050 |  |
| 2025-12-02 01:01:12 | Badalgama (Maha Oya) | 3.82 | 🟢 Normal | -0.042 |  |
| 2025-12-02 01:00:47 | Giriulla (Maha Oya) | 2.67 | 🟢 Normal | -0.011 |  |
| 2025-12-02 01:00:21 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-02 00:59:51 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2025-12-02 00:58:38 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-02 00:34:27 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-02 01:03:49 | Nagalagam Street (Kelani Ganga) | 2.47 | 🔴 Major Flood | 0.000 |  |
| 2025-12-02 00:01:43 | Thanthirimale (Malwathu Oya) | 9.05 | 🔴 Major Flood | -0.030 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-02 01:19:46 | Putupaula (Kalu Ganga) | 4.02 | 🟠 Minor Flood | -0.016 |  |
| 2025-12-02 01:08:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.64 | 🟠 Minor Flood | -0.036 |  |
| 2025-12-02 01:06:28 | Hanwella (Kelani Ganga) | 8.07 | 🟠 Minor Flood | -0.070 |  |
| 2025-12-02 01:04:54 | Ellagawa (Kalu Ganga) | 10.45 | 🟡 Alert | -0.047 |  |
| 2025-12-02 00:59:51 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2025-12-02 01:03:09 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-02 01:03:18 | Nakkala (Kumbukkan Oya) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-02 00:02:18 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | 0.003 |  |
| 2025-12-02 01:00:21 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-02 01:03:51 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-02 00:07:40 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-02 01:08:04 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-02 01:04:27 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-02 01:07:32 | Glencourse (Kelani Ganga) | 11.81 | 🟢 Normal | 0.000 |  |
| 2025-12-02 01:26:07 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-02 00:09:34 | Katharagama (Menik Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-02 01:10:24 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-02 00:34:27 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-02 01:03:21 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-02 00:06:21 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2025-12-02 01:00:47 | Giriulla (Maha Oya) | 2.67 | 🟢 Normal | -0.011 |  |
| 2025-12-02 00:01:36 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | -0.011 |  |
| 2025-12-02 01:03:16 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | -0.011 |  |
| 2025-12-02 00:03:51 | Panadugama (Nilwala Ganga) | 3.18 | 🟢 Normal | -0.011 |  |
| 2025-12-02 01:04:23 | Moraketiya (Walawe Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2025-12-01 18:00:59 | Galgamuwa (Mee Oya) | 3.58 | 🟢 Normal | -0.021 |  |
| 2025-12-02 01:01:12 | Badalgama (Maha Oya) | 3.82 | 🟢 Normal | -0.042 |  |
| 2025-12-02 01:05:03 | Dunamale (Aththanagalu Oya) | 3.20 | 🟢 Normal | -0.049 |  |
| 2025-12-02 01:02:34 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.050 |  |
| 2025-12-02 01:05:55 | Rathnapura (Kalu Ganga) | 4.47 | 🟢 Normal | -0.081 |  |
| 2025-12-01 14:07:27 | Manampitiya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.135 |  |
| 2025-12-02 00:00:49 | Horowpothana (Yan Oya) | 5.84 | 🟢 Normal | -0.144 |  |
| 2025-12-02 01:11:55 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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