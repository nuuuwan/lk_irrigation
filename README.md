# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_03:18:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **120,025 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 03:18:37 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:18:13 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 3.000 | 🔺 Rising |
| 2026-04-09 03:17:49 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 3.000 | 🔺 Rising |
| 2026-04-09 03:12:43 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:10:59 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.003 |  |
| 2026-04-09 03:09:25 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.019 |  |
| 2026-04-09 03:06:50 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:06:49 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -2.323 |  |
| 2026-04-09 03:06:27 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.019 |  |
| 2026-04-09 03:06:23 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-09 03:06:18 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -2.323 |  |
| 2026-04-09 03:06:17 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:05:44 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -2.323 |  |
| 2026-04-09 03:05:37 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-04-09 03:05:30 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:04:51 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:04:05 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.068 |  |
| 2026-04-09 03:03:49 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:03:42 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:03:28 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-09 03:03:23 | Panadugama (Nilwala Ganga) | 1.76 | 🟢 Normal | -0.004 |  |
| 2026-04-09 03:03:21 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:03:13 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-04-09 03:03:11 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:02:48 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-04-09 03:01:55 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-04-09 03:01:44 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:01:42 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.023 |  |
| 2026-04-09 03:01:41 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:01:34 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.118 |  |
| 2026-04-09 03:01:04 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | 0.327 | 🔺 Rising |
| 2026-04-09 02:44:05 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.082 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 01:01:50 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-04-08 18:05:20 | Weraganthota (Mahaweli Ganga) | 3.20 | 🟢 Normal | 5.983 | 🔺 Rising |
| 2026-04-09 01:12:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.22 | 🟢 Normal | 3.086 | 🔺 Rising |
| 2026-04-09 03:18:13 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 3.000 | 🔺 Rising |
| 2026-04-09 03:01:04 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | 0.327 | 🔺 Rising |
| 2026-04-09 03:06:23 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-09 03:03:28 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-09 02:10:09 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-09 01:04:03 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 03:10:59 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.003 |  |
| 2026-04-09 02:05:43 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:06:50 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:12:43 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:03:21 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:01:41 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:02:48 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-09 01:12:57 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-09 00:01:59 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-09 02:01:28 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:05:30 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:01:44 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:18:37 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:03:42 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:04:51 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:03:49 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:06:17 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:03:23 | Panadugama (Nilwala Ganga) | 1.76 | 🟢 Normal | -0.004 |  |
| 2026-04-08 18:02:20 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-09 03:03:13 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-04-09 03:05:37 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-04-09 03:09:25 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.019 |  |
| 2026-04-09 03:06:27 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.019 |  |
| 2026-04-09 03:01:55 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-04-09 03:02:48 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-04-09 03:01:42 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.023 |  |
| 2026-04-09 03:04:05 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.068 |  |
| 2026-04-08 23:03:56 | Putupaula (Kalu Ganga) | 0.21 | 🟢 Normal | -0.098 |  |
| 2026-04-09 03:01:34 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.118 |  |
| 2026-04-09 03:06:49 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -2.323 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)