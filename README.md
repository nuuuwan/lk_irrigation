# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--08_21:20:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **200,960 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-08 21:20:43 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:19:30 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:10:24 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.028 |  |
| 2026-07-08 21:09:43 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.038 |  |
| 2026-07-08 21:08:23 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-08 21:08:19 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-08 21:07:23 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-07-08 21:07:18 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-07-08 21:07:18 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-08 21:07:12 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:06:56 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:06:13 | Ellagawa (Kalu Ganga) | 4.51 | 🟢 Normal | -0.010 |  |
| 2026-07-08 21:06:01 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:05:58 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:05:49 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-08 21:05:01 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | -0.011 |  |
| 2026-07-08 21:04:57 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:04:50 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.011 |  |
| 2026-07-08 21:03:59 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:03:58 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:03:44 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:02:46 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:02:27 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.272 | 🔺 Rising |
| 2026-07-08 21:02:26 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:02:19 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | -0.041 |  |
| 2026-07-08 21:02:12 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:02:08 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:02:08 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:02:07 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:02:07 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 21:02:04 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:01:50 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-08 21:01:35 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:01:18 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:01:03 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-08 20:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | 2.448 | 🔺 Rising |
| 2026-07-08 21:02:27 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.272 | 🔺 Rising |
| 2026-07-08 21:07:18 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-08 21:01:50 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-08 21:08:23 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-08 21:08:19 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-08 21:02:07 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 21:02:08 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:07:12 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-08 20:02:41 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:01:35 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:02:12 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:04:57 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:02:07 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-08 17:08:44 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:20:43 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:03:59 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:06:01 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:05:58 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:01:03 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:02:04 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:02:26 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:06:56 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:03:44 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:01:29 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:02:08 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:19:30 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:01:18 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:03:58 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-08 21:05:49 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-08 21:07:23 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-07-08 21:06:13 | Ellagawa (Kalu Ganga) | 4.51 | 🟢 Normal | -0.010 |  |
| 2026-07-08 21:07:18 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-07-08 21:05:01 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | -0.011 |  |
| 2026-07-08 21:04:50 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.011 |  |
| 2026-07-08 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.021 |  |
| 2026-07-08 21:10:24 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.028 |  |
| 2026-07-08 21:09:43 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.038 |  |
| 2026-07-08 21:02:19 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | -0.041 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)