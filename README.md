# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--21_17:31:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **51,834 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 17:31:29 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:16:30 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.009 |  |
| 2026-01-21 17:10:17 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:09:17 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:08:32 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-21 17:07:54 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.274 |  |
| 2026-01-21 17:07:51 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:05:53 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:04:23 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:04:17 | Padiyathalawa (Maduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:04:03 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:03:44 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.030 |  |
| 2026-01-21 17:03:30 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:03:25 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:03:23 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 17:03:23 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:03:21 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:03:06 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:02:47 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:02:46 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.061 |  |
| 2026-01-21 17:02:44 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-01-21 17:02:43 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-01-21 17:02:43 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-21 17:02:42 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-21 17:02:34 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 17:01:59 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:01:57 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-21 17:01:56 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:01:51 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:01:50 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:01:19 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-21 17:01:00 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:00:44 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-01-21 17:00:42 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:00:37 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 17:00:13 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:00:06 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-21 16:59:50 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.063 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 16:59:50 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-21 17:02:42 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-21 17:08:32 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-21 17:01:19 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-21 17:02:43 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-21 17:03:23 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 17:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 17:00:37 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 17:02:34 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:00:13 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:01:51 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:03:06 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:01:00 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:10:17 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:01:56 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:04:03 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:03:21 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:02:47 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:04:17 | Padiyathalawa (Maduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:01:50 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:03:23 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:03:30 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:31:29 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:04:23 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:03:25 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:00:42 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:09:17 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:07:51 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:01:59 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-21 17:16:30 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.009 |  |
| 2026-01-21 17:00:06 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-21 17:02:44 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-01-21 17:00:44 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-01-21 17:01:57 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-21 17:02:43 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-01-21 17:03:44 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.030 |  |
| 2026-01-21 17:02:46 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.061 |  |
| 2026-01-21 16:04:05 | Thawalama (Gin Ganga) | 0.81 | 🟢 Normal | -0.071 |  |
| 2026-01-21 17:07:54 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.274 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)