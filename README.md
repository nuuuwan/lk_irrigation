# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--20_17:05:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **50,920 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-20 17:05:46 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:05:18 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:05:15 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-20 17:05:12 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 17:04:54 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-20 17:04:53 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-01-20 17:04:52 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | -0.011 |  |
| 2026-01-20 17:04:50 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:04:22 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.010 |  |
| 2026-01-20 17:03:32 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:03:27 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-20 17:02:59 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-01-20 17:02:55 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-20 17:02:54 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-20 17:02:54 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-20 17:02:37 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.040 |  |
| 2026-01-20 17:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-01-20 17:02:22 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:02:21 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.020 |  |
| 2026-01-20 17:02:07 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:02:01 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-20 17:01:56 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-01-20 17:01:56 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:01:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.060 |  |
| 2026-01-20 17:01:41 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:01:17 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:01:01 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:00:41 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:00:40 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:00:14 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:28:06 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:20:15 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:19:23 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-20 16:19:20 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:13:13 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-01-20 16:09:20 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-20 15:16:50 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.559 | 🔺 Rising |
| 2026-01-20 17:01:56 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-01-20 17:04:54 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-20 17:03:27 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-20 17:02:54 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-20 17:05:15 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-20 16:19:23 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-20 17:05:12 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 17:01:01 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:00:40 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:00:14 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:28:06 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:20:15 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:03:32 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:03:01 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:01:41 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:04:50 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:01:56 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:19:20 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:05:18 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:02:07 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:02:32 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:05:46 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:00:41 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:01:17 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:02:22 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:02:54 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-20 17:02:55 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-20 17:02:01 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-20 17:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-01-20 17:04:22 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.010 |  |
| 2026-01-20 16:03:57 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.011 |  |
| 2026-01-20 17:04:52 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | -0.011 |  |
| 2026-01-20 17:02:59 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-01-20 17:02:21 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.020 |  |
| 2026-01-20 17:04:53 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-01-20 17:02:37 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.040 |  |
| 2026-01-20 17:01:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.060 |  |
| 2026-01-20 16:05:03 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)