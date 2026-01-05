# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--06_02:07:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,781 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 02:07:21 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-01-06 02:06:37 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-06 02:04:59 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 02:04:30 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-06 02:04:03 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.054 |  |
| 2026-01-06 02:03:51 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-01-06 02:03:46 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-06 02:03:42 | Siyambalanduwa (Heda Oya) | 1.98 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-01-06 02:03:31 | Peradeniya (Mahaweli Ganga) | 2.59 | 🟢 Normal | -0.059 |  |
| 2026-01-06 02:03:24 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-06 02:03:18 | Padiyathalawa (Maduru Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-01-06 02:02:37 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-06 02:02:36 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-06 02:02:05 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-06 02:01:57 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-01-06 02:01:55 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-01-06 02:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-06 02:01:10 | Manampitiya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 02:01:04 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-06 02:00:24 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-01-06 02:00:04 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 01:33:14 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-01-06 01:17:52 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.016 |  |
| 2026-01-06 01:10:49 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-01-06 01:10:13 | Siyambalanduwa (Heda Oya) | 1.76 | 🟢 Normal | 0.247 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 02:01:57 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-01-06 00:09:00 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 4.154 | 🔺 Rising |
| 2026-01-06 02:03:42 | Siyambalanduwa (Heda Oya) | 1.98 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-01-05 23:06:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-01-06 02:03:51 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-01-06 01:10:49 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-01-05 18:04:03 | Weraganthota (Mahaweli Ganga) | -1.35 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-01-06 02:00:24 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-01-06 01:33:14 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-01-06 01:04:53 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-06 02:02:05 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-06 00:03:06 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-06 01:04:02 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-06 02:01:10 | Manampitiya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 01:01:05 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-06 02:02:37 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-06 02:01:04 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-06 02:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-06 02:03:46 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-06 02:06:37 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:12:56 | Galgamuwa (Mee Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-06 02:02:36 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-06 02:03:24 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-06 02:04:30 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-06 02:03:18 | Padiyathalawa (Maduru Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-01-05 23:00:10 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-06 02:04:59 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 01:02:48 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 01:05:45 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-06 01:02:23 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-06 02:07:21 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-01-06 00:04:36 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.010 |  |
| 2026-01-06 01:03:38 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-05 18:04:30 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-01-06 01:01:08 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-01-06 01:17:52 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.016 |  |
| 2026-01-06 01:00:53 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-01-06 02:04:03 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.054 |  |
| 2026-01-06 02:03:31 | Peradeniya (Mahaweli Ganga) | 2.59 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)