# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_17:08:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **116,105 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 17:08:42 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-04-04 17:07:48 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.038 |  |
| 2026-04-04 17:07:41 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.019 |  |
| 2026-04-04 17:06:58 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-04 17:06:48 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-04-04 17:06:32 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.125 |  |
| 2026-04-04 17:06:21 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | -0.020 |  |
| 2026-04-04 17:06:17 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-04-04 17:06:00 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:05:25 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:04:27 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-04-04 17:04:11 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-04-04 17:03:49 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-04-04 17:03:33 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:03:17 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:02:53 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-04 17:02:50 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-04 17:02:36 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 17:02:30 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:02:29 | Manampitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-04 17:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.040 |  |
| 2026-04-04 17:02:23 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 17:02:16 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:02:06 | Thanthirimale (Malwathu Oya) | 2.55 | 🟢 Normal | -0.020 |  |
| 2026-04-04 17:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:01:33 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:01:21 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | -0.020 |  |
| 2026-04-04 17:01:19 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-04-04 17:00:48 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.031 |  |
| 2026-04-04 17:00:31 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-04-04 17:00:28 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:00:10 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:00:08 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-04 16:20:16 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:20:14 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.040 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 17:06:48 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-04-04 17:01:19 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-04-04 17:02:50 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-04 16:15:28 | Horowpothana (Yan Oya) | 1.96 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-04 16:20:14 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-04 17:02:29 | Manampitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-04 17:02:53 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-04 17:06:58 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-04 17:02:23 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 17:02:36 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 17:03:33 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:02:30 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:01:33 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:06:00 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:03:17 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:02:16 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:00:10 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:02:55 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:05:25 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:20:16 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:00:28 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:04:27 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-04-04 17:04:11 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-04-04 17:06:17 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-04-04 17:03:49 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-04-04 15:02:24 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-04 17:00:08 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-04 17:00:31 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-04-04 17:07:41 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.019 |  |
| 2026-04-04 17:02:06 | Thanthirimale (Malwathu Oya) | 2.55 | 🟢 Normal | -0.020 |  |
| 2026-04-04 17:06:21 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | -0.020 |  |
| 2026-04-04 17:01:21 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | -0.020 |  |
| 2026-04-04 17:08:42 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-04-04 17:00:48 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.031 |  |
| 2026-04-04 16:05:42 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.032 |  |
| 2026-04-04 17:07:48 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.038 |  |
| 2026-04-04 17:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.040 |  |
| 2026-04-04 17:06:32 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)