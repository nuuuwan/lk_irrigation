# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_02:21:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **153,902 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 02:21:19 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-17 02:17:11 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.017 |  |
| 2026-05-17 02:16:31 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-17 02:15:47 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-17 02:10:42 | Putupaula (Kalu Ganga) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-05-17 02:10:22 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-17 02:08:51 | Panadugama (Nilwala Ganga) | 3.15 | 🟢 Normal | -0.011 |  |
| 2026-05-17 02:07:10 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.003 |  |
| 2026-05-17 02:06:48 | Glencourse (Kelani Ganga) | 11.22 | 🟢 Normal | -1.500 |  |
| 2026-05-17 02:06:37 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-05-17 02:06:31 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-17 02:05:41 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.015 |  |
| 2026-05-17 02:05:37 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-05-17 02:05:29 | Rathnapura (Kalu Ganga) | 3.78 | 🟢 Normal | -0.071 |  |
| 2026-05-17 02:05:16 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-17 02:05:13 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-17 02:04:35 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-05-17 02:04:12 | Hanwella (Kelani Ganga) | 3.44 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-17 02:03:39 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 02:03:36 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | -1.500 |  |
| 2026-05-17 02:03:23 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.005 |  |
| 2026-05-17 02:03:05 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 02:02:59 | Dunamale (Aththanagalu Oya) | 3.39 | 🟡 Alert | -0.026 |  |
| 2026-05-17 02:02:58 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 02:02:36 | Moragaswewa (Deduru Oya) | 2.24 | 🟢 Normal | -0.118 |  |
| 2026-05-17 02:02:28 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-05-17 02:02:19 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-05-17 02:02:16 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-17 02:02:13 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 02:02:08 | Badalgama (Maha Oya) | 3.06 | 🟢 Normal | -0.010 |  |
| 2026-05-17 02:01:59 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-17 02:01:47 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-17 02:01:40 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 02:01:28 | Ellagawa (Kalu Ganga) | 8.05 | 🟢 Normal | -0.011 |  |
| 2026-05-17 02:01:26 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-05-17 02:00:20 | Magura (Kalu Ganga) | 3.27 | 🟢 Normal | -0.041 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 00:01:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.93 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-17 02:02:59 | Dunamale (Aththanagalu Oya) | 3.39 | 🟡 Alert | -0.026 |  |
| 2026-05-17 02:01:26 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-05-17 02:04:12 | Hanwella (Kelani Ganga) | 3.44 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-17 02:06:31 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-16 18:01:12 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-17 02:02:13 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 02:03:39 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 02:03:05 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 02:02:58 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 02:01:40 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 02:07:10 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.003 |  |
| 2026-05-17 02:16:31 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-17 02:01:59 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-17 02:02:28 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-05-17 01:02:24 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-17 02:21:19 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-17 02:05:16 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-17 02:10:22 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-17 02:02:16 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-17 02:03:23 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.005 |  |
| 2026-05-17 02:10:42 | Putupaula (Kalu Ganga) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-05-17 02:01:47 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-17 02:02:08 | Badalgama (Maha Oya) | 3.06 | 🟢 Normal | -0.010 |  |
| 2026-05-17 02:02:19 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-05-17 02:06:37 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-05-17 02:04:35 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-05-17 02:01:28 | Ellagawa (Kalu Ganga) | 8.05 | 🟢 Normal | -0.011 |  |
| 2026-05-17 02:08:51 | Panadugama (Nilwala Ganga) | 3.15 | 🟢 Normal | -0.011 |  |
| 2026-05-17 02:05:41 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.015 |  |
| 2026-05-17 02:17:11 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.017 |  |
| 2026-05-17 02:05:37 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-05-16 18:01:55 | Thanthirimale (Malwathu Oya) | 3.80 | 🟢 Normal | -0.030 |  |
| 2026-05-17 01:11:19 | Baddegama (Gin Ganga) | 2.51 | 🟢 Normal | -0.034 |  |
| 2026-05-17 02:00:20 | Magura (Kalu Ganga) | 3.27 | 🟢 Normal | -0.041 |  |
| 2026-05-16 18:04:15 | Galgamuwa (Mee Oya) | 2.90 | 🟢 Normal | -0.048 |  |
| 2026-05-17 02:05:29 | Rathnapura (Kalu Ganga) | 3.78 | 🟢 Normal | -0.071 |  |
| 2026-05-17 02:02:36 | Moragaswewa (Deduru Oya) | 2.24 | 🟢 Normal | -0.118 |  |
| 2026-05-17 02:06:48 | Glencourse (Kelani Ganga) | 11.22 | 🟢 Normal | -1.500 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)