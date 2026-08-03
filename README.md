# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_23:21:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,189 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 23:21:28 | Panadugama (Nilwala Ganga) | 4.74 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-08-03 23:17:08 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-03 23:13:30 | Magura (Kalu Ganga) | 3.29 | 🟢 Normal | -0.058 |  |
| 2026-08-03 23:13:03 | Pitabeddara (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-08-03 23:11:01 | Glencourse (Kelani Ganga) | 16.38 | 🟡 Alert | -0.045 |  |
| 2026-08-03 23:10:09 | Kithulgala (Kelani Ganga) | 3.08 | 🟡 Alert | 0.265 | 🔺 Rising |
| 2026-08-03 23:09:49 | Rathnapura (Kalu Ganga) | 8.00 | 🟠 Minor Flood | -0.068 |  |
| 2026-08-03 23:09:42 | Baddegama (Gin Ganga) | 2.37 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-03 23:08:11 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-08-03 23:07:33 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-03 23:07:04 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-03 23:05:54 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.051 |  |
| 2026-08-03 23:04:44 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-03 23:04:09 | Peradeniya (Mahaweli Ganga) | 8.09 | 🟠 Minor Flood | -0.514 |  |
| 2026-08-03 23:03:48 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.043 |  |
| 2026-08-03 23:03:43 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-03 23:03:38 | Holombuwa (Kelani Ganga) | 1.58 | 🟢 Normal | -0.103 |  |
| 2026-08-03 23:03:29 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-08-03 23:03:23 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 23:03:15 | Giriulla (Maha Oya) | 4.73 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-03 23:03:08 | Nawalapitiya (Mahaweli Ganga) | 3.50 | 🟡 Alert | -0.498 |  |
| 2026-08-03 23:02:55 | Hanwella (Kelani Ganga) | 6.91 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-08-03 23:02:53 | Norwood (Kelani Ganga) | 1.68 | 🟡 Alert | -0.032 |  |
| 2026-08-03 23:02:47 | Ellagawa (Kalu Ganga) | 8.21 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-08-03 23:02:42 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-03 23:02:34 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-03 23:02:14 | Thawalama (Gin Ganga) | 3.71 | 🟢 Normal | -0.089 |  |
| 2026-08-03 23:02:11 | Deraniyagala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.100 |  |
| 2026-08-03 23:02:10 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-03 23:01:43 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 23:01:34 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-03 23:00:46 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 23:00:39 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 23:00:35 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 23:09:49 | Rathnapura (Kalu Ganga) | 8.00 | 🟠 Minor Flood | -0.068 |  |
| 2026-08-03 23:04:09 | Peradeniya (Mahaweli Ganga) | 8.09 | 🟠 Minor Flood | -0.514 |  |
| 2026-08-03 23:10:09 | Kithulgala (Kelani Ganga) | 3.08 | 🟡 Alert | 0.265 | 🔺 Rising |
| 2026-08-03 23:02:53 | Norwood (Kelani Ganga) | 1.68 | 🟡 Alert | -0.032 |  |
| 2026-08-03 23:11:01 | Glencourse (Kelani Ganga) | 16.38 | 🟡 Alert | -0.045 |  |
| 2026-08-03 23:03:08 | Nawalapitiya (Mahaweli Ganga) | 3.50 | 🟡 Alert | -0.498 |  |
| 2026-08-03 23:03:29 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-08-03 23:02:55 | Hanwella (Kelani Ganga) | 6.91 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-08-03 23:21:28 | Panadugama (Nilwala Ganga) | 4.74 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-08-03 23:13:03 | Pitabeddara (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-08-03 23:02:47 | Ellagawa (Kalu Ganga) | 8.21 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-08-03 23:03:15 | Giriulla (Maha Oya) | 4.73 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-03 23:08:11 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-08-03 23:02:34 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-03 23:07:04 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-03 23:09:42 | Baddegama (Gin Ganga) | 2.37 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-03 22:36:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.80 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-03 23:04:44 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-03 23:03:23 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 23:02:42 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-03 23:01:34 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-03 23:00:39 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 23:01:43 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 23:00:46 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:52 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 23:03:43 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-03 23:00:35 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-03 23:17:08 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-03 23:02:10 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:22 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-03 21:02:57 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-03 23:07:33 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-03 23:03:48 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.043 |  |
| 2026-08-03 23:05:54 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.051 |  |
| 2026-08-03 23:13:30 | Magura (Kalu Ganga) | 3.29 | 🟢 Normal | -0.058 |  |
| 2026-08-03 18:00:23 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.070 |  |
| 2026-08-03 23:02:14 | Thawalama (Gin Ganga) | 3.71 | 🟢 Normal | -0.089 |  |
| 2026-08-03 23:02:11 | Deraniyagala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.100 |  |
| 2026-08-03 23:03:38 | Holombuwa (Kelani Ganga) | 1.58 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)