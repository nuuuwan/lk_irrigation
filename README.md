# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--06_13:12:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **198,860 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-06 13:12:30 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:11:14 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-07-06 13:09:26 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:07:59 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:07:47 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | -0.019 |  |
| 2026-07-06 13:07:46 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:07:33 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-07-06 13:07:25 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.028 |  |
| 2026-07-06 13:06:47 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-06 13:06:39 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-07-06 13:06:10 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.019 |  |
| 2026-07-06 13:05:41 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:04:58 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-06 13:04:57 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-07-06 13:04:56 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.019 |  |
| 2026-07-06 13:04:56 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-07-06 13:04:47 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 13:04:35 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:04:25 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-07-06 13:04:01 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-06 13:03:28 | Hanwella (Kelani Ganga) | 1.79 | 🟢 Normal | -0.030 |  |
| 2026-07-06 13:03:25 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:03:25 | Glencourse (Kelani Ganga) | 10.06 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-06 13:03:12 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-07-06 13:03:07 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-07-06 13:03:06 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:03:03 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:02:47 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:02:46 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.203 |  |
| 2026-07-06 13:02:40 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 13:02:29 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:01:57 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:01:33 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-07-06 13:01:28 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 13:01:27 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:01:16 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.010 |  |
| 2026-07-06 13:01:10 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-06 13:04:57 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-07-06 13:06:47 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-06 13:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-06 13:04:58 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-06 13:03:25 | Glencourse (Kelani Ganga) | 10.06 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-06 13:01:28 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 13:02:40 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 13:04:47 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 13:01:27 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:03:25 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:02:29 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:04:01 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:07:59 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:09:26 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:01:57 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:05:41 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:03:03 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:03:06 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:12:30 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:07:46 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-06 12:03:21 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:02:47 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:01:10 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-06 13:06:39 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-07-06 13:11:14 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-07-06 13:04:25 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-07-06 13:03:07 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-07-06 13:04:56 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-07-06 13:01:33 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-07-06 13:01:16 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.010 |  |
| 2026-07-06 13:07:33 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-07-06 13:03:12 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-07-06 13:07:47 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | -0.019 |  |
| 2026-07-06 13:04:56 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.019 |  |
| 2026-07-06 13:06:10 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.019 |  |
| 2026-07-06 13:07:25 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.028 |  |
| 2026-07-06 13:03:28 | Hanwella (Kelani Ganga) | 1.79 | 🟢 Normal | -0.030 |  |
| 2026-07-06 13:02:46 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.203 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)