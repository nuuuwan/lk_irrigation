# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_20:18:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **122,446 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 20:18:45 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-04-11 20:16:05 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:11:53 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:11:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-04-11 20:10:25 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-04-11 20:10:01 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-11 20:09:12 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-11 20:08:56 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.030 |  |
| 2026-04-11 20:07:18 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:07:04 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-04-11 20:06:23 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.014 |  |
| 2026-04-11 20:06:21 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.028 |  |
| 2026-04-11 20:06:08 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:05:47 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-11 20:05:17 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:04:37 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:04:20 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:03:31 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-11 20:03:31 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:03:25 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-04-11 20:03:05 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:02:54 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-04-11 20:02:48 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-11 20:02:47 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:02:41 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-11 20:02:33 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-04-11 20:02:28 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:02:23 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-11 20:02:16 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:02:16 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:02:13 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:01:49 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:01:41 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:01:18 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.031 |  |
| 2026-04-11 20:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:00:20 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 20:02:33 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-04-11 20:02:41 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-11 20:10:01 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-11 20:03:31 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-11 20:05:47 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-11 20:02:23 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-11 20:09:12 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-11 20:00:20 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:02:28 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:01:41 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:04:37 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:06:08 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:02:16 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 18:03:33 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:03:05 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:16:05 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:04:20 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:02:16 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:07:18 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:01:49 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:05:17 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:02:13 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:11:53 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:02:47 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:03:31 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:11:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-04-11 20:02:48 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-11 18:00:38 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-04-11 20:18:45 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-04-11 20:02:54 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-04-11 20:07:04 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-04-11 20:06:23 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.014 |  |
| 2026-04-11 20:10:25 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-04-11 20:03:25 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-04-11 20:06:21 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.028 |  |
| 2026-04-11 20:08:56 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.030 |  |
| 2026-04-11 20:01:18 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.031 |  |
| 2026-04-11 18:01:56 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)