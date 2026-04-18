# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_21:10:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **128,735 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 21:10:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:08:19 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.029 |  |
| 2026-04-18 21:08:09 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | -0.019 |  |
| 2026-04-18 21:07:17 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:07:01 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:06:44 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:05:59 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.028 |  |
| 2026-04-18 21:05:52 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:05:39 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-18 21:05:29 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.038 |  |
| 2026-04-18 21:04:55 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:04:50 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-18 21:04:41 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-18 21:04:26 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.028 |  |
| 2026-04-18 21:04:17 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:04:04 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:03:59 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.021 |  |
| 2026-04-18 21:03:45 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:03:39 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:03:25 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:03:16 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:03:10 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-18 21:03:07 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-18 21:02:52 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:02:51 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 21:02:44 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-18 21:02:30 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.031 |  |
| 2026-04-18 21:02:18 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:02:11 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.115 |  |
| 2026-04-18 21:01:59 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:01:58 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:01:35 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:01:21 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:00:56 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-04-18 21:00:16 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-18 20:24:49 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-18 20:21:09 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.028 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 21:04:41 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-18 21:03:07 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-18 21:04:50 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-18 21:03:10 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-18 21:02:51 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 21:07:01 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:00:16 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:02:52 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:01:58 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:01:35 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:03:45 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:07:17 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:01:59 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:05:52 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:01:21 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:03:25 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:04:55 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:03:16 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:06:44 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:04:04 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:02:18 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:04:17 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:03:39 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:10:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-18 21:05:39 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-18 18:01:26 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-04-18 21:00:56 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-04-18 21:02:44 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-18 18:01:26 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | -0.011 |  |
| 2026-04-18 21:08:09 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | -0.019 |  |
| 2026-04-18 21:03:59 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.021 |  |
| 2026-04-18 21:04:26 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.028 |  |
| 2026-04-18 21:05:59 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.028 |  |
| 2026-04-18 21:08:19 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.029 |  |
| 2026-04-18 21:02:30 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.031 |  |
| 2026-04-18 21:05:29 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.038 |  |
| 2026-04-18 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.068 |  |
| 2026-04-18 21:02:11 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.115 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)