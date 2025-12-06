# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--06_06:08:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,517 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-06 06:08:03 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-06 06:07:50 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | 0.000 |  |
| 2025-12-06 06:07:11 | Thanthirimale (Malwathu Oya) | 6.85 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2025-12-06 06:06:51 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.009 |  |
| 2025-12-06 06:06:31 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.009 |  |
| 2025-12-06 06:06:20 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | -0.400 |  |
| 2025-12-06 06:04:56 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-06 06:04:12 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-06 06:03:37 | Giriulla (Maha Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2025-12-06 06:03:36 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | -0.073 |  |
| 2025-12-06 06:03:08 | Dunamale (Aththanagalu Oya) | 2.14 | 🟢 Normal | -0.053 |  |
| 2025-12-06 06:02:37 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-06 06:02:36 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-06 06:02:33 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 06:02:29 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-06 06:02:23 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-06 06:02:14 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.020 |  |
| 2025-12-06 06:01:53 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2025-12-06 06:01:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-06 06:01:34 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2025-12-06 06:01:28 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-06 06:01:11 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-06 06:01:11 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.095 |  |
| 2025-12-06 06:01:07 | Rathnapura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.089 |  |
| 2025-12-06 06:00:52 | Magura (Kalu Ganga) | 4.20 | 🟡 Alert | -0.283 |  |
| 2025-12-06 06:00:13 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.030 |  |
| 2025-12-06 06:00:08 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:35:28 | Magura (Kalu Ganga) | 4.32 | 🟡 Alert | -0.283 |  |
| 2025-12-06 05:35:27 | Magura (Kalu Ganga) | 4.43 | 🟡 Alert | -0.283 |  |
| 2025-12-06 05:19:44 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2025-12-06 05:19:01 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2025-12-06 05:17:53 | Dunamale (Aththanagalu Oya) | 2.18 | 🟢 Normal | -0.053 |  |
| 2025-12-06 05:14:06 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.089 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-06 06:07:11 | Thanthirimale (Malwathu Oya) | 6.85 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2025-12-06 06:00:52 | Magura (Kalu Ganga) | 4.20 | 🟡 Alert | -0.283 |  |
| 2025-12-06 05:04:05 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2025-12-05 18:01:43 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-06 06:01:53 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2025-12-05 18:04:31 | Galgamuwa (Mee Oya) | 0.79 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-06 05:04:28 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2025-12-05 16:03:28 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-06 06:04:12 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-06 06:01:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-06 06:01:11 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-06 05:08:42 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-06 06:00:08 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-06 06:02:36 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-06 06:02:23 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-06 06:02:37 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-06 06:07:50 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | 0.000 |  |
| 2025-12-06 06:02:33 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 06:02:29 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:07:47 | Katharagama (Menik Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:05:20 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-06 06:08:03 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-06 03:17:34 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | -0.006 |  |
| 2025-12-06 06:06:51 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.009 |  |
| 2025-12-06 06:06:31 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.009 |  |
| 2025-12-06 06:03:37 | Giriulla (Maha Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2025-12-06 06:04:56 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-06 06:01:34 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2025-12-06 06:01:28 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-06 06:02:14 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.020 |  |
| 2025-12-06 06:00:13 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.030 |  |
| 2025-12-06 06:03:08 | Dunamale (Aththanagalu Oya) | 2.14 | 🟢 Normal | -0.053 |  |
| 2025-12-06 06:03:36 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | -0.073 |  |
| 2025-12-06 06:01:07 | Rathnapura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.089 |  |
| 2025-12-06 06:01:11 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.095 |  |
| 2025-12-05 18:05:43 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.177 |  |
| 2025-12-06 06:06:20 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | -0.400 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)