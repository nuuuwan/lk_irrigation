# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--06_20:24:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **199,131 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-06 20:24:04 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.064 |  |
| 2026-07-06 20:17:14 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:15:04 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:12:13 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-07-06 20:12:05 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:10:39 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:08:54 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-07-06 20:07:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.024 |  |
| 2026-07-06 20:06:42 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.046 |  |
| 2026-07-06 20:06:31 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-07-06 20:06:18 | Ellagawa (Kalu Ganga) | 4.84 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:06:17 | Ellagawa (Kalu Ganga) | 4.84 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:06:10 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-07-06 20:06:10 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | -0.010 |  |
| 2026-07-06 20:06:07 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:05:24 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 20:05:12 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-07-06 20:04:55 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-07-06 20:04:46 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:04:44 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | -0.040 |  |
| 2026-07-06 20:04:15 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:03:55 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:03:54 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:03:49 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.060 |  |
| 2026-07-06 20:03:12 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.017 |  |
| 2026-07-06 20:03:07 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-07-06 20:02:37 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:02:18 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:02:15 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.101 |  |
| 2026-07-06 20:01:40 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.010 |  |
| 2026-07-06 20:01:33 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 20:01:32 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:01:30 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:00:24 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:00:16 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:00:12 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-06 20:05:12 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-07-06 20:01:33 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 20:05:24 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 20:01:30 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:03:54 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:10:39 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:00:24 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:01:32 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:15:04 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:12:05 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:03:55 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:06:18 | Ellagawa (Kalu Ganga) | 4.84 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:05:38 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:00:12 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:04:46 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:04:15 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:02:37 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-06 18:00:56 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:06:07 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:17:14 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:02:18 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:00:16 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-06 20:04:55 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-07-06 20:06:10 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | -0.010 |  |
| 2026-07-06 20:06:31 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-07-06 18:02:06 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-07-06 18:06:11 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-07-06 20:03:07 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-07-06 20:01:40 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.010 |  |
| 2026-07-06 20:06:10 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-07-06 20:03:12 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.017 |  |
| 2026-07-06 20:12:13 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-07-06 20:07:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.024 |  |
| 2026-07-06 20:08:54 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-07-06 20:04:44 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | -0.040 |  |
| 2026-07-06 20:06:42 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.046 |  |
| 2026-07-06 20:03:49 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.060 |  |
| 2026-07-06 20:24:04 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.064 |  |
| 2026-07-06 20:02:15 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)