# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--11--30_20:20:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **6,145 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-30 20:20:44 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-11-30 20:14:36 | Giriulla (Maha Oya) | 3.89 | 🟢 Normal | -0.062 |  |
| 2025-11-30 20:13:03 | Holombuwa (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-11-30 20:10:57 | Holombuwa (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-11-30 20:10:17 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-11-30 20:07:33 | Glencourse (Kelani Ganga) | 15.80 | 🟡 Alert | -0.225 |  |
| 2025-11-30 20:07:23 | Thanamalwila (Kirindi Oya) | 1.71 | 🟢 Normal | -0.020 |  |
| 2025-11-30 20:06:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.70 | 🟠 Minor Flood | -0.043 |  |
| 2025-11-30 20:06:28 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2025-11-30 20:06:14 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | -0.010 |  |
| 2025-11-30 20:06:03 | Katharagama (Menik Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-11-30 20:05:33 | Dunamale (Aththanagalu Oya) | 4.97 | 🟠 Minor Flood | -0.010 |  |
| 2025-11-30 20:05:26 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | -0.030 |  |
| 2025-11-30 20:05:14 | Hanwella (Kelani Ganga) | 10.40 | 🔴 Major Flood | -0.060 |  |
| 2025-11-30 20:05:08 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.075 |  |
| 2025-11-30 20:04:33 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.043 |  |
| 2025-11-30 20:04:32 | Nagalagam Street (Kelani Ganga) | 2.38 | 🔴 Major Flood | 0.045 | 🔺 Rising |
| 2025-11-30 20:03:57 | Putupaula (Kalu Ganga) | 4.28 | 🟠 Minor Flood | 0.000 |  |
| 2025-11-30 20:03:51 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-11-30 20:03:51 | Siyambalanduwa (Heda Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2025-11-30 20:03:41 | Deraniyagala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-11-30 20:03:36 | Rathnapura (Kalu Ganga) | 6.46 | 🟡 Alert | -0.040 |  |
| 2025-11-30 20:02:34 | Kuda Oya (Kirindi Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2025-11-30 20:02:27 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2025-11-30 20:02:21 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | -0.050 |  |
| 2025-11-30 20:02:19 | Kithulgala (Kelani Ganga) | 2.69 | 🟢 Normal | -0.055 |  |
| 2025-11-30 20:02:18 | Nawalapitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.019 |  |
| 2025-11-30 20:02:12 | Yaka Wewa (Ma Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2025-11-30 20:01:40 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | -0.040 |  |
| 2025-11-30 20:01:32 | Thanthirimale (Malwathu Oya) | 10.79 | 🔴 Major Flood | -0.040 |  |
| 2025-11-30 20:00:16 | Horowpothana (Yan Oya) | 7.50 | 🟠 Minor Flood | 0.000 |  |
| 2025-11-30 20:00:10 | Nakkala (Kumbukkan Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2025-11-30 20:00:08 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-11-30 20:04:32 | Nagalagam Street (Kelani Ganga) | 2.38 | 🔴 Major Flood | 0.045 | 🔺 Rising |
| 2025-11-30 20:01:32 | Thanthirimale (Malwathu Oya) | 10.79 | 🔴 Major Flood | -0.040 |  |
| 2025-11-30 20:05:14 | Hanwella (Kelani Ganga) | 10.40 | 🔴 Major Flood | -0.060 |  |
| 2025-11-28 02:13:33⌛ | Manampitiya (Mahaweli Ganga) | 5.95 | 🟠 Minor Flood | 0.095 | 🔺 Rising |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-11-27 18:42:59⌛ | Galgamuwa (Mee Oya) | 6.12 | 🟠 Minor Flood | 0.045 | 🔺 Rising |
| 2025-11-30 14:56:34 | Ellagawa (Kalu Ganga) | 11.94 | 🟠 Minor Flood | 0.044 | 🔺 Rising |
| 2025-11-30 20:00:16 | Horowpothana (Yan Oya) | 7.50 | 🟠 Minor Flood | 0.000 |  |
| 2025-11-30 20:03:57 | Putupaula (Kalu Ganga) | 4.28 | 🟠 Minor Flood | 0.000 |  |
| 2025-11-30 20:05:33 | Dunamale (Aththanagalu Oya) | 4.97 | 🟠 Minor Flood | -0.010 |  |
| 2025-11-30 20:06:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.70 | 🟠 Minor Flood | -0.043 |  |
| 2025-11-30 18:48:59 | Badalgama (Maha Oya) | 6.80 | 🟠 Minor Flood | -0.293 |  |
| 2025-11-30 20:03:36 | Rathnapura (Kalu Ganga) | 6.46 | 🟡 Alert | -0.040 |  |
| 2025-11-30 20:07:33 | Glencourse (Kelani Ganga) | 15.80 | 🟡 Alert | -0.225 |  |
| 2025-11-30 20:03:41 | Deraniyagala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-11-30 20:00:08 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-11-30 20:20:44 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-11-30 20:06:03 | Katharagama (Menik Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-11-30 20:13:03 | Holombuwa (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-11-30 20:02:34 | Kuda Oya (Kirindi Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2025-11-30 20:06:14 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | -0.010 |  |
| 2025-11-30 20:03:51 | Siyambalanduwa (Heda Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2025-11-30 20:00:10 | Nakkala (Kumbukkan Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2025-11-30 20:03:51 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-11-30 20:02:18 | Nawalapitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.019 |  |
| 2025-11-30 20:07:23 | Thanamalwila (Kirindi Oya) | 1.71 | 🟢 Normal | -0.020 |  |
| 2025-11-30 20:02:12 | Yaka Wewa (Ma Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2025-11-30 20:02:27 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2025-11-30 14:03:57 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal | -0.021 |  |
| 2025-11-30 20:05:26 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | -0.030 |  |
| 2025-11-30 20:01:40 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | -0.040 |  |
| 2025-11-30 20:04:33 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.043 |  |
| 2025-11-30 20:02:21 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | -0.050 |  |
| 2025-11-30 20:02:19 | Kithulgala (Kelani Ganga) | 2.69 | 🟢 Normal | -0.055 |  |
| 2025-11-30 20:14:36 | Giriulla (Maha Oya) | 3.89 | 🟢 Normal | -0.062 |  |
| 2025-11-30 20:05:08 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.075 |  |

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)