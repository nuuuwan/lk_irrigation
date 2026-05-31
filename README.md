# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_13:19:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **166,630 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 13:19:33 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | -0.008 |  |
| 2026-05-31 13:12:45 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:09:56 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | -0.010 |  |
| 2026-05-31 13:08:51 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-05-31 13:08:40 | Baddegama (Gin Ganga) | 2.23 | 🟢 Normal | -0.009 |  |
| 2026-05-31 13:07:44 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:07:44 | Rathnapura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.038 |  |
| 2026-05-31 13:07:42 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:07:37 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:06:16 | Peradeniya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.019 |  |
| 2026-05-31 13:06:09 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:06:05 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.009 |  |
| 2026-05-31 13:05:48 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-31 13:05:26 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:05:00 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:04:58 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:04:53 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:04:52 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:04:33 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-05-31 13:04:13 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-31 13:03:46 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | -0.020 |  |
| 2026-05-31 13:03:42 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | -0.022 |  |
| 2026-05-31 13:03:28 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:03:18 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-31 13:03:15 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-05-31 13:03:03 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-05-31 13:02:57 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-05-31 13:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.88 | 🟢 Normal | -0.199 |  |
| 2026-05-31 13:02:40 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-05-31 13:02:32 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-05-31 13:02:25 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-31 13:01:42 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.040 |  |
| 2026-05-31 13:01:18 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:01:16 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:01:04 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:00:56 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:00:33 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:00:09 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 13:02:32 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-05-31 13:05:48 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-31 13:04:13 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-31 13:03:18 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-31 13:00:56 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:05:26 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:00:33 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:06:09 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:07:44 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:04:53 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:04:52 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:03:28 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:01:18 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:07:37 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:05:00 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:07:42 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:01:04 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:12:45 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:01:48 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:04:58 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:19:33 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | -0.008 |  |
| 2026-05-31 13:08:40 | Baddegama (Gin Ganga) | 2.23 | 🟢 Normal | -0.009 |  |
| 2026-05-31 13:06:05 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.009 |  |
| 2026-05-31 13:04:33 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-05-31 13:02:40 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-05-31 13:02:57 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-05-31 13:09:56 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | -0.010 |  |
| 2026-05-31 13:02:25 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-31 13:08:51 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-05-31 13:06:16 | Peradeniya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.019 |  |
| 2026-05-31 13:03:03 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-05-31 13:03:46 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | -0.020 |  |
| 2026-05-31 13:03:15 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-05-31 13:00:09 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.021 |  |
| 2026-05-31 13:03:42 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | -0.022 |  |
| 2026-05-31 13:07:44 | Rathnapura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.038 |  |
| 2026-05-31 13:01:42 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.040 |  |
| 2026-05-31 12:03:05 | Putupaula (Kalu Ganga) | 1.68 | 🟢 Normal | -0.043 |  |
| 2026-05-31 13:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.88 | 🟢 Normal | -0.199 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)