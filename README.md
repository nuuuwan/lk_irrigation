# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--08_02:45:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,064 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-08 02:45:31 | Glencourse (Kelani Ganga) | 11.13 | 🟢 Normal | -36.000 |  |
| 2025-12-08 02:45:29 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | -36.000 |  |
| 2025-12-08 02:41:59 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-08 02:36:52 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-08 02:30:50 | Hanwella (Kelani Ganga) | 2.40 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-08 02:21:31 | Magura (Kalu Ganga) | 3.01 | 🟢 Normal | 216.000 | 🔺 Rising |
| 2025-12-08 02:21:29 | Magura (Kalu Ganga) | 2.89 | 🟢 Normal | 216.000 | 🔺 Rising |
| 2025-12-08 02:19:03 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-08 02:18:43 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-08 02:11:32 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-08 02:09:55 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-08 02:08:50 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-08 02:07:01 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-08 02:06:31 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | -0.010 |  |
| 2025-12-08 02:05:29 | Rathnapura (Kalu Ganga) | 3.08 | 🟢 Normal | -0.103 |  |
| 2025-12-08 02:05:07 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | 10.000 | 🔺 Rising |
| 2025-12-08 02:04:31 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | 10.000 | 🔺 Rising |
| 2025-12-08 02:03:23 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-08 02:03:16 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-08 02:03:11 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2025-12-08 02:02:52 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-08 02:02:40 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-08 02:02:40 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.020 |  |
| 2025-12-08 02:02:32 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-08 02:02:28 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.051 |  |
| 2025-12-08 02:02:24 | Thanthirimale (Malwathu Oya) | 5.00 | 🟡 Alert | -10.286 |  |
| 2025-12-08 02:02:19 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-08 02:01:56 | Thanthirimale (Malwathu Oya) | 5.08 | 🟡 Alert | -10.286 |  |
| 2025-12-08 02:01:49 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2025-12-08 02:01:47 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-08 02:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.096 |  |
| 2025-12-08 02:01:07 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.311 | 🔺 Rising |
| 2025-12-08 01:55:13 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.096 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-08 02:02:24 | Thanthirimale (Malwathu Oya) | 5.00 | 🟡 Alert | -10.286 |  |
| 2025-12-08 02:21:31 | Magura (Kalu Ganga) | 3.01 | 🟢 Normal | 216.000 | 🔺 Rising |
| 2025-12-08 02:05:07 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | 10.000 | 🔺 Rising |
| 2025-12-07 18:19:39 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.563 | 🔺 Rising |
| 2025-12-08 02:01:07 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.311 | 🔺 Rising |
| 2025-12-08 02:03:11 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2025-12-08 01:00:47 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2025-12-08 02:11:32 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-08 01:08:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-08 01:03:56 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-08 02:30:50 | Hanwella (Kelani Ganga) | 2.40 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-08 02:03:16 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-08 02:09:55 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-08 00:11:32 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-08 02:08:50 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-07 18:08:26 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-08 02:41:59 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-08 02:02:40 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-08 02:01:47 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-08 02:02:19 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-08 02:02:52 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-08 01:00:43 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2025-12-08 02:19:03 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-08 02:07:01 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-08 02:36:52 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-08 02:03:23 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-08 00:01:11 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-08 02:06:31 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | -0.010 |  |
| 2025-12-08 01:07:42 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-08 02:02:40 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.020 |  |
| 2025-12-08 02:01:49 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2025-12-08 02:02:28 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.051 |  |
| 2025-12-07 18:13:05 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.067 |  |
| 2025-12-07 18:08:15 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | -0.069 |  |
| 2025-12-08 02:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.096 |  |
| 2025-12-08 02:05:29 | Rathnapura (Kalu Ganga) | 3.08 | 🟢 Normal | -0.103 |  |
| 2025-12-08 02:45:31 | Glencourse (Kelani Ganga) | 11.13 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)