# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_19:07:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,039 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 19:07:08 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-03 19:05:51 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.015 |  |
| 2026-08-03 19:05:44 | Putupaula (Kalu Ganga) | 1.53 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-03 19:05:35 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-03 19:05:02 | Ellagawa (Kalu Ganga) | 7.98 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-03 19:04:48 | Hanwella (Kelani Ganga) | 6.09 | 🟢 Normal | 0.281 | 🔺 Rising |
| 2026-08-03 19:04:31 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.087 |  |
| 2026-08-03 19:04:09 | Peradeniya (Mahaweli Ganga) | 9.62 | 🔴 Major Flood | -0.099 |  |
| 2026-08-03 19:04:04 | Holombuwa (Kelani Ganga) | 2.70 | 🟢 Normal | -0.437 |  |
| 2026-08-03 19:04:02 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 19:03:48 | Deraniyagala (Kelani Ganga) | 2.82 | 🟢 Normal | -0.637 |  |
| 2026-08-03 19:03:41 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-03 19:03:29 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-03 19:03:26 | Urawa (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-03 19:03:21 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 19:03:00 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-03 19:02:52 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-03 19:02:49 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-08-03 19:02:47 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-08-03 19:02:44 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-08-03 19:02:24 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 19:02:22 | Pitabeddara (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-08-03 19:01:43 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 19:01:29 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-03 19:01:24 | Nawalapitiya (Mahaweli Ganga) | 5.50 | 🟠 Minor Flood | -0.619 |  |
| 2026-08-03 19:01:13 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-03 19:01:09 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 19:01:00 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:38:27 | Norwood (Kelani Ganga) | 2.28 | 🟡 Alert | -0.173 |  |
| 2026-08-03 18:35:02 | Glencourse (Kelani Ganga) | 15.96 | 🟡 Alert | 372.000 | 🔺 Rising |
| 2026-08-03 18:34:59 | Glencourse (Kelani Ganga) | 15.65 | 🟡 Alert | 372.000 | 🔺 Rising |
| 2026-08-03 18:26:48 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 19:04:09 | Peradeniya (Mahaweli Ganga) | 9.62 | 🔴 Major Flood | -0.099 |  |
| 2026-08-03 18:05:47 | Rathnapura (Kalu Ganga) | 8.24 | 🟠 Minor Flood | 0.140 | 🔺 Rising |
| 2026-08-03 19:01:24 | Nawalapitiya (Mahaweli Ganga) | 5.50 | 🟠 Minor Flood | -0.619 |  |
| 2026-08-03 18:35:02 | Glencourse (Kelani Ganga) | 15.96 | 🟡 Alert | 372.000 | 🔺 Rising |
| 2026-08-03 18:38:27 | Norwood (Kelani Ganga) | 2.28 | 🟡 Alert | -0.173 |  |
| 2026-08-03 18:07:26 | Kithulgala (Kelani Ganga) | 3.30 | 🟡 Alert | -0.191 |  |
| 2026-08-03 18:09:14 | Magura (Kalu Ganga) | 2.97 | 🟢 Normal | 0.415 | 🔺 Rising |
| 2026-08-03 19:02:22 | Pitabeddara (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-08-03 19:04:48 | Hanwella (Kelani Ganga) | 6.09 | 🟢 Normal | 0.281 | 🔺 Rising |
| 2026-08-03 18:03:28 | Thawalama (Gin Ganga) | 3.33 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-08-03 19:02:44 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-08-03 19:02:47 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-08-03 19:02:49 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-08-03 18:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-08-03 19:05:02 | Ellagawa (Kalu Ganga) | 7.98 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-03 19:05:44 | Putupaula (Kalu Ganga) | 1.53 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-03 19:03:00 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-03 19:03:26 | Urawa (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-03 19:05:35 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-03 19:01:43 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 19:01:09 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 19:03:21 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 19:01:13 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-03 19:02:24 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 19:04:02 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 19:01:00 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:52 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 19:07:08 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-03 19:01:29 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-03 19:02:52 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:02:38 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:22 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:00:31 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-03 19:03:29 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-03 19:05:51 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.015 |  |
| 2026-08-03 18:00:23 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.070 |  |
| 2026-08-03 19:04:31 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.087 |  |
| 2026-08-03 19:04:04 | Holombuwa (Kelani Ganga) | 2.70 | 🟢 Normal | -0.437 |  |
| 2026-08-03 19:03:48 | Deraniyagala (Kelani Ganga) | 2.82 | 🟢 Normal | -0.637 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)