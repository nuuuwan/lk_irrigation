# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--09_00:12:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **40,410 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 00:12:03 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.783 | 🔺 Rising |
| 2026-01-09 00:11:43 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-09 00:11:01 | Manampitiya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:10:39 | Manampitiya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:09:37 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-01-09 00:08:56 | Peradeniya (Mahaweli Ganga) | 2.39 | 🟢 Normal | -0.009 |  |
| 2026-01-09 00:08:22 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-01-09 00:07:48 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:06:15 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:05:17 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | -0.020 |  |
| 2026-01-09 00:04:39 | Moragaswewa (Deduru Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:04:34 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-09 00:04:27 | Padiyathalawa (Maduru Oya) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-01-09 00:04:20 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.031 |  |
| 2026-01-09 00:04:20 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-09 00:03:54 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:03:54 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:03:30 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:03:28 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:03:02 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:02:41 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.026 |  |
| 2026-01-09 00:02:38 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:02:15 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-01-09 00:02:14 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:02:08 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-09 00:01:53 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:01:51 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.026 |  |
| 2026-01-09 00:01:31 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-09 00:01:30 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:01:27 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:01:22 | Moragaswewa (Deduru Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:01:19 | Siyambalanduwa (Heda Oya) | 1.23 | 🟢 Normal | -0.030 |  |
| 2026-01-09 00:00:44 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:00:39 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:46:07 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:35:52 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.053 |  |
| 2026-01-08 23:22:04 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | -0.007 |  |
| 2026-01-08 23:16:32 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.026 |  |
| 2026-01-08 23:15:36 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.026 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 00:12:03 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.783 | 🔺 Rising |
| 2026-01-09 00:01:31 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-09 00:04:20 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-09 00:11:43 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-08 18:00:51 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-09 00:01:27 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:04:39 | Moragaswewa (Deduru Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:00:44 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:01:53 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:03:30 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:03:54 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:02:38 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:03:54 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:06:15 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:03:28 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:03:02 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:02:14 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:07:48 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:11:01 | Manampitiya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:00:39 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-09 00:01:30 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:04:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:22:04 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | -0.007 |  |
| 2026-01-09 00:08:22 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-01-09 00:08:56 | Peradeniya (Mahaweli Ganga) | 2.39 | 🟢 Normal | -0.009 |  |
| 2026-01-09 00:04:34 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-08 18:02:13 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-09 00:02:08 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-09 00:09:37 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-01-09 00:04:27 | Padiyathalawa (Maduru Oya) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-01-09 00:02:15 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-01-09 00:05:17 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | -0.020 |  |
| 2026-01-08 23:04:49 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | -0.024 |  |
| 2026-01-09 00:01:51 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.026 |  |
| 2026-01-09 00:02:41 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.026 |  |
| 2026-01-09 00:01:19 | Siyambalanduwa (Heda Oya) | 1.23 | 🟢 Normal | -0.030 |  |
| 2026-01-09 00:04:20 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.031 |  |
| 2026-01-08 18:07:05 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.038 |  |
| 2026-01-08 23:35:52 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.053 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)