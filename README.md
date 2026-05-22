# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_06:35:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **158,494 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 06:35:13 | Galgamuwa (Mee Oya) | 0.72 | 🟢 Normal | -0.002 |  |
| 2026-05-22 06:16:10 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-05-22 06:13:50 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-22 06:10:56 | Badalgama (Maha Oya) | 4.15 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-22 06:08:26 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.019 |  |
| 2026-05-22 06:08:00 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-22 06:07:18 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-22 06:06:43 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-22 06:06:27 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.021 |  |
| 2026-05-22 06:06:10 | Rathnapura (Kalu Ganga) | 7.03 | 🟡 Alert | 0.613 | 🔺 Rising |
| 2026-05-22 06:05:54 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-22 06:05:52 | Glencourse (Kelani Ganga) | 14.09 | 🟢 Normal | 0.777 | 🔺 Rising |
| 2026-05-22 06:05:43 | Hanwella (Kelani Ganga) | 5.38 | 🟢 Normal | 0.907 | 🔺 Rising |
| 2026-05-22 06:05:43 | Dunamale (Aththanagalu Oya) | 4.25 | 🟡 Alert | 0.973 | 🔺 Rising |
| 2026-05-22 06:05:38 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-05-22 06:05:22 | Ellagawa (Kalu Ganga) | 7.50 | 🟢 Normal | 30.075 | 🔺 Rising |
| 2026-05-22 06:05:08 | Deraniyagala (Kelani Ganga) | 4.36 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-05-22 06:04:29 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-22 06:04:27 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-22 06:04:13 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | -0.020 |  |
| 2026-05-22 06:04:12 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-22 06:03:59 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-22 06:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-05-22 06:03:31 | Magura (Kalu Ganga) | 2.46 | 🟢 Normal | 0.497 | 🔺 Rising |
| 2026-05-22 06:03:23 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.012 |  |
| 2026-05-22 06:03:12 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-22 06:02:49 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-22 06:02:23 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.021 |  |
| 2026-05-22 06:01:50 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-22 06:01:48 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-22 06:01:43 | Moragaswewa (Deduru Oya) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 06:01:25 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-05-22 06:01:19 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | -0.003 |  |
| 2026-05-22 06:01:18 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.014 |  |
| 2026-05-22 06:01:12 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 06:05:43 | Dunamale (Aththanagalu Oya) | 4.25 | 🟡 Alert | 0.973 | 🔺 Rising |
| 2026-05-22 06:06:10 | Rathnapura (Kalu Ganga) | 7.03 | 🟡 Alert | 0.613 | 🔺 Rising |
| 2026-05-22 06:05:22 | Ellagawa (Kalu Ganga) | 7.50 | 🟢 Normal | 30.075 | 🔺 Rising |
| 2026-05-22 06:05:43 | Hanwella (Kelani Ganga) | 5.38 | 🟢 Normal | 0.907 | 🔺 Rising |
| 2026-05-22 06:05:52 | Glencourse (Kelani Ganga) | 14.09 | 🟢 Normal | 0.777 | 🔺 Rising |
| 2026-05-22 06:03:31 | Magura (Kalu Ganga) | 2.46 | 🟢 Normal | 0.497 | 🔺 Rising |
| 2026-05-22 06:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-05-22 06:05:08 | Deraniyagala (Kelani Ganga) | 4.36 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-05-22 06:16:10 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-05-22 06:05:38 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-05-22 06:07:18 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-22 06:10:56 | Badalgama (Maha Oya) | 4.15 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-22 06:08:00 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-22 06:04:12 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-22 06:03:59 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-22 06:05:54 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-22 06:00:19 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-22 06:01:43 | Moragaswewa (Deduru Oya) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 06:00:18 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 06:00:25 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 06:01:12 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 06:01:48 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-22 06:04:27 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-22 06:13:50 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-22 06:04:29 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-22 06:06:43 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-22 06:02:49 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-22 06:01:50 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-22 06:03:12 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-22 06:35:13 | Galgamuwa (Mee Oya) | 0.72 | 🟢 Normal | -0.002 |  |
| 2026-05-22 06:01:19 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | -0.003 |  |
| 2026-05-22 06:03:23 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.012 |  |
| 2026-05-22 06:01:18 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.014 |  |
| 2026-05-22 06:08:26 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.019 |  |
| 2026-05-22 06:01:25 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-05-22 06:04:13 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | -0.020 |  |
| 2026-05-22 06:06:27 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.021 |  |
| 2026-05-22 06:02:23 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.021 |  |
| 2026-05-21 18:01:04 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)