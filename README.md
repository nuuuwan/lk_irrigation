# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--21_19:19:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **51,909 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 19:19:21 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-21 19:18:01 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:16:00 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:13:16 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:12:43 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:12:36 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:11:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.33 | 🟢 Normal | -0.009 |  |
| 2026-01-21 19:06:49 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:06:38 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:06:35 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.056 |  |
| 2026-01-21 19:05:02 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-01-21 19:04:31 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:04:27 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.091 |  |
| 2026-01-21 19:04:14 | Padiyathalawa (Maduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:04:00 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2026-01-21 19:03:56 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.344 | 🔺 Rising |
| 2026-01-21 19:03:56 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:03:52 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.837 | 🔺 Rising |
| 2026-01-21 19:03:23 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.020 |  |
| 2026-01-21 19:03:19 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | -0.010 |  |
| 2026-01-21 19:03:12 | Manampitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-21 19:03:09 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.837 | 🔺 Rising |
| 2026-01-21 19:03:05 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.013 |  |
| 2026-01-21 19:03:03 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:02:46 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:02:46 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:02:45 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:02:35 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:02:19 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:02:14 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 19:02:13 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:01:18 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-21 19:01:17 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:00:55 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:00:47 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:00:42 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 19:03:52 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.837 | 🔺 Rising |
| 2026-01-21 19:03:56 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.344 | 🔺 Rising |
| 2026-01-21 18:00:57 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-01-21 19:01:18 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-21 19:03:12 | Manampitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-21 19:19:21 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-21 19:02:14 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 18:03:38 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:00:55 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:02:45 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:18:01 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:02:35 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:02:13 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:16:00 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:00:47 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-21 18:02:52 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:02:46 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:03:03 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:13:16 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:02:46 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:04:14 | Padiyathalawa (Maduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:01:17 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:03:56 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:00:42 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:12:36 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:06:49 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:02:19 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:12:43 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-21 18:01:41 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:04:31 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:06:38 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:11:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.33 | 🟢 Normal | -0.009 |  |
| 2026-01-21 19:05:02 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-01-21 19:03:19 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | -0.010 |  |
| 2026-01-21 19:03:05 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.013 |  |
| 2026-01-21 19:03:23 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.020 |  |
| 2026-01-21 19:04:00 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2026-01-21 19:06:35 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.056 |  |
| 2026-01-21 19:04:27 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)