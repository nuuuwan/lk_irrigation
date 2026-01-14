# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--14_22:11:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **45,717 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 22:11:56 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-14 22:11:20 | Peradeniya (Mahaweli Ganga) | 2.25 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-01-14 22:09:50 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-14 22:09:19 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:08:44 | Manampitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.027 |  |
| 2026-01-14 22:06:56 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:06:45 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:06:32 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | -0.019 |  |
| 2026-01-14 22:06:21 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:06:04 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:05:42 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | 0.265 | 🔺 Rising |
| 2026-01-14 22:05:30 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-14 22:05:28 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-14 22:05:26 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2026-01-14 22:05:26 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-14 22:04:46 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:04:32 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.360 |  |
| 2026-01-14 22:04:28 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.020 |  |
| 2026-01-14 22:04:01 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:04:00 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-01-14 22:03:23 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-01-14 22:02:51 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:02:51 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:02:39 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.021 |  |
| 2026-01-14 22:01:54 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:01:49 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-14 22:01:40 | Yaka Wewa (Ma Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:01:39 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:01:38 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:01:20 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:01:17 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:00:58 | Horowpothana (Yan Oya) | 2.74 | 🟢 Normal | -0.065 |  |
| 2026-01-14 22:00:51 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:00:36 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 22:05:42 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | 0.265 | 🔺 Rising |
| 2026-01-14 22:11:20 | Peradeniya (Mahaweli Ganga) | 2.25 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-01-14 21:11:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-01-14 22:05:28 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-14 22:09:50 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-14 22:01:49 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-14 22:05:26 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-14 22:11:56 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-14 18:00:19 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:02:51 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:01:54 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:01:38 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:01:40 | Yaka Wewa (Ma Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:02:51 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:02:43 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:04:01 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:01:20 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:00:51 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:00:36 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:06:56 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:06:21 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:04:46 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:01:39 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:09:19 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:06:45 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:06:04 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:01:17 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-14 22:05:30 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-14 21:01:24 | Siyambalanduwa (Heda Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-14 22:04:00 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-01-14 22:03:23 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-01-14 22:06:32 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | -0.019 |  |
| 2026-01-14 18:02:52 | Thanthirimale (Malwathu Oya) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-01-14 22:04:28 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.020 |  |
| 2026-01-14 22:05:26 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2026-01-14 22:02:39 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.021 |  |
| 2026-01-14 22:08:44 | Manampitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.027 |  |
| 2026-01-14 22:00:58 | Horowpothana (Yan Oya) | 2.74 | 🟢 Normal | -0.065 |  |
| 2026-01-14 22:04:32 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.360 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)