# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--22_08:06:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **104,105 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 08:06:03 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.172 |  |
| 2026-03-22 08:05:53 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.137 |  |
| 2026-03-22 08:05:47 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-22 08:05:42 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:05:24 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.201 |  |
| 2026-03-22 08:05:04 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 08:04:42 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-03-22 08:04:39 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-22 08:04:04 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:03:45 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:03:42 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-22 08:03:38 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:03:37 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:03:29 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-03-22 08:03:28 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-22 08:03:27 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:03:15 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:02:42 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.041 |  |
| 2026-03-22 08:02:33 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 08:02:14 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-22 08:02:07 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:01:25 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:01:22 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:01:15 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:01:07 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.056 |  |
| 2026-03-22 08:01:03 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:00:59 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.040 |  |
| 2026-03-22 08:00:31 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | -0.021 |  |
| 2026-03-22 08:00:14 | Weraganthota (Mahaweli Ganga) | -2.64 | 🟢 Normal | -0.090 |  |
| 2026-03-22 07:39:33 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-22 07:24:17 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-22 07:23:38 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.201 |  |
| 2026-03-22 07:18:09 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 07:14:04 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-22 07:12:35 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.137 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 07:02:50 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-22 07:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-03-22 08:03:28 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-22 08:02:14 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-22 08:05:47 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-22 07:07:32 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-03-22 08:03:42 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-22 08:04:39 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-22 08:05:04 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 08:02:33 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 08:02:07 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:03:27 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:01:15 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-22 07:01:50 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:05:42 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 07:39:33 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:03:15 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:03:45 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:01:22 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-22 07:01:32 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-22 07:08:24 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:01:03 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:03:38 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:03:37 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:04:04 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:00:59 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-22 07:24:17 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:01:25 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-22 07:08:42 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-03-22 08:03:29 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-03-22 08:04:42 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-03-22 08:00:31 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | -0.021 |  |
| 2026-03-22 08:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.040 |  |
| 2026-03-22 08:02:42 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.041 |  |
| 2026-03-22 08:01:07 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.056 |  |
| 2026-03-22 08:00:14 | Weraganthota (Mahaweli Ganga) | -2.64 | 🟢 Normal | -0.090 |  |
| 2026-03-22 08:05:53 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.137 |  |
| 2026-03-22 08:06:03 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.172 |  |
| 2026-03-22 08:05:24 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.201 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)