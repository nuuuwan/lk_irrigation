# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--02_11:22:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **7,389 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-02 11:22:30 | Galgamuwa (Mee Oya) | 3.12 | 🟢 Normal | -0.047 |  |
| 2025-12-02 11:16:05 | Rathnapura (Kalu Ganga) | 3.69 | 🟢 Normal | -0.072 |  |
| 2025-12-02 11:15:24 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-02 11:10:01 | Giriulla (Maha Oya) | 2.52 | 🟢 Normal | -0.018 |  |
| 2025-12-02 11:09:53 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2025-12-02 11:09:40 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.010 |  |
| 2025-12-02 11:07:23 | Horowpothana (Yan Oya) | 4.46 | 🟢 Normal | -0.055 |  |
| 2025-12-02 11:07:08 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2025-12-02 11:06:18 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2025-12-02 11:05:53 | Dunamale (Aththanagalu Oya) | 2.78 | 🟢 Normal | -0.019 |  |
| 2025-12-02 11:04:58 | Putupaula (Kalu Ganga) | 3.81 | 🟡 Alert | -0.029 |  |
| 2025-12-02 11:04:42 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2025-12-02 11:04:39 | Hanwella (Kelani Ganga) | 7.36 | 🟡 Alert | -0.072 |  |
| 2025-12-02 11:04:30 | Badalgama (Maha Oya) | 3.60 | 🟢 Normal | -0.010 |  |
| 2025-12-02 11:04:19 | Glencourse (Kelani Ganga) | 11.39 | 🟢 Normal | -0.022 |  |
| 2025-12-02 11:04:10 | Nagalagam Street (Kelani Ganga) | 2.19 | 🔴 Major Flood | 0.000 |  |
| 2025-12-02 11:04:05 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2025-12-02 11:03:29 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-02 11:03:26 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-02 11:03:21 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-02 11:03:20 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | -0.011 |  |
| 2025-12-02 11:03:14 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | -0.062 |  |
| 2025-12-02 11:03:11 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-02 11:03:06 | Ellagawa (Kalu Ganga) | 9.83 | 🟢 Normal | -0.069 |  |
| 2025-12-02 11:03:06 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2025-12-02 11:02:50 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal | -0.011 |  |
| 2025-12-02 11:02:45 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-02 11:02:34 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-02 11:02:12 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | -0.020 |  |
| 2025-12-02 11:02:11 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-02 11:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.10 | 🟡 Alert | -0.050 |  |
| 2025-12-02 11:01:40 | Thanthirimale (Malwathu Oya) | 8.43 | 🔴 Major Flood | -0.093 |  |
| 2025-12-02 11:00:10 | Nakkala (Kumbukkan Oya) | 1.54 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-02 11:04:10 | Nagalagam Street (Kelani Ganga) | 2.19 | 🔴 Major Flood | 0.000 |  |
| 2025-12-02 11:01:40 | Thanthirimale (Malwathu Oya) | 8.43 | 🔴 Major Flood | -0.093 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-02 11:04:58 | Putupaula (Kalu Ganga) | 3.81 | 🟡 Alert | -0.029 |  |
| 2025-12-02 11:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.10 | 🟡 Alert | -0.050 |  |
| 2025-12-02 11:04:39 | Hanwella (Kelani Ganga) | 7.36 | 🟡 Alert | -0.072 |  |
| 2025-12-02 11:04:42 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2025-12-02 11:02:45 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-02 11:02:11 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-02 11:03:29 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-02 11:02:34 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-02 11:15:24 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-02 11:09:53 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2025-12-02 11:06:18 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2025-12-02 11:04:05 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2025-12-02 11:07:08 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2025-12-02 11:03:06 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2025-12-02 11:03:11 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-02 11:03:26 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-02 11:00:10 | Nakkala (Kumbukkan Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-02 11:04:30 | Badalgama (Maha Oya) | 3.60 | 🟢 Normal | -0.010 |  |
| 2025-12-02 11:03:21 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-02 11:09:40 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.010 |  |
| 2025-12-02 11:03:20 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | -0.011 |  |
| 2025-12-02 11:02:50 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal | -0.011 |  |
| 2025-12-02 10:06:19 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | -0.011 |  |
| 2025-12-02 11:10:01 | Giriulla (Maha Oya) | 2.52 | 🟢 Normal | -0.018 |  |
| 2025-12-02 11:05:53 | Dunamale (Aththanagalu Oya) | 2.78 | 🟢 Normal | -0.019 |  |
| 2025-12-02 11:02:12 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | -0.020 |  |
| 2025-12-02 11:04:19 | Glencourse (Kelani Ganga) | 11.39 | 🟢 Normal | -0.022 |  |
| 2025-12-02 11:22:30 | Galgamuwa (Mee Oya) | 3.12 | 🟢 Normal | -0.047 |  |
| 2025-12-02 11:07:23 | Horowpothana (Yan Oya) | 4.46 | 🟢 Normal | -0.055 |  |
| 2025-12-02 11:03:14 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | -0.062 |  |
| 2025-12-02 11:03:06 | Ellagawa (Kalu Ganga) | 9.83 | 🟢 Normal | -0.069 |  |
| 2025-12-02 11:16:05 | Rathnapura (Kalu Ganga) | 3.69 | 🟢 Normal | -0.072 |  |
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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)