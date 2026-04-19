# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_17:16:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **129,459 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-19 17:16:24 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:13:36 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-19 17:13:09 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-19 17:10:30 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-19 17:10:04 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:09:56 | Peradeniya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-04-19 17:09:31 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-19 17:09:04 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-19 17:08:20 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:07:14 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-19 17:06:58 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-19 17:06:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:06:31 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.062 |  |
| 2026-04-19 17:06:03 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-19 17:05:58 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:05:16 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:04:58 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-04-19 17:04:53 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.362 | 🔺 Rising |
| 2026-04-19 17:04:44 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:03:33 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-04-19 17:03:18 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | -0.011 |  |
| 2026-04-19 17:03:17 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 17:03:16 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-19 17:03:12 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-19 17:03:11 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-19 17:03:04 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 1.824 | 🔺 Rising |
| 2026-04-19 17:02:38 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | -0.010 |  |
| 2026-04-19 17:02:35 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:02:12 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:01:59 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:01:56 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:01:47 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:01:19 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 17:01:08 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.030 |  |
| 2026-04-19 17:01:08 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-04-19 17:00:52 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-19 17:03:04 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 1.824 | 🔺 Rising |
| 2026-04-19 17:04:53 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.362 | 🔺 Rising |
| 2026-04-19 17:03:16 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-19 17:13:09 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-19 17:03:12 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-19 17:03:11 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-19 17:06:58 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-19 17:07:14 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-19 17:04:58 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-04-19 17:06:03 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-19 17:01:19 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 17:03:17 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 17:10:30 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-19 17:09:04 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-19 17:13:36 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-19 17:02:35 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:01:56 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:05:58 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-19 16:04:17 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-19 16:03:45 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:00:52 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:16:24 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:01:59 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:08:20 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:01:47 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:04:44 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:10:04 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:05:16 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:02:12 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:06:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-19 17:09:56 | Peradeniya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-04-19 17:03:33 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-04-19 17:02:38 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | -0.010 |  |
| 2026-04-19 17:09:31 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-19 17:01:08 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-04-19 17:03:18 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | -0.011 |  |
| 2026-04-19 17:01:08 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.030 |  |
| 2026-04-19 17:06:31 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.062 |  |
| 2026-04-19 06:01:33 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.086 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)