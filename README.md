# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_13:21:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **124,861 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 13:21:55 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:21:30 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | -0.008 |  |
| 2026-04-14 13:14:54 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.011 |  |
| 2026-04-14 13:11:49 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:11:03 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-04-14 13:10:27 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:08:07 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.009 |  |
| 2026-04-14 13:07:34 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.030 |  |
| 2026-04-14 13:06:32 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:04:48 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:04:39 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-14 13:04:37 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:04:17 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.078 |  |
| 2026-04-14 13:04:12 | Thanamalwila (Kirindi Oya) | 1.51 | 🟢 Normal | -0.043 |  |
| 2026-04-14 13:04:06 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.012 |  |
| 2026-04-14 13:03:59 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:03:32 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:03:29 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-14 13:03:10 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-14 13:02:56 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.071 |  |
| 2026-04-14 13:02:46 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:02:46 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-04-14 13:02:10 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:01:59 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.011 |  |
| 2026-04-14 13:01:44 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.011 |  |
| 2026-04-14 13:01:34 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-14 13:01:14 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:01:13 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:01:13 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-14 13:00:56 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.031 |  |
| 2026-04-14 13:00:47 | Thanthirimale (Malwathu Oya) | 4.12 | 🟢 Normal | -0.050 |  |
| 2026-04-14 13:00:40 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 13:00:17 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-04-14 13:00:14 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-04-14 12:48:51 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-04-14 12:39:10 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:37:08 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:28:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 13:00:17 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-04-14 13:11:03 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-04-14 13:01:34 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-14 13:04:39 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-14 10:01:40 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-14 13:01:13 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-14 13:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 13:02:10 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:10:27 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:00:40 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:01:13 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:03:32 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:04:37 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:02:46 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:21:55 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:11:49 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:06:32 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:03:59 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:01:14 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:04:48 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:21:30 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | -0.008 |  |
| 2026-04-14 13:08:07 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.009 |  |
| 2026-04-14 13:00:14 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-04-14 13:03:10 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-14 13:03:29 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-14 13:01:59 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.011 |  |
| 2026-04-14 13:14:54 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.011 |  |
| 2026-04-14 13:01:44 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.011 |  |
| 2026-04-14 13:04:06 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.012 |  |
| 2026-04-14 13:02:46 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-04-14 11:02:38 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.022 |  |
| 2026-04-14 13:07:34 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.030 |  |
| 2026-04-14 13:00:56 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.031 |  |
| 2026-04-14 12:20:50 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.032 |  |
| 2026-04-14 12:28:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | -0.040 |  |
| 2026-04-14 13:04:12 | Thanamalwila (Kirindi Oya) | 1.51 | 🟢 Normal | -0.043 |  |
| 2026-04-14 13:00:47 | Thanthirimale (Malwathu Oya) | 4.12 | 🟢 Normal | -0.050 |  |
| 2026-04-14 13:02:56 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.071 |  |
| 2026-04-14 13:04:17 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.078 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)