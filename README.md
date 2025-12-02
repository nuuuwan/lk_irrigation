# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--02_06:13:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **7,201 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-02 06:13:45 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:13:43 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:13:40 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:13:39 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:13:37 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:13:32 | Kuda Oya (Kirindi Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:10:51 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2025-12-02 06:10:00 | Giriulla (Maha Oya) | 2.61 | 🟢 Normal | -96.000 |  |
| 2025-12-02 06:09:52 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:09:42 | Nawalapitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.037 |  |
| 2025-12-02 06:09:10 | Panadugama (Nilwala Ganga) | 3.12 | 🟢 Normal | -0.011 |  |
| 2025-12-02 06:08:57 | Hanwella (Kelani Ganga) | 7.73 | 🟡 Alert | -0.068 |  |
| 2025-12-02 06:08:45 | Giriulla (Maha Oya) | 4.61 | 🟢 Normal | -96.000 |  |
| 2025-12-02 06:08:39 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.052 |  |
| 2025-12-02 06:08:22 | Badalgama (Maha Oya) | 3.68 | 🟢 Normal | -0.027 |  |
| 2025-12-02 06:08:05 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.005 |  |
| 2025-12-02 06:07:55 | Glencourse (Kelani Ganga) | 11.56 | 🟢 Normal | -0.038 |  |
| 2025-12-02 06:07:35 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:07:30 | Nagalagam Street (Kelani Ganga) | 2.29 | 🔴 Major Flood | -0.030 |  |
| 2025-12-02 06:06:13 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:05:24 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:04:53 | Dunamale (Aththanagalu Oya) | 2.95 | 🟢 Normal | -0.046 |  |
| 2025-12-02 06:04:49 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:04:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.40 | 🟡 Alert | -0.042 |  |
| 2025-12-02 06:04:25 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:04:04 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-02 06:03:09 | Rathnapura (Kalu Ganga) | 4.14 | 🟢 Normal | -0.068 |  |
| 2025-12-02 06:03:02 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.023 |  |
| 2025-12-02 06:02:45 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | -7.579 |  |
| 2025-12-02 06:02:40 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2025-12-02 06:02:38 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-02 06:02:26 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -7.579 |  |
| 2025-12-02 06:02:18 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.034 |  |
| 2025-12-02 06:02:14 | Ellagawa (Kalu Ganga) | 10.17 | 🟡 Alert | -0.041 |  |
| 2025-12-02 06:02:07 | Nakkala (Kumbukkan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:02:03 | Thanthirimale (Malwathu Oya) | 8.85 | 🔴 Major Flood | -0.040 |  |
| 2025-12-02 06:01:46 | Putupaula (Kalu Ganga) | 3.96 | 🟡 Alert | -0.020 |  |
| 2025-12-02 06:00:18 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:00:17 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:00:15 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-02 06:07:30 | Nagalagam Street (Kelani Ganga) | 2.29 | 🔴 Major Flood | -0.030 |  |
| 2025-12-02 06:02:03 | Thanthirimale (Malwathu Oya) | 8.85 | 🔴 Major Flood | -0.040 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-02 06:01:46 | Putupaula (Kalu Ganga) | 3.96 | 🟡 Alert | -0.020 |  |
| 2025-12-02 06:02:14 | Ellagawa (Kalu Ganga) | 10.17 | 🟡 Alert | -0.041 |  |
| 2025-12-02 06:04:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.40 | 🟡 Alert | -0.042 |  |
| 2025-12-02 06:08:57 | Hanwella (Kelani Ganga) | 7.73 | 🟡 Alert | -0.068 |  |
| 2025-12-02 06:02:40 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2025-12-02 06:10:51 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2025-12-02 06:02:38 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-02 06:00:18 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:02:07 | Nakkala (Kumbukkan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:05:24 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:06:13 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:09:52 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-02 01:26:07 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:04:25 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:07:35 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:13:45 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:08:05 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.005 |  |
| 2025-12-02 06:04:04 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-02 00:01:36 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | -0.011 |  |
| 2025-12-02 06:09:10 | Panadugama (Nilwala Ganga) | 3.12 | 🟢 Normal | -0.011 |  |
| 2025-12-01 18:00:59 | Galgamuwa (Mee Oya) | 3.58 | 🟢 Normal | -0.021 |  |
| 2025-12-02 06:03:02 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.023 |  |
| 2025-12-02 06:08:22 | Badalgama (Maha Oya) | 3.68 | 🟢 Normal | -0.027 |  |
| 2025-12-02 06:02:18 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.034 |  |
| 2025-12-02 06:09:42 | Nawalapitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.037 |  |
| 2025-12-02 06:07:55 | Glencourse (Kelani Ganga) | 11.56 | 🟢 Normal | -0.038 |  |
| 2025-12-02 06:04:53 | Dunamale (Aththanagalu Oya) | 2.95 | 🟢 Normal | -0.046 |  |
| 2025-12-02 06:08:39 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.052 |  |
| 2025-12-02 06:03:09 | Rathnapura (Kalu Ganga) | 4.14 | 🟢 Normal | -0.068 |  |
| 2025-12-01 14:07:27 | Manampitiya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.135 |  |
| 2025-12-02 00:00:49 | Horowpothana (Yan Oya) | 5.84 | 🟢 Normal | -0.144 |  |
| 2025-12-02 06:02:45 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | -7.579 |  |
| 2025-12-02 06:10:00 | Giriulla (Maha Oya) | 2.61 | 🟢 Normal | -96.000 |  |

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

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)