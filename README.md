# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_06:11:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **115,680 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **46** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 06:11:52 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-04 06:11:43 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | -72.000 |  |
| 2026-04-04 06:11:41 | Padiyathalawa (Maduru Oya) | 0.50 | 🟢 Normal | -72.000 |  |
| 2026-04-04 06:11:40 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | -72.000 |  |
| 2026-04-04 06:11:39 | Padiyathalawa (Maduru Oya) | 0.61 | 🟢 Normal | -72.000 |  |
| 2026-04-04 06:11:37 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | -72.000 |  |
| 2026-04-04 06:11:36 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | -72.000 |  |
| 2026-04-04 06:09:41 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.047 |  |
| 2026-04-04 06:07:55 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-04-04 06:07:26 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -108.000 |  |
| 2026-04-04 06:07:25 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -108.000 |  |
| 2026-04-04 06:07:19 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.152 |  |
| 2026-04-04 06:06:26 | Kithulgala (Kelani Ganga) | 1.21 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-04-04 06:05:44 | Manampitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.065 |  |
| 2026-04-04 06:05:44 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-04-04 06:05:42 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.047 |  |
| 2026-04-04 06:05:34 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-04 06:05:15 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.011 |  |
| 2026-04-04 06:04:04 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-04 06:03:59 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 06:03:55 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-04 06:03:53 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-04 06:03:51 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-04-04 06:03:50 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-04-04 06:03:37 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | -0.010 |  |
| 2026-04-04 06:03:03 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-04-04 06:02:34 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-04 06:02:32 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-04-04 06:02:30 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-04 06:02:26 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-04-04 06:02:25 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-04 06:02:13 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-04 06:02:13 | Magura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.275 |  |
| 2026-04-04 06:01:54 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-04 06:01:45 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.074 |  |
| 2026-04-04 06:01:43 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 06:01:42 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 06:01:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.25 | 🟢 Normal | -0.179 |  |
| 2026-04-04 06:01:31 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-04-04 06:01:30 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.127 |  |
| 2026-04-04 06:01:00 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-04 06:00:21 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-04 06:00:19 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-04 05:51:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | -0.179 |  |
| 2026-04-04 05:33:44 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-04-04 05:33:43 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.159 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 06:03:50 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-04-04 06:03:03 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-04-04 06:00:19 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-04 06:06:26 | Kithulgala (Kelani Ganga) | 1.21 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-04-04 06:01:00 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-04 06:02:34 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-04 06:01:54 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-03 18:05:32 | Thanthirimale (Malwathu Oya) | 3.43 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-04 06:03:53 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-04 06:04:04 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-04 06:03:55 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-04 06:11:52 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-04 06:01:43 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 18:02:55 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 06:01:42 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 06:03:59 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 06:00:21 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-04 06:02:30 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-04 06:05:34 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-04 06:02:25 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-04 06:02:13 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-04 06:05:44 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-04-04 06:03:37 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | -0.010 |  |
| 2026-04-04 06:03:51 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-04-04 06:02:32 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-04-04 06:05:15 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.011 |  |
| 2026-04-04 06:07:55 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-04-04 06:02:26 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-04-04 06:01:31 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-04-04 06:05:42 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.047 |  |
| 2026-04-04 06:09:41 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.047 |  |
| 2026-04-04 06:05:44 | Manampitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.065 |  |
| 2026-04-04 06:01:45 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.074 |  |
| 2026-04-04 06:01:30 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.127 |  |
| 2026-04-04 06:07:19 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.152 |  |
| 2026-04-04 06:01:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.25 | 🟢 Normal | -0.179 |  |
| 2026-04-04 06:02:13 | Magura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.275 |  |
| 2026-04-04 06:11:43 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | -72.000 |  |
| 2026-04-04 06:07:26 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)