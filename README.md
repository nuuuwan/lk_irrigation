# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_12:21:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **129,268 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-19 12:21:30 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.015 |  |
| 2026-04-19 12:17:19 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:09:33 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.027 |  |
| 2026-04-19 12:09:24 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:09:12 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-04-19 12:08:16 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:07:45 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | -0.009 |  |
| 2026-04-19 12:06:29 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:06:21 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-19 12:06:09 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-19 12:06:00 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-04-19 12:05:05 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:04:54 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-04-19 12:04:40 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-19 12:04:30 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.031 |  |
| 2026-04-19 12:03:58 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 1.584 | 🔺 Rising |
| 2026-04-19 12:03:36 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:03:26 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:03:07 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:02:48 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.022 |  |
| 2026-04-19 12:02:45 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:02:42 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-04-19 12:02:25 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-04-19 12:02:20 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-19 12:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.033 |  |
| 2026-04-19 12:02:19 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 12:02:18 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 12:02:17 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:02:14 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:01:48 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:01:40 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:01:32 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:01:16 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.080 |  |
| 2026-04-19 12:01:15 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:01:07 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:01:07 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-19 12:00:43 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:00:13 | Weraganthota (Mahaweli Ganga) | -2.36 | 🟢 Normal | -0.093 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-19 12:03:58 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 1.584 | 🔺 Rising |
| 2026-04-19 12:06:00 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-04-19 12:02:20 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-19 12:01:07 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-19 12:06:09 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-19 12:02:19 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 12:02:18 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 12:02:17 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:01:32 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:01:40 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:02:14 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:03:26 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:05:05 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:06:29 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:01:07 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:03:07 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:09:24 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:01:48 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:02:45 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:17:19 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:03:36 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:08:16 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:01:15 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:07:45 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | -0.009 |  |
| 2026-04-19 12:04:40 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-19 12:02:25 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-04-19 12:06:21 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-19 12:04:54 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-04-19 12:02:42 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-04-19 11:03:37 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | -0.012 |  |
| 2026-04-19 12:21:30 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.015 |  |
| 2026-04-19 12:09:12 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-04-19 12:02:48 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.022 |  |
| 2026-04-19 12:09:33 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.027 |  |
| 2026-04-19 12:04:30 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.031 |  |
| 2026-04-19 12:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.033 |  |
| 2026-04-19 12:01:16 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.080 |  |
| 2026-04-19 06:01:33 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.086 |  |
| 2026-04-19 12:00:13 | Weraganthota (Mahaweli Ganga) | -2.36 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)