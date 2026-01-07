# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--08_03:16:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **39,610 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 03:16:05 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:14:04 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:11:23 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:10:47 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:10:46 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-01-08 03:10:30 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | -0.009 |  |
| 2026-01-08 03:07:19 | Panadugama (Nilwala Ganga) | 3.96 | 🟢 Normal | 198.000 | 🔺 Rising |
| 2026-01-08 03:07:17 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 198.000 | 🔺 Rising |
| 2026-01-08 03:07:04 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:06:39 | Pitabeddara (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.195 |  |
| 2026-01-08 03:06:37 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:06:08 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.032 |  |
| 2026-01-08 03:05:49 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:05:29 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:05:16 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 03:05:04 | Katharagama (Menik Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:05:02 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-01-08 03:04:58 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-01-08 03:04:33 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-01-08 03:04:13 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-01-08 03:04:03 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:03:51 | Peradeniya (Mahaweli Ganga) | 2.23 | 🟢 Normal | -0.283 |  |
| 2026-01-08 03:03:50 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:03:27 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:02:37 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.005 |  |
| 2026-01-08 03:02:33 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:02:23 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:02:19 | Siyambalanduwa (Heda Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:02:15 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-08 03:02:13 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -1.161 |  |
| 2026-01-08 03:02:11 | Padiyathalawa (Maduru Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:01:42 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -1.161 |  |
| 2026-01-08 03:01:35 | Manampitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -8.780 |  |
| 2026-01-08 03:00:57 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:00:54 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -8.780 |  |
| 2026-01-08 03:00:54 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.005 |  |
| 2026-01-08 02:22:15 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-08 02:21:46 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 03:07:19 | Panadugama (Nilwala Ganga) | 3.96 | 🟢 Normal | 198.000 | 🔺 Rising |
| 2026-01-08 03:05:02 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-01-08 03:04:13 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-01-08 03:04:33 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-01-08 01:08:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-01-08 03:10:46 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-01-07 18:01:49 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 03:05:16 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 03:00:54 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.005 |  |
| 2026-01-08 03:02:23 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:06:37 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:02:33 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:07:04 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:00:57 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:04:03 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:01:21 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-08 02:04:25 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:03:50 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:02:11 | Padiyathalawa (Maduru Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:05:49 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:02:19 | Siyambalanduwa (Heda Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:16:05 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:05:04 | Katharagama (Menik Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:14:04 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:11:23 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:05:29 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:10:47 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-08 01:55:48 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-08 03:02:37 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.005 |  |
| 2026-01-08 03:10:30 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | -0.009 |  |
| 2026-01-08 01:02:08 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | -0.009 |  |
| 2026-01-08 03:02:15 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-07 18:03:25 | Thanthirimale (Malwathu Oya) | 1.77 | 🟢 Normal | -0.023 |  |
| 2026-01-08 03:06:08 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.032 |  |
| 2026-01-08 03:06:39 | Pitabeddara (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.195 |  |
| 2026-01-08 03:03:51 | Peradeniya (Mahaweli Ganga) | 2.23 | 🟢 Normal | -0.283 |  |
| 2026-01-08 03:02:13 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -1.161 |  |
| 2026-01-08 03:01:35 | Manampitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -8.780 |  |
| 2026-01-08 02:05:23 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | -9.333 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)