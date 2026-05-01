# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_12:15:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **139,970 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 12:15:19 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:11:49 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:11:43 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:09:17 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:08:20 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-05-01 12:07:33 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-05-01 12:07:24 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-05-01 12:06:40 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.019 |  |
| 2026-05-01 12:05:59 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-01 12:05:50 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.159 |  |
| 2026-05-01 12:05:09 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:04:59 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:04:57 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:04:32 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.029 |  |
| 2026-05-01 12:04:16 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-05-01 12:04:07 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 12:03:55 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:03:50 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 12.000 | 🔺 Rising |
| 2026-05-01 12:03:47 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 12.000 | 🔺 Rising |
| 2026-05-01 12:03:36 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:03:36 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.010 |  |
| 2026-05-01 12:03:35 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-05-01 12:03:11 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:03:10 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.051 |  |
| 2026-05-01 12:03:09 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-01 12:03:08 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.049 |  |
| 2026-05-01 12:03:08 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-05-01 12:03:01 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:02:57 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-01 12:02:54 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:02:39 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:02:19 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.040 |  |
| 2026-05-01 12:02:17 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-05-01 12:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | -0.040 |  |
| 2026-05-01 12:01:56 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:01:04 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:00:56 | Thanthirimale (Malwathu Oya) | 2.70 | 🟢 Normal | -0.010 |  |
| 2026-05-01 12:00:53 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 12:03:50 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 12.000 | 🔺 Rising |
| 2026-05-01 12:07:24 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-05-01 12:02:57 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-01 12:05:59 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-01 12:04:07 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 12:02:54 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:03:01 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:01:56 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:01:04 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:03:55 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:11:49 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:04:59 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:11:43 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:03:11 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:09:17 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:05:09 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:00:53 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:02:39 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:15:19 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:04:57 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:03:36 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-01 12:03:36 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.010 |  |
| 2026-05-01 12:03:35 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-05-01 12:07:33 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-05-01 12:03:09 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-01 12:00:56 | Thanthirimale (Malwathu Oya) | 2.70 | 🟢 Normal | -0.010 |  |
| 2026-05-01 12:08:20 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-05-01 12:06:40 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.019 |  |
| 2026-05-01 11:08:48 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.019 |  |
| 2026-05-01 12:02:17 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-05-01 12:03:08 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-05-01 12:04:16 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-05-01 12:04:32 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.029 |  |
| 2026-05-01 12:02:19 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.040 |  |
| 2026-05-01 12:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | -0.040 |  |
| 2026-05-01 12:03:08 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.049 |  |
| 2026-05-01 12:03:10 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.051 |  |
| 2026-05-01 11:01:59 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | -0.112 |  |
| 2026-05-01 12:05:50 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.159 |  |

## River Water Level Charts by Station

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)