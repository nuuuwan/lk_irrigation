# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_16:30:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **221,316 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 16:30:01 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:22:58 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:12:23 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:11:19 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:09:08 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:09:08 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-31 16:08:43 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-07-31 16:08:11 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:07:29 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-31 16:07:24 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-31 16:05:27 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:05:19 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.364 | 🔺 Rising |
| 2026-07-31 16:05:13 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-31 16:04:51 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:04:44 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-31 16:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.03 | 🟢 Normal | 2.348 | 🔺 Rising |
| 2026-07-31 16:04:27 | Ellagawa (Kalu Ganga) | 0.79 | 🟢 Normal | -99.467 |  |
| 2026-07-31 16:04:00 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.016 |  |
| 2026-07-31 16:03:57 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:03:54 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:03:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 2.348 | 🔺 Rising |
| 2026-07-31 16:03:13 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:03:08 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 16:03:01 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:02:59 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:02:42 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:02:40 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-07-31 16:02:35 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-31 16:02:33 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:02:31 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-07-31 16:02:20 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 16:02:12 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | -99.467 |  |
| 2026-07-31 16:01:46 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:01:38 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:01:24 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:01:16 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:01:15 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:01:07 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:01:04 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:00:36 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:00:36 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.085 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 16:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.03 | 🟢 Normal | 2.348 | 🔺 Rising |
| 2026-07-31 16:05:19 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.364 | 🔺 Rising |
| 2026-07-31 16:07:29 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-31 16:05:13 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-31 16:04:44 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-31 16:02:35 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-31 16:07:24 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-31 16:03:08 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 16:02:20 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 16:09:08 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-31 16:02:33 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:01:04 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:01:46 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:01:38 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:03:13 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:00:36 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:03:57 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:22:58 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:08:11 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:04:51 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:02:42 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:02:59 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:03:01 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:11:19 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:01:16 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:30:01 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:01:15 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:01:24 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:05:27 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:09:08 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:12:23 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:03:54 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:01:07 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-31 16:02:40 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-07-31 16:04:00 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.016 |  |
| 2026-07-31 16:08:43 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-07-31 16:02:31 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-07-31 16:00:36 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.085 |  |
| 2026-07-31 16:04:27 | Ellagawa (Kalu Ganga) | 0.79 | 🟢 Normal | -99.467 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)