# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_16:18:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,823 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 16:18:33 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-13 16:10:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.55 | 🟡 Alert | 0.160 | 🔺 Rising |
| 2026-05-13 16:09:43 | Panadugama (Nilwala Ganga) | 5.28 | 🟡 Alert | 0.128 | 🔺 Rising |
| 2026-05-13 16:08:20 | Rathnapura (Kalu Ganga) | 6.24 | 🟡 Alert | -0.019 |  |
| 2026-05-13 16:08:05 | Moraketiya (Walawe Ganga) | 2.19 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-13 16:07:52 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-13 16:07:46 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-05-13 16:06:24 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.024 |  |
| 2026-05-13 16:06:10 | Hanwella (Kelani Ganga) | 2.47 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-05-13 16:06:09 | Magura (Kalu Ganga) | 5.13 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-13 16:05:08 | Putupaula (Kalu Ganga) | 2.17 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-13 16:05:05 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | -0.020 |  |
| 2026-05-13 16:05:00 | Thanthirimale (Malwathu Oya) | 3.45 | 🟢 Normal | -0.028 |  |
| 2026-05-13 16:04:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.060 |  |
| 2026-05-13 16:03:48 | Giriulla (Maha Oya) | 2.00 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-13 16:03:36 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-05-13 16:03:25 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.116 |  |
| 2026-05-13 16:03:24 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-13 16:03:22 | Glencourse (Kelani Ganga) | 11.16 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-05-13 16:03:22 | Thawalama (Gin Ganga) | 3.25 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-05-13 16:03:17 | Wellawaya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.040 |  |
| 2026-05-13 16:03:12 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-05-13 16:03:10 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-05-13 16:03:06 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-05-13 16:02:43 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-05-13 16:02:27 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.111 |  |
| 2026-05-13 16:02:25 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-13 16:02:17 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-13 16:02:11 | Thanamalwila (Kirindi Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-05-13 16:01:41 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -1.015 |  |
| 2026-05-13 16:01:39 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-05-13 16:01:28 | Pitabeddara (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.167 |  |
| 2026-05-13 16:01:15 | Dunamale (Aththanagalu Oya) | 3.38 | 🟡 Alert | 0.080 | 🔺 Rising |
| 2026-05-13 16:01:02 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-13 16:00:45 | Galgamuwa (Mee Oya) | 2.87 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-13 16:00:27 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-13 16:00:21 | Moragaswewa (Deduru Oya) | 2.96 | 🟢 Normal | -0.023 |  |
| 2026-05-13 16:00:08 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 16:10:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.55 | 🟡 Alert | 0.160 | 🔺 Rising |
| 2026-05-13 16:09:43 | Panadugama (Nilwala Ganga) | 5.28 | 🟡 Alert | 0.128 | 🔺 Rising |
| 2026-05-13 16:01:15 | Dunamale (Aththanagalu Oya) | 3.38 | 🟡 Alert | 0.080 | 🔺 Rising |
| 2026-05-13 16:06:09 | Magura (Kalu Ganga) | 5.13 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-13 16:08:20 | Rathnapura (Kalu Ganga) | 6.24 | 🟡 Alert | -0.019 |  |
| 2026-05-13 15:02:44 | Baddegama (Gin Ganga) | 2.90 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-05-13 16:03:22 | Thawalama (Gin Ganga) | 3.25 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-05-13 16:03:22 | Glencourse (Kelani Ganga) | 11.16 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-05-13 16:06:10 | Hanwella (Kelani Ganga) | 2.47 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-05-13 16:03:48 | Giriulla (Maha Oya) | 2.00 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-13 16:02:17 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-13 16:05:08 | Putupaula (Kalu Ganga) | 2.17 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-13 16:02:25 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-13 16:00:45 | Galgamuwa (Mee Oya) | 2.87 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-13 16:03:24 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-13 16:08:05 | Moraketiya (Walawe Ganga) | 2.19 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-13 16:00:08 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | 0.000 |  |
| 2026-05-13 16:18:33 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-13 16:01:02 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-13 16:02:11 | Thanamalwila (Kirindi Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-05-13 16:07:52 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-13 16:03:12 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-05-13 16:02:43 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-05-13 16:00:27 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-13 16:05:05 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | -0.020 |  |
| 2026-05-13 16:03:06 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-05-13 16:01:39 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-05-13 16:03:10 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-05-13 16:03:36 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-05-13 16:00:21 | Moragaswewa (Deduru Oya) | 2.96 | 🟢 Normal | -0.023 |  |
| 2026-05-13 16:06:24 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.024 |  |
| 2026-05-13 16:05:00 | Thanthirimale (Malwathu Oya) | 3.45 | 🟢 Normal | -0.028 |  |
| 2026-05-13 16:07:46 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-05-13 16:03:17 | Wellawaya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.040 |  |
| 2026-05-13 16:04:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.060 |  |
| 2026-05-13 16:02:27 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.111 |  |
| 2026-05-13 16:03:25 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.116 |  |
| 2026-05-13 16:01:28 | Pitabeddara (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.167 |  |
| 2026-05-13 16:01:41 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -1.015 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)