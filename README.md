# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_07:22:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,543 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 07:22:12 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-24 07:15:58 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-24 07:15:57 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-24 07:15:12 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.008 |  |
| 2026-04-24 07:10:19 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.017 |  |
| 2026-04-24 07:09:56 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.173 |  |
| 2026-04-24 07:08:48 | Dunamale (Aththanagalu Oya) | 1.83 | 🟢 Normal | -0.045 |  |
| 2026-04-24 07:08:21 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.111 |  |
| 2026-04-24 07:08:00 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.090 |  |
| 2026-04-24 07:06:05 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.350 | 🔺 Rising |
| 2026-04-24 07:06:04 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-04-24 07:05:32 | Ellagawa (Kalu Ganga) | 5.36 | 🟢 Normal | -0.019 |  |
| 2026-04-24 07:05:03 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-04-24 07:04:56 | Katharagama (Menik Ganga) | 2.12 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-24 07:04:24 | Hanwella (Kelani Ganga) | 1.42 | 🟢 Normal | -0.021 |  |
| 2026-04-24 07:03:52 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 07:03:46 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.047 |  |
| 2026-04-24 07:03:44 | Glencourse (Kelani Ganga) | 9.64 | 🟢 Normal | 0.000 |  |
| 2026-04-24 07:03:21 | Kuda Oya (Kirindi Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-04-24 07:03:14 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.032 |  |
| 2026-04-24 07:03:10 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-24 07:02:49 | Kuda Oya (Kirindi Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-04-24 07:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | -0.059 |  |
| 2026-04-24 07:02:42 | Thanamalwila (Kirindi Oya) | 1.85 | 🟢 Normal | -0.030 |  |
| 2026-04-24 07:02:38 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 07:02:38 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 07:02:07 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 07:02:04 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-04-24 07:01:59 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-24 07:01:57 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-04-24 07:01:44 | Thanthirimale (Malwathu Oya) | 1.72 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-04-24 07:01:40 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-24 07:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-24 07:01:04 | Galgamuwa (Mee Oya) | 0.96 | 🟢 Normal | -0.037 |  |
| 2026-04-24 07:01:03 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.094 |  |
| 2026-04-24 07:01:00 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-24 07:00:38 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | -0.054 |  |
| 2026-04-24 07:00:09 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-24 07:00:08 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 07:06:05 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.350 | 🔺 Rising |
| 2026-04-24 07:04:56 | Katharagama (Menik Ganga) | 2.12 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-24 07:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-24 07:01:44 | Thanthirimale (Malwathu Oya) | 1.72 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-04-24 07:02:38 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 06:06:32 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 07:03:52 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 07:22:12 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-24 07:02:04 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-04-24 07:03:10 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-24 07:02:38 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 07:15:58 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-24 07:02:07 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 07:03:44 | Glencourse (Kelani Ganga) | 9.64 | 🟢 Normal | 0.000 |  |
| 2026-04-24 07:00:09 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-24 07:01:40 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-24 07:01:00 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-24 07:03:21 | Kuda Oya (Kirindi Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-04-24 07:15:12 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.008 |  |
| 2026-04-24 07:06:04 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-04-24 07:01:59 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-24 07:05:03 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-04-24 07:01:57 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-04-24 07:10:19 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.017 |  |
| 2026-04-24 07:05:32 | Ellagawa (Kalu Ganga) | 5.36 | 🟢 Normal | -0.019 |  |
| 2026-04-24 07:04:24 | Hanwella (Kelani Ganga) | 1.42 | 🟢 Normal | -0.021 |  |
| 2026-04-24 07:02:42 | Thanamalwila (Kirindi Oya) | 1.85 | 🟢 Normal | -0.030 |  |
| 2026-04-24 07:00:08 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.031 |  |
| 2026-04-24 07:03:14 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.032 |  |
| 2026-04-24 05:35:35 | Panadugama (Nilwala Ganga) | 3.19 | 🟢 Normal | -0.034 |  |
| 2026-04-24 07:01:04 | Galgamuwa (Mee Oya) | 0.96 | 🟢 Normal | -0.037 |  |
| 2026-04-24 07:08:48 | Dunamale (Aththanagalu Oya) | 1.83 | 🟢 Normal | -0.045 |  |
| 2026-04-24 07:03:46 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.047 |  |
| 2026-04-24 07:00:38 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | -0.054 |  |
| 2026-04-24 07:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | -0.059 |  |
| 2026-04-24 07:08:00 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.090 |  |
| 2026-04-24 07:01:03 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.094 |  |
| 2026-04-24 07:08:21 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.111 |  |
| 2026-04-24 07:09:56 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.173 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)