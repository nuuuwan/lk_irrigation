# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--30_16:06:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **193,594 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 16:06:18 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-30 16:06:14 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-06-30 16:06:08 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-06-30 16:05:36 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-06-30 16:04:45 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | -0.070 |  |
| 2026-06-30 16:04:34 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-30 16:03:59 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | 0.000 |  |
| 2026-06-30 16:03:50 | Baddegama (Gin Ganga) | 2.58 | 🟢 Normal | -0.031 |  |
| 2026-06-30 16:03:41 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-30 16:03:38 | Hanwella (Kelani Ganga) | 2.56 | 🟢 Normal | -0.040 |  |
| 2026-06-30 16:03:35 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | -0.040 |  |
| 2026-06-30 16:03:19 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | -0.020 |  |
| 2026-06-30 16:03:19 | Rathnapura (Kalu Ganga) | 3.03 | 🟢 Normal | -0.121 |  |
| 2026-06-30 16:02:52 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-06-30 16:02:48 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-30 16:02:44 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-30 16:02:38 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-30 16:02:36 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-30 16:02:29 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-30 16:02:21 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-30 16:02:21 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-30 16:02:15 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-06-30 16:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.17 | 🟢 Normal | -0.070 |  |
| 2026-06-30 16:01:56 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 16:01:51 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-30 16:01:49 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-30 16:01:27 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-30 16:01:03 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 16:00:47 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-30 16:00:36 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-30 16:00:08 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-30 15:17:06 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.111 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 16:02:52 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-06-30 16:05:36 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-06-30 16:03:41 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-30 16:01:49 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-30 16:02:48 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-30 16:02:36 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-30 15:02:54 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-30 16:02:29 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-30 16:02:21 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-30 16:00:08 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-30 16:01:03 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 16:03:59 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | 0.000 |  |
| 2026-06-30 16:02:21 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-30 16:00:36 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-30 16:01:56 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 16:04:34 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-30 16:00:47 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-30 16:02:44 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-30 16:01:51 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-30 16:02:38 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-30 15:08:14 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-30 16:06:18 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-30 15:05:26 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-06-30 16:01:27 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-30 16:06:08 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-06-30 16:06:14 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-06-30 16:02:15 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-06-30 15:05:31 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.012 |  |
| 2026-06-30 16:03:19 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | -0.020 |  |
| 2026-06-30 15:01:33 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.020 |  |
| 2026-06-30 15:01:24 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.025 |  |
| 2026-06-30 16:03:50 | Baddegama (Gin Ganga) | 2.58 | 🟢 Normal | -0.031 |  |
| 2026-06-30 16:03:35 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | -0.040 |  |
| 2026-06-30 16:03:38 | Hanwella (Kelani Ganga) | 2.56 | 🟢 Normal | -0.040 |  |
| 2026-06-30 15:01:29 | Panadugama (Nilwala Ganga) | 3.22 | 🟢 Normal | -0.052 |  |
| 2026-06-30 15:14:25 | Ellagawa (Kalu Ganga) | 7.79 | 🟢 Normal | -0.062 |  |
| 2026-06-30 16:04:45 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | -0.070 |  |
| 2026-06-30 16:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.17 | 🟢 Normal | -0.070 |  |
| 2026-06-30 16:03:19 | Rathnapura (Kalu Ganga) | 3.03 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)