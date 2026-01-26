# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--26_15:15:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **56,241 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-26 15:15:49 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-26 15:11:30 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:10:12 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:07:20 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:07:15 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:06:46 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:06:19 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-01-26 15:06:16 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:05:45 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-01-26 15:04:54 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-26 15:04:43 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 15:04:43 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-26 15:04:41 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:04:31 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:04:07 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:03:51 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -55.636 |  |
| 2026-01-26 15:03:40 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -55.636 |  |
| 2026-01-26 15:03:27 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-26 15:03:26 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-26 15:03:22 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:03:19 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:03:12 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:02:55 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.012 |  |
| 2026-01-26 15:02:50 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-26 15:02:48 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:02:47 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:02:41 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | -0.049 |  |
| 2026-01-26 15:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-26 15:02:28 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:02:26 | Weraganthota (Mahaweli Ganga) | -2.08 | 🟢 Normal | -0.140 |  |
| 2026-01-26 15:02:23 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:02:18 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:02:11 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-26 15:02:10 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:01:49 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | -0.063 |  |
| 2026-01-26 15:01:27 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:01:21 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:01:16 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:01:10 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.108 |  |
| 2026-01-26 15:00:40 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-26 15:06:19 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-01-26 15:03:27 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-26 15:03:26 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-26 15:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-26 15:15:49 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-26 15:04:54 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-26 15:02:11 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-26 15:02:50 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-26 15:04:43 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 15:11:30 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:01:16 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:02:18 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:00:40 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:04:07 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:01:21 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:02:47 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:04:41 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:07:15 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:03:12 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:03:22 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:02:23 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:04:31 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:07:20 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:02:10 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:03:19 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:06:16 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:02:48 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:01:27 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:10:12 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:02:28 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:06:46 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-26 15:05:45 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-01-26 15:04:43 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-26 15:02:55 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.012 |  |
| 2026-01-26 15:02:41 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | -0.049 |  |
| 2026-01-26 15:01:49 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | -0.063 |  |
| 2026-01-26 15:01:10 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.108 |  |
| 2026-01-26 15:02:26 | Weraganthota (Mahaweli Ganga) | -2.08 | 🟢 Normal | -0.140 |  |
| 2026-01-26 15:03:51 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -55.636 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)