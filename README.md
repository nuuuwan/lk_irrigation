# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--07_09:09:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,944 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 09:09:49 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:08:07 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:08:02 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-07 09:07:26 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:06:29 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.011 |  |
| 2026-01-07 09:06:19 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:05:54 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:05:30 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:05:21 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.015 |  |
| 2026-01-07 09:05:06 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | -0.010 |  |
| 2026-01-07 09:04:57 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:04:43 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-07 09:04:43 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-01-07 09:03:56 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -0.029 |  |
| 2026-01-07 09:03:52 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:03:45 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.024 |  |
| 2026-01-07 09:03:26 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 09:03:25 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-07 09:03:13 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-01-07 09:02:52 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-01-07 09:02:28 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.146 |  |
| 2026-01-07 09:02:22 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-07 09:02:22 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:02:19 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | -0.060 |  |
| 2026-01-07 09:02:13 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-01-07 09:02:09 | Horowpothana (Yan Oya) | 2.82 | 🟢 Normal | -0.076 |  |
| 2026-01-07 09:02:03 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.247 |  |
| 2026-01-07 09:01:47 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-01-07 09:01:37 | Weraganthota (Mahaweli Ganga) | -1.02 | 🟢 Normal | -0.030 |  |
| 2026-01-07 09:01:35 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:01:27 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.011 |  |
| 2026-01-07 09:01:27 | Siyambalanduwa (Heda Oya) | 1.86 | 🟢 Normal | -0.049 |  |
| 2026-01-07 09:01:18 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:01:10 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:00:55 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.121 |  |
| 2026-01-07 09:00:40 | Manampitiya (Mahaweli Ganga) | 2.97 | 🟢 Normal | -0.139 |  |
| 2026-01-07 09:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:30:30 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.247 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 09:03:13 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-01-07 09:08:02 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-07 09:03:26 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 09:02:22 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:01:35 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:01:18 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:04:57 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:09:49 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:06:19 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:05:30 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:07:26 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:03:52 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:05:54 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:08:07 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:02:19 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:08:50 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-07 08:05:43 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:05:06 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | -0.010 |  |
| 2026-01-07 09:04:43 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-07 09:02:22 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-07 09:02:52 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-01-07 09:01:47 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-01-07 09:04:43 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-01-07 09:03:25 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-07 09:06:29 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.011 |  |
| 2026-01-07 09:01:27 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.011 |  |
| 2026-01-07 09:05:21 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.015 |  |
| 2026-01-07 09:03:45 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.024 |  |
| 2026-01-07 09:03:56 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -0.029 |  |
| 2026-01-07 09:01:37 | Weraganthota (Mahaweli Ganga) | -1.02 | 🟢 Normal | -0.030 |  |
| 2026-01-07 09:02:13 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-01-07 09:01:27 | Siyambalanduwa (Heda Oya) | 1.86 | 🟢 Normal | -0.049 |  |
| 2026-01-07 09:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | -0.060 |  |
| 2026-01-07 09:02:09 | Horowpothana (Yan Oya) | 2.82 | 🟢 Normal | -0.076 |  |
| 2026-01-07 09:00:55 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.121 |  |
| 2026-01-07 09:00:40 | Manampitiya (Mahaweli Ganga) | 2.97 | 🟢 Normal | -0.139 |  |
| 2026-01-07 09:02:28 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.146 |  |
| 2026-01-07 09:02:03 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.247 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)