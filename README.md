# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_04:17:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **157,524 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 04:17:18 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-21 04:16:53 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-21 04:13:32 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-21 04:13:02 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.059 |  |
| 2026-05-21 04:08:46 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-05-21 04:07:23 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.007 |  |
| 2026-05-21 04:06:32 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.005 |  |
| 2026-05-21 04:05:59 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 04:04:44 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-21 04:04:11 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-21 04:03:49 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-21 04:03:03 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | 1.096 | 🔺 Rising |
| 2026-05-21 04:02:49 | Glencourse (Kelani Ganga) | 10.17 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-05-21 04:02:43 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-21 04:02:41 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.143 |  |
| 2026-05-21 04:02:40 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.488 | 🔺 Rising |
| 2026-05-21 04:02:35 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-05-21 04:02:23 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-21 04:02:20 | Hanwella (Kelani Ganga) | 1.90 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-05-21 04:02:19 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-21 04:02:08 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-21 04:01:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.33 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-21 04:01:17 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-05-21 04:01:12 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 04:01:05 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-21 04:01:03 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-21 04:00:49 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-21 04:00:47 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:45:33 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.012 |  |
| 2026-05-21 03:41:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.31 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-21 03:40:50 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -1.895 |  |
| 2026-05-21 03:40:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-21 03:40:31 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -1.895 |  |
| 2026-05-21 03:38:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.25 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-21 03:38:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | 0.059 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 04:03:03 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | 1.096 | 🔺 Rising |
| 2026-05-21 04:02:40 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.488 | 🔺 Rising |
| 2026-05-21 04:02:49 | Glencourse (Kelani Ganga) | 10.17 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-05-21 04:02:35 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-05-21 04:02:20 | Hanwella (Kelani Ganga) | 1.90 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-05-21 04:01:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.33 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-21 04:13:32 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-21 03:03:53 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-21 04:04:11 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-21 04:01:12 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 04:05:59 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 18:01:24 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-05-21 04:00:47 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:02:16 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 04:03:49 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-21 04:01:03 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-21 04:02:23 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-21 04:02:08 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-21 04:17:18 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-21 04:01:05 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-21 04:02:43 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-21 04:00:49 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-21 04:04:44 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-21 03:03:50 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-21 04:06:32 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.005 |  |
| 2026-05-21 04:07:23 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.007 |  |
| 2026-05-21 03:10:58 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-05-21 04:08:46 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-05-21 04:02:19 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-20 18:01:19 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-05-21 04:01:17 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-05-21 03:45:33 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.012 |  |
| 2026-05-21 03:02:53 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.020 |  |
| 2026-05-21 03:10:41 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.027 |  |
| 2026-05-20 18:02:19 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.030 |  |
| 2026-05-21 03:02:58 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | -0.041 |  |
| 2026-05-21 04:13:02 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.059 |  |
| 2026-05-21 04:02:41 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.143 |  |
| 2026-05-21 03:40:50 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -1.895 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)