# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_21:50:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **158,190 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 21:50:47 | Rathnapura (Kalu Ganga) | 2.26 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-05-21 21:26:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.014 |  |
| 2026-05-21 21:19:47 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-21 21:09:04 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | -0.010 |  |
| 2026-05-21 21:07:21 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.022 |  |
| 2026-05-21 21:07:13 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-21 21:06:47 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-05-21 21:06:22 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.090 |  |
| 2026-05-21 21:06:15 | Hanwella (Kelani Ganga) | 1.59 | 🟢 Normal | -0.039 |  |
| 2026-05-21 21:06:14 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-21 21:06:01 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-21 21:05:40 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-21 21:05:24 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-21 21:05:10 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-21 21:04:53 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-21 21:04:50 | Ellagawa (Kalu Ganga) | 5.49 | 🟢 Normal | 0.000 |  |
| 2026-05-21 21:04:47 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-05-21 21:04:37 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-21 21:04:36 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-21 21:03:43 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 21:03:42 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-21 21:03:37 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 21:50:47 | Rathnapura (Kalu Ganga) | 2.26 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-05-21 21:05:40 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-21 21:04:53 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-21 21:03:05 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-21 21:02:17 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-21 21:05:24 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-21 21:04:37 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-21 21:01:13 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 21:03:43 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 18:16:06 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-21 21:00:16 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-21 21:03:06 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-21 21:00:52 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-21 21:01:40 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 21:03:37 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-21 21:01:31 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:03:27 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 21:19:47 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-21 21:04:50 | Ellagawa (Kalu Ganga) | 5.49 | 🟢 Normal | 0.000 |  |
| 2026-05-21 21:03:42 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-21 21:00:38 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-21 21:05:10 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-21 21:07:13 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-21 21:04:36 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-21 21:01:28 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-21 21:01:59 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-21 21:06:01 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-21 21:09:04 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | -0.010 |  |
| 2026-05-21 21:04:47 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-05-21 21:06:47 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-05-21 21:26:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.014 |  |
| 2026-05-21 21:01:40 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.019 |  |
| 2026-05-21 21:02:05 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.021 |  |
| 2026-05-21 21:07:21 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.022 |  |
| 2026-05-21 21:06:15 | Hanwella (Kelani Ganga) | 1.59 | 🟢 Normal | -0.039 |  |
| 2026-05-21 18:01:04 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | -0.040 |  |
| 2026-05-21 21:06:22 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.090 |  |
| 2026-05-21 21:03:08 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.090 |  |
| 2026-05-21 21:03:10 | Deraniyagala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.217 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)