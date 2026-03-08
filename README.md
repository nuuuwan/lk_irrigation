# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--08_09:28:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **92,408 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 09:28:49 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.023 |  |
| 2026-03-08 09:19:22 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:11:37 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | -0.085 |  |
| 2026-03-08 09:11:08 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:09:18 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.069 |  |
| 2026-03-08 09:09:01 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:08:44 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-03-08 09:07:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:06:41 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:05:42 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 09:05:36 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 09:05:25 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:05:13 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:04:54 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:04:27 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.352 |  |
| 2026-03-08 09:04:10 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-03-08 09:03:57 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:03:46 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.020 |  |
| 2026-03-08 09:03:44 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:03:28 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.142 |  |
| 2026-03-08 09:03:16 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.140 |  |
| 2026-03-08 09:03:08 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.019 |  |
| 2026-03-08 09:02:53 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 09:02:51 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-08 09:02:47 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:02:47 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-03-08 09:02:38 | Horowpothana (Yan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:02:32 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:02:15 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:02:00 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-03-08 09:01:34 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:01:33 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-03-08 09:01:15 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:01:14 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.058 |  |
| 2026-03-08 09:00:48 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | 0.356 | 🔺 Rising |
| 2026-03-08 09:00:29 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 09:00:48 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | 0.356 | 🔺 Rising |
| 2026-03-08 09:02:47 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-03-08 09:08:44 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-03-08 09:04:10 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-03-08 09:02:51 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-08 09:02:53 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 09:05:36 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 09:05:42 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 09:01:15 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:02:15 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:04:37 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:01:33 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:02:47 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:02:38 | Horowpothana (Yan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:06:41 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:09:01 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:03:57 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:08:04 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:05:25 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:02:32 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:19:22 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:05:13 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:03:44 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:01:34 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:11:08 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:04:54 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:07:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-03-08 09:02:00 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-03-08 09:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-03-08 09:00:29 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-03-08 09:03:08 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.019 |  |
| 2026-03-08 09:03:46 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.020 |  |
| 2026-03-08 09:28:49 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.023 |  |
| 2026-03-08 09:01:14 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.058 |  |
| 2026-03-08 09:09:18 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.069 |  |
| 2026-03-08 09:11:37 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | -0.085 |  |
| 2026-03-08 09:03:16 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.140 |  |
| 2026-03-08 09:03:28 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.142 |  |
| 2026-03-08 09:04:27 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.352 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)