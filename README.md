# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--07_05:05:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,774 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 05:05:35 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.030 |  |
| 2026-01-07 05:05:14 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.021 |  |
| 2026-01-07 05:05:13 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.124 |  |
| 2026-01-07 05:04:56 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-07 05:04:51 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-07 05:04:48 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-07 05:04:14 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-01-07 05:03:55 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | -0.010 |  |
| 2026-01-07 05:03:23 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 05:02:55 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-07 05:02:52 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-07 05:02:47 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-07 05:02:28 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-07 05:01:52 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-07 05:01:29 | Nakkala (Kumbukkan Oya) | 1.50 | 🟢 Normal | -0.040 |  |
| 2026-01-07 05:01:18 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-01-07 05:01:17 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-07 05:01:12 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | -0.041 |  |
| 2026-01-07 05:00:47 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-01-07 05:00:21 | Manampitiya (Mahaweli Ganga) | 3.36 | 🟡 Alert | -0.424 |  |
| 2026-01-07 05:00:18 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-01-07 04:53:16 | Manampitiya (Mahaweli Ganga) | 3.41 | 🟡 Alert | -0.424 |  |
| 2026-01-07 04:43:15 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:17:08 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.016 |  |
| 2026-01-07 04:15:59 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:13:01 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.005 |  |
| 2026-01-07 04:12:02 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:11:57 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:11:08 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:09:33 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:09:08 | Glencourse (Kelani Ganga) | 8.86 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 05:00:21 | Manampitiya (Mahaweli Ganga) | 3.36 | 🟡 Alert | -0.424 |  |
| 2026-01-07 04:03:06 | Horowpothana (Yan Oya) | 2.95 | 🟢 Normal | 3.429 | 🔺 Rising |
| 2026-01-07 05:00:18 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-01-07 05:04:14 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-01-07 05:02:47 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-07 04:04:17 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-07 05:04:56 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-06 18:00:39 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 04:09:08 | Glencourse (Kelani Ganga) | 8.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 04:02:55 | Katharagama (Menik Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 18:02:01 | Weraganthota (Mahaweli Ganga) | -0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 05:02:55 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-07 05:01:52 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-07 05:02:52 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:03:13 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:11:08 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-07 05:03:23 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 05:04:51 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:43:15 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:00:54 | Thaldena (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-07 05:04:48 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:06:35 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:15:59 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:06:41 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-07 05:01:17 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:05:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:13:01 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.005 |  |
| 2026-01-07 05:01:18 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-01-07 03:02:48 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-01-07 05:03:55 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | -0.010 |  |
| 2026-01-07 05:00:47 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-01-07 04:17:08 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.016 |  |
| 2026-01-07 03:09:42 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-01-07 05:05:14 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.021 |  |
| 2026-01-07 05:05:35 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.030 |  |
| 2026-01-07 05:01:29 | Nakkala (Kumbukkan Oya) | 1.50 | 🟢 Normal | -0.040 |  |
| 2026-01-07 05:01:12 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | -0.041 |  |
| 2026-01-07 04:02:47 | Siyambalanduwa (Heda Oya) | 2.04 | 🟢 Normal | -0.069 |  |
| 2026-01-07 05:05:13 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)