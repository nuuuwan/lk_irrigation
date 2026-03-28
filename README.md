# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_03:50:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **110,191 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-29 03:50:22 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-03-29 03:33:36 | Ellagawa (Kalu Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:33:34 | Ellagawa (Kalu Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:32:05 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 5.021 | 🔺 Rising |
| 2026-03-29 03:20:01 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:17:25 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | -0.003 |  |
| 2026-03-29 03:10:27 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:10:20 | Panadugama (Nilwala Ganga) | 0.05 | 🟢 Normal | 5.021 | 🔺 Rising |
| 2026-03-29 03:09:48 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | 5.143 | 🔺 Rising |
| 2026-03-29 03:09:37 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:09:13 | Thawalama (Gin Ganga) | 0.84 | 🟢 Normal | 5.143 | 🔺 Rising |
| 2026-03-29 03:09:12 | Thawalama (Gin Ganga) | 0.79 | 🟢 Normal | 5.143 | 🔺 Rising |
| 2026-03-29 03:09:09 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-29 03:08:24 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:07:33 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 5.021 | 🔺 Rising |
| 2026-03-29 03:06:45 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-03-29 03:06:43 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.037 |  |
| 2026-03-29 03:06:42 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:06:23 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | -0.009 |  |
| 2026-03-29 03:06:19 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:05:51 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:05:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 03:04:59 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-29 03:04:58 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:04:13 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-03-29 03:03:29 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:03:12 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | -0.022 |  |
| 2026-03-29 03:03:10 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.174 |  |
| 2026-03-29 03:02:59 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:02:52 | Hanwella (Kelani Ganga) | 0.23 | 🟢 Normal | -0.011 |  |
| 2026-03-29 03:02:21 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:02:19 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 03:02:17 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:02:16 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:02:15 | Norwood (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:01:29 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 03:00:44 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-29 03:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-29 03:09:48 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | 5.143 | 🔺 Rising |
| 2026-03-29 03:32:05 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 5.021 | 🔺 Rising |
| 2026-03-29 03:00:44 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-29 03:04:59 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-29 03:09:09 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-29 03:50:22 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-03-29 03:05:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 03:01:29 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 03:02:19 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 03:04:58 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:02:21 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-29 01:03:14 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:02:16 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-28 18:03:02 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-28 23:03:22 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-29 02:08:22 | Pitabeddara (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:02:15 | Norwood (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:33:36 | Ellagawa (Kalu Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-03-29 02:05:15 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:03:29 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:06:42 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:02:17 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:20:01 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:10:27 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:05:51 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-29 02:11:41 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:02:59 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:08:24 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-28 18:04:13 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:17:25 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | -0.003 |  |
| 2026-03-29 03:06:23 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | -0.009 |  |
| 2026-03-29 03:04:13 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-03-29 03:06:45 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-03-29 03:02:52 | Hanwella (Kelani Ganga) | 0.23 | 🟢 Normal | -0.011 |  |
| 2026-03-29 03:03:12 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | -0.022 |  |
| 2026-03-29 03:06:43 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.037 |  |
| 2026-03-29 03:03:10 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.174 |  |
| 2026-03-28 18:02:29 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.215 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)