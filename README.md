# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--26_14:15:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **162,206 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 14:15:59 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-05-26 14:11:02 | Magura (Kalu Ganga) | 2.86 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-26 14:09:22 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:08:09 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.009 |  |
| 2026-05-26 14:07:45 | Rathnapura (Kalu Ganga) | 4.50 | 🟢 Normal | -0.097 |  |
| 2026-05-26 14:07:35 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-26 14:07:34 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | -0.069 |  |
| 2026-05-26 14:07:14 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.019 |  |
| 2026-05-26 14:07:10 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-05-26 14:07:08 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:07:03 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-26 14:06:24 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:06:16 | Putupaula (Kalu Ganga) | 2.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 14:05:10 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 14:05:08 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:04:21 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-26 14:04:18 | Hanwella (Kelani Ganga) | 4.78 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-26 14:04:11 | Glencourse (Kelani Ganga) | 12.51 | 🟢 Normal | -0.117 |  |
| 2026-05-26 14:03:56 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:03:44 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-05-26 14:03:39 | Deraniyagala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.029 |  |
| 2026-05-26 14:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.27 | 🟡 Alert | -0.011 |  |
| 2026-05-26 14:03:28 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:02:57 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.009 |  |
| 2026-05-26 14:02:50 | Dunamale (Aththanagalu Oya) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-05-26 14:02:46 | Peradeniya (Mahaweli Ganga) | 2.01 | 🟢 Normal | -0.096 |  |
| 2026-05-26 14:02:43 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.030 |  |
| 2026-05-26 14:02:29 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:02:15 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:02:05 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:01:42 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:01:38 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.031 |  |
| 2026-05-26 14:01:20 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:01:18 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:01:15 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:00:55 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:00:54 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:00:07 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:59:48 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 14:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.27 | 🟡 Alert | -0.011 |  |
| 2026-05-26 14:07:03 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-26 14:04:18 | Hanwella (Kelani Ganga) | 4.78 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-26 14:15:59 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-05-26 14:11:02 | Magura (Kalu Ganga) | 2.86 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-26 14:04:21 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-26 14:07:35 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-26 14:05:10 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 14:06:16 | Putupaula (Kalu Ganga) | 2.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 14:02:15 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:00:07 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:01:18 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:02:29 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:00:55 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:01:20 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:09:22 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:01:15 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:02:05 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:06:24 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:07:08 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:03:56 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:00:54 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:05:08 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:03:28 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:01:57 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:02:57 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.009 |  |
| 2026-05-26 14:07:10 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-05-26 14:08:09 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.009 |  |
| 2026-05-26 14:02:50 | Dunamale (Aththanagalu Oya) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-05-26 13:59:48 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-05-26 14:03:44 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-05-26 14:07:14 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.019 |  |
| 2026-05-26 14:03:39 | Deraniyagala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.029 |  |
| 2026-05-26 14:02:43 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.030 |  |
| 2026-05-26 14:01:38 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.031 |  |
| 2026-05-26 14:07:34 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | -0.069 |  |
| 2026-05-26 14:02:46 | Peradeniya (Mahaweli Ganga) | 2.01 | 🟢 Normal | -0.096 |  |
| 2026-05-26 14:07:45 | Rathnapura (Kalu Ganga) | 4.50 | 🟢 Normal | -0.097 |  |
| 2026-05-26 14:04:11 | Glencourse (Kelani Ganga) | 12.51 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)