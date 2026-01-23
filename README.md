# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--23_07:21:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **53,243 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-23 07:21:24 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:16:01 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:12:08 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:11:51 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-23 07:11:47 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:09:33 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:08:46 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.054 |  |
| 2026-01-23 07:08:28 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:07:34 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | -0.009 |  |
| 2026-01-23 07:06:54 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:06:54 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:06:50 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:06:26 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:05:43 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:05:42 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:05:37 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.020 |  |
| 2026-01-23 07:05:34 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.114 |  |
| 2026-01-23 07:05:34 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-23 07:05:19 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:04:36 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:04:11 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.141 |  |
| 2026-01-23 07:03:57 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 07:03:50 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | -0.033 |  |
| 2026-01-23 07:03:33 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-23 07:03:10 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:02:38 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-23 07:02:19 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-23 07:02:14 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-23 07:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.039 |  |
| 2026-01-23 07:02:06 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:02:05 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:01:33 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:01:23 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:01:12 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:00:39 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:00:15 | Manampitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.065 |  |
| 2026-01-23 07:00:08 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-23 06:38:43 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-23 07:02:14 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-23 06:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-23 07:11:51 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-23 07:03:33 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-23 07:02:38 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-23 07:02:19 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-23 07:03:57 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 07:05:34 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-23 06:06:50 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-23 07:01:33 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:00:08 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:02:05 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:04:36 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:08:28 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:01:23 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:11:47 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:03:10 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:06:50 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:06:54 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:00:39 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:05:19 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:05:42 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:02:06 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:05:43 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:06:54 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:12:08 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:09:33 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:21:24 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:16:01 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:01:12 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:06:26 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-23 07:07:34 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | -0.009 |  |
| 2026-01-23 07:05:37 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.020 |  |
| 2026-01-23 07:03:50 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | -0.033 |  |
| 2026-01-23 07:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.039 |  |
| 2026-01-23 07:08:46 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.054 |  |
| 2026-01-23 07:00:15 | Manampitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.065 |  |
| 2026-01-23 07:05:34 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.114 |  |
| 2026-01-23 07:04:11 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.141 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)