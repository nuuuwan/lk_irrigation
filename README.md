# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_07:12:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **118,393 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 07:12:32 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:11:21 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:08:32 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | -0.011 |  |
| 2026-04-07 07:08:29 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.027 |  |
| 2026-04-07 07:07:50 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.028 |  |
| 2026-04-07 07:07:40 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:05:37 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:05:29 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-04-07 07:04:55 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:04:54 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.028 |  |
| 2026-04-07 07:04:52 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.041 |  |
| 2026-04-07 07:04:32 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:04:29 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:04:02 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-07 07:03:49 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-04-07 07:03:38 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.021 |  |
| 2026-04-07 07:03:33 | Glencourse (Kelani Ganga) | 8.93 | 🟢 Normal | -0.117 |  |
| 2026-04-07 07:02:53 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-07 07:02:48 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-07 07:02:45 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.070 |  |
| 2026-04-07 07:02:37 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.011 |  |
| 2026-04-07 07:02:30 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:02:29 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:02:22 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-07 07:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.215 |  |
| 2026-04-07 07:02:13 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.019 |  |
| 2026-04-07 07:02:04 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:02:03 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:02:03 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 07:02:00 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-07 07:01:36 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.044 |  |
| 2026-04-07 07:01:36 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:01:28 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.132 |  |
| 2026-04-07 07:01:27 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | -0.005 |  |
| 2026-04-07 07:01:21 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.096 |  |
| 2026-04-07 07:00:56 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-04-07 07:00:51 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-07 06:37:19 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.024 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 07:05:29 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-04-07 06:07:36 | Weraganthota (Mahaweli Ganga) | -2.20 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-07 07:02:22 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-07 07:04:02 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-07 07:02:00 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-07 06:04:08 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-07 07:02:53 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-07 07:02:03 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 07:00:51 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:02:03 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:02:29 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:02:04 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:12:32 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:11:21 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:07:40 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:04:32 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:02:30 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:04:55 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:01:36 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:05:37 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:04:29 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:01:27 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | -0.005 |  |
| 2026-04-07 07:03:49 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-04-07 07:00:56 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-04-07 07:02:48 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-07 07:02:37 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.011 |  |
| 2026-04-07 07:08:32 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | -0.011 |  |
| 2026-04-07 07:02:13 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.019 |  |
| 2026-04-07 07:03:38 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.021 |  |
| 2026-04-07 07:08:29 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.027 |  |
| 2026-04-07 07:04:54 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.028 |  |
| 2026-04-07 07:07:50 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.028 |  |
| 2026-04-07 07:04:52 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.041 |  |
| 2026-04-07 07:01:36 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.044 |  |
| 2026-04-07 07:02:45 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.070 |  |
| 2026-04-07 07:01:21 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.096 |  |
| 2026-04-07 07:03:33 | Glencourse (Kelani Ganga) | 8.93 | 🟢 Normal | -0.117 |  |
| 2026-04-07 07:01:28 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.132 |  |
| 2026-04-07 07:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.215 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)