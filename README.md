# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--06_21:16:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,519 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 21:16:16 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:12:06 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.012 |  |
| 2026-01-06 21:11:56 | Manampitiya (Mahaweli Ganga) | 3.79 | 🟡 Alert | -0.026 |  |
| 2026-01-06 21:10:02 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.026 |  |
| 2026-01-06 21:08:29 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.057 |  |
| 2026-01-06 21:08:10 | Katharagama (Menik Ganga) | 0.52 | 🟢 Normal | -0.046 |  |
| 2026-01-06 21:07:30 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.033 |  |
| 2026-01-06 21:07:21 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:06:48 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:06:32 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:06:13 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:05:38 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-06 21:05:32 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 21:05:27 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:05:02 | Peradeniya (Mahaweli Ganga) | 2.59 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-01-06 21:04:51 | Padiyathalawa (Maduru Oya) | 1.65 | 🟢 Normal | -0.051 |  |
| 2026-01-06 21:04:51 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:04:45 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:04:33 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-06 21:03:50 | Horowpothana (Yan Oya) | 2.74 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-06 21:03:49 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:03:40 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:03:37 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:03:28 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-06 21:03:27 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.137 |  |
| 2026-01-06 21:03:25 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-01-06 21:03:21 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:03:16 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:03:11 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.110 |  |
| 2026-01-06 21:02:49 | Siyambalanduwa (Heda Oya) | 2.91 | 🟢 Normal | -0.240 |  |
| 2026-01-06 21:02:29 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:02:17 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.030 |  |
| 2026-01-06 21:02:17 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:02:11 | Thaldena (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.089 |  |
| 2026-01-06 21:01:14 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:00:44 | Nakkala (Kumbukkan Oya) | 1.70 | 🟢 Normal | -0.082 |  |
| 2026-01-06 20:22:25 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 21:11:56 | Manampitiya (Mahaweli Ganga) | 3.79 | 🟡 Alert | -0.026 |  |
| 2026-01-06 21:05:02 | Peradeniya (Mahaweli Ganga) | 2.59 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-01-06 21:03:50 | Horowpothana (Yan Oya) | 2.74 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-06 21:05:38 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-06 18:00:39 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 18:02:01 | Weraganthota (Mahaweli Ganga) | -0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 21:05:32 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 21:03:49 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:16:16 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:03:16 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:03:37 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:03:13 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:02:29 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:06:13 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:03:21 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:07:21 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:01:14 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:04:51 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:06:32 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:03:40 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:02:17 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:05:27 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:06:48 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-06 21:03:25 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-01-06 21:04:33 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-06 21:03:28 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-06 21:12:06 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.012 |  |
| 2026-01-06 21:10:02 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.026 |  |
| 2026-01-06 21:02:17 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.030 |  |
| 2026-01-06 21:07:30 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.033 |  |
| 2026-01-06 21:08:10 | Katharagama (Menik Ganga) | 0.52 | 🟢 Normal | -0.046 |  |
| 2026-01-06 21:04:51 | Padiyathalawa (Maduru Oya) | 1.65 | 🟢 Normal | -0.051 |  |
| 2026-01-06 21:08:29 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.057 |  |
| 2026-01-06 20:07:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.072 |  |
| 2026-01-06 21:00:44 | Nakkala (Kumbukkan Oya) | 1.70 | 🟢 Normal | -0.082 |  |
| 2026-01-06 21:02:11 | Thaldena (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.089 |  |
| 2026-01-06 21:03:11 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.110 |  |
| 2026-01-06 21:03:27 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.137 |  |
| 2026-01-06 21:02:49 | Siyambalanduwa (Heda Oya) | 2.91 | 🟢 Normal | -0.240 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)