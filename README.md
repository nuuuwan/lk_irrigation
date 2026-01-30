# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--30_23:11:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **60,126 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-30 23:11:22 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:10:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.20 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-30 23:10:18 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-30 23:08:23 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:07:51 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 23:06:57 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.029 |  |
| 2026-01-30 23:06:55 | Manampitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-30 23:06:34 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.462 |  |
| 2026-01-30 23:06:33 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:06:17 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:05:30 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | -1.072 |  |
| 2026-01-30 23:05:16 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.462 |  |
| 2026-01-30 23:04:50 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:04:40 | Padiyathalawa (Maduru Oya) | 1.12 | 🟢 Normal | -0.031 |  |
| 2026-01-30 23:04:21 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:04:21 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:03:55 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:03:45 | Peradeniya (Mahaweli Ganga) | 1.87 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-01-30 23:03:08 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:02:39 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:02:39 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:02:26 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-30 23:02:23 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:02:12 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | -0.010 |  |
| 2026-01-30 23:01:48 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:01:38 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:01:36 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:01:25 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-30 23:01:20 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:01:10 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:01:09 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-30 23:00:36 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:00:35 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 23:00:15 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:25:08 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:21:14 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-30 23:03:45 | Peradeniya (Mahaweli Ganga) | 1.87 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-01-30 23:01:25 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-30 23:10:18 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-30 23:10:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.20 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-30 23:01:09 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-30 23:02:26 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-30 18:02:48 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 23:00:35 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 23:07:51 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 23:06:55 | Manampitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-30 23:01:20 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:00:15 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:02:39 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:01:36 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:04:24 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:01:38 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:02:17 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:00:36 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-30 18:03:49 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:11:15 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:06:17 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:02:23 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:03:08 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:08:23 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:01:48 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:06:33 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:04:50 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:02:39 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:11:22 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-30 18:02:10 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:25:08 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:04:21 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:01:10 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:03:55 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-30 23:02:12 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | -0.010 |  |
| 2026-01-30 23:06:57 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.029 |  |
| 2026-01-30 23:04:40 | Padiyathalawa (Maduru Oya) | 1.12 | 🟢 Normal | -0.031 |  |
| 2026-01-30 23:06:34 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.462 |  |
| 2026-01-30 23:05:30 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | -1.072 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)