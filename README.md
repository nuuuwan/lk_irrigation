# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--28_05:18:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **57,643 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **48** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-28 05:18:11 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.017 |  |
| 2026-01-28 05:16:15 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:15:01 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:12:01 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:11:41 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:11:28 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:11:27 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:08:46 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:08:45 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:08:22 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-28 05:07:01 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.032 |  |
| 2026-01-28 05:06:47 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:06:02 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:05:52 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:05:07 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | -0.009 |  |
| 2026-01-28 05:05:02 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.117 |  |
| 2026-01-28 05:04:48 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:04:37 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-28 05:04:15 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | -0.030 |  |
| 2026-01-28 05:04:09 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-01-28 05:04:00 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -180.000 |  |
| 2026-01-28 05:03:59 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -180.000 |  |
| 2026-01-28 05:03:57 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -180.000 |  |
| 2026-01-28 05:03:56 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -180.000 |  |
| 2026-01-28 05:03:56 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:03:52 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.048 |  |
| 2026-01-28 05:03:43 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.040 |  |
| 2026-01-28 05:03:06 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:03:04 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:03:03 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:02:51 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:02:33 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-28 05:02:30 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:02:01 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:01:55 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | -0.005 |  |
| 2026-01-28 05:01:50 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-28 05:01:44 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:01:18 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:01:12 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:01:10 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.174 |  |
| 2026-01-28 05:01:10 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:00:29 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-28 04:39:43 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-28 04:29:35 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.032 |  |
| 2026-01-28 04:25:53 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-01-28 04:23:59 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.117 |  |
| 2026-01-28 04:22:24 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-28 05:04:09 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-01-27 18:01:37 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-28 05:08:22 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-28 05:02:33 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-28 05:04:37 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-28 05:01:50 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-28 05:01:12 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:11:41 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:02:01 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:04:48 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:03:04 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:11:28 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:06:02 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:02:51 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:16:15 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:05:52 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:15:01 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:00:29 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:03:06 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:02:30 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:03:56 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:01:18 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:08:46 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:01:44 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:12:01 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:01:10 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:06:47 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-28 05:01:55 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | -0.005 |  |
| 2026-01-28 05:05:07 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | -0.009 |  |
| 2026-01-27 17:06:09 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-01-28 05:18:11 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.017 |  |
| 2026-01-27 18:02:53 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-01-28 05:04:15 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | -0.030 |  |
| 2026-01-28 05:07:01 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.032 |  |
| 2026-01-28 05:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.040 |  |
| 2026-01-28 05:03:52 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.048 |  |
| 2026-01-28 05:05:02 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.117 |  |
| 2026-01-28 05:01:10 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.174 |  |
| 2026-01-28 05:04:00 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -180.000 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)