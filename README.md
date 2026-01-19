# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--20_04:06:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **50,418 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-20 04:06:39 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:06:24 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:06:01 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:05:43 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:05:29 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:05:09 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:05:08 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:04:09 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.070 |  |
| 2026-01-20 04:03:45 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:03:36 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | -0.005 |  |
| 2026-01-20 04:03:24 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-01-20 04:03:21 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:03:20 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:03:17 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-20 04:03:12 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:03:05 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:03:02 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.117 |  |
| 2026-01-20 04:02:55 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:02:49 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.052 |  |
| 2026-01-20 04:02:15 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:02:05 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:01:53 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:01:51 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:01:41 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:01:37 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-20 04:01:14 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:00:20 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:00:13 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-01-20 03:35:17 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:35:15 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:13:26 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-01-20 03:13:22 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-01-20 03:13:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-01-20 03:11:41 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:11:15 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-20 04:03:24 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-01-20 03:13:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-01-20 00:03:48 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-01-20 04:00:13 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-01-20 03:04:25 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-20 04:03:17 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-20 03:04:06 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | 0.005 |  |
| 2026-01-20 04:00:20 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:02:43 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:01:41 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:02:05 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:02:55 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:06:39 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:03:09 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:01:51 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:03:05 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:02:15 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:03:45 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:03:46 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:03:12 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:03:20 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:03:21 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-20 01:03:22 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-20 03:35:17 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:05:08 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:05:43 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-19 18:02:06 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:06:24 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:01:53 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:01:14 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:03:36 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | -0.005 |  |
| 2026-01-20 01:08:42 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | -0.009 |  |
| 2026-01-19 18:01:58 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-01-19 18:00:21 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | -0.010 |  |
| 2026-01-20 04:01:37 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-20 04:02:49 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.052 |  |
| 2026-01-20 04:04:09 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.070 |  |
| 2026-01-20 04:03:02 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)