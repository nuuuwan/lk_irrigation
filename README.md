# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--23_03:05:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **53,087 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-23 03:05:49 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:05:39 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-23 03:05:28 | Manampitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.005 |  |
| 2026-01-23 03:05:04 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:04:48 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.057 |  |
| 2026-01-23 03:04:46 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:04:12 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.003 |  |
| 2026-01-23 03:04:06 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:03:59 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:03:58 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:03:51 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.009 |  |
| 2026-01-23 03:03:31 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:03:30 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:02:51 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:02:34 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:02:25 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:02:14 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.350 |  |
| 2026-01-23 03:02:12 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:01:50 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:01:48 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:01:41 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-01-23 03:01:01 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:00:57 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-23 02:58:28 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-23 02:15:05 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 1.895 | 🔺 Rising |
| 2026-01-23 02:12:15 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.057 |  |
| 2026-01-23 02:10:49 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 02:10:48 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 02:10:46 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 02:10:45 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-23 02:15:05 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 1.895 | 🔺 Rising |
| 2026-01-23 03:01:41 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-01-23 02:58:28 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-23 02:02:38 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-01-23 03:05:39 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-23 03:04:12 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.003 |  |
| 2026-01-23 01:01:18 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:03:30 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-23 02:03:51 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:02:51 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:01:48 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:07:08 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:02:34 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 02:10:49 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:03:31 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:00:57 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:05:49 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:03:59 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:02:12 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:01:50 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:01:01 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-23 00:05:08 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:04:06 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:05:04 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-23 02:05:13 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:01:34 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-23 01:01:30 | Thawalama (Gin Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:02:25 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:04:46 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-23 03:05:28 | Manampitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.005 |  |
| 2026-01-23 03:03:51 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.009 |  |
| 2026-01-23 02:06:23 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-01-22 21:04:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | -0.026 |  |
| 2026-01-23 01:03:57 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.031 |  |
| 2026-01-22 18:00:06 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | -0.050 |  |
| 2026-01-23 03:04:48 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.057 |  |
| 2026-01-23 02:03:13 | Peradeniya (Mahaweli Ganga) | 2.14 | 🟢 Normal | -0.060 |  |
| 2026-01-23 03:02:14 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.350 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)