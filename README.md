# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--23_08:06:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **53,277 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-23 08:06:43 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:06:27 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.096 |  |
| 2026-01-23 08:06:25 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:05:24 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:05:09 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.010 |  |
| 2026-01-23 08:05:03 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.050 |  |
| 2026-01-23 08:04:53 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:04:48 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:04:22 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.124 |  |
| 2026-01-23 08:04:06 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:04:01 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-01-23 08:03:26 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 08:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.049 |  |
| 2026-01-23 08:03:00 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-23 08:02:44 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:02:32 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:02:21 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.157 |  |
| 2026-01-23 08:02:17 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 08:02:08 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:02:08 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:02:05 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:01:56 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-23 08:01:53 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:01:48 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:01:33 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:01:27 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | -0.090 |  |
| 2026-01-23 08:01:07 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:00:58 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:00:56 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:00:47 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:00:31 | Manampitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.040 |  |
| 2026-01-23 08:00:20 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:30:39 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-23 07:26:16 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:21:24 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-23 07:16:01 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:12:08 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:11:51 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-23 07:11:47 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-23 08:04:01 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-01-23 07:11:51 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-23 08:01:56 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-23 07:30:39 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-23 08:03:00 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-23 08:03:26 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 08:02:17 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 08:02:08 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:00:20 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:00:47 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:02:05 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:04:36 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:05:24 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:02:05 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:00:58 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:01:33 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:01:07 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:01:48 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:04:48 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:04:06 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:02:08 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:06:25 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:02:44 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:06:43 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:06:54 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:02:32 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:00:56 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:16:01 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:04:53 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:01:53 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:05:09 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.010 |  |
| 2026-01-23 07:03:50 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | -0.033 |  |
| 2026-01-23 08:00:31 | Manampitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.040 |  |
| 2026-01-23 08:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.049 |  |
| 2026-01-23 08:05:03 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.050 |  |
| 2026-01-23 08:01:27 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | -0.090 |  |
| 2026-01-23 08:06:27 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.096 |  |
| 2026-01-23 08:04:22 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.124 |  |
| 2026-01-23 08:02:21 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.157 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)