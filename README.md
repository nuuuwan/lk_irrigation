# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--27_14:10:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **217,678 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-27 14:10:46 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-07-27 14:09:08 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:08:13 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:07:59 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:07:03 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-27 14:06:56 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:06:54 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:06:09 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:06:00 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-27 14:05:56 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:05:43 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.088 |  |
| 2026-07-27 14:04:55 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:04:37 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:04:06 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:03:54 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:03:34 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-27 14:03:24 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-27 14:03:24 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-07-27 14:03:16 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-27 14:03:12 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-07-27 14:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-07-27 14:03:04 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-07-27 14:02:44 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:02:40 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-07-27 14:02:27 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-27 14:02:20 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:02:20 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | -0.010 |  |
| 2026-07-27 14:02:16 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:02:13 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:02:11 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:02:08 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.030 |  |
| 2026-07-27 14:01:33 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:01:29 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:01:12 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:00:50 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-07-27 14:00:49 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-27 14:00:46 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-27 14:02:40 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-07-27 14:10:46 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-07-27 14:03:16 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-27 14:03:24 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-27 14:02:27 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-27 14:03:34 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-27 14:00:49 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-27 14:07:03 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-27 14:06:00 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-27 14:02:16 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-27 13:00:51 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:00:46 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:08:13 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:01:29 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:03:54 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:07:59 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:02:44 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:01:33 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:05:56 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:02:11 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:06:54 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:06:09 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:04:55 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:02:13 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:06:56 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:04:06 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:01:12 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:09:08 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:04:37 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:02:20 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-27 14:03:12 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-07-27 14:03:04 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-07-27 14:02:20 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | -0.010 |  |
| 2026-07-27 14:00:50 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-07-27 14:03:24 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-07-27 14:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-07-27 14:02:08 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.030 |  |
| 2026-07-27 14:05:43 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)