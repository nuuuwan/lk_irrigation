# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_06:18:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,050 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 06:18:08 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.060 |  |
| 2025-12-09 06:11:38 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2025-12-09 06:10:42 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-09 06:10:25 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-09 06:10:23 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.009 |  |
| 2025-12-09 06:09:50 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:09:06 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-09 06:08:25 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:07:40 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:07:07 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | -0.038 |  |
| 2025-12-09 06:06:45 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-09 06:06:27 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:06:00 | Thanthirimale (Malwathu Oya) | 3.55 | 🟢 Normal | -0.062 |  |
| 2025-12-09 06:05:49 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:05:13 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:04:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | -0.251 |  |
| 2025-12-09 06:04:11 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:04:00 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:03:36 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:03:35 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-09 06:03:22 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.035 |  |
| 2025-12-09 06:03:19 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:02:40 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.060 |  |
| 2025-12-09 06:02:25 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:02:09 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2025-12-09 06:01:55 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.011 |  |
| 2025-12-09 06:01:44 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-09 06:01:27 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-09 06:01:12 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.062 |  |
| 2025-12-09 06:01:05 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-09 06:01:00 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:00:47 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:00:39 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2025-12-09 06:00:39 | Rathnapura (Kalu Ganga) | 2.69 | 🟢 Normal | -0.138 |  |
| 2025-12-09 06:00:19 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-09 05:45:59 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.035 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 06:00:39 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2025-12-09 06:01:27 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-09 06:03:35 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-09 06:11:38 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2025-12-08 18:02:40 | Galgamuwa (Mee Oya) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-09 06:10:25 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-09 06:06:45 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-09 06:01:05 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-09 06:01:44 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-08 17:05:58 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-09 06:10:42 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-09 06:09:06 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-09 06:03:36 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:00:19 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:01:00 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:03:19 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:04:11 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:07:40 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:05:49 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:09:50 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:05:13 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:08:25 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:04:00 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:06:27 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:02:25 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 06:10:23 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.009 |  |
| 2025-12-09 06:02:09 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2025-12-08 18:00:48 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-09 06:01:55 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.011 |  |
| 2025-12-09 06:03:22 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.035 |  |
| 2025-12-09 06:07:07 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | -0.038 |  |
| 2025-12-09 06:18:08 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.060 |  |
| 2025-12-09 06:02:40 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.060 |  |
| 2025-12-09 06:06:00 | Thanthirimale (Malwathu Oya) | 3.55 | 🟢 Normal | -0.062 |  |
| 2025-12-09 06:01:12 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.062 |  |
| 2025-12-09 06:00:39 | Rathnapura (Kalu Ganga) | 2.69 | 🟢 Normal | -0.138 |  |
| 2025-12-08 18:03:06 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | -0.251 |  |
| 2025-12-09 06:04:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | -0.251 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)