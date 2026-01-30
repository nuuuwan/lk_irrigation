# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--31_02:29:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **60,220 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 02:29:44 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:25:09 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:15:39 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-31 02:14:50 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:11:21 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-01-31 02:09:54 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.028 |  |
| 2026-01-31 02:07:15 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-01-31 02:07:07 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-01-31 02:07:01 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.089 |  |
| 2026-01-31 02:05:56 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:05:34 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:05:26 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:04:56 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:03:40 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-31 02:02:57 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:02:42 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:02:17 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:02:14 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-31 02:01:51 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:01:44 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.136 |  |
| 2026-01-31 02:01:38 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:01:12 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:01:01 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-31 01:40:09 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 02:11:21 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-01-31 01:29:53 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-31 02:03:40 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-31 02:02:14 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-30 18:02:48 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 02:15:39 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-31 02:01:01 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-31 01:01:19 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:01:38 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:01:51 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:05:26 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-31 01:04:08 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-30 18:03:49 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:25:09 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 01:02:28 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:02:17 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-31 01:00:52 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:05:56 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:29:44 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:02:42 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:02:57 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:01:12 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:05:34 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-31 01:03:33 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:14:50 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:04:56 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-30 18:02:10 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-31 01:09:33 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-31 01:01:49 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-31 01:03:33 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-31 01:04:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:07:15 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-01-31 02:07:07 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-01-31 01:01:58 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-01-31 01:03:41 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-01-31 00:03:17 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.022 |  |
| 2026-01-31 02:09:54 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.028 |  |
| 2026-01-31 02:07:01 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.089 |  |
| 2026-01-31 02:01:44 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.136 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)