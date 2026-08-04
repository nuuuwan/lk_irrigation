# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_09:14:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,553 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 09:14:12 | Panadugama (Nilwala Ganga) | 4.37 | 🟢 Normal | -0.046 |  |
| 2026-08-04 09:13:58 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:12:36 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-04 09:10:49 | Rathnapura (Kalu Ganga) | 7.11 | 🟡 Alert | -0.123 |  |
| 2026-08-04 09:06:58 | Glencourse (Kelani Ganga) | 14.30 | 🟢 Normal | -0.292 |  |
| 2026-08-04 09:06:48 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:06:44 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:06:38 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:05:19 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:04:46 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:04:46 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-04 09:04:29 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | -0.123 |  |
| 2026-08-04 09:04:16 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:04:05 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:03:54 | Nagalagam Street (Kelani Ganga) | 1.14 | 🟢 Normal | -0.045 |  |
| 2026-08-04 09:03:49 | Thawalama (Gin Ganga) | 2.49 | 🟢 Normal | -0.030 |  |
| 2026-08-04 09:03:30 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-04 09:03:15 | Hanwella (Kelani Ganga) | 6.73 | 🟢 Normal | -0.122 |  |
| 2026-08-04 09:02:59 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.106 |  |
| 2026-08-04 09:02:41 | Deraniyagala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.090 |  |
| 2026-08-04 09:02:32 | Badalgama (Maha Oya) | 3.48 | 🟢 Normal | -0.214 |  |
| 2026-08-04 09:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.37 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-08-04 09:02:27 | Nawalapitiya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-04 09:02:27 | Kithulgala (Kelani Ganga) | 2.98 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-08-04 09:02:20 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-08-04 09:02:12 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:02:11 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:02:04 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | -0.012 |  |
| 2026-08-04 09:01:53 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-04 09:01:52 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:01:49 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.021 |  |
| 2026-08-04 09:01:49 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:01:48 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:01:26 | Peradeniya (Mahaweli Ganga) | 4.72 | 🟢 Normal | -0.134 |  |
| 2026-08-04 09:01:18 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:01:05 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:00:59 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:00:16 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-08-04 09:00:14 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 18.000 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 09:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.37 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-08-04 09:10:49 | Rathnapura (Kalu Ganga) | 7.11 | 🟡 Alert | -0.123 |  |
| 2026-08-04 09:00:16 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-08-04 09:02:27 | Kithulgala (Kelani Ganga) | 2.98 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-08-04 08:16:10 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-08-04 09:02:20 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-08-04 09:03:30 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-04 09:01:53 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-04 09:12:36 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-04 09:04:46 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-04 09:02:27 | Nawalapitiya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-04 09:01:05 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:00:59 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:06:38 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:01:49 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:06:44 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:04:46 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:05:19 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:04:05 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:02:11 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:13:58 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:02:12 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:06:48 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:01:52 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:01:18 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:01:48 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:04:16 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:02:04 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | -0.012 |  |
| 2026-08-04 09:01:49 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.021 |  |
| 2026-08-04 09:03:49 | Thawalama (Gin Ganga) | 2.49 | 🟢 Normal | -0.030 |  |
| 2026-08-04 09:03:54 | Nagalagam Street (Kelani Ganga) | 1.14 | 🟢 Normal | -0.045 |  |
| 2026-08-04 09:14:12 | Panadugama (Nilwala Ganga) | 4.37 | 🟢 Normal | -0.046 |  |
| 2026-08-04 09:02:41 | Deraniyagala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.090 |  |
| 2026-08-04 09:02:59 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.106 |  |
| 2026-08-04 09:03:15 | Hanwella (Kelani Ganga) | 6.73 | 🟢 Normal | -0.122 |  |
| 2026-08-04 09:04:29 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | -0.123 |  |
| 2026-08-04 09:01:26 | Peradeniya (Mahaweli Ganga) | 4.72 | 🟢 Normal | -0.134 |  |
| 2026-08-04 09:02:32 | Badalgama (Maha Oya) | 3.48 | 🟢 Normal | -0.214 |  |
| 2026-08-04 09:06:58 | Glencourse (Kelani Ganga) | 14.30 | 🟢 Normal | -0.292 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)