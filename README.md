# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--04_09:11:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **36,275 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 09:11:29 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-01-04 09:09:01 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-01-04 09:08:42 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.031 |  |
| 2026-01-04 09:08:28 | Horowpothana (Yan Oya) | 1.97 | 🟢 Normal | -0.018 |  |
| 2026-01-04 09:08:28 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:07:59 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:07:26 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:07:21 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-01-04 09:06:57 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.066 |  |
| 2026-01-04 09:06:19 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.134 |  |
| 2026-01-04 09:06:13 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:05:33 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-04 09:05:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | -0.019 |  |
| 2026-01-04 09:04:58 | Kithulgala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.199 |  |
| 2026-01-04 09:04:46 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.009 |  |
| 2026-01-04 09:04:15 | Galgamuwa (Mee Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:04:07 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | -7.826 |  |
| 2026-01-04 09:03:50 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:03:32 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:03:21 | Dunamale (Aththanagalu Oya) | 0.79 | 🟢 Normal | -7.826 |  |
| 2026-01-04 09:03:19 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:03:16 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-01-04 09:03:14 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:03:11 | Weraganthota (Mahaweli Ganga) | -1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 09:03:03 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-04 09:02:58 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.012 |  |
| 2026-01-04 09:02:56 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:02:48 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:02:46 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.085 |  |
| 2026-01-04 09:02:39 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:02:32 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.091 |  |
| 2026-01-04 09:02:20 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:02:07 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:01:53 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:01:19 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 09:01:05 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:00:57 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:00:56 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | -0.024 |  |
| 2026-01-04 09:00:52 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:00:49 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:00:40 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 09:07:21 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-01-04 09:11:29 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-01-04 09:05:33 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-04 09:03:03 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-04 09:00:40 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 09:03:11 | Weraganthota (Mahaweli Ganga) | -1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 09:01:19 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 09:02:20 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:03:32 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:01:05 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:00:52 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:04:15 | Galgamuwa (Mee Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:02:39 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:03:19 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:03:50 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:02:48 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:07:26 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:00:57 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:01:53 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:06:13 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:07:59 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:08:28 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:03:14 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:00:49 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:02:07 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-04 09:04:46 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.009 |  |
| 2026-01-04 09:03:16 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-01-04 09:09:01 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-01-04 09:02:58 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.012 |  |
| 2026-01-04 09:08:28 | Horowpothana (Yan Oya) | 1.97 | 🟢 Normal | -0.018 |  |
| 2026-01-04 09:05:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | -0.019 |  |
| 2026-01-04 09:00:56 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | -0.024 |  |
| 2026-01-04 09:08:42 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.031 |  |
| 2026-01-04 09:06:57 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.066 |  |
| 2026-01-04 09:02:46 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.085 |  |
| 2026-01-04 09:02:32 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.091 |  |
| 2026-01-04 09:06:19 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.134 |  |
| 2026-01-04 09:04:58 | Kithulgala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.199 |  |
| 2026-01-04 09:04:07 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | -7.826 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)