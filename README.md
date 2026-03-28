# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_00:25:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **110,092 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-29 00:25:44 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:23:32 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:09:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:08:45 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:07:01 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-29 00:06:13 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:06:09 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:05:48 | Thawalama (Gin Ganga) | 0.78 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-29 00:05:28 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:04:30 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.031 |  |
| 2026-03-29 00:03:56 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-03-29 00:03:39 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:03:23 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-29 00:03:17 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:03:16 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.040 |  |
| 2026-03-29 00:02:55 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:02:53 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:02:37 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:02:37 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:02:32 | Horowpothana (Yan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:02:27 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:02:27 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-29 00:02:24 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:01:48 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-03-29 00:01:46 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:01:43 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:01:42 | Rathnapura (Kalu Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 00:01:38 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:01:38 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:01:34 | Ellagawa (Kalu Ganga) | 3.65 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-28 23:02:34 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.900 | 🔺 Rising |
| 2026-03-29 00:03:56 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-03-29 00:02:27 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-29 00:05:48 | Thawalama (Gin Ganga) | 0.78 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-29 00:01:48 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-03-29 00:01:42 | Rathnapura (Kalu Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 00:07:01 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-29 00:06:09 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:02:37 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:25:44 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:01:38 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:02:53 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:02:32 | Horowpothana (Yan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-28 18:03:02 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-28 23:03:22 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-28 22:34:25 | Pitabeddara (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:08:45 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:01:34 | Ellagawa (Kalu Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:05:28 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:03:39 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:03:17 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | 0.000 |  |
| 2026-03-28 23:18:37 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:01:43 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:02:24 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:01:46 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:02:55 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:02:27 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:06:13 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-28 18:04:13 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:23:32 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:01:38 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:02:37 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:09:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 00:03:23 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-28 22:03:36 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-03-29 00:04:30 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.031 |  |
| 2026-03-28 23:08:07 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.031 |  |
| 2026-03-29 00:03:16 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.040 |  |
| 2026-03-28 18:02:29 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.215 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)