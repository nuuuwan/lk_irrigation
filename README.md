# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--04_19:24:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,321 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-04 19:24:44 | Urawa (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.577 | 🔺 Rising |
| 2025-12-04 19:11:55 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-04 19:10:31 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-04 19:08:22 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-04 19:07:45 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-04 19:07:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.51 | 🟢 Normal | -0.028 |  |
| 2025-12-04 19:07:01 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | 0.000 |  |
| 2025-12-04 19:06:37 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-04 19:06:29 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 19:06:24 | Hanwella (Kelani Ganga) | 3.46 | 🟢 Normal | -0.039 |  |
| 2025-12-04 19:06:21 | Panadugama (Nilwala Ganga) | 3.40 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2025-12-04 19:04:15 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-04 19:04:04 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-04 19:04:02 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2025-12-04 19:03:58 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.111 |  |
| 2025-12-04 19:03:52 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-04 19:03:43 | Deraniyagala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2025-12-04 19:03:43 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 19:03:26 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2025-12-04 19:03:19 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.048 |  |
| 2025-12-04 19:03:11 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.032 |  |
| 2025-12-04 19:03:06 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 19:02:54 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-04 19:02:51 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2025-12-04 19:02:25 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2025-12-04 19:02:18 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 19:02:07 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-04 19:01:01 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-04 19:00:53 | Thanthirimale (Malwathu Oya) | 5.80 | 🟡 Alert | -0.038 |  |
| 2025-12-04 19:00:12 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-04 19:00:12 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-04 19:00:07 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-04 19:00:53 | Thanthirimale (Malwathu Oya) | 5.80 | 🟡 Alert | -0.038 |  |
| 2025-12-04 19:24:44 | Urawa (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.577 | 🔺 Rising |
| 2025-12-04 19:06:21 | Panadugama (Nilwala Ganga) | 3.40 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2025-12-04 19:02:25 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2025-12-04 19:04:02 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2025-12-04 19:03:43 | Deraniyagala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2025-12-04 18:03:45 | Ellagawa (Kalu Ganga) | 5.67 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-04 19:10:31 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-04 19:06:37 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-04 19:04:04 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-04 19:02:07 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-04 19:03:52 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-04 19:06:29 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 19:00:12 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-04 19:04:15 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-04 19:03:26 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2025-12-04 19:00:07 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:19:13 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 19:02:18 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:04:32 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 19:03:06 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 19:08:22 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-04 19:07:01 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | 0.000 |  |
| 2025-12-04 19:03:43 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 19:02:54 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-04 19:11:55 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-04 19:01:01 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-04 19:02:51 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2025-12-04 19:00:12 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-04 18:05:39 | Manampitiya (Mahaweli Ganga) | 2.29 | 🟢 Normal | -0.019 |  |
| 2025-12-04 18:04:34 | Galgamuwa (Mee Oya) | 0.53 | 🟢 Normal | -0.020 |  |
| 2025-12-04 19:07:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.51 | 🟢 Normal | -0.028 |  |
| 2025-12-04 19:03:11 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.032 |  |
| 2025-12-04 19:06:24 | Hanwella (Kelani Ganga) | 3.46 | 🟢 Normal | -0.039 |  |
| 2025-12-04 18:08:34 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | -0.047 |  |
| 2025-12-04 19:03:19 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.048 |  |
| 2025-12-04 19:03:58 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)