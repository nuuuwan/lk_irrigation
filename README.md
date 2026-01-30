# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--30_17:14:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **59,909 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-30 17:14:12 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.042 |  |
| 2026-01-30 17:13:28 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-30 17:09:55 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:09:18 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-01-30 17:09:05 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:08:52 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:07:17 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-01-30 17:07:15 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-01-30 17:06:04 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:05:25 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.025 |  |
| 2026-01-30 17:05:16 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-30 17:04:55 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:04:51 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-30 17:04:06 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-01-30 17:04:02 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:03:47 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:03:45 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:03:39 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:03:37 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:03:37 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-01-30 17:03:28 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:03:25 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.012 |  |
| 2026-01-30 17:03:20 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 17:03:19 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:03:18 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:03:14 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-01-30 17:02:53 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.040 |  |
| 2026-01-30 17:02:46 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-30 17:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-30 17:01:48 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.076 |  |
| 2026-01-30 17:01:47 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:01:36 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:01:28 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:01:05 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:01:03 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-30 17:01:01 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:00:56 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:00:48 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:00:23 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.066 |  |
| 2026-01-30 16:29:55 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-30 17:07:17 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-01-30 17:03:14 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-01-30 17:09:18 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-01-30 17:13:28 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-30 16:06:12 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-30 17:02:46 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-30 17:05:16 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-30 17:04:51 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-30 16:04:35 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-30 17:03:20 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 17:03:45 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:01:01 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:01:28 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:29:55 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:03:47 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:00:48 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:04:55 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:08:52 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:01:05 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:03:28 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:01:47 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:03:19 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:09:55 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:03:37 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:06:04 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:09:05 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:00:56 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:04:02 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:03:18 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:03:39 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-30 17:03:37 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-01-30 17:01:03 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-30 17:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-30 17:03:25 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.012 |  |
| 2026-01-30 17:05:25 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.025 |  |
| 2026-01-30 17:02:53 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.040 |  |
| 2026-01-30 17:14:12 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.042 |  |
| 2026-01-30 17:00:23 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.066 |  |
| 2026-01-30 17:01:48 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.076 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)