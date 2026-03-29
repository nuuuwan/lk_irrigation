# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_09:12:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **110,422 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-29 09:12:38 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.018 |  |
| 2026-03-29 09:09:23 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-29 09:08:57 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:08:46 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:08:42 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:08:33 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:08:30 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-29 09:08:09 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.029 |  |
| 2026-03-29 09:06:23 | Magura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:05:38 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:05:34 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:05:13 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:05:00 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:04:55 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 09:04:17 | Ellagawa (Kalu Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:04:10 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:03:58 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:03:36 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-03-29 09:03:28 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.063 |  |
| 2026-03-29 09:03:06 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-03-29 09:03:02 | Hanwella (Kelani Ganga) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 09:03:01 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:02:54 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-29 09:02:46 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:02:27 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:02:17 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.101 |  |
| 2026-03-29 09:02:16 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:02:00 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.348 |  |
| 2026-03-29 09:01:51 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 09:01:28 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:01:20 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.037 |  |
| 2026-03-29 09:01:16 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:01:09 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:01:07 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:00:55 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.061 |  |
| 2026-03-29 09:00:44 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | -0.030 |  |
| 2026-03-29 09:00:14 | Nawalapitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-29 08:23:20 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.052 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-29 09:03:36 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-03-29 09:09:23 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-29 09:08:30 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-29 09:01:51 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 09:03:02 | Hanwella (Kelani Ganga) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 09:04:55 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 09:01:07 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:08:46 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:03:28 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:02:27 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:03:58 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:06:23 | Magura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:03:01 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:04:17 | Ellagawa (Kalu Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:08:42 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:01:09 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:01:16 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:04:10 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:08:57 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:02:46 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:05:00 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:05:38 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:05:13 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:00:36 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:02:16 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:05:34 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:01:28 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:08:33 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-29 09:03:06 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-03-29 09:02:54 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-29 09:00:14 | Nawalapitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-29 09:12:38 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.018 |  |
| 2026-03-29 09:08:09 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.029 |  |
| 2026-03-29 09:00:44 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | -0.030 |  |
| 2026-03-29 09:01:20 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.037 |  |
| 2026-03-29 09:00:55 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.061 |  |
| 2026-03-29 09:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.063 |  |
| 2026-03-29 09:02:17 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.101 |  |
| 2026-03-29 09:02:00 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.348 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)