# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--03_10:08:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,159 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-03 10:08:39 | Rathnapura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.036 |  |
| 2025-12-03 10:08:16 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:07:57 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-03 10:07:09 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2025-12-03 10:07:06 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.023 |  |
| 2025-12-03 10:07:04 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2025-12-03 10:05:52 | Horowpothana (Yan Oya) | 2.90 | 🟢 Normal | -0.052 |  |
| 2025-12-03 10:05:49 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.061 |  |
| 2025-12-03 10:05:17 | Galgamuwa (Mee Oya) | 1.93 | 🟢 Normal | -0.037 |  |
| 2025-12-03 10:04:09 | Putupaula (Kalu Ganga) | 2.94 | 🟢 Normal | -0.039 |  |
| 2025-12-03 10:03:38 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-03 10:03:17 | Hanwella (Kelani Ganga) | 5.44 | 🟢 Normal | -0.072 |  |
| 2025-12-03 10:03:17 | Glencourse (Kelani Ganga) | 11.01 | 🟢 Normal | -0.010 |  |
| 2025-12-03 10:03:13 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:03:03 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:02:48 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:02:33 | Ellagawa (Kalu Ganga) | 7.60 | 🟢 Normal | -0.059 |  |
| 2025-12-03 10:02:26 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-03 10:02:23 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-03 10:02:18 | Katharagama (Menik Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:02:10 | Nagalagam Street (Kelani Ganga) | 1.42 | 🟡 Alert | -0.015 |  |
| 2025-12-03 10:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.66 | 🟢 Normal | -0.071 |  |
| 2025-12-03 10:02:06 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:01:51 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:01:47 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:01:35 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:01:30 | Badalgama (Maha Oya) | 3.30 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:01:29 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:01:14 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:01:08 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-03 10:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:00:37 | Thanthirimale (Malwathu Oya) | 7.35 | 🟠 Minor Flood | -0.052 |  |
| 2025-12-03 10:00:10 | Nakkala (Kumbukkan Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2025-12-03 09:15:48 | Panadugama (Nilwala Ganga) | 3.02 | 🟢 Normal | -0.023 |  |
| 2025-12-03 09:12:55 | Manampitiya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.005 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-03 10:00:37 | Thanthirimale (Malwathu Oya) | 7.35 | 🟠 Minor Flood | -0.052 |  |
| 2025-12-03 10:02:10 | Nagalagam Street (Kelani Ganga) | 1.42 | 🟡 Alert | -0.015 |  |
| 2025-12-03 10:02:23 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-03 10:07:57 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-03 09:05:38 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-03 10:02:26 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-03 10:02:48 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:03:03 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:02:06 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:01:51 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:01:35 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:03:13 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:02:18 | Katharagama (Menik Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:01:30 | Badalgama (Maha Oya) | 3.30 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:01:47 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:08:16 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-03 10:01:29 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:12:55 | Manampitiya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.005 |  |
| 2025-12-03 09:04:56 | Giriulla (Maha Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2025-12-03 10:07:09 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2025-12-03 10:03:38 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-03 10:00:10 | Nakkala (Kumbukkan Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2025-12-03 09:01:10 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-03 10:07:04 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2025-12-03 10:03:17 | Glencourse (Kelani Ganga) | 11.01 | 🟢 Normal | -0.010 |  |
| 2025-12-03 10:01:08 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-03 10:07:06 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.023 |  |
| 2025-12-03 10:08:39 | Rathnapura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.036 |  |
| 2025-12-03 10:05:17 | Galgamuwa (Mee Oya) | 1.93 | 🟢 Normal | -0.037 |  |
| 2025-12-03 10:04:09 | Putupaula (Kalu Ganga) | 2.94 | 🟢 Normal | -0.039 |  |
| 2025-12-03 10:05:52 | Horowpothana (Yan Oya) | 2.90 | 🟢 Normal | -0.052 |  |
| 2025-12-03 10:02:33 | Ellagawa (Kalu Ganga) | 7.60 | 🟢 Normal | -0.059 |  |
| 2025-12-03 10:05:49 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.061 |  |
| 2025-12-03 10:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.66 | 🟢 Normal | -0.071 |  |
| 2025-12-03 10:03:17 | Hanwella (Kelani Ganga) | 5.44 | 🟢 Normal | -0.072 |  |

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)