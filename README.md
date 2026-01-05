# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--05_17:15:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,483 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 17:15:16 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:11:01 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:10:43 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:09:49 | Galgamuwa (Mee Oya) | 1.20 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-05 17:08:31 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-05 17:07:35 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:06:46 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-01-05 17:05:56 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:05:12 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -0.085 |  |
| 2026-01-05 17:04:55 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.010 |  |
| 2026-01-05 17:04:38 | Padiyathalawa (Maduru Oya) | 1.59 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-01-05 17:04:16 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-05 17:04:13 | Weraganthota (Mahaweli Ganga) | -1.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 17:03:46 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.068 |  |
| 2026-01-05 17:03:40 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:02:42 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 17:02:30 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:02:20 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:02:16 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-01-05 17:02:11 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.013 |  |
| 2026-01-05 17:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-01-05 17:02:04 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:02:02 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | -0.010 |  |
| 2026-01-05 17:02:01 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:01:59 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:01:53 | Manampitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | 3.273 | 🔺 Rising |
| 2026-01-05 17:01:50 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:01:50 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:01:46 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-01-05 17:01:29 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-01-05 17:01:21 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:01:20 | Manampitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 3.273 | 🔺 Rising |
| 2026-01-05 17:01:13 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:01:13 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:01:09 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-05 17:01:06 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:00:28 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:25:32 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.215 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 17:01:53 | Manampitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | 3.273 | 🔺 Rising |
| 2026-01-05 17:04:38 | Padiyathalawa (Maduru Oya) | 1.59 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-01-05 17:01:46 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-01-05 17:02:16 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-01-05 17:08:31 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-05 17:01:09 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-05 17:02:42 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 17:04:13 | Weraganthota (Mahaweli Ganga) | -1.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 17:04:16 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-05 16:02:27 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 17:09:49 | Galgamuwa (Mee Oya) | 1.20 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-05 17:02:20 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:01:59 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:01:21 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:01:50 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:01:06 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:01:13 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:01:50 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:00:28 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-05 16:09:05 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:15:16 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:02:04 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:01:13 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:02:01 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:05:56 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:03:40 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:10:43 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:07:35 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:11:01 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:02:30 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-05 17:02:02 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | -0.010 |  |
| 2026-01-05 17:01:29 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-01-05 17:04:55 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.010 |  |
| 2026-01-05 17:02:11 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.013 |  |
| 2026-01-05 17:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-01-05 17:06:46 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-01-05 17:03:46 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.068 |  |
| 2026-01-05 17:05:12 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)