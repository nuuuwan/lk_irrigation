# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_19:13:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **156,331 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 19:13:09 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:12:20 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:10:40 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:09:59 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.026 |  |
| 2026-05-19 19:09:43 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -0.009 |  |
| 2026-05-19 19:09:06 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:08:34 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-05-19 19:08:06 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | -0.027 |  |
| 2026-05-19 19:08:01 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.140 |  |
| 2026-05-19 19:06:54 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:06:51 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | -0.019 |  |
| 2026-05-19 19:06:46 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-05-19 19:06:44 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 19:06:37 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | -0.019 |  |
| 2026-05-19 19:06:04 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:05:46 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.019 |  |
| 2026-05-19 19:05:22 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:05:06 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-05-19 19:04:48 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-19 19:04:44 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-05-19 19:04:36 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:04:15 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-05-19 19:03:49 | Moragaswewa (Deduru Oya) | 1.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-19 19:03:42 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:03:19 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-05-19 19:03:07 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-05-19 19:02:45 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:02:40 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:02:31 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:02:19 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-05-19 19:01:42 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:01:13 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:00:52 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-05-19 19:00:07 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.005 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 19:06:46 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-05-19 19:04:48 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-19 19:03:49 | Moragaswewa (Deduru Oya) | 1.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-19 19:06:44 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 18:04:04 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:01:13 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:02:45 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:04:36 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:03:48 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:09:06 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:03:42 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:12:20 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:13:09 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:01:42 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:02:40 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:05:22 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:06:04 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:10:40 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:06:54 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:02:31 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:00:07 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.005 |  |
| 2026-05-19 19:08:34 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-05-19 19:09:43 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -0.009 |  |
| 2026-05-19 19:05:06 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-05-19 19:03:19 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-05-19 19:04:44 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-05-19 19:02:19 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-05-19 18:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.43 | 🟢 Normal | -0.010 |  |
| 2026-05-19 19:04:15 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-05-19 19:00:52 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-05-19 19:05:46 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.019 |  |
| 2026-05-19 19:06:51 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | -0.019 |  |
| 2026-05-19 19:06:37 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | -0.019 |  |
| 2026-05-19 19:03:07 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-05-19 18:02:04 | Thanthirimale (Malwathu Oya) | 2.22 | 🟢 Normal | -0.021 |  |
| 2026-05-19 19:09:59 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.026 |  |
| 2026-05-19 19:08:06 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | -0.027 |  |
| 2026-05-19 18:01:45 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | -0.063 |  |
| 2026-05-19 19:08:01 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)