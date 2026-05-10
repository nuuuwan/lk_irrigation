# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_19:16:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **148,253 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 19:16:50 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.032 |  |
| 2026-05-10 19:16:07 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.016 |  |
| 2026-05-10 19:10:36 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-05-10 19:10:12 | Moragaswewa (Deduru Oya) | 1.56 | 🟢 Normal | -0.036 |  |
| 2026-05-10 19:10:11 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-10 19:09:32 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-10 19:09:31 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | 0.436 | 🔺 Rising |
| 2026-05-10 19:09:20 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 19:08:41 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-10 19:07:43 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-10 19:04:54 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-10 19:04:50 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.033 |  |
| 2026-05-10 19:04:37 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-10 19:04:14 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-10 19:04:14 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-10 19:04:11 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-10 19:03:59 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.011 |  |
| 2026-05-10 19:03:23 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-05-10 19:03:22 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 19:03:11 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 19:03:01 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-05-10 19:02:59 | Ellagawa (Kalu Ganga) | 4.62 | 🟢 Normal | 0.000 |  |
| 2026-05-10 19:02:42 | Katharagama (Menik Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-05-10 19:02:35 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-05-10 19:02:30 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-05-10 19:02:30 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | -0.061 |  |
| 2026-05-10 19:02:30 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-10 19:02:29 | Thanamalwila (Kirindi Oya) | 1.82 | 🟢 Normal | -0.011 |  |
| 2026-05-10 19:01:45 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-10 19:01:35 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-05-10 19:01:33 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-10 19:01:17 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-10 19:01:13 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-10 18:59:48 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 19:09:31 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | 0.436 | 🔺 Rising |
| 2026-05-10 19:01:35 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-05-10 19:03:01 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-05-10 19:09:32 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-10 19:07:43 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-10 18:00:11 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-10 19:04:37 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-10 19:04:11 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-10 19:01:33 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-10 19:04:14 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-10 19:04:54 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-10 19:09:20 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 19:03:11 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 19:03:22 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 19:08:41 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-10 18:06:14 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-10 19:10:11 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-10 18:04:06 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-10 19:02:59 | Ellagawa (Kalu Ganga) | 4.62 | 🟢 Normal | 0.000 |  |
| 2026-05-10 19:10:36 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-05-10 19:02:30 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-10 19:01:45 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-10 18:01:26 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-05-10 19:04:14 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-10 19:01:13 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-10 19:02:35 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-05-10 19:02:42 | Katharagama (Menik Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-05-10 18:59:48 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | -0.011 |  |
| 2026-05-10 19:02:29 | Thanamalwila (Kirindi Oya) | 1.82 | 🟢 Normal | -0.011 |  |
| 2026-05-10 19:03:59 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.011 |  |
| 2026-05-10 19:03:23 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-05-10 19:16:07 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.016 |  |
| 2026-05-10 19:02:30 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-05-10 18:03:02 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.020 |  |
| 2026-05-10 19:16:50 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.032 |  |
| 2026-05-10 19:04:50 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.033 |  |
| 2026-05-10 19:10:12 | Moragaswewa (Deduru Oya) | 1.56 | 🟢 Normal | -0.036 |  |
| 2026-05-10 19:02:30 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | -0.061 |  |
| 2026-05-10 17:59:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)