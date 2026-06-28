# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--29_03:06:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **192,174 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 03:06:50 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:06:50 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:06:47 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-29 03:06:37 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:06:16 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.056 |  |
| 2026-06-29 03:06:13 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 03:05:07 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-29 03:04:32 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 2.842 | 🔺 Rising |
| 2026-06-29 03:04:04 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 03:03:54 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 2.842 | 🔺 Rising |
| 2026-06-29 03:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | 0.621 | 🔺 Rising |
| 2026-06-29 03:03:30 | Hanwella (Kelani Ganga) | 1.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-29 03:03:22 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:03:22 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 03:03:10 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-06-29 03:02:52 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-29 03:02:45 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | 0.621 | 🔺 Rising |
| 2026-06-29 03:02:08 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:02:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.58 | 🟢 Normal | 0.621 | 🔺 Rising |
| 2026-06-29 03:01:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:01:39 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-06-29 03:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.884 |  |
| 2026-06-29 03:01:31 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:01:28 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:01:22 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:01:11 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:01:08 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-06-29 03:00:48 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:00:01 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:56:47 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.884 |  |
| 2026-06-29 02:54:09 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:41:15 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:36:09 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-29 02:29:46 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | 4.235 | 🔺 Rising |
| 2026-06-29 02:28:55 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | 4.235 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 02:29:46 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | 4.235 | 🔺 Rising |
| 2026-06-29 03:04:32 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 2.842 | 🔺 Rising |
| 2026-06-29 03:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | 0.621 | 🔺 Rising |
| 2026-06-29 01:13:23 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-06-29 01:37:14 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-29 03:02:52 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-29 03:05:07 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-29 03:03:30 | Hanwella (Kelani Ganga) | 1.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-29 02:05:57 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-29 03:06:13 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 03:03:22 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 03:04:04 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 02:36:09 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-28 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:01:11 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:01:31 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:01:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 01:00:51 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:04:59 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:06:50 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-29 01:03:37 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:06:50 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:01:22 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:02:45 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:00:01 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:03:22 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:05:55 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:01:28 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:06:37 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:01:22 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-29 03:02:08 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:01:23 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-06-29 03:03:10 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-06-29 03:06:47 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-29 03:01:39 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-06-29 03:01:08 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-06-29 03:06:16 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.056 |  |
| 2026-06-29 02:01:48 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.180 |  |
| 2026-06-29 03:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.884 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)