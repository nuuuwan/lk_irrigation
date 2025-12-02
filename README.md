# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--02_15:07:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **7,527 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-02 15:07:04 | Ellagawa (Kalu Ganga) | 9.56 | 🟢 Normal | -0.057 |  |
| 2025-12-02 15:06:50 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-02 15:06:47 | Hanwella (Kelani Ganga) | 7.07 | 🟡 Alert | -0.069 |  |
| 2025-12-02 15:06:26 | Nagalagam Street (Kelani Ganga) | 2.06 | 🟠 Minor Flood | -0.045 |  |
| 2025-12-02 15:06:03 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-02 15:06:03 | Glencourse (Kelani Ganga) | 11.27 | 🟢 Normal | -0.051 |  |
| 2025-12-02 15:05:28 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | -0.037 |  |
| 2025-12-02 15:04:28 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.011 |  |
| 2025-12-02 15:04:24 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-02 15:04:19 | Giriulla (Maha Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2025-12-02 15:04:12 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2025-12-02 15:03:33 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-02 15:03:31 | Dunamale (Aththanagalu Oya) | 2.64 | 🟢 Normal | -0.043 |  |
| 2025-12-02 15:03:30 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2025-12-02 15:03:28 | Putupaula (Kalu Ganga) | 3.70 | 🟡 Alert | -0.030 |  |
| 2025-12-02 15:03:26 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -55.268 |  |
| 2025-12-02 15:02:54 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-02 15:02:47 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-02 15:02:44 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | -0.019 |  |
| 2025-12-02 15:02:37 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 15:02:35 | Thanthirimale (Malwathu Oya) | 8.19 | 🔴 Major Flood | -1.040 |  |
| 2025-12-02 15:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.85 | 🟡 Alert | -0.060 |  |
| 2025-12-02 15:02:26 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-02 15:02:24 | Rathnapura (Kalu Ganga) | 3.33 | 🟢 Normal | -0.103 |  |
| 2025-12-02 15:02:20 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-02 15:02:15 | Badalgama (Maha Oya) | 3.56 | 🟢 Normal | -55.268 |  |
| 2025-12-02 15:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-02 15:02:04 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | -0.020 |  |
| 2025-12-02 15:01:32 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.030 |  |
| 2025-12-02 15:01:19 | Moraketiya (Walawe Ganga) | 1.71 | 🟢 Normal | -0.020 |  |
| 2025-12-02 15:00:15 | Horowpothana (Yan Oya) | 4.03 | 🟢 Normal | -0.094 |  |
| 2025-12-02 15:00:09 | Nakkala (Kumbukkan Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2025-12-02 14:23:43 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-02 14:21:40 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.000 |  |
| 2025-12-02 14:16:38 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | -0.037 |  |
| 2025-12-02 14:13:18 | Galgamuwa (Mee Oya) | 2.95 | 🟢 Normal | -0.074 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-02 15:02:35 | Thanthirimale (Malwathu Oya) | 8.19 | 🔴 Major Flood | -1.040 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-02 15:06:26 | Nagalagam Street (Kelani Ganga) | 2.06 | 🟠 Minor Flood | -0.045 |  |
| 2025-12-02 15:03:28 | Putupaula (Kalu Ganga) | 3.70 | 🟡 Alert | -0.030 |  |
| 2025-12-02 15:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.85 | 🟡 Alert | -0.060 |  |
| 2025-12-02 15:06:47 | Hanwella (Kelani Ganga) | 7.07 | 🟡 Alert | -0.069 |  |
| 2025-12-02 15:06:50 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-02 13:20:19 | Manampitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2025-12-02 15:02:37 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 15:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-02 15:03:33 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-02 15:04:19 | Giriulla (Maha Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2025-12-02 15:02:20 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-02 14:21:40 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.000 |  |
| 2025-12-02 15:02:54 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-02 15:02:26 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-02 15:02:47 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-02 15:04:24 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-02 15:06:03 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-02 15:04:12 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2025-12-02 15:03:30 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2025-12-02 15:00:09 | Nakkala (Kumbukkan Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2025-12-02 15:04:28 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.011 |  |
| 2025-12-02 10:06:19 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | -0.011 |  |
| 2025-12-02 15:02:44 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | -0.019 |  |
| 2025-12-02 15:01:19 | Moraketiya (Walawe Ganga) | 1.71 | 🟢 Normal | -0.020 |  |
| 2025-12-02 15:02:04 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | -0.020 |  |
| 2025-12-02 15:01:32 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.030 |  |
| 2025-12-02 15:05:28 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | -0.037 |  |
| 2025-12-02 15:03:31 | Dunamale (Aththanagalu Oya) | 2.64 | 🟢 Normal | -0.043 |  |
| 2025-12-02 15:06:03 | Glencourse (Kelani Ganga) | 11.27 | 🟢 Normal | -0.051 |  |
| 2025-12-02 15:07:04 | Ellagawa (Kalu Ganga) | 9.56 | 🟢 Normal | -0.057 |  |
| 2025-12-02 14:13:18 | Galgamuwa (Mee Oya) | 2.95 | 🟢 Normal | -0.074 |  |
| 2025-12-02 15:00:15 | Horowpothana (Yan Oya) | 4.03 | 🟢 Normal | -0.094 |  |
| 2025-12-02 15:02:24 | Rathnapura (Kalu Ganga) | 3.33 | 🟢 Normal | -0.103 |  |
| 2025-12-02 15:03:26 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -55.268 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)