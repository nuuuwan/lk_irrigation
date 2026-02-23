# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--23_17:20:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **81,053 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **49** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 17:20:34 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | -108.000 |  |
| 2026-02-23 17:20:32 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | -108.000 |  |
| 2026-02-23 17:20:28 | Weraganthota (Mahaweli Ganga) | -1.77 | 🟢 Normal | -108.000 |  |
| 2026-02-23 17:14:26 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-02-23 17:12:47 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.030 |  |
| 2026-02-23 17:11:05 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.024 |  |
| 2026-02-23 17:09:20 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-02-23 17:08:41 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:07:45 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:07:44 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:07:42 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:07:40 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:07:37 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:05:39 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:05:24 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-23 17:05:19 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:05:06 | Ellagawa (Kalu Ganga) | 4.96 | 🟢 Normal | -0.068 |  |
| 2026-02-23 17:04:45 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | -60.000 |  |
| 2026-02-23 17:04:45 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | -9.000 |  |
| 2026-02-23 17:04:42 | Glencourse (Kelani Ganga) | 8.86 | 🟢 Normal | -60.000 |  |
| 2026-02-23 17:04:41 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | -0.033 |  |
| 2026-02-23 17:04:41 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | -9.000 |  |
| 2026-02-23 17:04:39 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | -60.000 |  |
| 2026-02-23 17:04:38 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | -9.000 |  |
| 2026-02-23 17:04:35 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-02-23 17:04:08 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | -0.020 |  |
| 2026-02-23 17:04:02 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -1.385 |  |
| 2026-02-23 17:03:58 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-02-23 17:03:36 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -1.385 |  |
| 2026-02-23 17:03:32 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:03:32 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-23 17:03:28 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:03:16 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-02-23 17:02:35 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | -0.122 |  |
| 2026-02-23 17:01:58 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | -0.062 |  |
| 2026-02-23 17:01:55 | Padiyathalawa (Maduru Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-02-23 17:01:53 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:01:51 | Manampitiya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.191 |  |
| 2026-02-23 17:01:51 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-23 17:01:49 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-02-23 17:01:42 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:01:30 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.027 |  |
| 2026-02-23 17:01:23 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:01:18 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:01:16 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:01:15 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-23 16:52:19 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.062 |  |
| 2026-02-23 16:52:18 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.062 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 17:01:49 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-02-23 17:05:24 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-23 17:03:32 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-23 17:01:51 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-23 17:01:18 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:07:45 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:02:35 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:01:23 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:08:41 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:01:53 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:03:28 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:01:42 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:03:32 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:05:39 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:05:19 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-23 17:14:26 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-02-23 15:08:34 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-02-23 17:04:35 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:01:48 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-02-23 17:03:58 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-02-23 17:09:20 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-02-23 17:01:55 | Padiyathalawa (Maduru Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:00:40 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.011 |  |
| 2026-02-23 17:03:16 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-02-23 14:05:44 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-02-23 17:04:08 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | -0.020 |  |
| 2026-02-23 17:11:05 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.024 |  |
| 2026-02-23 17:01:30 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.027 |  |
| 2026-02-23 14:10:34 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.029 |  |
| 2026-02-23 17:12:47 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.030 |  |
| 2026-02-23 17:04:41 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | -0.033 |  |
| 2026-02-23 17:01:58 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | -0.062 |  |
| 2026-02-23 17:05:06 | Ellagawa (Kalu Ganga) | 4.96 | 🟢 Normal | -0.068 |  |
| 2026-02-23 17:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | -0.122 |  |
| 2026-02-23 17:01:51 | Manampitiya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.191 |  |
| 2026-02-23 17:04:02 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -1.385 |  |
| 2026-02-23 17:04:45 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | -9.000 |  |
| 2026-02-23 17:04:45 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | -60.000 |  |
| 2026-02-23 17:20:34 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)