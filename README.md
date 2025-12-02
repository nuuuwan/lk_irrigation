# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--02_09:07:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **7,309 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-02 09:07:18 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.009 |  |
| 2025-12-02 09:06:13 | Hanwella (Kelani Ganga) | 7.50 | 🟡 Alert | -0.077 |  |
| 2025-12-02 09:05:44 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-02 09:05:15 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.035 |  |
| 2025-12-02 09:05:00 | Katharagama (Menik Ganga) | 0.56 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-02 09:04:02 | Nagalagam Street (Kelani Ganga) | 2.23 | 🔴 Major Flood | -0.015 |  |
| 2025-12-02 09:04:01 | Putupaula (Kalu Ganga) | 3.86 | 🟡 Alert | -0.030 |  |
| 2025-12-02 09:03:45 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-02 09:03:30 | Dunamale (Aththanagalu Oya) | 2.84 | 🟢 Normal | -0.030 |  |
| 2025-12-02 09:03:28 | Rathnapura (Kalu Ganga) | 3.89 | 🟢 Normal | -0.080 |  |
| 2025-12-02 09:03:19 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.059 |  |
| 2025-12-02 09:03:04 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.011 |  |
| 2025-12-02 09:02:52 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | -0.022 |  |
| 2025-12-02 09:02:42 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-02 09:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.20 | 🟡 Alert | -0.061 |  |
| 2025-12-02 09:02:21 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | -0.020 |  |
| 2025-12-02 09:02:05 | Nakkala (Kumbukkan Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-02 09:02:05 | Siyambalanduwa (Heda Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-02 09:02:00 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2025-12-02 09:01:55 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-02 09:01:55 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 09:01:50 | Thanthirimale (Malwathu Oya) | 8.64 | 🔴 Major Flood | -0.090 |  |
| 2025-12-02 09:01:34 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-02 09:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2025-12-02 09:00:47 | Horowpothana (Yan Oya) | 4.81 | 🟢 Normal | 0.000 |  |
| 2025-12-02 08:13:09 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.035 |  |
| 2025-12-02 08:11:21 | Galgamuwa (Mee Oya) | 3.22 | 🟢 Normal | -0.027 |  |
| 2025-12-02 08:11:20 | Ellagawa (Kalu Ganga) | 10.05 | 🟡 Alert | -0.045 |  |
| 2025-12-02 08:09:31 | Badalgama (Maha Oya) | 3.64 | 🟢 Normal | -0.018 |  |
| 2025-12-02 08:09:20 | Holombuwa (Kelani Ganga) | 1.29 | 🟢 Normal | 0.009 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-02 09:04:02 | Nagalagam Street (Kelani Ganga) | 2.23 | 🔴 Major Flood | -0.015 |  |
| 2025-12-02 09:01:50 | Thanthirimale (Malwathu Oya) | 8.64 | 🔴 Major Flood | -0.090 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-02 09:04:01 | Putupaula (Kalu Ganga) | 3.86 | 🟡 Alert | -0.030 |  |
| 2025-12-02 08:11:20 | Ellagawa (Kalu Ganga) | 10.05 | 🟡 Alert | -0.045 |  |
| 2025-12-02 09:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.20 | 🟡 Alert | -0.061 |  |
| 2025-12-02 09:06:13 | Hanwella (Kelani Ganga) | 7.50 | 🟡 Alert | -0.077 |  |
| 2025-12-02 09:05:00 | Katharagama (Menik Ganga) | 0.56 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-02 08:09:20 | Holombuwa (Kelani Ganga) | 1.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-02 09:02:42 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-02 08:05:50 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-02 09:00:47 | Horowpothana (Yan Oya) | 4.81 | 🟢 Normal | 0.000 |  |
| 2025-12-02 09:01:55 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 08:03:01 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-02 09:01:34 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-02 09:02:05 | Siyambalanduwa (Heda Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-02 09:01:55 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:13:45 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-02 09:07:18 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.009 |  |
| 2025-12-02 09:02:05 | Nakkala (Kumbukkan Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-02 09:03:45 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-02 09:05:44 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-02 09:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2025-12-02 09:02:00 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2025-12-02 09:03:04 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.011 |  |
| 2025-12-02 08:07:24 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | -0.013 |  |
| 2025-12-02 08:09:31 | Badalgama (Maha Oya) | 3.64 | 🟢 Normal | -0.018 |  |
| 2025-12-02 09:02:21 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | -0.020 |  |
| 2025-12-02 08:02:38 | Giriulla (Maha Oya) | 2.56 | 🟢 Normal | -0.020 |  |
| 2025-12-02 09:02:52 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | -0.022 |  |
| 2025-12-02 08:11:21 | Galgamuwa (Mee Oya) | 3.22 | 🟢 Normal | -0.027 |  |
| 2025-12-02 09:03:30 | Dunamale (Aththanagalu Oya) | 2.84 | 🟢 Normal | -0.030 |  |
| 2025-12-02 09:05:15 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.035 |  |
| 2025-12-02 09:03:19 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.059 |  |
| 2025-12-02 09:03:28 | Rathnapura (Kalu Ganga) | 3.89 | 🟢 Normal | -0.080 |  |
| 2025-12-01 14:07:27 | Manampitiya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.135 |  |

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)