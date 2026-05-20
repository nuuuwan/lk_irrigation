# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--20_07:26:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **156,758 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 07:26:25 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.008 |  |
| 2026-05-20 07:20:00 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:11:35 | Hanwella (Kelani Ganga) | 1.91 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-20 07:09:46 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-20 07:09:08 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-20 07:08:56 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.036 |  |
| 2026-05-20 07:08:32 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.072 |  |
| 2026-05-20 07:08:26 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:08:01 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:07:58 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:07:37 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-05-20 07:07:32 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.018 |  |
| 2026-05-20 07:07:24 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:07:15 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.018 |  |
| 2026-05-20 07:07:07 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-05-20 07:07:06 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-05-20 07:06:59 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | -0.039 |  |
| 2026-05-20 07:05:45 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.046 |  |
| 2026-05-20 07:05:38 | Thanthirimale (Malwathu Oya) | 2.14 | 🟢 Normal | -0.006 |  |
| 2026-05-20 07:05:14 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.105 |  |
| 2026-05-20 07:04:23 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:04:09 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 07:03:50 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 07:03:48 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.12 | 🟢 Normal | -0.039 |  |
| 2026-05-20 07:03:32 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:02:47 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:02:40 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:02:24 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:02:23 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.029 |  |
| 2026-05-20 07:02:09 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:02:04 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:01:36 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:01:10 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:01:02 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.042 |  |
| 2026-05-20 07:01:02 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.030 |  |
| 2026-05-20 07:00:43 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | -0.021 |  |
| 2026-05-20 07:00:38 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:00:27 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 07:09:08 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-20 07:11:35 | Hanwella (Kelani Ganga) | 1.91 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-20 07:04:09 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 07:03:50 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 07:09:46 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-20 07:03:48 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:07:24 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:20:00 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:03:32 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:02:04 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:08:26 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:02:24 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:04:23 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:00:38 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:02:47 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:02:40 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:07:58 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:08:01 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:01:10 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:01:36 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:02:09 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-20 07:05:38 | Thanthirimale (Malwathu Oya) | 2.14 | 🟢 Normal | -0.006 |  |
| 2026-05-20 07:26:25 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.008 |  |
| 2026-05-20 07:07:07 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-05-20 07:07:37 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-05-20 07:00:27 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-05-20 07:07:15 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.018 |  |
| 2026-05-20 07:07:32 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.018 |  |
| 2026-05-20 07:07:06 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-05-20 07:00:43 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | -0.021 |  |
| 2026-05-20 07:02:23 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.029 |  |
| 2026-05-20 07:01:02 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.030 |  |
| 2026-05-20 07:08:56 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.036 |  |
| 2026-05-20 07:06:59 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | -0.039 |  |
| 2026-05-20 07:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.12 | 🟢 Normal | -0.039 |  |
| 2026-05-20 07:01:02 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.042 |  |
| 2026-05-20 07:05:45 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.046 |  |
| 2026-05-20 07:08:32 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.072 |  |
| 2026-05-20 07:05:14 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)