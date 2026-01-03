# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--04_04:16:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **36,075 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 04:16:29 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:14:02 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:13:45 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:12:22 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.038 |  |
| 2026-01-04 04:09:26 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-01-04 04:08:03 | Thawalama (Gin Ganga) | 2.71 | 🟢 Normal | -0.427 |  |
| 2026-01-04 04:07:26 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:07:21 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-01-04 04:06:56 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:06:54 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:06:53 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:06:52 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:06:50 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:05:45 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-01-04 04:05:36 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:05:01 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.089 |  |
| 2026-01-04 04:04:30 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:03:59 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:03:54 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:03:25 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:03:14 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.252 |  |
| 2026-01-04 04:03:12 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:03:07 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:03:06 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:03:06 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-01-04 04:03:04 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:02:51 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-01-04 04:02:46 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:02:41 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:02:36 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-01-04 04:02:29 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:02:16 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:01:54 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-04 04:01:23 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-04 04:01:08 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.000 |  |
| 2026-01-04 03:59:10 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.042 |  |
| 2026-01-04 03:55:25 | Thawalama (Gin Ganga) | 2.80 | 🟢 Normal | -0.427 |  |
| 2026-01-04 03:48:41 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-01-04 03:41:03 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-04 03:22:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | 0.121 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 18:08:58 | Galgamuwa (Mee Oya) | 2.51 | 🟢 Normal | 17.419 | 🔺 Rising |
| 2026-01-04 04:07:21 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-01-04 03:22:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-01-04 04:03:06 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-01-04 04:02:36 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-01-04 04:09:26 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-01-04 02:35:32 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-04 04:01:54 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-04 03:02:03 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-04 04:01:23 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-04 02:01:12 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | 0.005 |  |
| 2026-01-04 04:02:16 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:04:30 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:02:41 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:03:54 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:03:07 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:03:59 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:03:04 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:03:25 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:01:08 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.000 |  |
| 2026-01-04 03:11:55 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-01-04 03:05:24 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:03:06 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:05:36 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:02:29 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:06:56 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:03:12 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:07:26 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:01:44 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:14:02 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:16:29 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-01-04 04:05:45 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-01-04 04:02:51 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-01-04 04:12:22 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.038 |  |
| 2026-01-04 03:59:10 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.042 |  |
| 2026-01-03 17:00:43 | Weraganthota (Mahaweli Ganga) | -1.61 | 🟢 Normal | -0.050 |  |
| 2026-01-04 04:05:01 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.089 |  |
| 2026-01-04 04:03:14 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.252 |  |
| 2026-01-04 04:08:03 | Thawalama (Gin Ganga) | 2.71 | 🟢 Normal | -0.427 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)