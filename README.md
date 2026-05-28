# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--28_12:05:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **163,900 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 12:05:42 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 12:05:29 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-28 12:05:01 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 12:04:37 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-28 12:04:26 | Deraniyagala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 12:04:23 | Magura (Kalu Ganga) | 4.66 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-05-28 12:04:21 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-28 12:04:18 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-28 12:04:02 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-28 12:03:43 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-05-28 12:03:29 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-28 12:03:29 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-28 12:03:24 | Hanwella (Kelani Ganga) | 4.15 | 🟢 Normal | -0.051 |  |
| 2026-05-28 12:03:22 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-05-28 12:03:12 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-28 12:02:58 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-28 12:02:53 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-28 12:02:47 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-28 12:02:39 | Glencourse (Kelani Ganga) | 11.56 | 🟢 Normal | -0.052 |  |
| 2026-05-28 12:02:26 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-05-28 12:02:24 | Baddegama (Gin Ganga) | 2.72 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-28 12:02:20 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-28 12:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.17 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-05-28 12:02:09 | Ellagawa (Kalu Ganga) | 8.59 | 🟢 Normal | -0.010 |  |
| 2026-05-28 12:02:04 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.011 |  |
| 2026-05-28 12:01:44 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.010 |  |
| 2026-05-28 12:01:32 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-05-28 12:01:26 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-28 12:01:24 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 12:01:09 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-28 12:01:00 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-28 12:00:42 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 11:38:02 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-28 11:20:14 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-05-28 11:16:20 | Rathnapura (Kalu Ganga) | 3.94 | 🟢 Normal | -0.074 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 12:04:23 | Magura (Kalu Ganga) | 4.66 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-05-28 12:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.17 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-05-28 12:03:29 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-28 12:01:00 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-28 12:05:29 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-28 12:02:24 | Baddegama (Gin Ganga) | 2.72 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-28 12:03:29 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-28 12:04:02 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-28 12:05:42 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 12:05:01 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 12:04:26 | Deraniyagala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 12:02:53 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-28 12:03:12 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-28 11:38:02 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-28 12:01:24 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 12:04:21 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-28 12:00:42 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 12:02:47 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-28 11:06:40 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 12:01:09 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-28 12:03:22 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-05-28 12:04:37 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-28 12:02:58 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-28 12:01:26 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-28 12:02:20 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-28 12:03:43 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-05-28 11:06:32 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-05-28 12:01:32 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-05-28 12:01:44 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.010 |  |
| 2026-05-28 12:02:09 | Ellagawa (Kalu Ganga) | 8.59 | 🟢 Normal | -0.010 |  |
| 2026-05-28 12:02:26 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-05-28 12:02:04 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.011 |  |
| 2026-05-28 11:05:35 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | -0.020 |  |
| 2026-05-28 11:05:17 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.030 |  |
| 2026-05-28 12:03:24 | Hanwella (Kelani Ganga) | 4.15 | 🟢 Normal | -0.051 |  |
| 2026-05-28 12:02:39 | Glencourse (Kelani Ganga) | 11.56 | 🟢 Normal | -0.052 |  |
| 2026-05-28 11:06:05 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.060 |  |
| 2026-05-28 11:16:20 | Rathnapura (Kalu Ganga) | 3.94 | 🟢 Normal | -0.074 |  |
| 2026-05-28 11:12:38 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | -0.078 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)