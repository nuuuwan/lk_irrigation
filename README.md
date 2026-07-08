# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--08_19:26:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **200,888 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-08 19:26:53 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:26:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 0.17 | 🟢 Normal | -1.115 |  |
| 2026-07-08 19:20:22 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.025 |  |
| 2026-07-08 19:12:17 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:10:24 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:08:37 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-08 19:08:17 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-08 19:06:51 | Glencourse (Kelani Ganga) | 9.32 | 🟢 Normal | -0.030 |  |
| 2026-07-08 19:06:49 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:06:28 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-07-08 19:06:18 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:05:56 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:05:38 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.019 |  |
| 2026-07-08 19:05:05 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:04:24 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-07-08 19:04:23 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:03:47 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.360 | 🔺 Rising |
| 2026-07-08 19:03:43 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-07-08 19:03:36 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-08 19:03:35 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:03:10 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:02:47 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:02:33 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 19:02:23 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:02:17 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-08 19:02:05 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.031 |  |
| 2026-07-08 19:02:04 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:02:00 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:01:47 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-07-08 19:01:31 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:01:20 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-07-08 19:01:19 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:00:39 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:00:27 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:00:18 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-08 19:03:47 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.360 | 🔺 Rising |
| 2026-07-08 19:06:28 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-07-08 19:03:36 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-08 19:02:17 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-08 19:02:33 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 19:08:17 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-08 19:08:37 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-08 19:00:39 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:03:35 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:06:18 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:02:04 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-08 17:08:44 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:10:24 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:06:49 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:04:23 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:02:47 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:26:53 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:02:00 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:00:27 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:03:10 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:05:05 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:02:23 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:12:17 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:01:29 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:05:56 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:01:31 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:01:19 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-08 19:03:43 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-07-08 19:01:47 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-07-08 19:01:20 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-07-08 19:04:24 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-07-08 19:05:38 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.019 |  |
| 2026-07-08 19:00:18 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-07-08 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.021 |  |
| 2026-07-08 19:20:22 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.025 |  |
| 2026-07-08 19:06:51 | Glencourse (Kelani Ganga) | 9.32 | 🟢 Normal | -0.030 |  |
| 2026-07-08 19:02:05 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.031 |  |
| 2026-07-08 19:26:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 0.17 | 🟢 Normal | -1.115 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)