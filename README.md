# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--07_13:30:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **39,102 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 13:30:20 | Horowpothana (Yan Oya) | 2.66 | 🟢 Normal | -0.027 |  |
| 2026-01-07 13:20:49 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-07 13:18:43 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.016 |  |
| 2026-01-07 13:15:45 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:14:56 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-01-07 13:12:49 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:10:18 | Manampitiya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.036 |  |
| 2026-01-07 13:06:57 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | -0.024 |  |
| 2026-01-07 13:06:41 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.021 |  |
| 2026-01-07 13:05:07 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:04:54 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:04:50 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:04:44 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.027 |  |
| 2026-01-07 13:04:12 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:03:59 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | -0.010 |  |
| 2026-01-07 13:03:57 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-07 13:03:49 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:03:38 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-01-07 13:03:30 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.029 |  |
| 2026-01-07 13:03:24 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:03:21 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-07 13:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 13:02:41 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-01-07 13:02:29 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:02:23 | Padiyathalawa (Maduru Oya) | 1.25 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-07 13:02:21 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.100 |  |
| 2026-01-07 13:02:10 | Katharagama (Menik Ganga) | 0.61 | 🟢 Normal | -0.023 |  |
| 2026-01-07 13:02:00 | Weraganthota (Mahaweli Ganga) | -1.07 | 🟢 Normal | -0.020 |  |
| 2026-01-07 13:01:54 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:01:47 | Siyambalanduwa (Heda Oya) | 1.68 | 🟢 Normal | -0.039 |  |
| 2026-01-07 13:01:33 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-07 13:01:32 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:01:28 | Thanthirimale (Malwathu Oya) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-01-07 13:01:28 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:01:21 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:01:17 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.053 |  |
| 2026-01-07 13:01:04 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:00:12 | Nakkala (Kumbukkan Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-01-07 13:00:11 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.067 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 13:00:11 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-07 13:01:33 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-07 13:02:23 | Padiyathalawa (Maduru Oya) | 1.25 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-07 13:03:57 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-07 13:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 13:20:49 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-07 13:02:29 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:01:28 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:01:04 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:04:50 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:05:07 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:12:49 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:15:45 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:01:32 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:03:24 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:04:54 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:01:21 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:01:54 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:04:12 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:03:49 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-07 13:14:56 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-01-07 13:03:59 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | -0.010 |  |
| 2026-01-07 13:03:21 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-07 13:18:43 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.016 |  |
| 2026-01-07 13:02:41 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-01-07 13:02:00 | Weraganthota (Mahaweli Ganga) | -1.07 | 🟢 Normal | -0.020 |  |
| 2026-01-07 13:00:12 | Nakkala (Kumbukkan Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-01-07 13:01:28 | Thanthirimale (Malwathu Oya) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-01-07 13:06:41 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.021 |  |
| 2026-01-07 13:02:10 | Katharagama (Menik Ganga) | 0.61 | 🟢 Normal | -0.023 |  |
| 2026-01-07 13:06:57 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | -0.024 |  |
| 2026-01-07 13:04:44 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.027 |  |
| 2026-01-07 13:30:20 | Horowpothana (Yan Oya) | 2.66 | 🟢 Normal | -0.027 |  |
| 2026-01-07 13:03:30 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.029 |  |
| 2026-01-07 13:03:38 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-01-07 13:10:18 | Manampitiya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.036 |  |
| 2026-01-07 13:01:47 | Siyambalanduwa (Heda Oya) | 1.68 | 🟢 Normal | -0.039 |  |
| 2026-01-07 13:01:17 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.053 |  |
| 2026-01-07 13:02:21 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)