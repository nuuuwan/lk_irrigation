# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--07_03:27:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **66,167 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 03:27:49 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-02-07 03:18:51 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-07 03:18:47 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-07 03:15:23 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 03:14:58 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.471 |  |
| 2026-02-07 03:14:10 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-02-07 03:13:00 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-07 03:12:27 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.430 | 🔺 Rising |
| 2026-02-07 03:11:26 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.019 |  |
| 2026-02-07 03:09:03 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-07 03:06:45 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-02-07 03:06:20 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-07 03:05:30 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-07 03:05:28 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.430 | 🔺 Rising |
| 2026-02-07 03:05:01 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-02-07 03:04:19 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-02-07 03:04:15 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.037 |  |
| 2026-02-07 03:03:14 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 03:02:57 | Peradeniya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.232 |  |
| 2026-02-07 03:02:53 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-07 03:02:33 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-07 03:02:23 | Horowpothana (Yan Oya) | 2.94 | 🟢 Normal | -0.069 |  |
| 2026-02-07 03:02:08 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-02-07 03:02:04 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-07 03:02:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-02-07 03:01:36 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-07 03:01:16 | Padiyathalawa (Maduru Oya) | 1.12 | 🟢 Normal | -0.031 |  |
| 2026-02-07 03:01:06 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-02-07 03:00:54 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 03:00:41 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 02:00:21 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 2.409 | 🔺 Rising |
| 2026-02-07 03:12:27 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.430 | 🔺 Rising |
| 2026-02-07 03:06:45 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-02-07 02:27:54 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-07 03:14:10 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-02-07 03:02:33 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-07 03:00:54 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 03:03:14 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 03:02:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-02-07 03:09:03 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-07 03:02:08 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-02-07 03:00:41 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-07 00:05:09 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-07 03:05:30 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:04:57 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-07 01:06:36 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-07 03:05:01 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-02-07 03:18:47 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-07 03:02:04 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-07 03:15:23 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 03:01:36 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-07 03:13:00 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:03:13 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-07 03:06:20 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-07 03:18:51 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-07 03:04:19 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-02-07 03:02:53 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-07 01:04:39 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-02-07 03:11:26 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.019 |  |
| 2026-02-07 03:01:06 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-02-07 03:27:49 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-02-07 03:01:16 | Padiyathalawa (Maduru Oya) | 1.12 | 🟢 Normal | -0.031 |  |
| 2026-02-07 03:04:15 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.037 |  |
| 2026-02-06 18:01:44 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | -0.039 |  |
| 2026-02-07 03:02:23 | Horowpothana (Yan Oya) | 2.94 | 🟢 Normal | -0.069 |  |
| 2026-02-07 03:02:57 | Peradeniya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.232 |  |
| 2026-02-07 03:14:58 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.471 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)