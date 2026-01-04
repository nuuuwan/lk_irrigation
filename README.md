# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--05_02:06:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **36,893 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 02:06:17 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-05 02:05:35 | Padiyathalawa (Maduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-05 02:05:14 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-05 02:03:52 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.191 |  |
| 2026-01-05 02:03:40 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-05 02:03:36 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-05 02:03:35 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-05 02:03:31 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.070 |  |
| 2026-01-05 02:03:12 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-05 02:02:51 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.005 |  |
| 2026-01-05 02:02:47 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 02:02:42 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-05 02:02:41 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 02:02:40 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-05 02:02:21 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-05 02:02:20 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 02:02:07 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | -0.142 |  |
| 2026-01-05 02:02:01 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-01-05 02:01:50 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-01-05 02:01:30 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-05 02:01:19 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.011 |  |
| 2026-01-05 02:01:14 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-05 02:00:54 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-05 01:46:41 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-05 01:34:10 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-05 01:21:56 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.007 |  |
| 2026-01-05 01:18:45 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-05 01:14:21 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-05 01:13:20 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.012 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 02:03:40 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-05 02:01:14 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-04 18:04:42 | Weraganthota (Mahaweli Ganga) | -1.62 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-05 02:02:21 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-05 02:03:36 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-05 02:02:42 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-05 01:02:55 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-05 02:02:41 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 02:01:30 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-05 02:03:35 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-05 01:18:45 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-05 01:02:26 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-05 00:07:00 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 02:00:54 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-05 02:05:35 | Padiyathalawa (Maduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-05 02:02:47 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 01:01:58 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-05 02:05:14 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-05 00:02:57 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 01:14:21 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:02:32 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-05 00:04:53 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-01-05 01:46:41 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-05 00:35:37 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-05 02:03:12 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-05 01:02:00 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-05 02:02:51 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.005 |  |
| 2026-01-05 01:21:56 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.007 |  |
| 2026-01-05 02:06:17 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-05 02:02:40 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-05 02:01:50 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-01-05 02:01:19 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.011 |  |
| 2026-01-05 02:02:01 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-01-05 01:01:43 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.022 |  |
| 2026-01-04 21:08:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-01-04 18:15:36 | Galgamuwa (Mee Oya) | 2.40 | 🟢 Normal | -0.048 |  |
| 2026-01-05 02:03:31 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.070 |  |
| 2026-01-05 02:02:07 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | -0.142 |  |
| 2026-01-05 02:03:52 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.191 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)