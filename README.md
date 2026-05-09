# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_20:13:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,373 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 20:13:59 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | -0.017 |  |
| 2026-05-09 20:13:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | -0.035 |  |
| 2026-05-09 20:11:04 | Katharagama (Menik Ganga) | 1.69 | 🟢 Normal | -0.048 |  |
| 2026-05-09 20:10:57 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-05-09 20:10:44 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-09 20:10:03 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-05-09 20:08:22 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.011 |  |
| 2026-05-09 20:07:26 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | -0.038 |  |
| 2026-05-09 20:06:54 | Putupaula (Kalu Ganga) | 1.29 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-09 20:05:58 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | -0.115 |  |
| 2026-05-09 20:05:43 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.033 |  |
| 2026-05-09 20:05:42 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-05-09 20:04:48 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.090 |  |
| 2026-05-09 20:04:32 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.033 |  |
| 2026-05-09 20:04:22 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.066 |  |
| 2026-05-09 20:03:37 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | 0.000 |  |
| 2026-05-09 20:03:31 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.025 |  |
| 2026-05-09 20:03:29 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-05-09 20:03:12 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-09 20:03:07 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.012 |  |
| 2026-05-09 20:03:02 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-09 20:03:00 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-09 20:02:54 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-09 20:02:52 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-09 20:02:45 | Moragaswewa (Deduru Oya) | 3.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 20:02:38 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-09 20:02:34 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-09 20:02:32 | Thanamalwila (Kirindi Oya) | 2.16 | 🟢 Normal | -0.039 |  |
| 2026-05-09 20:02:20 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-09 20:02:07 | Kuda Oya (Kirindi Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-05-09 20:02:06 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.022 |  |
| 2026-05-09 20:02:00 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 20:01:58 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-09 20:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-05-09 20:01:05 | Wellawaya (Kirindi Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 20:00:36 | Wellawaya (Kirindi Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 20:00:12 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-09 19:38:06 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 20:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-05-09 20:05:42 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-05-09 18:02:49 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-09 20:02:34 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-09 20:03:02 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-09 20:02:54 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-09 20:02:00 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 20:06:54 | Putupaula (Kalu Ganga) | 1.29 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-09 20:01:05 | Wellawaya (Kirindi Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 20:02:20 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-09 20:02:45 | Moragaswewa (Deduru Oya) | 3.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 20:01:58 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-09 20:02:38 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-09 20:03:37 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | 0.000 |  |
| 2026-05-09 20:03:12 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-09 20:02:52 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-09 20:03:00 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-09 20:10:44 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-09 20:00:12 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-09 20:10:03 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-05-09 20:02:07 | Kuda Oya (Kirindi Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-05-09 20:03:29 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-05-09 20:08:22 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.011 |  |
| 2026-05-09 20:10:57 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-05-09 20:03:07 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.012 |  |
| 2026-05-09 20:13:59 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | -0.017 |  |
| 2026-05-09 20:02:06 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.022 |  |
| 2026-05-09 20:03:31 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.025 |  |
| 2026-05-09 20:05:43 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.033 |  |
| 2026-05-09 20:04:32 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.033 |  |
| 2026-05-09 20:13:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | -0.035 |  |
| 2026-05-09 20:07:26 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | -0.038 |  |
| 2026-05-09 20:02:32 | Thanamalwila (Kirindi Oya) | 2.16 | 🟢 Normal | -0.039 |  |
| 2026-05-09 20:11:04 | Katharagama (Menik Ganga) | 1.69 | 🟢 Normal | -0.048 |  |
| 2026-05-09 18:00:42 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | -0.051 |  |
| 2026-05-09 20:04:22 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.066 |  |
| 2026-05-09 18:04:22 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | -0.081 |  |
| 2026-05-09 20:04:48 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.090 |  |
| 2026-05-09 20:05:58 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | -0.115 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)