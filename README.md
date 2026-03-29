# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_06:19:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **110,305 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-29 06:19:42 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:11:23 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-03-29 06:08:06 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:07:36 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 06:06:56 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-29 06:06:27 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.036 |  |
| 2026-03-29 06:05:47 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:05:40 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-29 06:05:38 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-29 06:04:52 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:04:40 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-03-29 06:04:21 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-29 06:04:20 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:04:14 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:03:53 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-29 06:03:16 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:03:16 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-03-29 06:03:09 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:03:06 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:03:05 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:02:49 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-03-29 06:02:41 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-29 06:02:22 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:02:18 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:02:13 | Hanwella (Kelani Ganga) | 0.19 | 🟢 Normal | -0.020 |  |
| 2026-03-29 06:02:02 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.180 |  |
| 2026-03-29 06:01:57 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:01:42 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:01:33 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:01:31 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.025 |  |
| 2026-03-29 06:01:25 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:01:18 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.905 |  |
| 2026-03-29 06:01:03 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:00:46 | Magura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:00:28 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:00:18 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-29 06:00:10 | Ellagawa (Kalu Ganga) | 3.64 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:00:09 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.023 |  |
| 2026-03-29 05:58:43 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-29 05:54:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.905 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-29 06:05:40 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-29 06:00:18 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-29 06:02:49 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-03-29 06:04:21 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-29 06:02:41 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-29 06:11:23 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-03-29 06:06:56 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-29 06:03:53 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-29 06:07:36 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 06:08:06 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:03:06 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:02:18 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:02:22 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:04:20 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:03:16 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:19:42 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-28 18:03:02 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:00:46 | Magura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:04:14 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:00:10 | Ellagawa (Kalu Ganga) | 3.64 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:00:28 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:01:25 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:01:42 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:03:09 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:01:57 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:05:47 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:01:18 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-28 18:04:13 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:04:52 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:01:33 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:03:05 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:04:40 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-03-29 06:03:16 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-03-29 06:02:13 | Hanwella (Kelani Ganga) | 0.19 | 🟢 Normal | -0.020 |  |
| 2026-03-29 06:00:09 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.023 |  |
| 2026-03-29 06:01:31 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.025 |  |
| 2026-03-29 06:06:27 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.036 |  |
| 2026-03-29 06:02:02 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.180 |  |
| 2026-03-29 06:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.905 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)