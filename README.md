# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--03_16:19:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **196,276 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 16:19:09 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-07-03 16:13:18 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:13:09 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:10:50 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-07-03 16:10:02 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:08:56 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:08:27 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 16:08:22 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:07:27 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-07-03 16:07:17 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:07:12 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:07:12 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:07:12 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:07:02 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -0.009 |  |
| 2026-07-03 16:06:58 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:06:17 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:06:10 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:06:06 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | -0.011 |  |
| 2026-07-03 16:05:41 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-07-03 16:05:12 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-03 16:04:07 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:04:06 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:03:20 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-07-03 16:02:44 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:02:43 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:02:24 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-03 16:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.021 |  |
| 2026-07-03 16:01:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:01:43 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-07-03 16:01:23 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:01:10 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | -0.010 |  |
| 2026-07-03 16:01:04 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.031 |  |
| 2026-07-03 16:00:52 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 16:00:51 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:00:48 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 16:00:27 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-03 16:00:13 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:00:08 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 16:03:20 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-07-03 16:00:27 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-03 16:02:24 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-03 16:19:09 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-07-03 16:00:08 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-03 16:05:12 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-03 16:00:48 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 16:00:52 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 16:08:27 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 16:00:13 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:02:44 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:01:23 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:02:43 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:01:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:04:07 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:13:18 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:13:09 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:08:22 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:07:17 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:01:30 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:08:56 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:06:10 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:06:17 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:00:51 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:04:06 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:06:58 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:07:12 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:10:02 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:07:12 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:07:12 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-03 16:10:50 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-07-03 16:07:02 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -0.009 |  |
| 2026-07-03 16:07:27 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-07-03 16:01:10 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | -0.010 |  |
| 2026-07-03 16:05:41 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-07-03 16:01:43 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-07-03 16:06:06 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | -0.011 |  |
| 2026-07-03 16:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.021 |  |
| 2026-07-03 16:01:04 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.031 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)