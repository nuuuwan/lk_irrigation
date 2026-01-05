# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--05_14:23:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,367 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 14:23:03 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:20:47 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:13:36 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:10:40 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.014 |  |
| 2026-01-05 14:09:35 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:09:03 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:07:34 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.018 |  |
| 2026-01-05 14:07:22 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-01-05 14:06:11 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-01-05 14:05:20 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:04:58 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:04:58 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:04:22 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.030 |  |
| 2026-01-05 14:04:01 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:03:56 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:03:37 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-01-05 14:03:36 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-01-05 14:03:32 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-05 14:03:23 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-01-05 14:03:14 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.137 |  |
| 2026-01-05 14:03:02 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 14:02:51 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:02:50 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-05 14:02:49 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-01-05 14:02:26 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:02:23 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 14:02:22 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:02:16 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:02:16 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:02:14 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 14:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:02:08 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 14:02:06 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:01:51 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:01:47 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:01:34 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:01:19 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:01:01 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-01-05 14:00:54 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-01-05 14:00:33 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:59:42 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:46:33 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 14:03:37 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-01-05 14:06:11 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-01-05 14:03:23 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-01-05 14:02:50 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-05 14:02:14 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 14:02:08 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 14:02:23 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 14:03:02 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 14:01:47 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-05 13:59:42 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:01:19 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:01:51 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:04:58 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:02:26 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:13:36 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:02:51 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:01:34 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:20:47 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:09:03 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:04:01 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:02:22 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:02:06 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:02:16 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:05:20 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:04:58 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:09:35 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:23:03 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:03:56 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:02:16 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-01-05 14:03:32 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-05 14:07:22 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-01-05 14:00:54 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-01-05 14:01:01 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-01-05 14:02:49 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-01-05 14:10:40 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.014 |  |
| 2026-01-05 14:07:34 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.018 |  |
| 2026-01-05 14:04:22 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.030 |  |
| 2026-01-05 14:03:14 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.137 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)