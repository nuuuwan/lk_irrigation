# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_19:15:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **198,190 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 19:15:07 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:14:27 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.024 |  |
| 2026-07-05 19:11:28 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:10:07 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:09:44 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:09:35 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-05 19:07:28 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.039 |  |
| 2026-07-05 19:07:01 | Glencourse (Kelani Ganga) | 10.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-05 19:06:55 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-07-05 19:06:49 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-07-05 19:06:41 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.028 |  |
| 2026-07-05 19:05:48 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.089 |  |
| 2026-07-05 19:05:00 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-07-05 19:04:50 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-07-05 19:04:40 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-07-05 19:04:26 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-05 19:03:54 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-05 19:03:50 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:03:28 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:03:14 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 324.000 | 🔺 Rising |
| 2026-07-05 19:03:13 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 324.000 | 🔺 Rising |
| 2026-07-05 19:03:09 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:02:54 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:02:37 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-07-05 19:02:29 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | -0.090 |  |
| 2026-07-05 19:02:19 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-07-05 19:01:55 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:01:54 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:01:41 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-07-05 19:01:34 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:01:21 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:01:12 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.012 |  |
| 2026-07-05 19:01:10 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:01:09 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.021 |  |
| 2026-07-05 19:00:59 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.010 |  |
| 2026-07-05 19:00:28 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 19:03:14 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 324.000 | 🔺 Rising |
| 2026-07-05 19:04:50 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-07-05 19:03:54 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-05 19:04:26 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-05 19:07:01 | Glencourse (Kelani Ganga) | 10.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-05 19:09:35 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-05 19:10:07 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:01:21 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:03:09 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:03:28 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:01:34 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:01:54 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:05:41 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:11:28 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:01:55 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:01:10 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:09:44 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:03:50 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:03:25 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:15:07 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:02:54 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:00:28 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 19:06:55 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-07-05 19:04:40 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-07-05 19:06:49 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-07-05 19:05:00 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-07-05 19:02:19 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-07-05 18:00:08 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-07-05 19:00:59 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.010 |  |
| 2026-07-05 19:01:12 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.012 |  |
| 2026-07-05 19:02:37 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-07-05 19:01:09 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.021 |  |
| 2026-07-05 19:14:27 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.024 |  |
| 2026-07-05 18:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.99 | 🟢 Normal | -0.025 |  |
| 2026-07-05 19:06:41 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.028 |  |
| 2026-07-05 19:01:41 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-07-05 19:07:28 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.039 |  |
| 2026-07-05 19:05:48 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.089 |  |
| 2026-07-05 19:02:29 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)