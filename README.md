# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--01_20:29:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **6,896 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-01 20:29:48 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.007 |  |
| 2025-12-01 20:16:17 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-01 20:12:39 | Ellagawa (Kalu Ganga) | 10.68 | 🟡 Alert | -0.034 |  |
| 2025-12-01 20:10:10 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-01 20:10:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.86 | 🟠 Minor Flood | -0.060 |  |
| 2025-12-01 20:08:51 | Thanamalwila (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-01 20:08:41 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-01 20:07:44 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-01 20:07:14 | Yaka Wewa (Ma Oya) | 1.09 | 🟢 Normal | -0.009 |  |
| 2025-12-01 20:07:07 | Hanwella (Kelani Ganga) | 8.44 | 🟠 Minor Flood | -0.089 |  |
| 2025-12-01 20:06:50 | Panadugama (Nilwala Ganga) | 3.22 | 🟢 Normal | -0.031 |  |
| 2025-12-01 20:06:26 | Badalgama (Maha Oya) | 3.92 | 🟢 Normal | -0.019 |  |
| 2025-12-01 20:06:16 | Thanamalwila (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-01 20:05:18 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.119 |  |
| 2025-12-01 20:05:11 | Glencourse (Kelani Ganga) | 12.05 | 🟢 Normal | -0.077 |  |
| 2025-12-01 20:05:08 | Katharagama (Menik Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-01 20:04:44 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.020 |  |
| 2025-12-01 20:04:33 | Putupaula (Kalu Ganga) | 4.12 | 🟠 Minor Flood | -0.020 |  |
| 2025-12-01 20:04:30 | Horowpothana (Yan Oya) | 6.31 | 🟡 Alert | -0.116 |  |
| 2025-12-01 20:03:42 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-01 20:03:34 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-01 20:03:23 | Nagalagam Street (Kelani Ganga) | 2.47 | 🔴 Major Flood | 0.000 |  |
| 2025-12-01 20:03:15 | Rathnapura (Kalu Ganga) | 4.89 | 🟢 Normal | -0.062 |  |
| 2025-12-01 20:03:03 | Giriulla (Maha Oya) | 2.80 | 🟢 Normal | -0.057 |  |
| 2025-12-01 20:02:46 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2025-12-01 20:02:13 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | -0.021 |  |
| 2025-12-01 20:02:00 | Moraketiya (Walawe Ganga) | 1.49 | 🟢 Normal | -0.058 |  |
| 2025-12-01 20:01:47 | Siyambalanduwa (Heda Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-01 20:01:41 | Nakkala (Kumbukkan Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-01 20:01:18 | Dunamale (Aththanagalu Oya) | 3.45 | 🟡 Alert | -0.051 |  |
| 2025-12-01 20:01:15 | Thanthirimale (Malwathu Oya) | 9.21 | 🔴 Major Flood | -0.041 |  |
| 2025-12-01 20:01:15 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.043 |  |
| 2025-12-01 20:00:42 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-01 20:03:23 | Nagalagam Street (Kelani Ganga) | 2.47 | 🔴 Major Flood | 0.000 |  |
| 2025-12-01 20:01:15 | Thanthirimale (Malwathu Oya) | 9.21 | 🔴 Major Flood | -0.041 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-01 20:04:33 | Putupaula (Kalu Ganga) | 4.12 | 🟠 Minor Flood | -0.020 |  |
| 2025-12-01 20:10:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.86 | 🟠 Minor Flood | -0.060 |  |
| 2025-12-01 20:07:07 | Hanwella (Kelani Ganga) | 8.44 | 🟠 Minor Flood | -0.089 |  |
| 2025-12-01 20:12:39 | Ellagawa (Kalu Ganga) | 10.68 | 🟡 Alert | -0.034 |  |
| 2025-12-01 20:01:18 | Dunamale (Aththanagalu Oya) | 3.45 | 🟡 Alert | -0.051 |  |
| 2025-12-01 20:04:30 | Horowpothana (Yan Oya) | 6.31 | 🟡 Alert | -0.116 |  |
| 2025-12-01 20:00:42 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-01 20:03:42 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-01 20:01:41 | Nakkala (Kumbukkan Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-01 20:03:34 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-01 20:08:41 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-01 20:16:17 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-01 18:04:12 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-01 20:10:10 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-01 20:08:51 | Thanamalwila (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-01 20:29:48 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.007 |  |
| 2025-12-01 20:07:14 | Yaka Wewa (Ma Oya) | 1.09 | 🟢 Normal | -0.009 |  |
| 2025-12-01 20:05:08 | Katharagama (Menik Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-01 20:01:47 | Siyambalanduwa (Heda Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-01 20:07:44 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-01 20:06:26 | Badalgama (Maha Oya) | 3.92 | 🟢 Normal | -0.019 |  |
| 2025-12-01 20:04:44 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.020 |  |
| 2025-12-01 20:02:46 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2025-12-01 20:02:13 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | -0.021 |  |
| 2025-12-01 18:00:59 | Galgamuwa (Mee Oya) | 3.58 | 🟢 Normal | -0.021 |  |
| 2025-12-01 20:06:50 | Panadugama (Nilwala Ganga) | 3.22 | 🟢 Normal | -0.031 |  |
| 2025-12-01 20:01:15 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.043 |  |
| 2025-12-01 20:03:03 | Giriulla (Maha Oya) | 2.80 | 🟢 Normal | -0.057 |  |
| 2025-12-01 20:02:00 | Moraketiya (Walawe Ganga) | 1.49 | 🟢 Normal | -0.058 |  |
| 2025-12-01 20:03:15 | Rathnapura (Kalu Ganga) | 4.89 | 🟢 Normal | -0.062 |  |
| 2025-12-01 20:05:11 | Glencourse (Kelani Ganga) | 12.05 | 🟢 Normal | -0.077 |  |
| 2025-12-01 20:05:18 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.119 |  |
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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)