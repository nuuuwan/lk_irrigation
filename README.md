# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_20:29:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **158,153 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 20:29:25 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-05-21 20:16:06 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:14:14 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:13:11 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | -0.008 |  |
| 2026-05-21 20:11:45 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-05-21 20:10:45 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-05-21 20:10:32 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-21 20:10:04 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:08:33 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | -0.038 |  |
| 2026-05-21 20:08:05 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-21 20:06:46 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-05-21 20:06:32 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:06:10 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:05:03 | Deraniyagala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.225 |  |
| 2026-05-21 20:04:51 | Rathnapura (Kalu Ganga) | 2.07 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-05-21 20:04:48 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-21 20:04:42 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-21 20:04:39 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-21 20:04:30 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-05-21 20:04:17 | Hanwella (Kelani Ganga) | 1.63 | 🟢 Normal | -0.030 |  |
| 2026-05-21 20:04:12 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:03:35 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:03:26 | Ellagawa (Kalu Ganga) | 5.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 20:03:20 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 20:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-21 20:02:33 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:02:25 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:02:24 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.093 |  |
| 2026-05-21 20:02:08 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:01:50 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 20:01:22 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-21 20:01:13 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:01:11 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 20:01:01 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 20:04:51 | Rathnapura (Kalu Ganga) | 2.07 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-05-21 20:04:42 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-21 20:01:22 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-21 20:04:39 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-21 20:10:32 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-21 20:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-21 20:08:05 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-21 20:01:11 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 20:03:26 | Ellagawa (Kalu Ganga) | 5.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 20:01:50 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 20:03:20 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 18:16:06 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-21 20:29:25 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-05-21 20:06:10 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:00:29 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:01:01 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:16:06 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:02:33 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:03:27 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:06:32 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:01:13 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:04:12 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:03:35 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:02:25 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:02:08 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:14:14 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:10:04 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:00:14 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-21 20:13:11 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | -0.008 |  |
| 2026-05-21 20:10:45 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-05-21 20:04:30 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-05-21 20:06:46 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-05-21 20:04:48 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-21 20:11:45 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-05-21 20:04:17 | Hanwella (Kelani Ganga) | 1.63 | 🟢 Normal | -0.030 |  |
| 2026-05-21 20:08:33 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | -0.038 |  |
| 2026-05-21 18:01:04 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | -0.040 |  |
| 2026-05-21 20:02:24 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.093 |  |
| 2026-05-21 20:05:03 | Deraniyagala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.225 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)