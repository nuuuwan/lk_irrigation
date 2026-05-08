# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_05:39:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **145,890 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 05:39:58 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-08 05:31:51 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.016 |  |
| 2026-05-08 05:15:57 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.016 |  |
| 2026-05-08 05:15:46 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.764 | 🔺 Rising |
| 2026-05-08 05:15:30 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.398 | 🔺 Rising |
| 2026-05-08 05:14:15 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.055 |  |
| 2026-05-08 05:10:23 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-08 05:08:44 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-08 05:07:08 | Thanamalwila (Kirindi Oya) | 2.45 | 🟢 Normal | -0.308 |  |
| 2026-05-08 05:06:49 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-08 05:06:40 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-08 05:05:44 | Rathnapura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.071 |  |
| 2026-05-08 05:05:22 | Pitabeddara (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.182 |  |
| 2026-05-08 05:05:18 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-08 05:05:16 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.031 |  |
| 2026-05-08 05:04:54 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-08 05:04:49 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-05-08 05:04:16 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | 0.434 | 🔺 Rising |
| 2026-05-08 05:04:13 | Hanwella (Kelani Ganga) | 2.60 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-05-08 05:04:06 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.048 |  |
| 2026-05-08 05:03:48 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.057 |  |
| 2026-05-08 05:03:48 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.015 |  |
| 2026-05-08 05:03:33 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | -0.269 |  |
| 2026-05-08 05:03:17 | Thawalama (Gin Ganga) | 2.56 | 🟢 Normal | -0.840 |  |
| 2026-05-08 05:03:14 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-08 05:03:00 | Giriulla (Maha Oya) | 2.37 | 🟢 Normal | -0.081 |  |
| 2026-05-08 05:02:05 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-05-08 05:01:57 | Moragaswewa (Deduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-08 05:01:57 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | -0.040 |  |
| 2026-05-08 05:01:38 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-08 05:01:14 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-05-08 05:00:50 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.085 |  |
| 2026-05-08 05:00:49 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.013 |  |
| 2026-05-08 05:00:38 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-05-08 04:58:54 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.398 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 03:15:48 | Panadugama (Nilwala Ganga) | 5.04 | 🟡 Alert | 0.068 | 🔺 Rising |
| 2026-05-08 05:15:46 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.764 | 🔺 Rising |
| 2026-05-07 23:00:34 | Weraganthota (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.746 | 🔺 Rising |
| 2026-05-08 05:04:16 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | 0.434 | 🔺 Rising |
| 2026-05-08 05:15:30 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.398 | 🔺 Rising |
| 2026-05-08 05:01:14 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-05-08 05:04:13 | Hanwella (Kelani Ganga) | 2.60 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-05-08 05:05:18 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-08 05:06:49 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-08 05:10:23 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-08 05:08:44 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-08 05:01:57 | Moragaswewa (Deduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-08 05:06:40 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-08 05:39:58 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-08 05:04:54 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-08 05:01:38 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-07 18:02:03 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-05-08 05:04:49 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-05-08 05:00:49 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.013 |  |
| 2026-05-08 05:03:48 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.015 |  |
| 2026-05-08 05:31:51 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.016 |  |
| 2026-05-08 05:15:57 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.016 |  |
| 2026-05-08 05:00:38 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-05-08 05:02:05 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-05-08 05:05:16 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.031 |  |
| 2026-05-08 05:01:57 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | -0.040 |  |
| 2026-05-08 05:04:06 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.048 |  |
| 2026-05-08 05:14:15 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.055 |  |
| 2026-05-08 05:03:48 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.057 |  |
| 2026-05-07 18:00:09 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | -0.063 |  |
| 2026-05-08 05:05:44 | Rathnapura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.071 |  |
| 2026-05-08 05:03:00 | Giriulla (Maha Oya) | 2.37 | 🟢 Normal | -0.081 |  |
| 2026-05-08 05:00:50 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.085 |  |
| 2026-05-08 05:05:22 | Pitabeddara (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.182 |  |
| 2026-05-08 05:03:33 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | -0.269 |  |
| 2026-05-08 05:07:08 | Thanamalwila (Kirindi Oya) | 2.45 | 🟢 Normal | -0.308 |  |
| 2026-05-08 04:14:04 | Kuda Oya (Kirindi Oya) | 2.72 | 🟢 Normal | -0.315 |  |
| 2026-05-08 05:03:17 | Thawalama (Gin Ganga) | 2.56 | 🟢 Normal | -0.840 |  |
| 2026-05-08 03:35:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.29 | 🟢 Normal | -6.495 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)