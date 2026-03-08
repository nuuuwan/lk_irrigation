# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--08_05:19:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **92,252 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 05:19:42 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:14:55 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | -0.005 |  |
| 2026-03-08 05:14:01 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.024 |  |
| 2026-03-08 05:10:39 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:08:39 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-03-08 05:06:06 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:05:36 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2026-03-08 05:05:19 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-08 05:04:25 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | -0.005 |  |
| 2026-03-08 05:04:07 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | 9.612 | 🔺 Rising |
| 2026-03-08 05:04:03 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:03:44 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-03-08 05:03:36 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.024 |  |
| 2026-03-08 05:03:17 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-03-08 05:02:54 | Horowpothana (Yan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:02:39 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-08 05:02:36 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:02:32 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-03-08 05:02:30 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:02:14 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.027 |  |
| 2026-03-08 05:02:08 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:02:06 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.230 |  |
| 2026-03-08 05:01:59 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:01:13 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:01:09 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 05:01:05 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:00:53 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 05:00:45 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:00:41 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 9.612 | 🔺 Rising |
| 2026-03-08 05:00:33 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:00:22 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:00:22 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-08 04:59:41 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.517 | 🔺 Rising |
| 2026-03-08 04:54:06 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 04:54:04 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 04:54:03 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 04:54:02 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 04:48:46 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.024 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 05:04:07 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | 9.612 | 🔺 Rising |
| 2026-03-08 04:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.795 | 🔺 Rising |
| 2026-03-08 04:59:41 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.517 | 🔺 Rising |
| 2026-03-08 03:32:33 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-03-08 05:03:17 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-03-08 05:08:39 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-03-08 05:02:39 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-08 05:05:19 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-08 05:01:09 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 05:00:53 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 05:00:22 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:02:08 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:01:05 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:00:45 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:01:59 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:02:54 | Horowpothana (Yan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:02:36 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:10:39 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:00:33 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:06:06 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:00:22 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:02:36 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:02:30 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 04:03:33 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:04:03 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:01:13 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:02:19 | Thanthirimale (Malwathu Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:19:42 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:14:55 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | -0.005 |  |
| 2026-03-08 05:04:25 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | -0.005 |  |
| 2026-03-08 05:03:44 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-03-08 05:02:32 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-03-08 05:14:01 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.024 |  |
| 2026-03-08 05:03:36 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.024 |  |
| 2026-03-08 04:04:07 | Thawalama (Gin Ganga) | 0.93 | 🟢 Normal | -0.027 |  |
| 2026-03-08 05:02:14 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.027 |  |
| 2026-03-08 05:05:36 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2026-03-07 18:04:37 | Weraganthota (Mahaweli Ganga) | -2.18 | 🟢 Normal | -0.065 |  |
| 2026-03-08 05:02:06 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.230 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)