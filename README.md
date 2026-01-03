# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--03_12:11:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **35,488 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 12:11:47 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.027 |  |
| 2026-01-03 12:07:36 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:07:19 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.034 |  |
| 2026-01-03 12:05:47 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-01-03 12:05:18 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-01-03 12:04:50 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:04:48 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.009 |  |
| 2026-01-03 12:04:43 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:04:34 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-03 12:04:25 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.062 |  |
| 2026-01-03 12:04:14 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:04:12 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-01-03 12:04:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-01-03 12:04:07 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:04:03 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-03 12:03:59 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:03:47 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:03:39 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:03:29 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-01-03 12:03:23 | Manampitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.020 |  |
| 2026-01-03 12:03:22 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-01-03 12:02:55 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-01-03 12:02:47 | Galgamuwa (Mee Oya) | 2.30 | 🟢 Normal | 0.920 | 🔺 Rising |
| 2026-01-03 12:02:40 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:02:37 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:02:36 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:02:30 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.029 |  |
| 2026-01-03 12:02:17 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:02:05 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:01:56 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:01:40 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | -0.010 |  |
| 2026-01-03 12:01:39 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:01:31 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.040 |  |
| 2026-01-03 12:01:10 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-01-03 12:00:49 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-03 12:00:15 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:00:05 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-01-03 11:58:06 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | -72.000 |  |
| 2026-01-03 11:58:05 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | -72.000 |  |
| 2026-01-03 11:17:32 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | -0.008 |  |
| 2026-01-03 11:14:52 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.034 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 12:02:47 | Galgamuwa (Mee Oya) | 2.30 | 🟢 Normal | 0.920 | 🔺 Rising |
| 2026-01-03 12:04:12 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-01-03 12:04:03 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-03 12:02:37 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:00:15 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:04:07 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:02:05 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:02:36 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:03:47 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:07:36 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:04:50 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:02:17 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:04:14 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:01:39 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:03:59 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:01:56 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-03 12:04:43 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:17:32 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | -0.008 |  |
| 2026-01-03 12:04:48 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.009 |  |
| 2026-01-03 12:04:34 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-03 12:01:10 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-01-03 12:03:22 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-01-03 12:03:29 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-01-03 12:00:05 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-01-03 12:00:49 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-03 12:01:40 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | -0.010 |  |
| 2026-01-03 12:05:18 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-01-03 12:04:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-01-03 12:02:55 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-01-03 12:03:23 | Manampitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.020 |  |
| 2026-01-03 12:05:47 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-01-03 12:11:47 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.027 |  |
| 2026-01-03 12:02:30 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.029 |  |
| 2026-01-03 12:07:19 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.034 |  |
| 2026-01-03 11:08:13 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.035 |  |
| 2026-01-03 12:01:31 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.040 |  |
| 2026-01-03 12:04:25 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.062 |  |
| 2026-01-03 11:58:06 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)