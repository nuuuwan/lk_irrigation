# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--16_21:14:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **47,480 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 21:14:21 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:10:27 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:09:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.018 |  |
| 2026-01-16 21:08:19 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.020 |  |
| 2026-01-16 21:07:59 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-01-16 21:07:10 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-01-16 21:06:33 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:06:16 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 21:06:12 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:05:40 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:05:29 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | -0.010 |  |
| 2026-01-16 21:05:04 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-16 21:05:01 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:04:45 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.038 |  |
| 2026-01-16 21:04:33 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:04:23 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-01-16 21:04:13 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-01-16 21:04:05 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:04:01 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-01-16 21:03:59 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:03:31 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.051 |  |
| 2026-01-16 21:03:31 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:03:13 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:03:02 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:02:56 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:02:53 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-01-16 21:02:27 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:02:19 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-01-16 21:02:18 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:02:02 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:01:59 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-01-16 21:01:48 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:01:47 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.020 |  |
| 2026-01-16 21:01:39 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.021 |  |
| 2026-01-16 21:01:32 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-01-16 21:01:26 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:01:22 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:00:10 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 21:01:32 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-01-16 21:02:19 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-01-16 18:00:22 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-16 21:05:04 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-16 21:06:16 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 21:03:02 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:00:10 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:03:31 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:01:48 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:02:02 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:02:27 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-16 18:06:10 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:04:33 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:02:56 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:03:59 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:01:26 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:10:27 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:03:13 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:14:21 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:05:01 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:04:05 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:06:12 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:01:22 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:05:40 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:07:59 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-01-16 21:04:23 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-01-16 21:05:29 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | -0.010 |  |
| 2026-01-16 21:04:13 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-01-16 21:07:10 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-01-16 21:02:53 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-01-16 21:04:01 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-01-16 21:09:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.018 |  |
| 2026-01-16 21:01:59 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-01-16 21:08:19 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.020 |  |
| 2026-01-16 21:01:47 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.020 |  |
| 2026-01-16 18:01:44 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-01-16 21:01:39 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.021 |  |
| 2026-01-16 21:04:45 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.038 |  |
| 2026-01-16 21:03:31 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.051 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)