# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--05_08:01:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,729 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-05 08:01:48 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2025-12-05 08:01:42 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:01:04 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:00:19 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:00:18 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:00:14 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-05 07:40:38 | Giriulla (Maha Oya) | 1.83 | 🟢 Normal | -0.006 |  |
| 2025-12-05 07:24:33 | Panadugama (Nilwala Ganga) | 4.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-05 07:19:00 | Rathnapura (Kalu Ganga) | 2.63 | 🟢 Normal | -0.088 |  |
| 2025-12-05 07:16:20 | Urawa (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.264 |  |
| 2025-12-05 07:15:15 | Pitabeddara (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.130 |  |
| 2025-12-05 07:15:07 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-05 07:08:30 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | -0.051 |  |
| 2025-12-05 07:07:23 | Thanthirimale (Malwathu Oya) | 5.81 | 🟡 Alert | 0.153 | 🔺 Rising |
| 2025-12-05 07:07:04 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 07:06:11 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.010 |  |
| 2025-12-05 07:05:48 | Glencourse (Kelani Ganga) | 10.72 | 🟢 Normal | 0.000 |  |
| 2025-12-05 07:04:59 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-05 07:04:53 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 07:04:46 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | -0.095 |  |
| 2025-12-05 07:04:39 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-05 07:04:28 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.019 |  |
| 2025-12-05 07:04:12 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-05 07:04:10 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-05 07:04:05 | Weraganthota (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2025-12-05 07:03:57 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-05 07:03:49 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | 0.000 |  |
| 2025-12-05 07:03:37 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-05 07:03:23 | Magura (Kalu Ganga) | 2.51 | 🟢 Normal | -0.159 |  |
| 2025-12-05 07:03:21 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-05 07:03:12 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 07:03:10 | Hanwella (Kelani Ganga) | 3.52 | 🟢 Normal | -0.036 |  |
| 2025-12-05 07:03:06 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.200 |  |
| 2025-12-05 07:03:04 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-05 07:03:03 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-05 07:07:23 | Thanthirimale (Malwathu Oya) | 5.81 | 🟡 Alert | 0.153 | 🔺 Rising |
| 2025-12-05 07:04:05 | Weraganthota (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2025-12-05 07:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.86 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-05 07:03:37 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-05 07:03:57 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-05 07:24:33 | Panadugama (Nilwala Ganga) | 4.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-05 07:03:12 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 07:07:04 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 07:02:31 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:00:19 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-05 07:03:04 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-05 07:04:10 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-05 07:03:49 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | 0.000 |  |
| 2025-12-05 00:01:47 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:01:42 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | 0.000 |  |
| 2025-12-05 08:01:04 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-05 07:04:53 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 07:03:03 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 07:04:59 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-05 07:15:07 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-05 07:01:29 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-05 07:04:39 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-05 07:40:38 | Giriulla (Maha Oya) | 1.83 | 🟢 Normal | -0.006 |  |
| 2025-12-05 08:00:14 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-05 08:01:48 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2025-12-05 07:02:15 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-05 07:06:11 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.010 |  |
| 2025-12-05 07:04:28 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.019 |  |
| 2025-12-04 19:33:02 | Manampitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.027 |  |
| 2025-12-05 07:03:10 | Hanwella (Kelani Ganga) | 3.52 | 🟢 Normal | -0.036 |  |
| 2025-12-05 07:08:30 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | -0.051 |  |
| 2025-12-05 07:19:00 | Rathnapura (Kalu Ganga) | 2.63 | 🟢 Normal | -0.088 |  |
| 2025-12-05 07:04:46 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | -0.095 |  |
| 2025-12-05 07:15:15 | Pitabeddara (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.130 |  |
| 2025-12-05 07:03:23 | Magura (Kalu Ganga) | 2.51 | 🟢 Normal | -0.159 |  |
| 2025-12-05 07:03:06 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.200 |  |
| 2025-12-05 07:16:20 | Urawa (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.264 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)