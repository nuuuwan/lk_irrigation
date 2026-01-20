# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--21_01:32:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **51,218 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 01:32:07 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-01-21 01:25:40 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:22:38 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-21 01:12:39 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:11:37 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-21 01:07:51 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:07:20 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:06:29 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:05:28 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:04:50 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:04:03 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:03:37 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:03:23 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:03:20 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-01-21 01:03:06 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-01-21 01:02:48 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:02:47 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:02:47 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.272 | 🔺 Rising |
| 2026-01-21 01:02:45 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:02:42 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:02:39 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-01-21 01:02:29 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:02:12 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:02:03 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:01:46 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:01:13 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 01:01:01 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:00:58 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:00:51 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 01:02:47 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.272 | 🔺 Rising |
| 2026-01-21 01:03:06 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-01-21 01:32:07 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-01-21 01:02:39 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-01-21 00:04:35 | Peradeniya (Mahaweli Ganga) | 2.53 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-01-21 01:22:38 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-21 01:11:37 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-20 18:00:20 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-21 01:01:13 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 01:00:51 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:02:47 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:02:45 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:01:46 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:02:42 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:02:25 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-20 18:01:04 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:04:03 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:02:48 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:02:29 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:09:27 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:00:58 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:04:50 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:01:01 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:02:12 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:02:03 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-20 21:01:57 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:25:40 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:03:37 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:05:28 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:10:03 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-20 18:01:15 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:12:39 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:06:29 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-21 01:07:20 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-20 21:10:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-21 00:02:13 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.019 |  |
| 2026-01-21 01:03:20 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-01-21 00:04:34 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.041 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)