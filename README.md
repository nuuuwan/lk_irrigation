# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_00:09:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **197,461 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 00:09:54 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-07-05 00:09:49 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | -6.995 |  |
| 2026-07-05 00:06:59 | Holombuwa (Kelani Ganga) | 1.48 | 🟢 Normal | -0.038 |  |
| 2026-07-05 00:06:55 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-05 00:06:40 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:06:18 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -6.995 |  |
| 2026-07-05 00:05:37 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:05:30 | Glencourse (Kelani Ganga) | 11.63 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-07-05 00:05:28 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.022 |  |
| 2026-07-05 00:05:18 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-07-05 00:04:47 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-05 00:04:20 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | -0.051 |  |
| 2026-07-05 00:04:20 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-05 00:04:18 | Deraniyagala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.179 |  |
| 2026-07-05 00:03:27 | Giriulla (Maha Oya) | 2.07 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-07-05 00:03:21 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-07-05 00:03:02 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:03:00 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:02:59 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:02:46 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-05 00:02:37 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:02:34 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-05 00:02:14 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:02:07 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:01:47 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-05 00:01:45 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-07-05 00:01:29 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.021 |  |
| 2026-07-05 00:01:09 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:00:46 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:00:27 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:36:55 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 00:03:27 | Giriulla (Maha Oya) | 2.07 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-07-05 00:03:21 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-07-05 00:05:30 | Glencourse (Kelani Ganga) | 11.63 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-07-05 00:09:54 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-07-05 00:02:34 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-05 00:04:47 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-05 00:01:47 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-04 23:01:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-05 00:06:55 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-05 00:04:20 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-05 00:02:46 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 22:14:56 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 18:00:43 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:05:37 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:02:37 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:02:07 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:03:02 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:00:27 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 18:04:06 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:23:33 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:08:20 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:01:09 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:02:14 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:02:59 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:00:46 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-04 18:00:35 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:03:00 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-05 00:06:40 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:07:18 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-07-05 00:01:45 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-07-05 00:05:18 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-07-05 00:01:29 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.021 |  |
| 2026-07-05 00:05:28 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.022 |  |
| 2026-07-05 00:06:59 | Holombuwa (Kelani Ganga) | 1.48 | 🟢 Normal | -0.038 |  |
| 2026-07-04 23:07:14 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.050 |  |
| 2026-07-05 00:04:20 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | -0.051 |  |
| 2026-07-04 22:12:46 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.092 |  |
| 2026-07-05 00:04:18 | Deraniyagala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.179 |  |
| 2026-07-05 00:09:49 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | -6.995 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)