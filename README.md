# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--07_17:01:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **11,741 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-07 17:01:46 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-07 17:01:45 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-07 17:01:40 | Glencourse (Kelani Ganga) | 10.08 | 🟢 Normal | -0.032 |  |
| 2025-12-07 17:01:38 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-07 17:01:16 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | -0.030 |  |
| 2025-12-07 17:01:11 | Thanthirimale (Malwathu Oya) | 5.59 | 🟡 Alert | -0.071 |  |
| 2025-12-07 17:01:09 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.111 |  |
| 2025-12-07 17:00:13 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-07 16:43:03 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.012 |  |
| 2025-12-07 16:13:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | -0.079 |  |
| 2025-12-07 16:10:10 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-07 16:10:09 | Galgamuwa (Mee Oya) | 1.25 | 🟢 Normal | -0.036 |  |
| 2025-12-07 16:08:08 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-07 16:07:14 | Manampitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.111 |  |
| 2025-12-07 16:06:55 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.028 |  |
| 2025-12-07 16:06:52 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.038 |  |
| 2025-12-07 16:06:29 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-07 16:06:16 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-07 16:06:14 | Glencourse (Kelani Ganga) | 10.11 | 🟢 Normal | -0.032 |  |
| 2025-12-07 16:05:30 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2025-12-07 16:05:26 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.009 |  |
| 2025-12-07 16:05:20 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-07 16:04:20 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-07 16:04:10 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.307 | 🔺 Rising |
| 2025-12-07 16:04:02 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2025-12-07 16:03:51 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-07 16:03:46 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-07 16:03:37 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-07 16:03:27 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-07 16:03:19 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2025-12-07 16:03:16 | Hanwella (Kelani Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-07 16:02:44 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-07 17:01:11 | Thanthirimale (Malwathu Oya) | 5.59 | 🟡 Alert | -0.071 |  |
| 2025-12-07 16:04:10 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.307 | 🔺 Rising |
| 2025-12-07 16:05:30 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2025-12-07 16:03:19 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2025-12-07 16:08:08 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-07 16:04:20 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-07 16:10:10 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-07 17:01:46 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-07 16:01:41 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-07 17:01:45 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-07 16:00:10 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2025-12-07 17:01:38 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-07 16:03:16 | Hanwella (Kelani Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-07 16:03:27 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-07 16:02:09 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-07 16:06:16 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-07 16:06:29 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-07 16:02:44 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | 0.000 |  |
| 2025-12-07 16:03:37 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-07 16:05:26 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.009 |  |
| 2025-12-07 16:03:51 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-07 16:04:02 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2025-12-07 16:05:20 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-07 17:00:13 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-07 16:03:46 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-07 16:02:00 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2025-12-07 16:01:10 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | -0.011 |  |
| 2025-12-07 16:43:03 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.012 |  |
| 2025-12-07 16:01:34 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2025-12-07 16:01:13 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | -0.020 |  |
| 2025-12-07 16:06:55 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.028 |  |
| 2025-12-07 17:01:16 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | -0.030 |  |
| 2025-12-07 17:01:40 | Glencourse (Kelani Ganga) | 10.08 | 🟢 Normal | -0.032 |  |
| 2025-12-07 16:10:09 | Galgamuwa (Mee Oya) | 1.25 | 🟢 Normal | -0.036 |  |
| 2025-12-07 16:06:52 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.038 |  |
| 2025-12-07 16:13:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | -0.079 |  |
| 2025-12-07 17:01:09 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)