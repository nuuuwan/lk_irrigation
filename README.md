# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--12_22:09:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,939 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 22:09:10 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-12 22:09:05 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-01-12 22:07:57 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2026-01-12 22:07:29 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.009 |  |
| 2026-01-12 22:07:04 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-01-12 22:07:02 | Glencourse (Kelani Ganga) | 9.32 | 🟢 Normal | 0.000 |  |
| 2026-01-12 22:06:18 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.061 |  |
| 2026-01-12 22:05:25 | Peradeniya (Mahaweli Ganga) | 2.59 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-01-12 22:05:23 | Dunamale (Aththanagalu Oya) | 1.46 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-01-12 22:04:52 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-12 22:04:29 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-12 22:03:50 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 22:03:18 | Hanwella (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-12 22:03:16 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-01-12 22:03:12 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-12 22:03:01 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-12 22:02:53 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 22:02:24 | Nakkala (Kumbukkan Oya) | 1.41 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-12 22:02:23 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.029 |  |
| 2026-01-12 22:02:19 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.062 |  |
| 2026-01-12 22:02:17 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-12 22:02:12 | Yaka Wewa (Ma Oya) | 1.42 | 🟢 Normal | -0.118 |  |
| 2026-01-12 22:01:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-01-12 22:01:24 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-12 22:01:21 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-01-12 22:00:59 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-12 22:00:51 | Horowpothana (Yan Oya) | 3.27 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-12 22:00:43 | Siyambalanduwa (Heda Oya) | 1.27 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-01-12 22:00:37 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-12 22:00:12 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-12 21:13:41 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 22:09:05 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-01-12 22:03:16 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-01-12 22:00:43 | Siyambalanduwa (Heda Oya) | 1.27 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-01-12 22:05:25 | Peradeniya (Mahaweli Ganga) | 2.59 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-01-12 22:05:23 | Dunamale (Aththanagalu Oya) | 1.46 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-01-12 22:04:52 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-12 22:00:51 | Horowpothana (Yan Oya) | 3.27 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-12 22:02:24 | Nakkala (Kumbukkan Oya) | 1.41 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-12 22:04:29 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-12 22:02:53 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 22:00:37 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-12 21:03:06 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 22:03:50 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 18:00:10 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-12 22:02:17 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-12 21:04:00 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:04:27 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-12 22:01:24 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-12 22:03:01 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-12 22:03:18 | Hanwella (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-12 22:01:21 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-01-12 22:07:02 | Glencourse (Kelani Ganga) | 9.32 | 🟢 Normal | 0.000 |  |
| 2026-01-12 22:00:12 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-12 21:05:46 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:02:58 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 22:00:59 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-12 22:09:10 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-12 22:03:12 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-12 22:07:57 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2026-01-12 21:10:36 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.009 |  |
| 2026-01-12 21:07:09 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-01-12 22:07:29 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.009 |  |
| 2026-01-12 22:07:04 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-01-12 21:07:37 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-12 22:01:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-01-12 22:02:23 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.029 |  |
| 2026-01-12 22:06:18 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.061 |  |
| 2026-01-12 22:02:19 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.062 |  |
| 2026-01-12 22:02:12 | Yaka Wewa (Ma Oya) | 1.42 | 🟢 Normal | -0.118 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)