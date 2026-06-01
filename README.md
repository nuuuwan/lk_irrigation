# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--01_12:13:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **167,493 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 12:13:45 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:10:45 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | -0.009 |  |
| 2026-06-01 12:09:36 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-06-01 12:09:06 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.009 |  |
| 2026-06-01 12:06:39 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:06:29 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-01 12:06:18 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:05:57 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:05:51 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:05:45 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.012 |  |
| 2026-06-01 12:05:15 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:05:13 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.011 |  |
| 2026-06-01 12:05:05 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | -0.019 |  |
| 2026-06-01 12:04:42 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:04:23 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.030 |  |
| 2026-06-01 12:04:08 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:04:05 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-01 12:03:58 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 12:03:57 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:03:55 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.056 |  |
| 2026-06-01 12:03:52 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:03:47 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:03:44 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:03:35 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:03:20 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.019 |  |
| 2026-06-01 12:02:58 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:02:42 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:02:34 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.021 |  |
| 2026-06-01 12:02:33 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:02:32 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 12:02:31 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-06-01 12:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | -0.040 |  |
| 2026-06-01 12:02:17 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:01:57 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.012 |  |
| 2026-06-01 12:01:54 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 12:01:41 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:01:36 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.020 |  |
| 2026-06-01 12:01:34 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.020 |  |
| 2026-06-01 12:01:25 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:00:56 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 12:09:36 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-06-01 12:04:05 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-01 12:06:29 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-01 12:03:58 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 12:02:32 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 12:01:54 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 12:05:57 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:02:58 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:00:56 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:01:41 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:02:33 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:04:08 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:06:18 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:03:52 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:13:45 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:03:47 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:03:57 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:04:42 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:03:35 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:05:15 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:05:51 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:01:25 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:03:44 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:02:17 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:06:39 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-01 12:10:45 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | -0.009 |  |
| 2026-06-01 12:09:06 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.009 |  |
| 2026-06-01 12:05:13 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.011 |  |
| 2026-06-01 12:05:45 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.012 |  |
| 2026-06-01 12:01:57 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.012 |  |
| 2026-06-01 12:03:20 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.019 |  |
| 2026-06-01 12:05:05 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | -0.019 |  |
| 2026-06-01 12:01:36 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.020 |  |
| 2026-06-01 12:01:34 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.020 |  |
| 2026-06-01 12:02:31 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-06-01 12:02:34 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.021 |  |
| 2026-06-01 12:04:23 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.030 |  |
| 2026-06-01 12:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | -0.040 |  |
| 2026-06-01 12:03:55 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.056 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)