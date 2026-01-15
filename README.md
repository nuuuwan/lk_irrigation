# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--16_01:26:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **46,712 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 01:26:35 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:16:05 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:11:00 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:10:50 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:07:58 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.009 |  |
| 2026-01-16 01:07:45 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:07:09 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-01-16 01:06:54 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-01-16 01:06:43 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:06:16 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-16 01:05:19 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.039 |  |
| 2026-01-16 01:04:42 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-01-16 01:03:59 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 1.800 | 🔺 Rising |
| 2026-01-16 01:03:55 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:03:39 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 1.800 | 🔺 Rising |
| 2026-01-16 01:03:24 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:03:23 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:03:00 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:02:52 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:02:43 | Peradeniya (Mahaweli Ganga) | 2.33 | 🟢 Normal | -0.051 |  |
| 2026-01-16 01:02:43 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:02:35 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-16 01:02:21 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:01:46 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-16 01:01:44 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-16 01:01:35 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:01:31 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.667 |  |
| 2026-01-16 01:01:17 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:00:37 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.667 |  |
| 2026-01-16 01:00:31 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 01:03:59 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 1.800 | 🔺 Rising |
| 2026-01-16 00:03:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-16 00:02:20 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-16 00:02:39 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-16 01:06:16 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-16 01:02:35 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-16 01:01:46 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-16 01:01:35 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:03:00 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:16:05 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:11:00 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:03:50 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:02:43 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:03:23 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:03:44 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:03:55 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:07:45 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:26:35 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:03:24 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:09:23 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:02:52 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:06:43 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:01:17 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 01:10:50 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-16 00:14:11 | Horowpothana (Yan Oya) | 2.25 | 🟢 Normal | -0.008 |  |
| 2026-01-16 01:07:09 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-01-16 01:07:58 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.009 |  |
| 2026-01-16 01:00:31 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-16 01:01:44 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-16 01:06:54 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-01-16 00:04:48 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.012 |  |
| 2026-01-16 01:04:42 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-01-16 01:05:19 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.039 |  |
| 2026-01-15 18:02:13 | Thanthirimale (Malwathu Oya) | 1.83 | 🟢 Normal | -0.040 |  |
| 2026-01-16 01:02:43 | Peradeniya (Mahaweli Ganga) | 2.33 | 🟢 Normal | -0.051 |  |
| 2026-01-15 18:07:05 | Weraganthota (Mahaweli Ganga) | -2.39 | 🟢 Normal | -0.400 |  |
| 2026-01-16 01:01:31 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.667 |  |
| 2026-01-16 00:17:16 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)