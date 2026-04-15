# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_03:30:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **126,263 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 03:30:44 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.005 |  |
| 2026-04-16 03:19:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | 4.000 | 🔺 Rising |
| 2026-04-16 03:18:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 4.000 | 🔺 Rising |
| 2026-04-16 03:16:18 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -144.000 |  |
| 2026-04-16 03:16:17 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | -144.000 |  |
| 2026-04-16 03:11:36 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-16 03:10:46 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-16 03:10:28 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-16 03:07:36 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 288.000 | 🔺 Rising |
| 2026-04-16 03:07:35 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 288.000 | 🔺 Rising |
| 2026-04-16 03:06:31 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.009 |  |
| 2026-04-16 03:06:04 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 15.344 | 🔺 Rising |
| 2026-04-16 03:04:38 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 03:04:14 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.019 |  |
| 2026-04-16 03:04:11 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-04-16 03:03:55 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-04-16 03:03:08 | Kithulgala (Kelani Ganga) | 1.17 | 🟢 Normal | -0.263 |  |
| 2026-04-16 03:02:49 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-16 03:02:41 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 03:02:39 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.013 |  |
| 2026-04-16 03:02:39 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 03:02:30 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-16 03:02:25 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 03:02:20 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-04-16 03:02:00 | Badalgama (Maha Oya) | 0.85 | 🟢 Normal | 15.344 | 🔺 Rising |
| 2026-04-16 03:01:47 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-16 03:01:36 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-16 03:01:28 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | -0.010 |  |
| 2026-04-16 03:01:14 | Kuda Oya (Kirindi Oya) | 2.45 | 🟢 Normal | 0.839 | 🔺 Rising |
| 2026-04-16 03:01:14 | Glencourse (Kelani Ganga) | 9.02 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-16 03:01:08 | Pitabeddara (Nilwala Ganga) | 2.33 | 🟢 Normal | 4.870 | 🔺 Rising |
| 2026-04-16 03:00:43 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.135 |  |
| 2026-04-16 03:00:16 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.528 |  |
| 2026-04-16 03:00:12 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.101 |  |
| 2026-04-16 02:44:22 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.528 |  |
| 2026-04-16 02:44:00 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.528 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 03:07:36 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 288.000 | 🔺 Rising |
| 2026-04-16 03:06:04 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 15.344 | 🔺 Rising |
| 2026-04-16 03:01:08 | Pitabeddara (Nilwala Ganga) | 2.33 | 🟢 Normal | 4.870 | 🔺 Rising |
| 2026-04-16 03:19:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | 4.000 | 🔺 Rising |
| 2026-04-16 03:01:14 | Kuda Oya (Kirindi Oya) | 2.45 | 🟢 Normal | 0.839 | 🔺 Rising |
| 2026-04-16 00:09:08 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-16 03:10:28 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-16 03:01:14 | Glencourse (Kelani Ganga) | 9.02 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-16 03:02:49 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-16 03:02:41 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 02:02:39 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:01:26 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 03:02:25 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:02:05 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:00:07 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-16 03:02:39 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:02:52 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-16 03:04:38 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 03:10:46 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-16 03:11:36 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-16 03:01:36 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-16 03:04:11 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:04:30 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-16 03:30:44 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.005 |  |
| 2026-04-16 03:06:31 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.009 |  |
| 2026-04-16 03:01:47 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-16 03:01:28 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | -0.010 |  |
| 2026-04-16 03:02:20 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-04-16 03:02:30 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-16 03:02:39 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.013 |  |
| 2026-04-16 03:04:14 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.019 |  |
| 2026-04-16 03:03:55 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-04-15 18:05:24 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.038 |  |
| 2026-04-15 18:01:03 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.062 |  |
| 2026-04-16 03:00:12 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.101 |  |
| 2026-04-16 03:00:43 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.135 |  |
| 2026-04-16 03:03:08 | Kithulgala (Kelani Ganga) | 1.17 | 🟢 Normal | -0.263 |  |
| 2026-04-16 03:00:16 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.528 |  |
| 2026-04-16 03:16:18 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)