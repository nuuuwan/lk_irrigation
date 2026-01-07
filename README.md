# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--07_20:19:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **39,373 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 20:19:26 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-07 20:16:14 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-07 20:14:12 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-01-07 20:12:26 | Urawa (Nilwala Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:09:15 | Manampitiya (Mahaweli Ganga) | 2.54 | 🟢 Normal | -0.077 |  |
| 2026-01-07 20:07:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.019 |  |
| 2026-01-07 20:06:52 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:06:37 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:06:27 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:05:57 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:05:14 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:05:03 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.071 |  |
| 2026-01-07 20:05:00 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:04:58 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | -0.010 |  |
| 2026-01-07 20:04:52 | Katharagama (Menik Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-01-07 20:04:25 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:04:22 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.058 |  |
| 2026-01-07 20:04:20 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-01-07 20:04:13 | Padiyathalawa (Maduru Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-07 20:04:10 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.039 |  |
| 2026-01-07 20:03:53 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:03:25 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:03:14 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.377 | 🔺 Rising |
| 2026-01-07 20:03:04 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:02:55 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-07 20:02:46 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-07 20:02:37 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:02:14 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-01-07 20:02:13 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-07 20:02:01 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-01-07 20:01:55 | Siyambalanduwa (Heda Oya) | 1.45 | 🟢 Normal | -0.042 |  |
| 2026-01-07 20:01:40 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:01:22 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.011 |  |
| 2026-01-07 20:01:21 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:01:01 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:00:38 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:59:14 | Urawa (Nilwala Ganga) | 1.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 20:03:14 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.377 | 🔺 Rising |
| 2026-01-07 20:14:12 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-01-07 20:02:55 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-07 20:02:13 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-07 18:01:49 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 19:03:23 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 20:00:38 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:03:25 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:01:40 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:01:21 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:05:57 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:03:04 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:03:53 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:06:27 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:05:14 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:04:25 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:06:37 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:05:00 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:12:26 | Urawa (Nilwala Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:01:01 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:02:37 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:06:52 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-07 20:16:14 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-07 20:04:13 | Padiyathalawa (Maduru Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-07 20:04:58 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | -0.010 |  |
| 2026-01-07 20:04:20 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-01-07 20:04:52 | Katharagama (Menik Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-01-07 20:02:14 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-01-07 20:02:46 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-07 20:19:26 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-07 20:02:01 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-01-07 20:01:22 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.011 |  |
| 2026-01-07 20:07:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.019 |  |
| 2026-01-07 18:03:25 | Thanthirimale (Malwathu Oya) | 1.77 | 🟢 Normal | -0.023 |  |
| 2026-01-07 20:04:10 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.039 |  |
| 2026-01-07 20:01:55 | Siyambalanduwa (Heda Oya) | 1.45 | 🟢 Normal | -0.042 |  |
| 2026-01-07 20:04:22 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.058 |  |
| 2026-01-07 20:05:03 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.071 |  |
| 2026-01-07 20:09:15 | Manampitiya (Mahaweli Ganga) | 2.54 | 🟢 Normal | -0.077 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)