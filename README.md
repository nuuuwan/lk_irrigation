# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_17:14:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **179,319 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 17:14:58 | Rathnapura (Kalu Ganga) | 2.97 | 🟢 Normal | -0.034 |  |
| 2026-06-14 17:13:26 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-06-14 17:12:46 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | -0.057 |  |
| 2026-06-14 17:11:36 | Baddegama (Gin Ganga) | 2.60 | 🟢 Normal | -0.026 |  |
| 2026-06-14 17:10:31 | Moragaswewa (Deduru Oya) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-06-14 17:09:21 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.018 |  |
| 2026-06-14 17:09:17 | Dunamale (Aththanagalu Oya) | 2.94 | 🟢 Normal | -0.035 |  |
| 2026-06-14 17:06:54 | Badalgama (Maha Oya) | 3.01 | 🟢 Normal | -0.020 |  |
| 2026-06-14 17:06:26 | Panadugama (Nilwala Ganga) | 3.64 | 🟢 Normal | -0.031 |  |
| 2026-06-14 17:05:36 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | -0.009 |  |
| 2026-06-14 17:04:26 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-06-14 17:04:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.14 | 🟡 Alert | -0.030 |  |
| 2026-06-14 17:04:21 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | -0.021 |  |
| 2026-06-14 17:04:19 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.051 |  |
| 2026-06-14 17:03:59 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-06-14 17:03:28 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-14 17:03:18 | Hanwella (Kelani Ganga) | 3.27 | 🟢 Normal | -0.050 |  |
| 2026-06-14 17:03:10 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-14 17:03:04 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-14 17:03:01 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.093 |  |
| 2026-06-14 17:02:54 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-06-14 17:02:50 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-06-14 17:02:26 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-06-14 17:02:26 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-06-14 17:02:17 | Giriulla (Maha Oya) | 1.72 | 🟢 Normal | -0.020 |  |
| 2026-06-14 17:02:17 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-06-14 17:01:39 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-06-14 17:01:34 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | -0.024 |  |
| 2026-06-14 17:01:33 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-06-14 17:01:14 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-14 17:01:13 | Ellagawa (Kalu Ganga) | 8.02 | 🟢 Normal | -0.083 |  |
| 2026-06-14 17:00:58 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.057 |  |
| 2026-06-14 17:00:56 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-14 17:00:44 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.015 |  |
| 2026-06-14 17:00:31 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-14 17:00:18 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-14 17:00:16 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 17:04:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.14 | 🟡 Alert | -0.030 |  |
| 2026-06-14 17:02:54 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-06-14 17:02:17 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-06-14 17:03:04 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-14 17:00:16 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-14 17:00:56 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-14 17:03:28 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-14 14:02:49 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-14 17:00:18 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-14 17:00:31 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-14 17:04:26 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-06-14 17:01:33 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-06-14 16:13:59 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-14 17:01:14 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-14 17:03:10 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-14 17:10:31 | Moragaswewa (Deduru Oya) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-06-14 17:05:36 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | -0.009 |  |
| 2026-06-14 17:13:26 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-06-14 17:02:50 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-06-14 17:03:59 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-06-14 17:02:26 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-06-14 17:01:39 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-06-14 17:00:44 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.015 |  |
| 2026-06-14 17:09:21 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.018 |  |
| 2026-06-14 17:06:54 | Badalgama (Maha Oya) | 3.01 | 🟢 Normal | -0.020 |  |
| 2026-06-14 17:02:26 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-06-14 17:02:17 | Giriulla (Maha Oya) | 1.72 | 🟢 Normal | -0.020 |  |
| 2026-06-14 17:04:21 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | -0.021 |  |
| 2026-06-14 17:01:34 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | -0.024 |  |
| 2026-06-14 17:11:36 | Baddegama (Gin Ganga) | 2.60 | 🟢 Normal | -0.026 |  |
| 2026-06-14 17:06:26 | Panadugama (Nilwala Ganga) | 3.64 | 🟢 Normal | -0.031 |  |
| 2026-06-14 17:14:58 | Rathnapura (Kalu Ganga) | 2.97 | 🟢 Normal | -0.034 |  |
| 2026-06-14 17:09:17 | Dunamale (Aththanagalu Oya) | 2.94 | 🟢 Normal | -0.035 |  |
| 2026-06-14 17:03:18 | Hanwella (Kelani Ganga) | 3.27 | 🟢 Normal | -0.050 |  |
| 2026-06-14 17:04:19 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.051 |  |
| 2026-06-14 17:12:46 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | -0.057 |  |
| 2026-06-14 17:00:58 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.057 |  |
| 2026-06-14 17:01:13 | Ellagawa (Kalu Ganga) | 8.02 | 🟢 Normal | -0.083 |  |
| 2026-06-14 17:03:01 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)