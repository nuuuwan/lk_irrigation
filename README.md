# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--07_02:24:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **66,133 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 02:24:59 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 02:15:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-07 02:11:20 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.361 | 🔺 Rising |
| 2026-02-07 02:08:58 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-02-07 02:07:49 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-07 02:07:48 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-07 02:05:38 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-07 02:05:28 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-07 02:03:57 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-07 02:03:44 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 02:03:32 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 02:03:23 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.157 |  |
| 2026-02-07 02:03:21 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-07 02:03:05 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-07 02:02:52 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-07 02:02:45 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-07 02:02:41 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-02-07 02:02:33 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-07 02:02:15 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-07 02:02:09 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-07 02:01:40 | Horowpothana (Yan Oya) | 3.01 | 🟢 Normal | -0.062 |  |
| 2026-02-07 02:01:21 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.023 |  |
| 2026-02-07 02:01:11 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-02-07 02:00:58 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.042 |  |
| 2026-02-07 02:00:47 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-02-07 02:00:21 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 2.409 | 🔺 Rising |
| 2026-02-07 02:00:13 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-07 01:56:08 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.361 | 🔺 Rising |
| 2026-02-07 01:46:50 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.042 |  |
| 2026-02-07 01:31:43 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.871 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 02:00:21 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 2.409 | 🔺 Rising |
| 2026-02-07 01:31:43 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.871 | 🔺 Rising |
| 2026-02-07 02:11:20 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.361 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-07 02:08:58 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-02-07 01:04:43 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-07 02:02:09 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-07 01:20:58 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-07 02:01:11 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-02-07 02:03:44 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 01:26:26 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-07 02:03:32 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 02:15:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-07 02:00:47 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-02-07 02:00:13 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-07 02:02:33 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-07 02:03:21 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-07 00:05:09 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-07 02:05:38 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:04:57 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-07 01:06:36 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-07 02:03:05 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-07 02:03:57 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-07 02:24:59 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 02:02:52 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-07 02:05:28 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:03:13 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-07 02:07:49 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-07 01:15:03 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-02-07 01:04:39 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-02-07 00:01:55 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-07 02:01:21 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.023 |  |
| 2026-02-07 02:02:41 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-02-06 18:01:44 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | -0.039 |  |
| 2026-02-07 02:00:58 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.042 |  |
| 2026-02-07 01:04:24 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.050 |  |
| 2026-02-07 02:01:40 | Horowpothana (Yan Oya) | 3.01 | 🟢 Normal | -0.062 |  |
| 2026-02-07 02:03:23 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.157 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)