# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_10:17:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,073 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 10:17:19 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:13:03 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.049 |  |
| 2026-04-20 10:08:44 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:07:14 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-20 10:06:32 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:06:20 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:06:08 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-04-20 10:05:14 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:04:54 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.032 |  |
| 2026-04-20 10:04:48 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:04:32 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.019 |  |
| 2026-04-20 10:04:23 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-04-20 10:04:14 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:04:13 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 10:03:46 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.030 |  |
| 2026-04-20 10:03:42 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.355 |  |
| 2026-04-20 10:03:28 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-04-20 10:03:17 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:03:08 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:03:07 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-04-20 10:02:55 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 10:02:39 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 10:02:31 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:02:27 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:02:19 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-20 10:02:15 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:02:13 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.031 |  |
| 2026-04-20 10:01:43 | Weraganthota (Mahaweli Ganga) | -2.53 | 🟢 Normal | 0.451 | 🔺 Rising |
| 2026-04-20 10:01:37 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:01:37 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-20 10:01:31 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | -0.023 |  |
| 2026-04-20 10:01:29 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:01:22 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:01:19 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-04-20 10:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 10:00:52 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:00:23 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 10:01:43 | Weraganthota (Mahaweli Ganga) | -2.53 | 🟢 Normal | 0.451 | 🔺 Rising |
| 2026-04-20 10:01:37 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-20 10:07:14 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-20 10:02:19 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-20 10:04:13 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 10:02:39 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 10:02:55 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 10:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 10:00:23 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:02:31 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:03:08 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:06:32 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:00:52 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:05:14 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:17:19 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:03:17 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:04:48 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:06:20 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:01:22 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:01:29 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:03:28 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:02:15 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:04:14 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:01:37 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:08:44 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:02:27 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:06:08 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-04-20 10:03:07 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-04-20 10:04:32 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.019 |  |
| 2026-04-20 10:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-04-20 09:00:23 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-04-20 10:04:23 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-04-20 10:01:31 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | -0.023 |  |
| 2026-04-20 10:01:19 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-04-20 10:03:46 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.030 |  |
| 2026-04-20 10:02:13 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.031 |  |
| 2026-04-20 10:04:54 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.032 |  |
| 2026-04-20 10:13:03 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.049 |  |
| 2026-04-20 10:03:42 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.355 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)