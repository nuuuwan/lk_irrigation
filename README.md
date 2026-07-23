# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--24_02:32:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **214,542 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-24 02:32:02 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:25:12 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:25:11 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:25:07 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.057 |  |
| 2026-07-24 02:17:44 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:17:31 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.016 |  |
| 2026-07-24 02:13:51 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-07-24 02:09:47 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:08:35 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.009 |  |
| 2026-07-24 02:06:37 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:06:17 | Thalgahagoda (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-24 02:06:16 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-07-24 02:06:01 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:05:00 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | -0.009 |  |
| 2026-07-24 02:04:41 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-07-24 02:04:06 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.057 |  |
| 2026-07-24 02:03:38 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:03:35 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:03:33 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.045 |  |
| 2026-07-24 02:03:29 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:03:22 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-07-24 02:03:07 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:03:05 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:02:58 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.102 |  |
| 2026-07-24 02:02:56 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-07-24 02:02:44 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:02:21 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:02:09 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-07-24 02:01:54 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:01:15 | Holombuwa (Kelani Ganga) | 2.00 | 🟢 Normal | 1.694 | 🔺 Rising |
| 2026-07-24 02:01:05 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.060 |  |
| 2026-07-24 02:00:25 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:58:50 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:56:14 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:53:16 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-07-24 01:53:07 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:49:29 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-24 02:01:15 | Holombuwa (Kelani Ganga) | 2.00 | 🟢 Normal | 1.694 | 🔺 Rising |
| 2026-07-24 02:04:41 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-07-24 02:02:09 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-07-24 02:13:51 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-07-24 02:06:16 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-07-24 02:06:17 | Thalgahagoda (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-24 02:32:02 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:03:38 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:00:25 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:05:34 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:02:21 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:01:54 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-23 18:04:13 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:25:12 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:06:01 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:09:47 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:02:56 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-24 01:00:14 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:03:29 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:03:05 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:02:44 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:03:35 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:03:07 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-07-23 18:01:54 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:17:44 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-24 02:06:37 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-23 20:53:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-24 00:18:28 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.004 |  |
| 2026-07-24 00:04:24 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.005 |  |
| 2026-07-24 02:08:35 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.009 |  |
| 2026-07-24 02:05:00 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | -0.009 |  |
| 2026-07-24 01:06:06 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-07-24 02:17:31 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.016 |  |
| 2026-07-24 02:02:56 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-07-24 02:03:33 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.045 |  |
| 2026-07-24 02:25:07 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.057 |  |
| 2026-07-24 02:01:05 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.060 |  |
| 2026-07-24 02:02:58 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.102 |  |
| 2026-07-23 18:06:44 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)