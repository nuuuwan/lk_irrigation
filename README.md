# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_16:09:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **156,216 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 16:09:26 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:07:41 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-19 16:06:22 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-05-19 16:06:21 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | -0.010 |  |
| 2026-05-19 16:05:57 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-19 16:05:37 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | -0.021 |  |
| 2026-05-19 16:05:27 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:05:24 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.011 |  |
| 2026-05-19 16:05:19 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-19 16:05:03 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:04:46 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:04:35 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-05-19 16:04:25 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-05-19 16:04:25 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:04:17 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.011 |  |
| 2026-05-19 16:04:09 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-05-19 16:04:00 | Moragaswewa (Deduru Oya) | 1.59 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-05-19 16:03:56 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:03:09 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:03:01 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-19 16:02:53 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-05-19 16:02:52 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-05-19 16:02:51 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-05-19 16:02:43 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-05-19 16:02:25 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | -0.021 |  |
| 2026-05-19 16:02:21 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:02:16 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:02:11 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-05-19 16:02:10 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 16:02:03 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:02:00 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:01:45 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | -0.011 |  |
| 2026-05-19 16:01:17 | Thanthirimale (Malwathu Oya) | 2.25 | 🟢 Normal | -0.020 |  |
| 2026-05-19 16:00:21 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:00:17 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 15:20:55 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | -0.017 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 16:02:43 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-05-19 16:04:00 | Moragaswewa (Deduru Oya) | 1.59 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-05-19 16:05:19 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-19 16:07:41 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-19 16:05:57 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-19 16:02:10 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 16:00:21 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:02:16 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:00:17 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:03:09 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:02:00 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:02:21 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:09:26 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:05:27 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:02:03 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:04:46 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:05:03 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:04:25 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-19 15:07:46 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:03:56 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-19 16:06:22 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-05-19 16:03:01 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-19 16:04:25 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-05-19 16:02:51 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-05-19 16:04:09 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-05-19 16:06:21 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | -0.010 |  |
| 2026-05-19 16:02:52 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-05-19 16:02:53 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-05-19 16:02:11 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-05-19 16:05:24 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.011 |  |
| 2026-05-19 16:04:17 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.011 |  |
| 2026-05-19 16:04:35 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-05-19 16:01:45 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | -0.011 |  |
| 2026-05-19 15:20:55 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | -0.017 |  |
| 2026-05-19 15:03:29 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.019 |  |
| 2026-05-19 16:01:17 | Thanthirimale (Malwathu Oya) | 2.25 | 🟢 Normal | -0.020 |  |
| 2026-05-19 16:02:25 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | -0.021 |  |
| 2026-05-19 16:05:37 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | -0.021 |  |
| 2026-05-19 15:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.53 | 🟢 Normal | -0.104 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)