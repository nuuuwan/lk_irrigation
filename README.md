# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--25_20:37:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **55,546 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 20:37:15 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:35:44 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-25 20:21:40 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.072 |  |
| 2026-01-25 20:19:56 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-01-25 20:14:39 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.008 |  |
| 2026-01-25 20:14:23 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:12:43 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:11:58 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:10:10 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:09:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:08:53 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-01-25 20:08:10 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:07:56 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:07:30 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:07:22 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:06:24 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-01-25 20:05:59 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:03:52 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-25 20:03:36 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:03:33 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-25 20:03:32 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:03:20 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:03:06 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-25 20:02:51 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.098 |  |
| 2026-01-25 20:02:42 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:02:41 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:02:39 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.041 |  |
| 2026-01-25 20:02:29 | Manampitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:02:28 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 20:02:24 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 20:02:22 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-01-25 20:02:19 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:02:16 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-01-25 20:02:11 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-25 20:01:59 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:01:57 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.050 |  |
| 2026-01-25 20:01:36 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:01:28 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 20:02:22 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-01-25 20:06:24 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-01-25 18:00:27 | Thanthirimale (Malwathu Oya) | 1.80 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-25 20:02:11 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-25 20:35:44 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-25 20:03:06 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-25 20:02:24 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 20:02:28 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 20:01:36 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:03:36 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:07:22 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:11:58 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-25 18:04:15 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:07:56 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:03:20 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:10:10 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:07:30 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:14:23 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:03:32 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:08:10 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:01:59 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:02:19 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:02:42 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:02:41 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:02:29 | Manampitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:37:15 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:05:59 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:09:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-25 20:14:39 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.008 |  |
| 2026-01-25 20:03:33 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-25 20:03:52 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-25 20:02:16 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-01-25 20:08:53 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-01-25 20:19:56 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-01-25 18:01:26 | Weraganthota (Mahaweli Ganga) | -2.35 | 🟢 Normal | -0.020 |  |
| 2026-01-25 20:02:39 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.041 |  |
| 2026-01-25 20:01:57 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.050 |  |
| 2026-01-25 20:21:40 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.072 |  |
| 2026-01-25 20:02:51 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.098 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)