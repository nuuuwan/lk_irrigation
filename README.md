# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_15:13:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,091 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 15:13:43 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:12:52 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.008 |  |
| 2026-05-01 15:11:47 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-01 15:11:38 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:11:20 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-01 15:08:57 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 15:08:29 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:07:46 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.051 |  |
| 2026-05-01 15:06:57 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-05-01 15:06:48 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:06:27 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-01 15:06:25 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:06:17 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-05-01 15:05:04 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-01 15:04:56 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:04:42 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:04:38 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.031 |  |
| 2026-05-01 15:04:32 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:04:03 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:03:29 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-05-01 15:03:26 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-01 15:03:22 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:03:14 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | -0.072 |  |
| 2026-05-01 15:03:02 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.084 |  |
| 2026-05-01 15:03:00 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-05-01 15:02:57 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-05-01 15:02:39 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | -0.030 |  |
| 2026-05-01 15:02:32 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | -0.018 |  |
| 2026-05-01 15:02:31 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-05-01 15:02:21 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-05-01 15:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:02:19 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:02:18 | Thanthirimale (Malwathu Oya) | 2.67 | 🟢 Normal | -0.019 |  |
| 2026-05-01 15:01:59 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:01:36 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.102 |  |
| 2026-05-01 15:01:30 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-01 15:01:26 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-05-01 15:00:59 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:00:12 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.020 |  |
| 2026-05-01 15:00:08 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -0.014 |  |
| 2026-05-01 14:28:28 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | -0.018 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 15:01:30 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-01 15:06:27 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-01 15:05:04 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-01 15:11:20 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-01 15:11:47 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-01 15:03:26 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-01 15:08:57 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 15:02:19 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:11:38 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:02:57 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:13:43 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:01:59 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:04:03 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:04:56 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:04:32 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:08:29 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:04:42 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:06:48 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:06:25 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-05-01 15:12:52 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.008 |  |
| 2026-05-01 15:06:57 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-05-01 15:06:17 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-05-01 15:03:29 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-05-01 15:03:00 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-05-01 15:02:31 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-05-01 15:00:08 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -0.014 |  |
| 2026-05-01 15:02:32 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | -0.018 |  |
| 2026-05-01 15:02:18 | Thanthirimale (Malwathu Oya) | 2.67 | 🟢 Normal | -0.019 |  |
| 2026-05-01 15:01:26 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-05-01 15:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-05-01 15:02:21 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-05-01 15:00:12 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.020 |  |
| 2026-05-01 15:02:39 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | -0.030 |  |
| 2026-05-01 15:04:38 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.031 |  |
| 2026-05-01 15:07:46 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.051 |  |
| 2026-05-01 15:03:14 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | -0.072 |  |
| 2026-05-01 15:03:02 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.084 |  |
| 2026-05-01 15:01:36 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)