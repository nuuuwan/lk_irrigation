# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_17:21:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,862 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 17:21:29 | Baddegama (Gin Ganga) | 3.01 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-05-13 17:13:05 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.053 |  |
| 2026-05-13 17:09:20 | Magura (Kalu Ganga) | 5.15 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-05-13 17:09:00 | Panadugama (Nilwala Ganga) | 5.38 | 🟡 Alert | 0.101 | 🔺 Rising |
| 2026-05-13 17:08:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.64 | 🟡 Alert | 0.093 | 🔺 Rising |
| 2026-05-13 17:07:08 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-05-13 17:06:56 | Moragaswewa (Deduru Oya) | 2.91 | 🟢 Normal | -0.045 |  |
| 2026-05-13 17:06:47 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-05-13 17:06:23 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.323 | 🔺 Rising |
| 2026-05-13 17:04:56 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-13 17:04:32 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-05-13 17:03:55 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-13 17:03:52 | Glencourse (Kelani Ganga) | 11.24 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-13 17:03:32 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-13 17:03:25 | Hanwella (Kelani Ganga) | 2.56 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-13 17:03:15 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.070 |  |
| 2026-05-13 17:03:13 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 17:03:12 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.049 |  |
| 2026-05-13 17:03:08 | Galgamuwa (Mee Oya) | 2.90 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-13 17:03:05 | Thanthirimale (Malwathu Oya) | 3.40 | 🟢 Normal | -0.052 |  |
| 2026-05-13 17:03:05 | Thawalama (Gin Ganga) | 3.36 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-05-13 17:02:56 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.137 |  |
| 2026-05-13 17:02:56 | Rathnapura (Kalu Ganga) | 6.17 | 🟡 Alert | -0.077 |  |
| 2026-05-13 17:02:52 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-13 17:02:49 | Putupaula (Kalu Ganga) | 2.19 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-13 17:02:38 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-05-13 17:02:35 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-05-13 17:02:14 | Thanamalwila (Kirindi Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-05-13 17:01:52 | Ellagawa (Kalu Ganga) | 7.85 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-13 17:01:48 | Giriulla (Maha Oya) | 2.11 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-05-13 17:01:42 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-05-13 17:01:22 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-13 17:01:11 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-13 17:01:11 | Dunamale (Aththanagalu Oya) | 3.40 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-13 17:00:54 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.983 | 🔺 Rising |
| 2026-05-13 17:00:39 | Moraketiya (Walawe Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-05-13 17:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.032 |  |
| 2026-05-13 17:00:31 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-13 16:50:18 | Baddegama (Gin Ganga) | 2.96 | 🟢 Normal | 0.096 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 17:09:00 | Panadugama (Nilwala Ganga) | 5.38 | 🟡 Alert | 0.101 | 🔺 Rising |
| 2026-05-13 17:08:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.64 | 🟡 Alert | 0.093 | 🔺 Rising |
| 2026-05-13 17:01:11 | Dunamale (Aththanagalu Oya) | 3.40 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-13 17:09:20 | Magura (Kalu Ganga) | 5.15 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-05-13 17:02:56 | Rathnapura (Kalu Ganga) | 6.17 | 🟡 Alert | -0.077 |  |
| 2026-05-13 17:00:54 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.983 | 🔺 Rising |
| 2026-05-13 17:06:23 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.323 | 🔺 Rising |
| 2026-05-13 17:01:48 | Giriulla (Maha Oya) | 2.11 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-05-13 17:03:05 | Thawalama (Gin Ganga) | 3.36 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-05-13 17:21:29 | Baddegama (Gin Ganga) | 3.01 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-05-13 17:03:25 | Hanwella (Kelani Ganga) | 2.56 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-13 17:06:47 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-05-13 17:03:52 | Glencourse (Kelani Ganga) | 11.24 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-13 17:01:52 | Ellagawa (Kalu Ganga) | 7.85 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-13 17:03:08 | Galgamuwa (Mee Oya) | 2.90 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-13 17:02:49 | Putupaula (Kalu Ganga) | 2.19 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-13 17:01:22 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-13 17:02:52 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-13 17:03:32 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-13 17:03:55 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-13 17:00:39 | Moraketiya (Walawe Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-05-13 17:03:13 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 17:04:56 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-13 17:00:31 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-13 17:01:42 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-05-13 17:02:14 | Thanamalwila (Kirindi Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-05-13 17:07:08 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-05-13 17:01:11 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-13 17:02:35 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-05-13 17:02:38 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-05-13 16:06:24 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.024 |  |
| 2026-05-13 17:04:32 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-05-13 17:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.032 |  |
| 2026-05-13 17:06:56 | Moragaswewa (Deduru Oya) | 2.91 | 🟢 Normal | -0.045 |  |
| 2026-05-13 17:03:12 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.049 |  |
| 2026-05-13 17:03:05 | Thanthirimale (Malwathu Oya) | 3.40 | 🟢 Normal | -0.052 |  |
| 2026-05-13 17:13:05 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.053 |  |
| 2026-05-13 17:03:15 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.070 |  |
| 2026-05-13 17:02:56 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.137 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)