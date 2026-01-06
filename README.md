# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--07_02:12:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,679 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 02:12:19 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.025 |  |
| 2026-01-07 02:10:36 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-01-07 02:10:34 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-01-07 02:08:50 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-07 02:08:39 | Manampitiya (Mahaweli Ganga) | 3.51 | 🟡 Alert | -0.075 |  |
| 2026-01-07 02:08:05 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:07:41 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:07:41 | Siyambalanduwa (Heda Oya) | 2.18 | 🟢 Normal | -0.103 |  |
| 2026-01-07 02:07:19 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:06:56 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-01-07 02:05:54 | Katharagama (Menik Ganga) | 0.68 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-01-07 02:05:44 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:05:42 | Peradeniya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.171 |  |
| 2026-01-07 02:04:56 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.006 |  |
| 2026-01-07 02:04:18 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:04:08 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:03:56 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:03:50 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:03:36 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.102 |  |
| 2026-01-07 02:03:23 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:03:18 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:03:09 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:03:05 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -1.125 |  |
| 2026-01-07 02:02:34 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:02:33 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -1.125 |  |
| 2026-01-07 02:02:06 | Nakkala (Kumbukkan Oya) | 1.58 | 🟢 Normal | -0.022 |  |
| 2026-01-07 02:01:59 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 02:01:23 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-01-07 02:01:17 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:00:40 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-01-07 02:00:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-01-07 02:00:31 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-07 01:48:13 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.025 |  |
| 2026-01-07 01:37:22 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 02:08:39 | Manampitiya (Mahaweli Ganga) | 3.51 | 🟡 Alert | -0.075 |  |
| 2026-01-07 02:10:36 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-01-07 02:01:23 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-01-07 02:05:54 | Katharagama (Menik Ganga) | 0.68 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-01-07 02:00:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-01-07 02:00:40 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-01-07 01:00:37 | Horowpothana (Yan Oya) | 2.89 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-06 18:00:39 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 02:08:50 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-07 01:22:35 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-06 18:02:01 | Weraganthota (Mahaweli Ganga) | -0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 02:01:59 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 02:02:34 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:03:09 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:03:56 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:03:13 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:04:08 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:03:18 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:07:41 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:01:17 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:07:19 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:00:31 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-07 00:03:09 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:03:50 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-07 01:06:25 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:04:18 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:05:44 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:03:23 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:08:05 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:04:56 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.006 |  |
| 2026-01-07 00:29:39 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.015 |  |
| 2026-01-07 02:06:56 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-01-07 02:02:06 | Nakkala (Kumbukkan Oya) | 1.58 | 🟢 Normal | -0.022 |  |
| 2026-01-07 02:12:19 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.025 |  |
| 2026-01-07 00:06:21 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.031 |  |
| 2026-01-07 02:03:36 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.102 |  |
| 2026-01-07 02:07:41 | Siyambalanduwa (Heda Oya) | 2.18 | 🟢 Normal | -0.103 |  |
| 2026-01-07 02:05:42 | Peradeniya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.171 |  |
| 2026-01-07 02:03:05 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -1.125 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)