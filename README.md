# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_21:07:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,115 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 21:07:55 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-03 21:07:54 | Holombuwa (Kelani Ganga) | 2.00 | 🟢 Normal | -0.362 |  |
| 2026-08-03 21:07:26 | Magura (Kalu Ganga) | 3.29 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-08-03 21:07:16 | Rathnapura (Kalu Ganga) | 8.16 | 🟠 Minor Flood | -0.069 |  |
| 2026-08-03 21:06:47 | Pitabeddara (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-08-03 21:05:58 | Panadugama (Nilwala Ganga) | 4.38 | 🟢 Normal | 0.389 | 🔺 Rising |
| 2026-08-03 21:05:44 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-08-03 21:05:34 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-03 21:05:05 | Glencourse (Kelani Ganga) | 16.43 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2026-08-03 21:04:25 | Deraniyagala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.447 |  |
| 2026-08-03 21:04:25 | Hanwella (Kelani Ganga) | 6.57 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-08-03 21:04:13 | Giriulla (Maha Oya) | 4.20 | 🟢 Normal | 0.978 | 🔺 Rising |
| 2026-08-03 21:04:11 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-03 21:03:34 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.025 |  |
| 2026-08-03 21:03:34 | Ellagawa (Kalu Ganga) | 8.07 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-03 21:03:24 | Putupaula (Kalu Ganga) | 1.61 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-03 21:03:18 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-03 21:03:17 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-03 21:03:14 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-08-03 21:03:06 | Nawalapitiya (Mahaweli Ganga) | 4.80 | 🟡 Alert | -0.133 |  |
| 2026-08-03 21:03:05 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-03 21:02:57 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-03 21:02:48 | Thawalama (Gin Ganga) | 3.85 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-08-03 21:02:21 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-08-03 21:02:08 | Peradeniya (Mahaweli Ganga) | 9.05 | 🔴 Major Flood | -0.356 |  |
| 2026-08-03 21:01:59 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-08-03 21:01:35 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 21:01:20 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-03 21:00:40 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 21:00:38 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-03 21:00:35 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-03 20:59:08 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 20:31:05 | Magura (Kalu Ganga) | 3.17 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-08-03 20:19:42 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-03 20:17:53 | Nawalapitiya (Mahaweli Ganga) | 4.90 | 🟡 Alert | -0.133 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 21:02:08 | Peradeniya (Mahaweli Ganga) | 9.05 | 🔴 Major Flood | -0.356 |  |
| 2026-08-03 21:07:16 | Rathnapura (Kalu Ganga) | 8.16 | 🟠 Minor Flood | -0.069 |  |
| 2026-08-03 21:05:05 | Glencourse (Kelani Ganga) | 16.43 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2026-08-03 20:06:24 | Kithulgala (Kelani Ganga) | 3.15 | 🟡 Alert | 0.093 | 🔺 Rising |
| 2026-08-03 19:08:44 | Norwood (Kelani Ganga) | 2.23 | 🟡 Alert | -0.099 |  |
| 2026-08-03 21:03:06 | Nawalapitiya (Mahaweli Ganga) | 4.80 | 🟡 Alert | -0.133 |  |
| 2026-08-03 21:04:13 | Giriulla (Maha Oya) | 4.20 | 🟢 Normal | 0.978 | 🔺 Rising |
| 2026-08-03 21:05:58 | Panadugama (Nilwala Ganga) | 4.38 | 🟢 Normal | 0.389 | 🔺 Rising |
| 2026-08-03 21:04:25 | Hanwella (Kelani Ganga) | 6.57 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-08-03 21:07:26 | Magura (Kalu Ganga) | 3.29 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-08-03 21:06:47 | Pitabeddara (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-08-03 21:02:48 | Thawalama (Gin Ganga) | 3.85 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-08-03 21:01:59 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-08-03 20:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.66 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-03 21:03:34 | Ellagawa (Kalu Ganga) | 8.07 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-03 21:03:24 | Putupaula (Kalu Ganga) | 1.61 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-03 21:07:55 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-03 21:00:35 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-03 21:03:17 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-03 21:00:40 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 21:01:35 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 20:59:08 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:52 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 21:00:38 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-03 21:02:21 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-08-03 21:04:11 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-03 21:03:18 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-03 21:03:05 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:22 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-03 21:02:57 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-03 21:01:20 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-03 21:05:34 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-03 21:03:14 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-08-03 21:03:34 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.025 |  |
| 2026-08-03 21:05:44 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-08-03 18:00:23 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.070 |  |
| 2026-08-03 20:05:09 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | -0.089 |  |
| 2026-08-03 21:07:54 | Holombuwa (Kelani Ganga) | 2.00 | 🟢 Normal | -0.362 |  |
| 2026-08-03 21:04:25 | Deraniyagala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.447 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)