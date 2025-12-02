# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--02_08:01:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **7,256 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-02 08:01:39 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 08:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.020 |  |
| 2025-12-02 08:01:30 | Siyambalanduwa (Heda Oya) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-02 08:01:00 | Horowpothana (Yan Oya) | 4.81 | 🟢 Normal | -0.204 |  |
| 2025-12-02 08:00:18 | Nakkala (Kumbukkan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-02 08:00:14 | Nakkala (Kumbukkan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-02 08:00:11 | Nakkala (Kumbukkan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-02 07:49:15 | Galgamuwa (Mee Oya) | 3.23 | 🟢 Normal | -0.010 |  |
| 2025-12-02 07:43:07 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.030 |  |
| 2025-12-02 07:41:13 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.006 |  |
| 2025-12-02 07:25:42 | Horowpothana (Yan Oya) | 4.93 | 🟢 Normal | -0.204 |  |
| 2025-12-02 07:25:41 | Horowpothana (Yan Oya) | 5.02 | 🟢 Normal | -0.204 |  |
| 2025-12-02 07:25:39 | Horowpothana (Yan Oya) | 5.12 | 🟢 Normal | -0.204 |  |
| 2025-12-02 07:25:38 | Horowpothana (Yan Oya) | 5.23 | 🟢 Normal | -0.204 |  |
| 2025-12-02 07:25:37 | Horowpothana (Yan Oya) | 5.35 | 🟢 Normal | -0.204 |  |
| 2025-12-02 07:25:35 | Horowpothana (Yan Oya) | 5.49 | 🟢 Normal | -0.204 |  |
| 2025-12-02 07:25:34 | Horowpothana (Yan Oya) | 5.67 | 🟢 Normal | -0.204 |  |
| 2025-12-02 07:21:24 | Panadugama (Nilwala Ganga) | 3.12 | 🟢 Normal | 0.000 |  |
| 2025-12-02 07:20:42 | Rathnapura (Kalu Ganga) | 4.05 | 🟢 Normal | -0.070 |  |
| 2025-12-02 07:17:18 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | -36.000 |  |
| 2025-12-02 07:17:16 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | -36.000 |  |
| 2025-12-02 07:11:14 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2025-12-02 07:11:12 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2025-12-02 07:09:21 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-02 07:08:55 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2025-12-02 07:07:58 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-02 07:07:50 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | -0.019 |  |
| 2025-12-02 07:07:35 | Hanwella (Kelani Ganga) | 7.64 | 🟡 Alert | -0.092 |  |
| 2025-12-02 07:06:44 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 07:06:21 | Glencourse (Kelani Ganga) | 11.52 | 🟢 Normal | -0.041 |  |
| 2025-12-02 07:05:10 | Ellagawa (Kalu Ganga) | 10.10 | 🟡 Alert | -0.067 |  |
| 2025-12-02 07:05:08 | Nagalagam Street (Kelani Ganga) | 2.26 | 🔴 Major Flood | -0.032 |  |
| 2025-12-02 07:04:02 | Giriulla (Maha Oya) | 2.58 | 🟢 Normal | -0.033 |  |
| 2025-12-02 07:03:55 | Badalgama (Maha Oya) | 3.66 | 🟢 Normal | -0.022 |  |
| 2025-12-02 07:03:53 | Katharagama (Menik Ganga) | 0.76 | 🟢 Normal | -0.141 |  |
| 2025-12-02 07:03:45 | Dunamale (Aththanagalu Oya) | 2.90 | 🟢 Normal | -0.051 |  |
| 2025-12-02 07:03:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.31 | 🟡 Alert | -0.092 |  |
| 2025-12-02 07:03:39 | Putupaula (Kalu Ganga) | 3.93 | 🟡 Alert | -0.029 |  |
| 2025-12-02 07:02:46 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-02 07:02:42 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-02 07:02:21 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | 0.060 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-02 07:05:08 | Nagalagam Street (Kelani Ganga) | 2.26 | 🔴 Major Flood | -0.032 |  |
| 2025-12-02 07:01:26 | Thanthirimale (Malwathu Oya) | 8.78 | 🔴 Major Flood | -0.071 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-02 07:03:39 | Putupaula (Kalu Ganga) | 3.93 | 🟡 Alert | -0.029 |  |
| 2025-12-02 07:05:10 | Ellagawa (Kalu Ganga) | 10.10 | 🟡 Alert | -0.067 |  |
| 2025-12-02 07:03:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.31 | 🟡 Alert | -0.092 |  |
| 2025-12-02 07:07:35 | Hanwella (Kelani Ganga) | 7.64 | 🟡 Alert | -0.092 |  |
| 2025-12-02 07:02:21 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-02 07:02:42 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-02 08:01:30 | Siyambalanduwa (Heda Oya) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-02 07:01:26 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-02 08:00:18 | Nakkala (Kumbukkan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-02 07:11:14 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2025-12-02 08:01:39 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 07:21:24 | Panadugama (Nilwala Ganga) | 3.12 | 🟢 Normal | 0.000 |  |
| 2025-12-02 07:09:21 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-02 07:07:58 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:13:45 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-02 06:08:05 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.005 |  |
| 2025-12-02 07:41:13 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.006 |  |
| 2025-12-02 07:01:37 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-02 07:02:46 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-02 07:49:15 | Galgamuwa (Mee Oya) | 3.23 | 🟢 Normal | -0.010 |  |
| 2025-12-02 07:01:38 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.011 |  |
| 2025-12-02 07:07:50 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | -0.019 |  |
| 2025-12-02 08:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.020 |  |
| 2025-12-02 07:03:55 | Badalgama (Maha Oya) | 3.66 | 🟢 Normal | -0.022 |  |
| 2025-12-02 07:43:07 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.030 |  |
| 2025-12-02 07:04:02 | Giriulla (Maha Oya) | 2.58 | 🟢 Normal | -0.033 |  |
| 2025-12-02 07:06:21 | Glencourse (Kelani Ganga) | 11.52 | 🟢 Normal | -0.041 |  |
| 2025-12-02 07:03:45 | Dunamale (Aththanagalu Oya) | 2.90 | 🟢 Normal | -0.051 |  |
| 2025-12-02 07:20:42 | Rathnapura (Kalu Ganga) | 4.05 | 🟢 Normal | -0.070 |  |
| 2025-12-01 14:07:27 | Manampitiya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.135 |  |
| 2025-12-02 07:03:53 | Katharagama (Menik Ganga) | 0.76 | 🟢 Normal | -0.141 |  |
| 2025-12-02 08:01:00 | Horowpothana (Yan Oya) | 4.81 | 🟢 Normal | -0.204 |  |
| 2025-12-02 07:17:18 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | -36.000 |  |

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)