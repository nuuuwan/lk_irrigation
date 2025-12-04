# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--04_20:13:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,359 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-04 20:13:18 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:12:34 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:12:29 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:08:26 | Giriulla (Maha Oya) | 2.93 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:08:16 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:08:13 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-04 20:07:52 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.028 |  |
| 2025-12-04 20:07:37 | Badalgama (Maha Oya) | 3.06 | 🟢 Normal | -0.010 |  |
| 2025-12-04 20:06:29 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:06:24 | Thanthirimale (Malwathu Oya) | 5.78 | 🟡 Alert | -0.018 |  |
| 2025-12-04 20:06:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:05:47 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:05:23 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:05:22 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2025-12-04 20:04:58 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-04 20:04:51 | Deraniyagala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:04:43 | Panadugama (Nilwala Ganga) | 3.57 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2025-12-04 20:04:37 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:04:35 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:04:32 | Deraniyagala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:04:29 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2025-12-04 20:04:06 | Hanwella (Kelani Ganga) | 3.44 | 🟢 Normal | -0.021 |  |
| 2025-12-04 20:04:02 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2025-12-04 20:03:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:03:40 | Urawa (Nilwala Ganga) | 2.74 | 🟡 Alert | 0.740 | 🔺 Rising |
| 2025-12-04 20:03:37 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:03:33 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-04 20:03:32 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:03:25 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | -0.009 |  |
| 2025-12-04 20:02:52 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2025-12-04 20:02:50 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2025-12-04 20:02:44 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.123 |  |
| 2025-12-04 20:02:21 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2025-12-04 20:02:14 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:01:58 | Dunamale (Aththanagalu Oya) | 2.50 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2025-12-04 20:00:35 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 19:34:16 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2025-12-04 19:33:02 | Manampitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.027 |  |
| 2025-12-04 19:24:44 | Urawa (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.740 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-04 20:03:40 | Urawa (Nilwala Ganga) | 2.74 | 🟡 Alert | 0.740 | 🔺 Rising |
| 2025-12-04 20:06:24 | Thanthirimale (Malwathu Oya) | 5.78 | 🟡 Alert | -0.018 |  |
| 2025-12-04 20:04:29 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2025-12-04 20:04:02 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2025-12-04 20:04:43 | Panadugama (Nilwala Ganga) | 3.57 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2025-12-04 20:02:52 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2025-12-04 20:02:50 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2025-12-04 20:01:58 | Dunamale (Aththanagalu Oya) | 2.50 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2025-12-04 20:04:58 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-04 19:03:52 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-04 20:00:35 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 20:13:18 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-04 19:00:07 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:04:51 | Deraniyagala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:19:13 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:05:47 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:04:37 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:03:37 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:04:32 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:06:29 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:08:16 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:12:29 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-04 19:11:55 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:06:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2025-12-04 20:03:25 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | -0.009 |  |
| 2025-12-04 20:05:22 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2025-12-04 20:07:37 | Badalgama (Maha Oya) | 3.06 | 🟢 Normal | -0.010 |  |
| 2025-12-04 20:08:13 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-04 20:03:33 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-04 18:04:34 | Galgamuwa (Mee Oya) | 0.53 | 🟢 Normal | -0.020 |  |
| 2025-12-04 20:02:21 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2025-12-04 20:04:06 | Hanwella (Kelani Ganga) | 3.44 | 🟢 Normal | -0.021 |  |
| 2025-12-04 19:33:02 | Manampitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.027 |  |
| 2025-12-04 20:07:52 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.028 |  |
| 2025-12-04 18:08:34 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | -0.047 |  |
| 2025-12-04 19:03:58 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.111 |  |
| 2025-12-04 20:02:44 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)