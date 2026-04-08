# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_02:12:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **119,992 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 02:12:50 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-09 02:10:44 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.400 | 🔺 Rising |
| 2026-04-09 02:10:09 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-09 02:09:28 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.005 |  |
| 2026-04-09 02:08:44 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-09 02:08:42 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.027 |  |
| 2026-04-09 02:05:43 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 02:05:18 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.028 |  |
| 2026-04-09 02:04:11 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-04-09 02:04:09 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-04-09 02:03:43 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-04-09 02:02:49 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-09 02:02:45 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.352 |  |
| 2026-04-09 02:02:29 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.050 |  |
| 2026-04-09 02:02:01 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-09 02:01:59 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-09 02:01:28 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-04-09 02:01:12 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-09 02:00:52 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | -0.005 |  |
| 2026-04-09 02:00:37 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 02:00:33 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-04-09 02:00:32 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.467 | 🔺 Rising |
| 2026-04-09 02:00:23 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.112 |  |
| 2026-04-09 01:58:41 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 01:52:49 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.467 | 🔺 Rising |
| 2026-04-09 01:23:46 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 01:01:50 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-04-08 18:05:20 | Weraganthota (Mahaweli Ganga) | 3.20 | 🟢 Normal | 5.983 | 🔺 Rising |
| 2026-04-09 01:12:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.22 | 🟢 Normal | 3.086 | 🔺 Rising |
| 2026-04-09 02:00:32 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.467 | 🔺 Rising |
| 2026-04-09 02:10:44 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.400 | 🔺 Rising |
| 2026-04-09 02:00:33 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-04-09 01:00:51 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-09 02:10:09 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-08 22:15:22 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 01:04:03 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 02:09:28 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.005 |  |
| 2026-04-09 02:05:43 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 02:00:37 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 02:04:09 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-04-09 02:02:01 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:02:48 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-09 01:12:57 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-09 00:01:59 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-09 02:01:28 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-04-09 02:12:50 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-09 00:36:09 | Panadugama (Nilwala Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-09 02:01:12 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-09 01:23:46 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-09 02:01:59 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-09 02:08:44 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-09 02:02:49 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-09 01:02:41 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-09 02:04:11 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-04-09 00:06:37 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-09 02:00:52 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | -0.005 |  |
| 2026-04-08 18:02:20 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-09 02:03:43 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-04-09 00:00:34 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-04-09 02:08:42 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.027 |  |
| 2026-04-09 02:05:18 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.028 |  |
| 2026-04-09 02:02:29 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.050 |  |
| 2026-04-08 23:03:56 | Putupaula (Kalu Ganga) | 0.21 | 🟢 Normal | -0.098 |  |
| 2026-04-09 02:00:23 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.112 |  |
| 2026-04-09 02:02:45 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.352 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)