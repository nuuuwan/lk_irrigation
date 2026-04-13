# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_01:37:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **124,404 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 01:37:30 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.007 |  |
| 2026-04-14 01:33:09 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-14 01:21:42 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-04-14 01:19:42 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | -0.071 |  |
| 2026-04-14 01:19:40 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.041 |  |
| 2026-04-14 01:16:35 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:14:21 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -684.000 |  |
| 2026-04-14 01:14:20 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -684.000 |  |
| 2026-04-14 01:14:19 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -684.000 |  |
| 2026-04-14 01:14:17 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -684.000 |  |
| 2026-04-14 01:08:24 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-14 01:06:47 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.878 | 🔺 Rising |
| 2026-04-14 01:05:16 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-04-14 01:04:44 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.878 | 🔺 Rising |
| 2026-04-14 01:04:42 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.878 | 🔺 Rising |
| 2026-04-14 01:04:27 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:04:24 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-14 01:04:12 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-04-14 01:04:05 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:03:45 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:03:42 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:03:27 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:03:11 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-04-14 01:02:58 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:02:55 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.071 |  |
| 2026-04-14 01:02:51 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.022 |  |
| 2026-04-14 01:02:45 | Moragaswewa (Deduru Oya) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 01:02:40 | Rathnapura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.078 |  |
| 2026-04-14 01:02:38 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:02:27 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:02:25 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:02:14 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.198 |  |
| 2026-04-14 01:02:13 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | -0.089 |  |
| 2026-04-14 01:01:59 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:01:31 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-14 01:01:19 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:01:11 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-14 01:01:11 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.033 |  |
| 2026-04-14 01:00:32 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.013 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 01:06:47 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.878 | 🔺 Rising |
| 2026-04-14 01:21:42 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-04-14 01:33:09 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-14 01:01:31 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-14 01:05:16 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-04-14 00:10:00 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-14 01:08:24 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-14 01:04:24 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-14 01:01:11 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-14 01:02:45 | Moragaswewa (Deduru Oya) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 01:00:32 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-04-13 18:01:02 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 00:01:34 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:04:27 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:02:58 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:03:42 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:01:19 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:16:35 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:09:05 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:02:25 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:02:38 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:01:59 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-14 01:01:19 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:26:34 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.004 |  |
| 2026-04-14 01:37:30 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.007 |  |
| 2026-04-13 18:03:40 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.010 |  |
| 2026-04-14 01:04:12 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-04-14 01:03:11 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-04-14 01:02:51 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.022 |  |
| 2026-04-13 21:01:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.029 |  |
| 2026-04-14 00:04:28 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.031 |  |
| 2026-04-14 01:01:11 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.033 |  |
| 2026-04-14 01:19:40 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.041 |  |
| 2026-04-14 01:19:42 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | -0.071 |  |
| 2026-04-14 01:02:40 | Rathnapura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.078 |  |
| 2026-04-14 01:02:13 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | -0.089 |  |
| 2026-04-14 01:02:14 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.198 |  |
| 2026-04-14 00:00:33 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -144.000 |  |
| 2026-04-14 01:14:21 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -684.000 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)