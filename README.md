# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_09:14:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,046 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 09:14:02 | Panadugama (Nilwala Ganga) | 4.34 | 🟢 Normal | -0.219 |  |
| 2026-05-08 09:08:57 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-05-08 09:08:26 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-08 09:07:10 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.032 |  |
| 2026-05-08 09:06:58 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-08 09:06:56 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.099 |  |
| 2026-05-08 09:06:01 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.098 |  |
| 2026-05-08 09:06:00 | Manampitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-08 09:05:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.98 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-08 09:05:30 | Katharagama (Menik Ganga) | 0.46 | 🟢 Normal | -0.039 |  |
| 2026-05-08 09:05:28 | Glencourse (Kelani Ganga) | 10.32 | 🟢 Normal | -0.186 |  |
| 2026-05-08 09:05:22 | Kithulgala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.031 |  |
| 2026-05-08 09:05:06 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-05-08 09:04:53 | Galgamuwa (Mee Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-05-08 09:04:47 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.097 |  |
| 2026-05-08 09:04:42 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-05-08 09:04:03 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | -0.042 |  |
| 2026-05-08 09:03:55 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-05-08 09:03:47 | Hanwella (Kelani Ganga) | 2.53 | 🟢 Normal | -0.090 |  |
| 2026-05-08 09:03:43 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-05-08 09:03:24 | Thanamalwila (Kirindi Oya) | 1.99 | 🟢 Normal | -0.029 |  |
| 2026-05-08 09:02:54 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | -0.080 |  |
| 2026-05-08 09:02:40 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.019 |  |
| 2026-05-08 09:02:39 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.040 |  |
| 2026-05-08 09:02:22 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.092 |  |
| 2026-05-08 09:02:17 | Badalgama (Maha Oya) | 3.19 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-08 09:01:48 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.052 |  |
| 2026-05-08 09:01:45 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-08 09:01:44 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-08 09:01:43 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-05-08 09:01:34 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-08 09:01:26 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-08 09:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-05-08 09:01:16 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-08 09:01:08 | Ellagawa (Kalu Ganga) | 5.71 | 🟢 Normal | 1.060 | 🔺 Rising |
| 2026-05-08 09:00:57 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.347 |  |
| 2026-05-08 09:00:56 | Thanthirimale (Malwathu Oya) | 1.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-08 09:00:30 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 09:01:08 | Ellagawa (Kalu Ganga) | 5.71 | 🟢 Normal | 1.060 | 🔺 Rising |
| 2026-05-08 09:03:43 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-05-08 09:05:06 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-05-08 09:01:34 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-08 09:06:00 | Manampitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-08 09:01:26 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-08 09:06:58 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-08 09:05:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.98 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-08 08:06:47 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-08 09:08:26 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-08 09:02:17 | Badalgama (Maha Oya) | 3.19 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-08 09:00:56 | Thanthirimale (Malwathu Oya) | 1.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-08 09:01:16 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-08 09:01:45 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-08 09:01:44 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-08 09:04:42 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-05-08 09:04:53 | Galgamuwa (Mee Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-05-08 09:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-05-08 09:08:57 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-05-08 09:02:40 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.019 |  |
| 2026-05-08 09:03:55 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-05-08 09:01:43 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-05-08 09:00:30 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-05-08 09:03:24 | Thanamalwila (Kirindi Oya) | 1.99 | 🟢 Normal | -0.029 |  |
| 2026-05-08 09:05:22 | Kithulgala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.031 |  |
| 2026-05-08 09:07:10 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.032 |  |
| 2026-05-08 09:05:30 | Katharagama (Menik Ganga) | 0.46 | 🟢 Normal | -0.039 |  |
| 2026-05-08 09:02:39 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.040 |  |
| 2026-05-08 09:04:03 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | -0.042 |  |
| 2026-05-08 09:01:48 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.052 |  |
| 2026-05-08 09:02:54 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | -0.080 |  |
| 2026-05-08 09:03:47 | Hanwella (Kelani Ganga) | 2.53 | 🟢 Normal | -0.090 |  |
| 2026-05-08 09:02:22 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.092 |  |
| 2026-05-08 09:04:47 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.097 |  |
| 2026-05-08 09:06:01 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.098 |  |
| 2026-05-08 09:06:56 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.099 |  |
| 2026-05-08 09:05:28 | Glencourse (Kelani Ganga) | 10.32 | 🟢 Normal | -0.186 |  |
| 2026-05-08 09:14:02 | Panadugama (Nilwala Ganga) | 4.34 | 🟢 Normal | -0.219 |  |
| 2026-05-08 09:00:57 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.347 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)