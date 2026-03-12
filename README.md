# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--13_01:22:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **95,802 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 01:22:37 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.026 |  |
| 2026-03-13 01:21:20 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-13 01:17:04 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:13:02 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-13 01:07:59 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:07:28 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:06:55 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.372 |  |
| 2026-03-13 01:06:53 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:06:44 | Wellawaya (Kirindi Oya) | 4.00 | 🟢 Normal | 121.455 | 🔺 Rising |
| 2026-03-13 01:06:42 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:06:40 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:06:28 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.032 |  |
| 2026-03-13 01:05:20 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:05:05 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 121.455 | 🔺 Rising |
| 2026-03-13 01:04:58 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:04:38 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.003 |  |
| 2026-03-13 01:04:25 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:04:13 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | 0.428 | 🔺 Rising |
| 2026-03-13 01:03:58 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.090 |  |
| 2026-03-13 01:03:57 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 01:03:42 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:03:40 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:03:37 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.061 |  |
| 2026-03-13 01:03:20 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 01:03:11 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.033 |  |
| 2026-03-13 01:02:36 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-13 01:02:19 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:02:13 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | -266.400 |  |
| 2026-03-13 01:02:08 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | -266.400 |  |
| 2026-03-13 01:01:48 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:00:56 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:00:31 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 01:06:44 | Wellawaya (Kirindi Oya) | 4.00 | 🟢 Normal | 121.455 | 🔺 Rising |
| 2026-03-13 01:04:13 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | 0.428 | 🔺 Rising |
| 2026-03-12 22:16:26 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-03-13 00:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-12 22:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-13 01:03:57 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 01:03:20 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 01:13:02 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-13 01:21:20 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-13 01:03:40 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:01:56 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:06:53 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:00:56 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:05:52 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:04:58 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:01:48 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:00:40 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:06:40 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:07:28 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:04:25 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:07:59 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:03:42 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:06:42 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:05:20 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:03:01 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:02:19 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:09:28 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:17:04 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:04:38 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.003 |  |
| 2026-03-13 01:02:36 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-13 01:00:31 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.021 |  |
| 2026-03-13 01:22:37 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.026 |  |
| 2026-03-13 01:06:28 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.032 |  |
| 2026-03-13 01:03:11 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.033 |  |
| 2026-03-13 01:03:37 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.061 |  |
| 2026-03-12 18:02:28 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.083 |  |
| 2026-03-13 01:03:58 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.090 |  |
| 2026-03-13 01:06:55 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.372 |  |
| 2026-03-13 01:02:13 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | -266.400 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)