# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_17:18:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **173,073 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 17:18:13 | Magura (Kalu Ganga) | 3.60 | 🟢 Normal | -0.041 |  |
| 2026-06-07 17:14:12 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-07 17:08:46 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-07 17:07:01 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:06:56 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | -0.112 |  |
| 2026-06-07 17:06:33 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-07 17:06:13 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 17:06:08 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:05:53 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-07 17:05:07 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-06-07 17:04:55 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-06-07 17:04:52 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-06-07 17:04:44 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:04:40 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:04:10 | Glencourse (Kelani Ganga) | 12.03 | 🟢 Normal | -0.069 |  |
| 2026-06-07 17:03:53 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:03:49 | Deraniyagala (Kelani Ganga) | 1.67 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-07 17:03:43 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-07 17:02:57 | Panadugama (Nilwala Ganga) | 3.27 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-07 17:02:49 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:02:41 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-07 17:02:39 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:02:31 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-07 17:02:24 | Putupaula (Kalu Ganga) | 1.67 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-06-07 17:02:20 | Rathnapura (Kalu Ganga) | 4.21 | 🟢 Normal | -0.070 |  |
| 2026-06-07 17:02:20 | Dunamale (Aththanagalu Oya) | 2.56 | 🟢 Normal | -0.042 |  |
| 2026-06-07 17:02:12 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:02:09 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-06-07 17:01:58 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:01:47 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:01:38 | Ellagawa (Kalu Ganga) | 7.65 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-07 17:01:14 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:01:12 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-07 17:00:58 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:00:42 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:00:40 | Nawalapitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.040 |  |
| 2026-06-07 17:00:36 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:00:17 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-07 16:33:58 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.042 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 17:04:52 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-06-07 17:02:24 | Putupaula (Kalu Ganga) | 1.67 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-06-07 17:03:49 | Deraniyagala (Kelani Ganga) | 1.67 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-07 17:14:12 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-07 17:03:43 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-07 17:01:38 | Ellagawa (Kalu Ganga) | 7.65 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-07 17:02:57 | Panadugama (Nilwala Ganga) | 3.27 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-07 17:02:41 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-07 17:01:12 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-07 17:00:17 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-07 17:02:31 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-07 17:05:53 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-07 16:06:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.74 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-07 17:06:13 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 17:06:33 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-07 17:08:46 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-07 17:02:12 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:01:58 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:01:14 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:01:47 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:00:42 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:02:39 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:04:44 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:04:40 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:03:53 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:06:08 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:07:01 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:00:36 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:00:58 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:02:49 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:04:55 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-06-07 17:05:07 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-06-07 17:02:09 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-06-07 17:00:40 | Nawalapitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.040 |  |
| 2026-06-07 17:18:13 | Magura (Kalu Ganga) | 3.60 | 🟢 Normal | -0.041 |  |
| 2026-06-07 17:02:20 | Dunamale (Aththanagalu Oya) | 2.56 | 🟢 Normal | -0.042 |  |
| 2026-06-07 17:04:10 | Glencourse (Kelani Ganga) | 12.03 | 🟢 Normal | -0.069 |  |
| 2026-06-07 17:02:20 | Rathnapura (Kalu Ganga) | 4.21 | 🟢 Normal | -0.070 |  |
| 2026-06-07 17:06:56 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)