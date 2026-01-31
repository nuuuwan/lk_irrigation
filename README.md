# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--31_07:41:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **60,411 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 07:41:25 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:31:49 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:25:53 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:22:53 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.007 |  |
| 2026-01-31 07:20:35 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:18:24 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:14:50 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:12:24 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:11:54 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:11:21 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:09:01 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | -1.908 |  |
| 2026-01-31 07:08:58 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | -0.001 |  |
| 2026-01-31 07:08:57 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-01-31 07:08:53 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:08:39 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-31 07:08:19 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:07:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-01-31 07:07:26 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:06:32 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:06:28 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.117 |  |
| 2026-01-31 07:04:54 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-31 07:04:42 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:04:26 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-31 07:04:26 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.054 |  |
| 2026-01-31 07:04:25 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.041 |  |
| 2026-01-31 07:04:22 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:04:18 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | -1.908 |  |
| 2026-01-31 07:04:11 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.087 |  |
| 2026-01-31 07:04:09 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:03:39 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:03:19 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-31 07:03:18 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-01-31 07:03:13 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.042 |  |
| 2026-01-31 07:03:13 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-31 07:03:10 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:02:40 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.064 |  |
| 2026-01-31 07:02:25 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-31 07:02:18 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-01-31 07:01:47 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 07:01:45 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.153 |  |
| 2026-01-31 07:01:39 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:01:10 | Padiyathalawa (Maduru Oya) | 1.42 | 🟢 Normal | 0.060 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 07:07:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-01-31 07:03:19 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-31 07:01:10 | Padiyathalawa (Maduru Oya) | 1.42 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-31 07:08:39 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-31 07:04:54 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-31 07:03:13 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-31 07:04:26 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-31 07:01:47 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 07:41:25 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:03:10 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:08:53 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:20:35 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:03:39 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:14:50 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:06:32 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:31:49 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:04:09 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:01:39 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:04:42 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:08:19 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:25:53 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:07:26 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:04:22 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:11:21 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:12:24 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-31 07:08:58 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | -0.001 |  |
| 2026-01-31 07:22:53 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.007 |  |
| 2026-01-31 07:08:57 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-01-31 07:03:18 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-01-31 07:02:25 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-31 07:02:18 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-01-31 07:04:25 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.041 |  |
| 2026-01-31 07:03:13 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.042 |  |
| 2026-01-31 07:04:26 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.054 |  |
| 2026-01-31 07:02:40 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.064 |  |
| 2026-01-31 07:04:11 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.087 |  |
| 2026-01-31 07:06:28 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.117 |  |
| 2026-01-31 07:01:45 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.153 |  |
| 2026-01-31 07:09:01 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | -1.908 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)