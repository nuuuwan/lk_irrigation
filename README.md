# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--01_12:29:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **6,625 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-01 12:29:53 | Manampitiya (Mahaweli Ganga) | 3.03 | 🟡 Alert | -0.121 |  |
| 2025-12-01 12:19:26 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-01 12:13:45 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2025-12-01 12:12:03 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-01 12:10:41 | Panadugama (Nilwala Ganga) | 3.33 | 🟢 Normal | -0.010 |  |
| 2025-12-01 12:09:54 | Badalgama (Maha Oya) | 4.06 | 🟢 Normal | -0.047 |  |
| 2025-12-01 12:07:45 | Rathnapura (Kalu Ganga) | 5.43 | 🟡 Alert | -0.067 |  |
| 2025-12-01 12:06:41 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2025-12-01 12:06:13 | Ellagawa (Kalu Ganga) | 11.09 | 🟠 Minor Flood | -0.042 |  |
| 2025-12-01 12:06:04 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.058 |  |
| 2025-12-01 12:05:50 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-01 12:05:17 | Nakkala (Kumbukkan Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2025-12-01 12:04:43 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.039 |  |
| 2025-12-01 12:04:33 | Dunamale (Aththanagalu Oya) | 4.00 | 🟡 Alert | -0.064 |  |
| 2025-12-01 12:04:25 | Hanwella (Kelani Ganga) | 9.12 | 🟠 Minor Flood | -0.089 |  |
| 2025-12-01 12:04:03 | Putupaula (Kalu Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-01 12:04:02 | Katharagama (Menik Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-01 12:03:36 | Glencourse (Kelani Ganga) | 12.71 | 🟢 Normal | -0.077 |  |
| 2025-12-01 12:03:17 | Nagalagam Street (Kelani Ganga) | 2.59 | 🔴 Major Flood | 0.000 |  |
| 2025-12-01 12:03:01 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.019 |  |
| 2025-12-01 12:02:53 | Galgamuwa (Mee Oya) | 4.10 | 🟢 Normal | -0.125 |  |
| 2025-12-01 12:02:20 | Holombuwa (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-01 12:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.20 | 🟠 Minor Flood | -0.030 |  |
| 2025-12-01 12:02:18 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-01 12:01:59 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.021 |  |
| 2025-12-01 12:01:19 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-01 12:01:18 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-01 12:01:14 | Yaka Wewa (Ma Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-01 12:01:08 | Siyambalanduwa (Heda Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-01 12:00:48 | Thanamalwila (Kirindi Oya) | 1.50 | 🟢 Normal | 0.985 | 🔺 Rising |
| 2025-12-01 12:00:27 | Horowpothana (Yan Oya) | 7.03 | 🟡 Alert | -0.040 |  |
| 2025-12-01 12:00:17 | Thanthirimale (Malwathu Oya) | 9.78 | 🔴 Major Flood | -0.115 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-01 12:03:17 | Nagalagam Street (Kelani Ganga) | 2.59 | 🔴 Major Flood | 0.000 |  |
| 2025-12-01 12:00:17 | Thanthirimale (Malwathu Oya) | 9.78 | 🔴 Major Flood | -0.115 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-01 12:04:03 | Putupaula (Kalu Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-01 12:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.20 | 🟠 Minor Flood | -0.030 |  |
| 2025-12-01 12:06:13 | Ellagawa (Kalu Ganga) | 11.09 | 🟠 Minor Flood | -0.042 |  |
| 2025-12-01 12:04:25 | Hanwella (Kelani Ganga) | 9.12 | 🟠 Minor Flood | -0.089 |  |
| 2025-12-01 12:00:27 | Horowpothana (Yan Oya) | 7.03 | 🟡 Alert | -0.040 |  |
| 2025-12-01 12:04:33 | Dunamale (Aththanagalu Oya) | 4.00 | 🟡 Alert | -0.064 |  |
| 2025-12-01 12:07:45 | Rathnapura (Kalu Ganga) | 5.43 | 🟡 Alert | -0.067 |  |
| 2025-12-01 12:29:53 | Manampitiya (Mahaweli Ganga) | 3.03 | 🟡 Alert | -0.121 |  |
| 2025-12-01 12:00:48 | Thanamalwila (Kirindi Oya) | 1.50 | 🟢 Normal | 0.985 | 🔺 Rising |
| 2025-12-01 11:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-01 12:05:50 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-01 12:02:18 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-01 12:01:18 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-01 12:04:02 | Katharagama (Menik Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-01 12:02:20 | Holombuwa (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-01 12:12:03 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-01 12:19:26 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-01 12:13:45 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2025-12-01 12:05:17 | Nakkala (Kumbukkan Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2025-12-01 12:10:41 | Panadugama (Nilwala Ganga) | 3.33 | 🟢 Normal | -0.010 |  |
| 2025-12-01 12:01:08 | Siyambalanduwa (Heda Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-01 12:01:19 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-01 12:01:14 | Yaka Wewa (Ma Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-01 12:03:01 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.019 |  |
| 2025-12-01 12:06:41 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2025-11-30 14:03:57 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal | -0.021 |  |
| 2025-12-01 12:01:59 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.021 |  |
| 2025-12-01 12:04:43 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.039 |  |
| 2025-12-01 11:04:11 | Giriulla (Maha Oya) | 3.15 | 🟢 Normal | -0.042 |  |
| 2025-12-01 12:09:54 | Badalgama (Maha Oya) | 4.06 | 🟢 Normal | -0.047 |  |
| 2025-12-01 12:06:04 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.058 |  |
| 2025-12-01 12:03:36 | Glencourse (Kelani Ganga) | 12.71 | 🟢 Normal | -0.077 |  |
| 2025-12-01 12:02:53 | Galgamuwa (Mee Oya) | 4.10 | 🟢 Normal | -0.125 |  |

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)