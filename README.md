# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--24_02:20:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **26,195 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 02:20:05 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -18.000 |  |
| 2025-12-24 02:20:03 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -18.000 |  |
| 2025-12-24 02:20:02 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -18.000 |  |
| 2025-12-24 02:20:01 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -18.000 |  |
| 2025-12-24 02:17:51 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:17:50 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:17:48 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:13:28 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:12:17 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.009 |  |
| 2025-12-24 02:09:23 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:09:10 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-24 02:08:43 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 02:08:17 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 198.000 | 🔺 Rising |
| 2025-12-24 02:08:15 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | 198.000 | 🔺 Rising |
| 2025-12-24 02:08:14 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 198.000 | 🔺 Rising |
| 2025-12-24 02:08:05 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | -108.000 |  |
| 2025-12-24 02:08:03 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | -108.000 |  |
| 2025-12-24 02:07:36 | Urawa (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.718 | 🔺 Rising |
| 2025-12-24 02:07:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2025-12-24 02:06:41 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:05:23 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:05:08 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.084 |  |
| 2025-12-24 02:05:07 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:04:04 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:03:12 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:02:59 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 4.675 | 🔺 Rising |
| 2025-12-24 02:02:40 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.013 |  |
| 2025-12-24 02:02:23 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.011 |  |
| 2025-12-24 02:02:20 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-24 02:02:09 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:01:44 | Peradeniya (Mahaweli Ganga) | 2.47 | 🟢 Normal | -0.030 |  |
| 2025-12-24 02:01:42 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 4.675 | 🔺 Rising |
| 2025-12-24 02:01:37 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:01:35 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2025-12-24 02:01:02 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:00:37 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-24 01:47:55 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:38:06 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | -0.007 |  |
| 2025-12-24 01:34:35 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 02:08:17 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 198.000 | 🔺 Rising |
| 2025-12-24 02:02:59 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 4.675 | 🔺 Rising |
| 2025-12-24 02:07:36 | Urawa (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.718 | 🔺 Rising |
| 2025-12-24 02:01:35 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2025-12-24 02:07:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2025-12-24 01:31:18 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-24 02:02:20 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-24 02:09:10 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-24 02:08:43 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 02:05:23 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:03:12 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:02:16 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:01:37 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:01:02 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:02:43 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:05:07 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:09:23 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:19:24 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-24 00:04:39 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:47:55 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:02:09 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:34:35 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:04:04 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:00:37 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:06:41 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:17:51 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-24 00:13:00 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-24 02:13:28 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-24 01:38:06 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | -0.007 |  |
| 2025-12-24 02:12:17 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.009 |  |
| 2025-12-24 02:00:37 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-23 18:03:15 | Weraganthota (Mahaweli Ganga) | -1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-24 02:02:23 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.011 |  |
| 2025-12-24 02:02:40 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.013 |  |
| 2025-12-24 01:01:12 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.020 |  |
| 2025-12-24 02:01:44 | Peradeniya (Mahaweli Ganga) | 2.47 | 🟢 Normal | -0.030 |  |
| 2025-12-24 02:05:08 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.084 |  |
| 2025-12-24 02:20:05 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -18.000 |  |
| 2025-12-24 02:08:05 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)