# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--21_03:21:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **78,698 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 03:21:06 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 03:20:45 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 03:15:55 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-21 03:12:48 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | -432.000 |  |
| 2026-02-21 03:12:47 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -432.000 |  |
| 2026-02-21 03:08:43 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-21 03:08:22 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 2.269 | 🔺 Rising |
| 2026-02-21 03:08:13 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-02-21 03:08:12 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-02-21 03:06:44 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-21 03:05:57 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-21 03:05:28 | Padiyathalawa (Maduru Oya) | 1.88 | 🟢 Normal | -0.057 |  |
| 2026-02-21 03:04:57 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.009 |  |
| 2026-02-21 03:04:33 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.005 |  |
| 2026-02-21 03:04:28 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-21 03:04:24 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-02-21 03:04:17 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-02-21 03:04:06 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-21 03:03:59 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-02-21 03:03:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.46 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-02-21 03:03:19 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-21 03:03:07 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 03:02:39 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-21 03:02:23 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.179 |  |
| 2026-02-21 03:02:07 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 03:02:03 | Manampitiya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.059 |  |
| 2026-02-21 03:01:58 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 03:01:55 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-21 03:01:51 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | -0.010 |  |
| 2026-02-21 03:01:34 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-21 03:01:22 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-21 03:01:14 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-21 03:00:50 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-02-21 03:00:44 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:41:13 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.118 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 03:08:22 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 2.269 | 🔺 Rising |
| 2026-02-21 02:03:23 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-02-21 02:41:13 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-02-21 03:03:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.46 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-02-21 03:05:57 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-21 03:08:43 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-21 03:04:28 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-21 03:15:55 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-21 03:04:24 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-02-21 03:01:22 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-21 03:00:44 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 03:04:06 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:01:36 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-21 03:03:07 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 03:01:55 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-20 18:04:38 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:01:55 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-21 03:08:13 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-02-21 03:01:34 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-21 03:01:14 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:06:08 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-21 03:02:07 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 03:21:06 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-20 18:01:33 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 03:01:58 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 03:06:44 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-21 03:04:33 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.005 |  |
| 2026-02-21 03:04:57 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.009 |  |
| 2026-02-21 03:04:17 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-02-21 03:02:39 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-21 03:03:19 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-21 03:01:51 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | -0.010 |  |
| 2026-02-21 03:00:50 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-02-21 03:03:59 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-02-20 18:02:20 | Weraganthota (Mahaweli Ganga) | -1.32 | 🟢 Normal | -0.051 |  |
| 2026-02-21 03:05:28 | Padiyathalawa (Maduru Oya) | 1.88 | 🟢 Normal | -0.057 |  |
| 2026-02-21 03:02:03 | Manampitiya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.059 |  |
| 2026-02-21 03:02:23 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.179 |  |
| 2026-02-21 03:12:48 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | -432.000 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)