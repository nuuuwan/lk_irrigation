# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--07_11:17:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **91,588 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 11:17:10 | Horowpothana (Yan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:16:50 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:15:27 | Weraganthota (Mahaweli Ganga) | -1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:15:16 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:11:36 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-07 11:10:03 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:09:52 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 11:09:45 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:07:21 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:05:45 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.124 |  |
| 2026-03-07 11:05:40 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:05:36 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.051 |  |
| 2026-03-07 11:05:11 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:05:08 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:05:01 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:05:00 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 11:04:50 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.048 |  |
| 2026-03-07 11:04:37 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-07 11:04:26 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:04:25 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | -0.010 |  |
| 2026-03-07 11:04:09 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:03:57 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:03:47 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-03-07 11:03:46 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-03-07 11:03:28 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.039 |  |
| 2026-03-07 11:03:11 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-07 11:02:32 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-03-07 11:02:31 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 11:02:21 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-07 11:02:18 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.33 | 🟢 Normal | -0.040 |  |
| 2026-03-07 11:01:56 | Pitabeddara (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:01:54 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.103 |  |
| 2026-03-07 11:01:38 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:01:28 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:01:19 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:00:57 | Thanthirimale (Malwathu Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:00:49 | Weraganthota (Mahaweli Ganga) | -1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:00:12 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 11:03:11 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-07 11:04:37 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-07 11:02:21 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-07 11:02:31 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 11:05:00 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 11:09:52 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 11:11:36 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-07 11:15:27 | Weraganthota (Mahaweli Ganga) | -1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:05:01 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:02:18 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:01:19 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:17:10 | Horowpothana (Yan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:01:28 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:10:03 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:01:56 | Pitabeddara (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:03:57 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:15:16 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:04:26 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:05:11 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:09:45 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:05:40 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:04:09 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:05:08 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:00:57 | Thanthirimale (Malwathu Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:07:21 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:16:50 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 11:01:38 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:16:07 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-03-07 11:03:47 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-03-07 11:03:46 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-03-07 11:04:25 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | -0.010 |  |
| 2026-03-07 11:00:12 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-03-07 11:02:32 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-03-07 11:03:28 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.039 |  |
| 2026-03-07 11:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.33 | 🟢 Normal | -0.040 |  |
| 2026-03-07 11:04:50 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.048 |  |
| 2026-03-07 11:05:36 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.051 |  |
| 2026-03-07 11:01:54 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.103 |  |
| 2026-03-07 11:05:45 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)