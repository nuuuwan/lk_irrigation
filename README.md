# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--28_05:17:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **218,218 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-28 05:17:21 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.009 |  |
| 2026-07-28 05:16:12 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-07-28 05:14:48 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | -0.009 |  |
| 2026-07-28 05:14:05 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-07-28 05:11:27 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:11:23 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.026 |  |
| 2026-07-28 05:10:51 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:09:48 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:08:35 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:07:45 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-07-28 05:07:14 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:06:04 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.046 |  |
| 2026-07-28 05:05:32 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-07-28 05:05:12 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:04:45 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:04:21 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:03:59 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:03:56 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-28 05:03:46 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.078 |  |
| 2026-07-28 05:03:44 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:03:11 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:03:10 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-28 05:03:03 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:03:02 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:02:58 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:02:49 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:02:39 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.118 |  |
| 2026-07-28 05:01:47 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:01:42 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:01:36 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:01:31 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.128 |  |
| 2026-07-28 05:01:29 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:01:08 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:00:47 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:00:26 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:59:06 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:43:17 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-07-28 04:42:22 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.047 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-28 01:16:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-07-28 05:05:32 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-07-28 05:07:45 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-07-28 05:03:56 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-28 05:03:10 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-28 05:14:05 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-07-28 05:16:12 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-07-28 05:00:47 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:05:12 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:01:42 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:01:38 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:01:47 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:02:49 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:03:06 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:03:53 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:04:21 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:01:29 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:01:08 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:11:27 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:07:14 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:08:35 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:01:36 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:03:21 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:09:48 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:02:58 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:00:26 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:03:11 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:00:30 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:04:45 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:03:03 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:03:02 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-28 05:14:48 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | -0.009 |  |
| 2026-07-28 05:17:21 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.009 |  |
| 2026-07-27 18:01:36 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.020 |  |
| 2026-07-28 05:11:23 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.026 |  |
| 2026-07-28 05:06:04 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.046 |  |
| 2026-07-28 05:03:46 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.078 |  |
| 2026-07-28 05:02:39 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.118 |  |
| 2026-07-28 05:01:31 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.128 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)