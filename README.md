# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_18:15:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **124,159 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 18:15:55 | Pitabeddara (Nilwala Ganga) | 2.05 | 🟢 Normal | 12.349 | 🔺 Rising |
| 2026-04-13 18:14:53 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-13 18:13:53 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:11:30 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:10:02 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-13 18:08:32 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | -0.041 |  |
| 2026-04-13 18:08:07 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-13 18:07:19 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 12.349 | 🔺 Rising |
| 2026-04-13 18:07:11 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 18:06:24 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:06:09 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:05:59 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:05:47 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.031 |  |
| 2026-04-13 18:05:46 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:05:44 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:05:23 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:05:18 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.057 |  |
| 2026-04-13 18:05:17 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:04:19 | Rathnapura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.198 |  |
| 2026-04-13 18:04:18 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:04:03 | Ellagawa (Kalu Ganga) | 5.59 | 🟢 Normal | -0.089 |  |
| 2026-04-13 18:03:57 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:03:51 | Katharagama (Menik Ganga) | -0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:03:40 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.010 |  |
| 2026-04-13 18:03:15 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.368 |  |
| 2026-04-13 18:02:49 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:02:38 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-13 18:02:37 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.089 |  |
| 2026-04-13 18:02:29 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:02:18 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | -0.041 |  |
| 2026-04-13 18:02:11 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2026-04-13 18:01:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.31 | 🟢 Normal | -0.041 |  |
| 2026-04-13 18:01:19 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:01:08 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-04-13 18:01:02 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 18:00:57 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.022 |  |
| 2026-04-13 18:00:56 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.429 | 🔺 Rising |
| 2026-04-13 18:00:11 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.054 |  |
| 2026-04-13 18:00:10 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.178 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 18:15:55 | Pitabeddara (Nilwala Ganga) | 2.05 | 🟢 Normal | 12.349 | 🔺 Rising |
| 2026-04-13 18:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.429 | 🔺 Rising |
| 2026-04-13 18:02:11 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2026-04-13 18:00:10 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-04-13 18:01:08 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-04-13 18:08:07 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-13 18:02:38 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-13 18:14:53 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-13 18:07:11 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 18:10:02 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-13 18:01:02 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 18:04:18 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-13 16:01:53 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:05:44 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:02:29 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:05:17 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:01:19 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:06:24 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:05:46 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:06:09 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:02:49 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:05:23 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:03:51 | Katharagama (Menik Ganga) | -0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:05:59 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:13:53 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:03:40 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.010 |  |
| 2026-04-13 17:02:13 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.011 |  |
| 2026-04-13 18:00:57 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.022 |  |
| 2026-04-13 18:05:47 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.031 |  |
| 2026-04-13 17:04:16 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.034 |  |
| 2026-04-13 18:02:18 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | -0.041 |  |
| 2026-04-13 18:01:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.31 | 🟢 Normal | -0.041 |  |
| 2026-04-13 18:08:32 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | -0.041 |  |
| 2026-04-13 18:00:11 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.054 |  |
| 2026-04-13 18:05:18 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.057 |  |
| 2026-04-13 18:04:03 | Ellagawa (Kalu Ganga) | 5.59 | 🟢 Normal | -0.089 |  |
| 2026-04-13 18:02:37 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.089 |  |
| 2026-04-13 18:04:19 | Rathnapura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.198 |  |
| 2026-04-13 18:03:15 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.368 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)