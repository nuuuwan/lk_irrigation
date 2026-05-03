# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_02:13:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **142,254 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 02:13:22 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-05-04 02:07:45 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-05-04 02:06:36 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:06:26 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.005 |  |
| 2026-05-04 02:06:09 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:04:44 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:04:32 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-04 02:04:06 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-04 02:03:24 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-05-04 02:02:49 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:02:35 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-05-04 02:02:24 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-05-04 02:02:10 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:01:53 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 3.724 | 🔺 Rising |
| 2026-05-04 02:01:52 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.015 |  |
| 2026-05-04 02:01:50 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:01:42 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:01:39 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:01:28 | Moragaswewa (Deduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:01:24 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 3.724 | 🔺 Rising |
| 2026-05-04 02:01:19 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:00:45 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-05-04 02:00:42 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:00:07 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-04 01:47:29 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-04 01:47:27 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-04 01:43:14 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-04 01:37:46 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-04 01:23:42 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.080 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 02:01:53 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 3.724 | 🔺 Rising |
| 2026-05-04 02:13:22 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-05-04 02:07:45 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-05-04 01:23:42 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-04 02:04:06 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-04 01:01:14 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-04 02:04:32 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-03 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-04 01:37:46 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-04 02:01:42 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:01:28 | Moragaswewa (Deduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:01:39 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:06:09 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:01:35 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 01:43:14 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-04 01:47:29 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:04:44 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:02:49 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 01:02:07 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:00:07 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:02:10 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-04 01:04:22 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-04 00:09:53 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:01:50 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-04 01:00:42 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:00:54 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:00:42 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-04 01:04:57 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:01:19 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:06:36 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:06:26 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.005 |  |
| 2026-05-04 02:02:24 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-05-04 02:00:45 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-05-04 02:01:52 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.015 |  |
| 2026-05-04 02:02:35 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-05-04 02:03:24 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-05-04 01:04:54 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | -0.023 |  |
| 2026-05-03 21:04:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | -0.031 |  |
| 2026-05-04 01:17:18 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.044 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)