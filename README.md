# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--01_09:10:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **61,413 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 09:10:59 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-01 09:10:37 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-01 09:08:37 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-01 09:08:15 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-02-01 09:07:59 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-01 09:07:55 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-02-01 09:07:34 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-01 09:07:23 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -54.000 |  |
| 2026-02-01 09:07:21 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -54.000 |  |
| 2026-02-01 09:07:03 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -54.000 |  |
| 2026-02-01 09:06:43 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-01 09:06:24 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 09:06:02 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.060 |  |
| 2026-02-01 09:06:00 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-02-01 09:05:58 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-01 09:05:56 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-02-01 09:05:44 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.039 |  |
| 2026-02-01 09:05:04 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-01 09:04:59 | Kithulgala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.198 |  |
| 2026-02-01 09:04:48 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-02-01 09:04:19 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-01 09:04:17 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.058 |  |
| 2026-02-01 09:04:13 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-01 09:04:03 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-01 09:03:52 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-01 09:03:48 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-01 09:03:42 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-01 09:03:36 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-02-01 09:03:06 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-01 09:03:05 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-01 09:03:04 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-01 09:03:00 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.053 |  |
| 2026-02-01 09:02:43 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-01 09:02:36 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 09:02:28 | Manampitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.029 |  |
| 2026-02-01 09:02:02 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-01 09:01:54 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 09:01:50 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-01 09:01:10 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-01 09:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-01 08:19:32 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.023 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 09:07:55 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-02-01 09:04:48 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-02-01 09:03:52 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-01 09:08:15 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-02-01 09:02:02 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-01 09:04:13 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-01 09:10:59 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-01 09:07:34 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-01 09:03:48 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-01 09:10:37 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-01 09:03:05 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-01 09:01:10 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-01 09:06:43 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-01 09:08:37 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-01 09:01:50 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-01 09:01:54 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 09:02:36 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 09:02:43 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-01 09:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-01 09:07:59 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-01 08:03:03 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 09:04:19 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-01 09:04:03 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-01 09:05:04 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-01 09:03:06 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-01 09:06:24 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 09:05:58 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-01 09:03:36 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-02-01 09:06:00 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-02-01 09:03:42 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-01 09:05:56 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-02-01 09:02:28 | Manampitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.029 |  |
| 2026-02-01 09:05:44 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.039 |  |
| 2026-02-01 09:03:00 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.053 |  |
| 2026-02-01 09:04:17 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.058 |  |
| 2026-02-01 09:06:02 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.060 |  |
| 2026-02-01 08:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.061 |  |
| 2026-02-01 09:04:59 | Kithulgala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.198 |  |
| 2026-02-01 09:07:23 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -54.000 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)