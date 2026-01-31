# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--31_13:29:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **60,649 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 13:29:08 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.007 |  |
| 2026-01-31 13:24:29 | Thawalama (Gin Ganga) | 0.88 | 🟢 Normal | -0.015 |  |
| 2026-01-31 13:17:16 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:14:58 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-31 13:10:58 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:08:14 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:08:09 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:07:09 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:06:56 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:06:39 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-31 13:06:36 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:06:30 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:06:19 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:06:10 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:05:43 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:05:32 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-01-31 13:05:29 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.029 |  |
| 2026-01-31 13:04:51 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:04:47 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:04:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | -0.039 |  |
| 2026-01-31 13:04:25 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-31 13:04:22 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-01-31 13:03:51 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:03:42 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | -0.137 |  |
| 2026-01-31 13:03:38 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 13:03:33 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-01-31 13:03:17 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:03:14 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-31 13:03:13 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:03:13 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:02:44 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-01-31 13:02:20 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-31 13:02:13 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:02:04 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.103 |  |
| 2026-01-31 13:01:50 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-31 13:01:16 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-01-31 13:00:57 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:00:43 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-31 13:00:13 | Weraganthota (Mahaweli Ganga) | -1.59 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 13:01:16 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-01-31 13:05:32 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-01-31 13:01:50 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-31 13:04:25 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-31 13:02:20 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-31 13:03:38 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 13:06:39 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-31 13:14:58 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-31 13:03:13 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:03:17 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:06:56 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:10:58 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:04:47 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:06:19 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:08:09 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:02:13 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:03:13 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:04:51 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:05:43 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:07:09 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:06:30 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:03:51 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:08:14 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:17:16 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:00:57 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:06:36 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:06:10 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-31 13:29:08 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.007 |  |
| 2026-01-31 13:03:14 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-31 13:02:44 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-01-31 13:00:43 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-31 13:24:29 | Thawalama (Gin Ganga) | 0.88 | 🟢 Normal | -0.015 |  |
| 2026-01-31 13:04:22 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-01-31 13:03:33 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-01-31 13:00:13 | Weraganthota (Mahaweli Ganga) | -1.59 | 🟢 Normal | -0.020 |  |
| 2026-01-31 13:05:29 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.029 |  |
| 2026-01-31 13:04:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | -0.039 |  |
| 2026-01-31 13:02:04 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.103 |  |
| 2026-01-31 13:03:42 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | -0.137 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)