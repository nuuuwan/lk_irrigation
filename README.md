# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--11--30_21:16:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **6,175 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-30 21:16:01 | Horowpothana (Yan Oya) | 7.49 | 🟡 Alert | -0.008 |  |
| 2025-11-30 21:14:08 | Giriulla (Maha Oya) | 3.84 | 🟢 Normal | -0.050 |  |
| 2025-11-30 21:10:44 | Holombuwa (Kelani Ganga) | 1.69 | 🟢 Normal | -0.094 |  |
| 2025-11-30 21:08:45 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-11-30 21:07:52 | Glencourse (Kelani Ganga) | 15.56 | 🟡 Alert | -0.239 |  |
| 2025-11-30 21:07:33 | Putupaula (Kalu Ganga) | 4.28 | 🟠 Minor Flood | 0.000 |  |
| 2025-11-30 21:07:17 | Thanamalwila (Kirindi Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2025-11-30 21:07:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.68 | 🟠 Minor Flood | -0.020 |  |
| 2025-11-30 21:06:04 | Baddegama (Gin Ganga) | 2.33 | 🟢 Normal | -0.030 |  |
| 2025-11-30 21:05:57 | Panadugama (Nilwala Ganga) | 3.61 | 🟢 Normal | -0.010 |  |
| 2025-11-30 21:05:53 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-11-30 21:05:49 | Hanwella (Kelani Ganga) | 10.35 | 🔴 Major Flood | -0.050 |  |
| 2025-11-30 21:05:35 | Badalgama (Maha Oya) | 6.09 | 🟡 Alert | -0.312 |  |
| 2025-11-30 21:04:54 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2025-11-30 21:04:17 | Nagalagam Street (Kelani Ganga) | 2.41 | 🔴 Major Flood | 0.031 | 🔺 Rising |
| 2025-11-30 21:03:50 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2025-11-30 21:03:41 | Rathnapura (Kalu Ganga) | 6.40 | 🟡 Alert | -0.060 |  |
| 2025-11-30 21:03:23 | Deraniyagala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.111 |  |
| 2025-11-30 21:03:02 | Nawalapitiya (Mahaweli Ganga) | 2.01 | 🟢 Normal | -0.020 |  |
| 2025-11-30 21:02:44 | Kithulgala (Kelani Ganga) | 2.65 | 🟢 Normal | -0.040 |  |
| 2025-11-30 21:02:26 | Dunamale (Aththanagalu Oya) | 4.95 | 🟠 Minor Flood | -0.021 |  |
| 2025-11-30 21:02:21 | Pitabeddara (Nilwala Ganga) | 1.19 | 🟢 Normal | -0.029 |  |
| 2025-11-30 21:02:10 | Thalgahagoda (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-11-30 21:02:09 | Katharagama (Menik Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-11-30 21:01:55 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | -0.050 |  |
| 2025-11-30 21:01:46 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2025-11-30 21:01:35 | Nakkala (Kumbukkan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2025-11-30 21:01:09 | Thanthirimale (Malwathu Oya) | 10.75 | 🔴 Major Flood | -0.040 |  |
| 2025-11-30 21:00:53 | Yaka Wewa (Ma Oya) | 1.39 | 🟢 Normal | -0.031 |  |
| 2025-11-30 21:00:16 | Siyambalanduwa (Heda Oya) | 1.33 | 🟢 Normal | -0.011 |  |
| 2025-11-30 20:20:44 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.029 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-11-30 21:04:17 | Nagalagam Street (Kelani Ganga) | 2.41 | 🔴 Major Flood | 0.031 | 🔺 Rising |
| 2025-11-30 21:01:09 | Thanthirimale (Malwathu Oya) | 10.75 | 🔴 Major Flood | -0.040 |  |
| 2025-11-30 21:05:49 | Hanwella (Kelani Ganga) | 10.35 | 🔴 Major Flood | -0.050 |  |
| 2025-11-28 02:13:33⌛ | Manampitiya (Mahaweli Ganga) | 5.95 | 🟠 Minor Flood | 0.095 | 🔺 Rising |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-11-27 18:42:59⌛ | Galgamuwa (Mee Oya) | 6.12 | 🟠 Minor Flood | 0.045 | 🔺 Rising |
| 2025-11-30 14:56:34 | Ellagawa (Kalu Ganga) | 11.94 | 🟠 Minor Flood | 0.044 | 🔺 Rising |
| 2025-11-30 21:07:33 | Putupaula (Kalu Ganga) | 4.28 | 🟠 Minor Flood | 0.000 |  |
| 2025-11-30 21:07:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.68 | 🟠 Minor Flood | -0.020 |  |
| 2025-11-30 21:02:26 | Dunamale (Aththanagalu Oya) | 4.95 | 🟠 Minor Flood | -0.021 |  |
| 2025-11-30 21:16:01 | Horowpothana (Yan Oya) | 7.49 | 🟡 Alert | -0.008 |  |
| 2025-11-30 21:03:41 | Rathnapura (Kalu Ganga) | 6.40 | 🟡 Alert | -0.060 |  |
| 2025-11-30 21:07:52 | Glencourse (Kelani Ganga) | 15.56 | 🟡 Alert | -0.239 |  |
| 2025-11-30 21:05:35 | Badalgama (Maha Oya) | 6.09 | 🟡 Alert | -0.312 |  |
| 2025-11-30 21:08:45 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-11-30 21:01:35 | Nakkala (Kumbukkan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2025-11-30 21:05:53 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-11-30 21:02:09 | Katharagama (Menik Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-11-30 21:03:50 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2025-11-30 21:07:17 | Thanamalwila (Kirindi Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2025-11-30 21:05:57 | Panadugama (Nilwala Ganga) | 3.61 | 🟢 Normal | -0.010 |  |
| 2025-11-30 21:01:46 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2025-11-30 21:02:10 | Thalgahagoda (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-11-30 21:00:16 | Siyambalanduwa (Heda Oya) | 1.33 | 🟢 Normal | -0.011 |  |
| 2025-11-30 21:04:54 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2025-11-30 21:03:02 | Nawalapitiya (Mahaweli Ganga) | 2.01 | 🟢 Normal | -0.020 |  |
| 2025-11-30 14:03:57 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal | -0.021 |  |
| 2025-11-30 21:02:21 | Pitabeddara (Nilwala Ganga) | 1.19 | 🟢 Normal | -0.029 |  |
| 2025-11-30 21:06:04 | Baddegama (Gin Ganga) | 2.33 | 🟢 Normal | -0.030 |  |
| 2025-11-30 21:00:53 | Yaka Wewa (Ma Oya) | 1.39 | 🟢 Normal | -0.031 |  |
| 2025-11-30 21:02:44 | Kithulgala (Kelani Ganga) | 2.65 | 🟢 Normal | -0.040 |  |
| 2025-11-30 21:01:55 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | -0.050 |  |
| 2025-11-30 21:14:08 | Giriulla (Maha Oya) | 3.84 | 🟢 Normal | -0.050 |  |
| 2025-11-30 20:05:08 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.075 |  |
| 2025-11-30 21:10:44 | Holombuwa (Kelani Ganga) | 1.69 | 🟢 Normal | -0.094 |  |
| 2025-11-30 21:03:23 | Deraniyagala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.111 |  |

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)