# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--21_05:06:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **51,342 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 05:06:19 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:06:07 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-21 05:06:00 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:05:48 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:05:38 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.053 |  |
| 2026-01-21 05:05:00 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:03:49 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.307 | 🔺 Rising |
| 2026-01-21 05:03:33 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:03:19 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-21 05:03:06 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:03:03 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.029 |  |
| 2026-01-21 05:03:03 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.050 |  |
| 2026-01-21 05:02:47 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:02:42 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:02:42 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:02:28 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 05:02:22 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.275 |  |
| 2026-01-21 05:02:02 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:01:53 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:01:52 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:01:52 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.411 | 🔺 Rising |
| 2026-01-21 05:01:35 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:01:29 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:01:23 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:00:57 | Manampitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.030 |  |
| 2026-01-21 05:00:25 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-21 04:31:12 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-21 04:21:15 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-21 04:11:30 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 04:11:23 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-21 04:11:06 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 05:01:52 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.411 | 🔺 Rising |
| 2026-01-21 05:03:49 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.307 | 🔺 Rising |
| 2026-01-21 04:05:13 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-01-21 05:06:07 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-21 04:31:12 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-20 18:00:20 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-21 02:05:21 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-21 05:02:28 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 05:00:25 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:03:06 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:01:52 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:02:47 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:01:23 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-20 18:01:04 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:05:48 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:06:00 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:02:02 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | 0.000 |  |
| 2026-01-21 03:26:40 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-01-21 04:04:21 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-21 04:01:39 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:01:35 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:02:42 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-20 21:01:57 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:02:42 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-21 04:11:30 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:06:19 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:05:00 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-20 18:01:15 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:01:53 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:03:33 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-21 04:11:06 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:01:29 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-21 04:00:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-01-21 05:03:19 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-21 05:03:03 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.029 |  |
| 2026-01-21 05:00:57 | Manampitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.030 |  |
| 2026-01-21 05:03:03 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.050 |  |
| 2026-01-21 05:05:38 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.053 |  |
| 2026-01-21 05:02:22 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.275 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)