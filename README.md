# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--02_04:41:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **7,137 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-02 04:41:06 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | -0.006 |  |
| 2025-12-02 04:12:46 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.018 |  |
| 2025-12-02 04:11:57 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | -0.019 |  |
| 2025-12-02 04:10:04 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.069 |  |
| 2025-12-02 04:09:20 | Ellagawa (Kalu Ganga) | 10.26 | 🟡 Alert | -0.036 |  |
| 2025-12-02 04:08:55 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-02 04:08:52 | Rathnapura (Kalu Ganga) | 4.29 | 🟢 Normal | -0.065 |  |
| 2025-12-02 04:08:10 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-02 04:07:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.50 | 🟠 Minor Flood | -0.059 |  |
| 2025-12-02 04:07:06 | Putupaula (Kalu Ganga) | 4.00 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-02 04:06:32 | Hanwella (Kelani Ganga) | 7.87 | 🟡 Alert | -0.060 |  |
| 2025-12-02 04:05:42 | Nagalagam Street (Kelani Ganga) | 2.36 | 🔴 Major Flood | -0.045 |  |
| 2025-12-02 04:05:12 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -144.000 |  |
| 2025-12-02 04:05:11 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -144.000 |  |
| 2025-12-02 04:04:55 | Moraketiya (Walawe Ganga) | 1.54 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2025-12-02 04:04:10 | Glencourse (Kelani Ganga) | 11.66 | 🟢 Normal | -0.051 |  |
| 2025-12-02 04:04:00 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-02 04:03:35 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-02 04:03:11 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-02 04:03:07 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-02 04:02:29 | Dunamale (Aththanagalu Oya) | 3.05 | 🟢 Normal | -0.049 |  |
| 2025-12-02 04:02:13 | Nakkala (Kumbukkan Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-02 04:02:10 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | -0.011 |  |
| 2025-12-02 04:01:53 | Thalgahagoda (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2025-12-02 04:01:31 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2025-12-02 04:01:30 | Thanthirimale (Malwathu Oya) | 8.91 | 🔴 Major Flood | -0.040 |  |
| 2025-12-02 04:01:30 | Giriulla (Maha Oya) | 2.65 | 🟢 Normal | -0.006 |  |
| 2025-12-02 04:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.012 |  |
| 2025-12-02 04:00:42 | Badalgama (Maha Oya) | 3.74 | 🟢 Normal | -0.034 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-02 04:01:30 | Thanthirimale (Malwathu Oya) | 8.91 | 🔴 Major Flood | -0.040 |  |
| 2025-12-02 04:05:42 | Nagalagam Street (Kelani Ganga) | 2.36 | 🔴 Major Flood | -0.045 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-02 04:07:06 | Putupaula (Kalu Ganga) | 4.00 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-02 04:07:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.50 | 🟠 Minor Flood | -0.059 |  |
| 2025-12-02 04:09:20 | Ellagawa (Kalu Ganga) | 10.26 | 🟡 Alert | -0.036 |  |
| 2025-12-02 04:06:32 | Hanwella (Kelani Ganga) | 7.87 | 🟡 Alert | -0.060 |  |
| 2025-12-02 04:04:55 | Moraketiya (Walawe Ganga) | 1.54 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2025-12-02 04:04:00 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-02 00:02:18 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | 0.003 |  |
| 2025-12-02 03:23:04 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-02 04:03:07 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-02 04:03:35 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-02 01:26:07 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-02 04:08:10 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-02 04:08:55 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-02 04:41:06 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | -0.006 |  |
| 2025-12-02 04:01:30 | Giriulla (Maha Oya) | 2.65 | 🟢 Normal | -0.006 |  |
| 2025-12-02 04:03:11 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-02 04:02:13 | Nakkala (Kumbukkan Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-02 04:02:10 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | -0.011 |  |
| 2025-12-02 00:01:36 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | -0.011 |  |
| 2025-12-02 04:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.012 |  |
| 2025-12-02 04:12:46 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.018 |  |
| 2025-12-02 04:11:57 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | -0.019 |  |
| 2025-12-02 04:01:53 | Thalgahagoda (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2025-12-02 04:01:31 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2025-12-01 18:00:59 | Galgamuwa (Mee Oya) | 3.58 | 🟢 Normal | -0.021 |  |
| 2025-12-02 04:00:42 | Badalgama (Maha Oya) | 3.74 | 🟢 Normal | -0.034 |  |
| 2025-12-02 04:02:29 | Dunamale (Aththanagalu Oya) | 3.05 | 🟢 Normal | -0.049 |  |
| 2025-12-02 04:04:10 | Glencourse (Kelani Ganga) | 11.66 | 🟢 Normal | -0.051 |  |
| 2025-12-02 04:08:52 | Rathnapura (Kalu Ganga) | 4.29 | 🟢 Normal | -0.065 |  |
| 2025-12-02 04:10:04 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.069 |  |
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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)