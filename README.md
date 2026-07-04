# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_03:17:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **197,563 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 03:17:39 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-07-05 03:16:13 | Thalgahagoda (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-07-05 03:13:03 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:10:23 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | -0.115 |  |
| 2026-07-05 03:09:34 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.067 |  |
| 2026-07-05 03:07:55 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-07-05 03:07:40 | Glencourse (Kelani Ganga) | 11.69 | 🟢 Normal | -0.019 |  |
| 2026-07-05 03:07:25 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:07:24 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:07:23 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:07:01 | Hanwella (Kelani Ganga) | 3.26 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-05 03:05:30 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-05 03:05:20 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:05:17 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | -0.133 |  |
| 2026-07-05 03:04:57 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-07-05 03:04:40 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.257 | 🔺 Rising |
| 2026-07-05 03:04:17 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:04:16 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-05 03:03:42 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-07-05 03:03:41 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.081 |  |
| 2026-07-05 03:03:39 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:03:39 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | -0.030 |  |
| 2026-07-05 03:03:20 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | -90.000 |  |
| 2026-07-05 03:03:20 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-07-05 03:03:18 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | -90.000 |  |
| 2026-07-05 03:03:18 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-07-05 03:03:13 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:03:08 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:03:04 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-07-05 03:02:46 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:02:34 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-07-05 03:01:54 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-07-05 03:01:53 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:01:47 | Dunamale (Aththanagalu Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-07-05 03:01:35 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:01:22 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.378 |  |
| 2026-07-05 03:00:58 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-05 03:00:35 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 02:55:30 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 02:52:57 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 02:51:41 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.378 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 03:03:20 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-07-05 03:04:40 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.257 | 🔺 Rising |
| 2026-07-05 03:17:39 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-07-05 03:03:42 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-07-05 03:05:30 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-05 03:04:16 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-05 03:07:01 | Hanwella (Kelani Ganga) | 3.26 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-05 03:16:13 | Thalgahagoda (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-07-05 03:07:55 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-07-04 23:01:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-05 03:00:58 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 18:00:43 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:00:35 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:01:22 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 02:03:47 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:01:53 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 18:04:06 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:13:03 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:05:20 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:04:17 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:02:46 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:03:08 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-04 18:00:35 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:03:39 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:01:35 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:03:13 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:04:57 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-07-05 03:01:54 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-07-05 03:01:47 | Dunamale (Aththanagalu Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-07-05 03:03:04 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-07-05 03:07:40 | Glencourse (Kelani Ganga) | 11.69 | 🟢 Normal | -0.019 |  |
| 2026-07-05 03:02:34 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-07-05 03:03:39 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | -0.030 |  |
| 2026-07-05 03:09:34 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.067 |  |
| 2026-07-05 03:03:41 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.081 |  |
| 2026-07-05 03:10:23 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | -0.115 |  |
| 2026-07-05 03:05:17 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | -0.133 |  |
| 2026-07-05 03:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.378 |  |
| 2026-07-05 03:03:20 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | -90.000 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)