# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_22:30:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,048 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 22:30:59 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.007 |  |
| 2026-05-13 22:29:28 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-13 22:26:11 | Ellagawa (Kalu Ganga) | 8.18 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-13 22:19:38 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-13 22:14:23 | Panadugama (Nilwala Ganga) | 5.19 | 🟡 Alert | -0.098 |  |
| 2026-05-13 22:13:41 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-13 22:09:47 | Moragaswewa (Deduru Oya) | 2.77 | 🟢 Normal | -0.028 |  |
| 2026-05-13 22:08:03 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-05-13 22:06:15 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 22:06:07 | Badalgama (Maha Oya) | 3.21 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-13 22:06:05 | Baddegama (Gin Ganga) | 3.21 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-13 22:05:50 | Rathnapura (Kalu Ganga) | 5.75 | 🟡 Alert | -0.104 |  |
| 2026-05-13 22:05:48 | Putupaula (Kalu Ganga) | 2.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-13 22:05:17 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | 0.270 | 🔺 Rising |
| 2026-05-13 22:05:17 | Hanwella (Kelani Ganga) | 2.92 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-13 22:05:02 | Dunamale (Aththanagalu Oya) | 3.46 | 🟡 Alert | -0.019 |  |
| 2026-05-13 22:04:58 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 22:04:44 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.049 |  |
| 2026-05-13 22:04:39 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.050 |  |
| 2026-05-13 22:04:26 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-13 22:04:06 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.098 |  |
| 2026-05-13 22:03:39 | Thawalama (Gin Ganga) | 2.85 | 🟢 Normal | -0.049 |  |
| 2026-05-13 22:03:38 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-05-13 22:03:29 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | -0.111 |  |
| 2026-05-13 22:02:59 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-13 22:02:46 | Magura (Kalu Ganga) | 5.14 | 🟡 Alert | -0.020 |  |
| 2026-05-13 22:02:34 | Pitabeddara (Nilwala Ganga) | 1.68 | 🟢 Normal | -0.070 |  |
| 2026-05-13 22:02:34 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | -0.060 |  |
| 2026-05-13 22:02:18 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.021 |  |
| 2026-05-13 22:01:59 | Moraketiya (Walawe Ganga) | 1.97 | 🟢 Normal | -0.060 |  |
| 2026-05-13 22:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-05-13 22:01:44 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-13 22:01:17 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-05-13 22:01:10 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-13 22:00:13 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 20:09:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.86 | 🟡 Alert | 0.076 | 🔺 Rising |
| 2026-05-13 22:05:02 | Dunamale (Aththanagalu Oya) | 3.46 | 🟡 Alert | -0.019 |  |
| 2026-05-13 22:02:46 | Magura (Kalu Ganga) | 5.14 | 🟡 Alert | -0.020 |  |
| 2026-05-13 22:14:23 | Panadugama (Nilwala Ganga) | 5.19 | 🟡 Alert | -0.098 |  |
| 2026-05-13 22:05:50 | Rathnapura (Kalu Ganga) | 5.75 | 🟡 Alert | -0.104 |  |
| 2026-05-13 22:05:17 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | 0.270 | 🔺 Rising |
| 2026-05-13 22:03:38 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-05-13 22:06:07 | Badalgama (Maha Oya) | 3.21 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-13 18:02:23 | Galgamuwa (Mee Oya) | 2.97 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-13 22:26:11 | Ellagawa (Kalu Ganga) | 8.18 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-13 22:00:13 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-13 22:06:05 | Baddegama (Gin Ganga) | 3.21 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-13 22:05:48 | Putupaula (Kalu Ganga) | 2.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-13 22:29:28 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-13 22:05:17 | Hanwella (Kelani Ganga) | 2.92 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-13 22:06:15 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 18:02:22 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 22:08:03 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-05-13 22:01:44 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-13 22:01:10 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-13 22:13:41 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-13 22:04:26 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-13 22:04:58 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 22:19:38 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-13 22:30:59 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.007 |  |
| 2026-05-13 22:02:59 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-13 22:01:17 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-05-13 22:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-05-13 22:02:18 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.021 |  |
| 2026-05-13 22:09:47 | Moragaswewa (Deduru Oya) | 2.77 | 🟢 Normal | -0.028 |  |
| 2026-05-13 22:03:39 | Thawalama (Gin Ganga) | 2.85 | 🟢 Normal | -0.049 |  |
| 2026-05-13 22:04:44 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.049 |  |
| 2026-05-13 22:04:39 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.050 |  |
| 2026-05-13 18:02:14 | Thanthirimale (Malwathu Oya) | 3.35 | 🟢 Normal | -0.051 |  |
| 2026-05-13 22:01:59 | Moraketiya (Walawe Ganga) | 1.97 | 🟢 Normal | -0.060 |  |
| 2026-05-13 22:02:34 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | -0.060 |  |
| 2026-05-13 22:02:34 | Pitabeddara (Nilwala Ganga) | 1.68 | 🟢 Normal | -0.070 |  |
| 2026-05-13 22:04:06 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.098 |  |
| 2026-05-13 22:03:29 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)