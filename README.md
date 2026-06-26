# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--27_02:22:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **190,364 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 02:22:07 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:13:44 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | -0.018 |  |
| 2026-06-27 02:11:10 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:08:05 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:06:09 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:06:09 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -0.054 |  |
| 2026-06-27 02:05:56 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-06-27 02:05:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-27 02:05:22 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:05:00 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-06-27 02:04:44 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.087 |  |
| 2026-06-27 02:04:23 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:04:17 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-27 02:03:45 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-27 02:03:44 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 02:03:34 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:03:08 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:03:02 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.021 |  |
| 2026-06-27 02:02:50 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:02:43 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:02:22 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-06-27 02:02:19 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:02:11 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.031 |  |
| 2026-06-27 02:01:36 | Dunamale (Aththanagalu Oya) | 1.55 | 🟢 Normal | -0.024 |  |
| 2026-06-27 02:01:35 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-06-27 02:01:28 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-27 02:01:05 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:00:48 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:00:32 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.011 |  |
| 2026-06-27 01:57:56 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 02:02:22 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-06-27 02:04:17 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-27 02:01:28 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-27 01:04:56 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-27 02:05:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-26 22:07:10 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-27 02:03:45 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-27 02:03:44 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 18:00:54 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:02:19 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:02:50 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:01:05 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:37:18 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:04:23 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:01:09 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-26 18:06:01 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:06:09 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:04:28 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:11:10 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-06-27 00:44:54 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:03:34 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:00:48 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:02:43 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:05:22 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-26 18:02:53 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:22:07 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:08:05 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:03:08 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-27 00:03:12 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:05:00 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-06-27 02:05:56 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-06-27 02:00:32 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.011 |  |
| 2026-06-27 02:13:44 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | -0.018 |  |
| 2026-06-27 02:03:02 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.021 |  |
| 2026-06-27 02:01:36 | Dunamale (Aththanagalu Oya) | 1.55 | 🟢 Normal | -0.024 |  |
| 2026-06-27 02:01:35 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-06-27 02:02:11 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.031 |  |
| 2026-06-27 02:06:09 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -0.054 |  |
| 2026-06-27 02:04:44 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.087 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)