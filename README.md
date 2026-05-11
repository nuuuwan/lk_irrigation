# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--11_06:30:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **148,638 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 06:30:44 | Galgamuwa (Mee Oya) | 2.10 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-05-11 06:11:42 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-11 06:09:46 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-11 06:08:24 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-11 06:05:34 | Katharagama (Menik Ganga) | 1.64 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-11 06:05:24 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-11 06:05:05 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-11 06:04:58 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-05-11 06:04:58 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-11 06:04:55 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 06:04:49 | Moragaswewa (Deduru Oya) | 1.18 | 🟢 Normal | -0.038 |  |
| 2026-05-11 06:04:47 | Ellagawa (Kalu Ganga) | 4.91 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-11 06:04:28 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-11 06:04:14 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.734 | 🔺 Rising |
| 2026-05-11 06:04:06 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.048 |  |
| 2026-05-11 06:03:51 | Kuda Oya (Kirindi Oya) | 3.90 | 🟢 Normal | -1.225 |  |
| 2026-05-11 06:03:46 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-11 06:03:40 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 324.000 | 🔺 Rising |
| 2026-05-11 06:03:39 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 324.000 | 🔺 Rising |
| 2026-05-11 06:03:28 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-11 06:03:23 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | -0.030 |  |
| 2026-05-11 06:03:03 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 06:02:54 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | 0.347 | 🔺 Rising |
| 2026-05-11 06:02:52 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.020 |  |
| 2026-05-11 06:02:45 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-11 06:02:41 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | 0.000 |  |
| 2026-05-11 06:02:33 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-11 06:02:24 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-05-11 06:02:16 | Thanamalwila (Kirindi Oya) | 4.10 | 🟡 Alert | -1.201 |  |
| 2026-05-11 06:02:15 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-11 06:02:14 | Wellawaya (Kirindi Oya) | 1.57 | 🟢 Normal | 0.943 | 🔺 Rising |
| 2026-05-11 06:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.031 |  |
| 2026-05-11 06:01:14 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.021 |  |
| 2026-05-11 06:01:08 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-11 06:00:35 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-05-11 06:00:32 | Moraketiya (Walawe Ganga) | 1.57 | 🟢 Normal | 0.368 | 🔺 Rising |
| 2026-05-11 06:00:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.82 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-11 06:00:26 | Rathnapura (Kalu Ganga) | 2.48 | 🟢 Normal | 0.161 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 06:02:16 | Thanamalwila (Kirindi Oya) | 4.10 | 🟡 Alert | -1.201 |  |
| 2026-05-11 06:03:40 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 324.000 | 🔺 Rising |
| 2026-05-11 06:02:14 | Wellawaya (Kirindi Oya) | 1.57 | 🟢 Normal | 0.943 | 🔺 Rising |
| 2026-05-11 06:04:14 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.734 | 🔺 Rising |
| 2026-05-11 06:00:32 | Moraketiya (Walawe Ganga) | 1.57 | 🟢 Normal | 0.368 | 🔺 Rising |
| 2026-05-11 06:02:54 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | 0.347 | 🔺 Rising |
| 2026-05-11 06:00:35 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-05-11 06:00:26 | Rathnapura (Kalu Ganga) | 2.48 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-05-11 06:30:44 | Galgamuwa (Mee Oya) | 2.10 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-05-11 06:05:05 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-11 06:04:47 | Ellagawa (Kalu Ganga) | 4.91 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-11 06:05:24 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-11 06:00:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.82 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-11 06:01:08 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-11 06:05:34 | Katharagama (Menik Ganga) | 1.64 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-11 06:03:46 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-11 06:04:28 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-11 06:09:46 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-11 06:03:03 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 06:04:55 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 06:02:41 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | 0.000 |  |
| 2026-05-11 06:08:24 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-11 06:11:42 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-11 06:04:58 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-11 06:03:28 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-11 06:02:45 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-11 06:04:58 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-05-11 06:02:33 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-10 18:01:26 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-05-11 05:03:59 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-05-11 06:02:15 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-11 06:02:24 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-05-11 06:02:52 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.020 |  |
| 2026-05-11 06:01:14 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.021 |  |
| 2026-05-11 06:03:23 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | -0.030 |  |
| 2026-05-11 06:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.031 |  |
| 2026-05-11 06:04:49 | Moragaswewa (Deduru Oya) | 1.18 | 🟢 Normal | -0.038 |  |
| 2026-05-11 06:04:06 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.048 |  |
| 2026-05-11 06:03:51 | Kuda Oya (Kirindi Oya) | 3.90 | 🟢 Normal | -1.225 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)