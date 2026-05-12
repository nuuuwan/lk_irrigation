# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_17:21:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **149,973 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 17:21:03 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 17:16:40 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | 0.533 | 🔺 Rising |
| 2026-05-12 17:12:02 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 17:11:16 | Thawalama (Gin Ganga) | 4.00 | 🟡 Alert | 0.177 | 🔺 Rising |
| 2026-05-12 17:10:35 | Rathnapura (Kalu Ganga) | 2.37 | 🟢 Normal | 0.398 | 🔺 Rising |
| 2026-05-12 17:10:28 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.048 |  |
| 2026-05-12 17:09:44 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-12 17:09:30 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.059 |  |
| 2026-05-12 17:09:06 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-05-12 17:07:41 | Pitabeddara (Nilwala Ganga) | 1.68 | 🟢 Normal | -0.155 |  |
| 2026-05-12 17:07:32 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-05-12 17:06:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.97 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-12 17:06:48 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 17:06:15 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-05-12 17:06:14 | Panadugama (Nilwala Ganga) | 3.69 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-05-12 17:05:44 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.020 |  |
| 2026-05-12 17:04:41 | Katharagama (Menik Ganga) | 1.97 | 🟢 Normal | -0.020 |  |
| 2026-05-12 17:04:24 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.049 |  |
| 2026-05-12 17:04:22 | Galgamuwa (Mee Oya) | 1.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-12 17:03:57 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-12 17:03:56 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-12 17:03:43 | Hanwella (Kelani Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-05-12 17:03:29 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.050 |  |
| 2026-05-12 17:03:24 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-12 17:03:23 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.044 |  |
| 2026-05-12 17:02:28 | Moragaswewa (Deduru Oya) | 1.98 | 🟢 Normal | -0.099 |  |
| 2026-05-12 17:02:26 | Thanthirimale (Malwathu Oya) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-05-12 17:02:25 | Thanamalwila (Kirindi Oya) | 1.92 | 🟢 Normal | -0.011 |  |
| 2026-05-12 17:02:20 | Kuda Oya (Kirindi Oya) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-05-12 17:02:14 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-05-12 17:02:08 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | -0.022 |  |
| 2026-05-12 17:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-12 17:01:53 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-12 17:01:48 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 17:01:10 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.070 |  |
| 2026-05-12 17:01:05 | Manampitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-12 17:00:40 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-12 17:00:27 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 17:11:16 | Thawalama (Gin Ganga) | 4.00 | 🟡 Alert | 0.177 | 🔺 Rising |
| 2026-05-12 17:16:40 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | 0.533 | 🔺 Rising |
| 2026-05-12 17:10:35 | Rathnapura (Kalu Ganga) | 2.37 | 🟢 Normal | 0.398 | 🔺 Rising |
| 2026-05-12 17:02:14 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-05-12 17:06:15 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-05-12 17:06:14 | Panadugama (Nilwala Ganga) | 3.69 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-05-12 17:07:32 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-05-12 17:06:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.97 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-12 17:03:24 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-12 17:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-12 17:01:05 | Manampitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-12 17:04:22 | Galgamuwa (Mee Oya) | 1.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-12 17:00:40 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-12 16:11:17 | Glencourse (Kelani Ganga) | 9.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 17:03:57 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-12 17:09:44 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-12 17:01:48 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 17:06:48 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 17:00:27 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-05-12 17:12:02 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 17:21:03 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 17:01:53 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-12 17:02:26 | Thanthirimale (Malwathu Oya) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-05-12 17:09:06 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-05-12 17:03:43 | Hanwella (Kelani Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-05-12 17:03:56 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-12 17:02:25 | Thanamalwila (Kirindi Oya) | 1.92 | 🟢 Normal | -0.011 |  |
| 2026-05-12 17:05:44 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.020 |  |
| 2026-05-12 17:04:41 | Katharagama (Menik Ganga) | 1.97 | 🟢 Normal | -0.020 |  |
| 2026-05-12 17:02:20 | Kuda Oya (Kirindi Oya) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-05-12 17:02:08 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | -0.022 |  |
| 2026-05-12 17:03:23 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.044 |  |
| 2026-05-12 17:10:28 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.048 |  |
| 2026-05-12 17:04:24 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.049 |  |
| 2026-05-12 17:03:29 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.050 |  |
| 2026-05-12 17:09:30 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.059 |  |
| 2026-05-12 17:01:10 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.070 |  |
| 2026-05-12 17:02:28 | Moragaswewa (Deduru Oya) | 1.98 | 🟢 Normal | -0.099 |  |
| 2026-05-12 17:07:41 | Pitabeddara (Nilwala Ganga) | 1.68 | 🟢 Normal | -0.155 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)