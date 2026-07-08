# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--08_11:13:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **200,577 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-08 11:13:26 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:10:48 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.009 |  |
| 2026-07-08 11:08:38 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:07:57 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.100 |  |
| 2026-07-08 11:07:49 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:06:56 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:06:13 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:06:08 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-07-08 11:05:31 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:05:29 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.093 |  |
| 2026-07-08 11:05:29 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-07-08 11:05:24 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:05:23 | Thanthirimale (Malwathu Oya) | 1.03 | 🟢 Normal | -0.009 |  |
| 2026-07-08 11:04:54 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:04:48 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | -0.048 |  |
| 2026-07-08 11:04:44 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:04:26 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:04:21 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-08 11:03:52 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-07-08 11:03:49 | Hanwella (Kelani Ganga) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-07-08 11:03:22 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 11:03:22 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:03:15 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-07-08 11:03:14 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.069 |  |
| 2026-07-08 11:03:13 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-07-08 11:02:47 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-08 11:02:43 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-07-08 11:02:34 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-07-08 11:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 11:02:21 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:02:18 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 11:01:59 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:01:56 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:01:27 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | -0.030 |  |
| 2026-07-08 11:01:27 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:01:09 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:00:59 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:00:45 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:00:30 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.020 |  |
| 2026-07-08 11:00:29 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-08 11:02:43 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-07-08 11:04:21 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-08 11:02:47 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-08 11:02:18 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 11:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 11:03:22 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 11:00:29 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:04:26 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:01:27 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:00:59 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:08:38 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:02:21 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:05:31 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:01:56 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:06:13 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:01:09 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:06:56 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:04:44 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:13:26 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:04:54 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:03:22 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:05:24 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:07:49 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:01:59 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-08 11:10:48 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.009 |  |
| 2026-07-08 11:05:23 | Thanthirimale (Malwathu Oya) | 1.03 | 🟢 Normal | -0.009 |  |
| 2026-07-08 11:03:52 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-07-08 11:03:13 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-07-08 11:03:15 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-07-08 11:05:29 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-07-08 11:02:34 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-07-08 11:06:08 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-07-08 11:03:49 | Hanwella (Kelani Ganga) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-07-08 11:00:30 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.020 |  |
| 2026-07-08 11:01:27 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | -0.030 |  |
| 2026-07-08 11:04:48 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | -0.048 |  |
| 2026-07-08 11:03:14 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.069 |  |
| 2026-07-08 11:05:29 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.093 |  |
| 2026-07-08 11:07:57 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)