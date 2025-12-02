# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--02_12:11:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **7,422 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-02 12:11:12 | Galgamuwa (Mee Oya) | 3.08 | 🟢 Normal | -0.049 |  |
| 2025-12-02 12:09:24 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.010 |  |
| 2025-12-02 12:08:56 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | -0.010 |  |
| 2025-12-02 12:08:54 | Badalgama (Maha Oya) | 3.69 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-02 12:08:42 | Rathnapura (Kalu Ganga) | 3.59 | 🟢 Normal | -0.114 |  |
| 2025-12-02 12:08:42 | Dunamale (Aththanagalu Oya) | 2.76 | 🟢 Normal | -0.019 |  |
| 2025-12-02 12:08:24 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-02 12:07:09 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.009 |  |
| 2025-12-02 12:06:11 | Glencourse (Kelani Ganga) | 11.37 | 🟢 Normal | -0.019 |  |
| 2025-12-02 12:05:58 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2025-12-02 12:05:38 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-02 12:05:19 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-02 12:04:56 | Hanwella (Kelani Ganga) | 7.29 | 🟡 Alert | -0.070 |  |
| 2025-12-02 12:04:40 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-02 12:04:09 | Ellagawa (Kalu Ganga) | 9.77 | 🟢 Normal | -0.059 |  |
| 2025-12-02 12:04:08 | Nagalagam Street (Kelani Ganga) | 2.16 | 🔴 Major Flood | -0.030 |  |
| 2025-12-02 12:04:01 | Katharagama (Menik Ganga) | 0.42 | 🟢 Normal | -0.079 |  |
| 2025-12-02 12:03:48 | Putupaula (Kalu Ganga) | 3.78 | 🟡 Alert | -0.031 |  |
| 2025-12-02 12:03:47 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.203 |  |
| 2025-12-02 12:03:46 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.020 |  |
| 2025-12-02 12:03:45 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2025-12-02 12:03:24 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-02 12:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.04 | 🟡 Alert | -0.059 |  |
| 2025-12-02 12:02:59 | Thanthirimale (Malwathu Oya) | 8.36 | 🔴 Major Flood | -0.068 |  |
| 2025-12-02 12:02:51 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | -0.020 |  |
| 2025-12-02 12:02:41 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-02 12:02:40 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2025-12-02 12:02:28 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-02 12:02:25 | Horowpothana (Yan Oya) | 4.34 | 🟢 Normal | -0.131 |  |
| 2025-12-02 12:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2025-12-02 12:01:51 | Moraketiya (Walawe Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2025-12-02 12:01:44 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-02 12:00:10 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | -1.010 |  |
| 2025-12-02 11:22:30 | Galgamuwa (Mee Oya) | 3.12 | 🟢 Normal | -0.049 |  |
| 2025-12-02 11:16:05 | Rathnapura (Kalu Ganga) | 3.69 | 🟢 Normal | -0.114 |  |
| 2025-12-02 11:15:24 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-02 12:04:08 | Nagalagam Street (Kelani Ganga) | 2.16 | 🔴 Major Flood | -0.030 |  |
| 2025-12-02 12:02:59 | Thanthirimale (Malwathu Oya) | 8.36 | 🔴 Major Flood | -0.068 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-02 12:03:48 | Putupaula (Kalu Ganga) | 3.78 | 🟡 Alert | -0.031 |  |
| 2025-12-02 12:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.04 | 🟡 Alert | -0.059 |  |
| 2025-12-02 12:04:56 | Hanwella (Kelani Ganga) | 7.29 | 🟡 Alert | -0.070 |  |
| 2025-12-02 12:08:54 | Badalgama (Maha Oya) | 3.69 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-02 12:02:28 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-02 12:02:41 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-02 12:05:38 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-02 12:03:24 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-02 12:08:24 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-02 12:05:58 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2025-12-02 12:07:09 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.009 |  |
| 2025-12-02 12:09:24 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.010 |  |
| 2025-12-02 12:02:40 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2025-12-02 12:08:56 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | -0.010 |  |
| 2025-12-02 12:01:51 | Moraketiya (Walawe Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2025-12-02 12:01:44 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-02 12:04:40 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-02 12:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2025-12-02 10:06:19 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | -0.011 |  |
| 2025-12-02 11:10:01 | Giriulla (Maha Oya) | 2.52 | 🟢 Normal | -0.018 |  |
| 2025-12-02 12:08:42 | Dunamale (Aththanagalu Oya) | 2.76 | 🟢 Normal | -0.019 |  |
| 2025-12-02 12:06:11 | Glencourse (Kelani Ganga) | 11.37 | 🟢 Normal | -0.019 |  |
| 2025-12-02 12:02:51 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | -0.020 |  |
| 2025-12-02 12:03:45 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2025-12-02 12:03:46 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.020 |  |
| 2025-12-02 12:11:12 | Galgamuwa (Mee Oya) | 3.08 | 🟢 Normal | -0.049 |  |
| 2025-12-02 12:04:09 | Ellagawa (Kalu Ganga) | 9.77 | 🟢 Normal | -0.059 |  |
| 2025-12-02 12:04:01 | Katharagama (Menik Ganga) | 0.42 | 🟢 Normal | -0.079 |  |
| 2025-12-02 12:08:42 | Rathnapura (Kalu Ganga) | 3.59 | 🟢 Normal | -0.114 |  |
| 2025-12-02 12:02:25 | Horowpothana (Yan Oya) | 4.34 | 🟢 Normal | -0.131 |  |
| 2025-12-01 14:07:27 | Manampitiya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.135 |  |
| 2025-12-02 12:03:47 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.203 |  |
| 2025-12-02 12:00:10 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | -1.010 |  |

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)