# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--02_13:20:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **7,461 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-02 13:20:19 | Manampitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2025-12-02 13:16:48 | Galgamuwa (Mee Oya) | 3.02 | 🟢 Normal | -0.055 |  |
| 2025-12-02 13:15:48 | Rathnapura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.080 |  |
| 2025-12-02 13:15:31 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:15:29 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | -8.041 |  |
| 2025-12-02 13:15:06 | Horowpothana (Yan Oya) | 3.02 | 🟢 Normal | -13.863 |  |
| 2025-12-02 13:15:00 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.008 |  |
| 2025-12-02 13:11:51 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:10:25 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:09:44 | Horowpothana (Yan Oya) | 4.26 | 🟢 Normal | -13.863 |  |
| 2025-12-02 13:09:30 | Dunamale (Aththanagalu Oya) | 2.74 | 🟢 Normal | -0.020 |  |
| 2025-12-02 13:09:21 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:07:28 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:07:21 | Badalgama (Maha Oya) | 3.58 | 🟢 Normal | -8.041 |  |
| 2025-12-02 13:06:31 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:05:56 | Hanwella (Kelani Ganga) | 7.22 | 🟡 Alert | -0.069 |  |
| 2025-12-02 13:05:16 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:05:10 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | -0.020 |  |
| 2025-12-02 13:04:22 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:04:00 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-02 13:03:57 | Putupaula (Kalu Ganga) | 3.75 | 🟡 Alert | -0.030 |  |
| 2025-12-02 13:03:55 | Ellagawa (Kalu Ganga) | 9.69 | 🟢 Normal | -0.080 |  |
| 2025-12-02 13:03:49 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:03:45 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-02 13:03:01 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2025-12-02 13:03:01 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.97 | 🟡 Alert | -0.070 |  |
| 2025-12-02 13:02:55 | Moraketiya (Walawe Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:02:47 | Nagalagam Street (Kelani Ganga) | 2.13 | 🔴 Major Flood | -0.031 |  |
| 2025-12-02 13:02:41 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-02 13:02:33 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:02:16 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | -0.062 |  |
| 2025-12-02 13:02:14 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:01:39 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:01:23 | Siyambalanduwa (Heda Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-02 13:01:16 | Thanthirimale (Malwathu Oya) | 8.32 | 🔴 Major Flood | -0.041 |  |
| 2025-12-02 13:00:52 | Nakkala (Kumbukkan Oya) | 1.53 | 🟢 Normal | 0.988 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-02 13:02:47 | Nagalagam Street (Kelani Ganga) | 2.13 | 🔴 Major Flood | -0.031 |  |
| 2025-12-02 13:01:16 | Thanthirimale (Malwathu Oya) | 8.32 | 🔴 Major Flood | -0.041 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-02 13:03:57 | Putupaula (Kalu Ganga) | 3.75 | 🟡 Alert | -0.030 |  |
| 2025-12-02 13:05:56 | Hanwella (Kelani Ganga) | 7.22 | 🟡 Alert | -0.069 |  |
| 2025-12-02 13:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.97 | 🟡 Alert | -0.070 |  |
| 2025-12-02 13:00:52 | Nakkala (Kumbukkan Oya) | 1.53 | 🟢 Normal | 0.988 | 🔺 Rising |
| 2025-12-02 13:03:45 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-02 13:20:19 | Manampitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2025-12-02 13:01:39 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:02:14 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:11:51 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:04:22 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:03:01 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:03:49 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:15:31 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:02:55 | Moraketiya (Walawe Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:05:16 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:02:33 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:06:31 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:09:21 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:15:00 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.008 |  |
| 2025-12-02 12:21:52 | Giriulla (Maha Oya) | 2.51 | 🟢 Normal | -0.008 |  |
| 2025-12-02 13:03:01 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2025-12-02 13:02:41 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-02 13:04:00 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-02 13:01:23 | Siyambalanduwa (Heda Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-02 10:06:19 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | -0.011 |  |
| 2025-12-02 13:09:30 | Dunamale (Aththanagalu Oya) | 2.74 | 🟢 Normal | -0.020 |  |
| 2025-12-02 13:05:10 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | -0.020 |  |
| 2025-12-02 13:16:48 | Galgamuwa (Mee Oya) | 3.02 | 🟢 Normal | -0.055 |  |
| 2025-12-02 13:02:16 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | -0.062 |  |
| 2025-12-02 13:03:55 | Ellagawa (Kalu Ganga) | 9.69 | 🟢 Normal | -0.080 |  |
| 2025-12-02 13:15:48 | Rathnapura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.080 |  |
| 2025-12-02 13:15:29 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | -8.041 |  |
| 2025-12-02 13:15:06 | Horowpothana (Yan Oya) | 3.02 | 🟢 Normal | -13.863 |  |

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)