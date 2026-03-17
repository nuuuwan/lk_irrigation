# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--17_22:44:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **100,167 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 22:44:27 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:13:42 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:12:23 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.066 |  |
| 2026-03-17 22:11:07 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-03-17 22:10:48 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | -0.027 |  |
| 2026-03-17 22:09:18 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:07:43 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-03-17 22:07:05 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-17 22:06:25 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-17 22:05:47 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.519 | 🔺 Rising |
| 2026-03-17 22:05:27 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-17 22:05:25 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:05:10 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-03-17 22:05:02 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-03-17 22:04:19 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-17 22:03:34 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:03:32 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.020 |  |
| 2026-03-17 22:03:11 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:03:05 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-03-17 22:03:01 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:02:47 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:02:44 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | -0.030 |  |
| 2026-03-17 22:02:38 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:02:27 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:02:21 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:02:19 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:02:11 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:02:02 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-03-17 22:02:02 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:01:31 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:01:17 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-03-17 22:00:49 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-17 22:00:43 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 22:05:47 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.519 | 🔺 Rising |
| 2026-03-17 20:03:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-03-17 22:06:25 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-17 22:11:07 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-03-17 22:05:27 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-17 22:03:05 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-03-17 22:07:05 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-17 22:00:49 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-17 21:01:57 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-17 22:00:43 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:02:47 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:03:11 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:02:27 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:03:34 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:44:27 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-17 18:04:05 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:05:25 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:02:38 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-17 21:07:02 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:13:42 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:09:18 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:02:02 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:03:01 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:02:21 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:02:11 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:01:31 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 18:01:54 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:02:19 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:07:43 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-03-17 22:04:19 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-17 22:05:10 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-03-17 22:01:17 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-03-17 22:03:32 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.020 |  |
| 2026-03-17 22:02:02 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-03-17 22:05:02 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-03-17 22:10:48 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | -0.027 |  |
| 2026-03-17 22:02:44 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | -0.030 |  |
| 2026-03-17 21:02:27 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.045 |  |
| 2026-03-17 22:12:23 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.066 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)