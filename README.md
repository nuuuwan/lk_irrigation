# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--09_10:18:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **40,790 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 10:18:04 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.008 |  |
| 2026-01-09 10:17:10 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.016 |  |
| 2026-01-09 10:12:45 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | -0.010 |  |
| 2026-01-09 10:06:44 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:06:32 | Manampitiya (Mahaweli Ganga) | 2.47 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-09 10:06:29 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:06:08 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:05:40 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-01-09 10:05:25 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-09 10:04:29 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:04:12 | Horowpothana (Yan Oya) | 2.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 10:03:47 | Siyambalanduwa (Heda Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-09 10:03:42 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-09 10:03:37 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-01-09 10:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.049 |  |
| 2026-01-09 10:03:23 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:03:13 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:03:09 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.231 |  |
| 2026-01-09 10:03:08 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-01-09 10:03:06 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 10:02:54 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:02:52 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.022 |  |
| 2026-01-09 10:02:48 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:02:45 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:02:26 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.118 |  |
| 2026-01-09 10:02:15 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:02:13 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:02:06 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:01:57 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 10:01:41 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | -0.010 |  |
| 2026-01-09 10:01:29 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.130 |  |
| 2026-01-09 10:01:10 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:01:07 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:01:07 | Moragaswewa (Deduru Oya) | 2.50 | 🟢 Normal | -0.100 |  |
| 2026-01-09 10:00:43 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:00:12 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 10:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-09 10:00:09 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 10:06:32 | Manampitiya (Mahaweli Ganga) | 2.47 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-09 10:05:25 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-09 10:04:12 | Horowpothana (Yan Oya) | 2.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 10:03:06 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 10:00:12 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 10:01:57 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 10:02:45 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:03:13 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:02:54 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:01:10 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:02:06 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:02:48 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:06:44 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:00:43 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:02:13 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:06:29 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:06:08 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:04:29 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:01:07 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:03:23 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:02:15 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 10:18:04 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.008 |  |
| 2026-01-09 10:12:45 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | -0.010 |  |
| 2026-01-09 10:03:47 | Siyambalanduwa (Heda Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-09 10:05:40 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-01-09 10:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-09 10:03:42 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-09 10:01:41 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | -0.010 |  |
| 2026-01-09 10:00:09 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-01-09 10:03:08 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-01-09 10:17:10 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.016 |  |
| 2026-01-09 10:03:37 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-01-09 09:07:09 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.022 |  |
| 2026-01-09 10:02:52 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.022 |  |
| 2026-01-09 10:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.049 |  |
| 2026-01-09 10:01:07 | Moragaswewa (Deduru Oya) | 2.50 | 🟢 Normal | -0.100 |  |
| 2026-01-09 10:02:26 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.118 |  |
| 2026-01-09 10:01:29 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.130 |  |
| 2026-01-09 10:03:09 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.231 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)