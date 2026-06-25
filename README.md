# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--26_00:18:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **189,414 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 00:18:31 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:13:10 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:12:31 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:08:05 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | -0.019 |  |
| 2026-06-26 00:07:20 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | -0.027 |  |
| 2026-06-26 00:07:20 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-26 00:06:24 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-26 00:06:23 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-26 00:06:12 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 00:05:05 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-06-26 00:04:55 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-26 00:04:51 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-26 00:04:44 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.013 |  |
| 2026-06-26 00:04:16 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:04:10 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:03:56 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-06-26 00:03:55 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-06-26 00:03:46 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:03:45 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:03:42 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-26 00:03:24 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:03:10 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-06-26 00:02:42 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-06-26 00:02:26 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:01:58 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-26 00:01:55 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-26 00:01:43 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.012 |  |
| 2026-06-26 00:01:24 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:00:59 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:00:55 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:00:26 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-06-26 00:00:09 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-25 23:44:42 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:42:57 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 00:03:56 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-06-26 00:03:42 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-26 00:04:51 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-26 00:01:55 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-26 00:06:23 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-26 00:07:20 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-26 00:06:24 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-26 00:00:09 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-26 00:01:58 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-26 00:06:12 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 00:01:24 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:00:55 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:05:17 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:02:26 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:07:55 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:13:10 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:03:46 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:12:31 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:00:59 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:03:45 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:04:16 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:04:10 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-25 18:02:21 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:18:31 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-26 00:03:24 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-25 23:08:43 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-06-25 18:01:28 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.010 |  |
| 2026-06-26 00:00:26 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-06-26 00:04:55 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-25 18:02:25 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-26 00:05:05 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-06-26 00:01:43 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.012 |  |
| 2026-06-26 00:04:44 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.013 |  |
| 2026-06-26 00:08:05 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | -0.019 |  |
| 2026-06-26 00:03:10 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-06-26 00:02:42 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-06-25 20:05:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | -0.024 |  |
| 2026-06-26 00:07:20 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | -0.027 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)