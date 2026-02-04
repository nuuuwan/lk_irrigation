# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--04_18:16:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **64,185 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-04 18:16:06 | Dunamale (Aththanagalu Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:13:21 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:10:51 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.026 |  |
| 2026-02-04 18:10:37 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-02-04 18:10:03 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:08:19 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:08:19 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:07:47 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:07:31 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:06:42 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.029 |  |
| 2026-02-04 18:06:30 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:04:55 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-04 18:04:39 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:04:19 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:04:19 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:04:11 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-04 18:03:44 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-02-04 18:03:35 | Weraganthota (Mahaweli Ganga) | -2.61 | 🟢 Normal | -0.061 |  |
| 2026-02-04 18:03:21 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.097 |  |
| 2026-02-04 18:03:02 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-02-04 18:02:49 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:02:35 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-04 18:02:28 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:02:24 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:02:19 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-04 18:01:55 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:01:55 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:01:36 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:00:35 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:00:15 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-04 18:03:02 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-02-04 17:03:35 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-04 18:04:11 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-04 18:02:19 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-04 18:04:55 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-04 18:02:35 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-04 18:06:30 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:00:15 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:08:19 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:00:35 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:10:03 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:01:55 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:13:21 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:04:19 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-04 17:04:44 | Baddegama (Gin Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:04:39 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:01:36 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:16:06 | Dunamale (Aththanagalu Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:07:31 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:02:28 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:08:19 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:07:47 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:04:19 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:02:24 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:02:49 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:13:11⌛ | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-04 18:10:37 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-02-04 18:03:44 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-02-02 18:03:26⌛ | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-04 18:10:51 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.026 |  |
| 2026-02-04 18:06:42 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.029 |  |
| 2026-02-04 18:03:35 | Weraganthota (Mahaweli Ganga) | -2.61 | 🟢 Normal | -0.061 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-04 18:03:21 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.097 |  |
| 2026-02-03 22:06:20 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)