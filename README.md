# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--25_10:30:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **106,863 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-25 10:30:57 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:19:45 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.059 |  |
| 2026-03-25 10:18:35 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-25 10:14:16 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-25 10:11:00 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.018 |  |
| 2026-03-25 10:08:23 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.127 |  |
| 2026-03-25 10:07:59 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:06:39 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:06:18 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:06:02 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:05:58 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -3.000 |  |
| 2026-03-25 10:05:33 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:05:22 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -3.000 |  |
| 2026-03-25 10:05:19 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:04:25 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-25 10:04:17 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:04:12 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-03-25 10:04:08 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.066 |  |
| 2026-03-25 10:03:59 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-25 10:03:29 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:03:02 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-03-25 10:02:20 | Weraganthota (Mahaweli Ganga) | 1.87 | 🟢 Normal | 3.646 | 🔺 Rising |
| 2026-03-25 10:02:20 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:02:20 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:02:18 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:01:57 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:01:55 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.229 |  |
| 2026-03-25 10:01:49 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-03-25 10:01:49 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:01:41 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:01:35 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | -0.032 |  |
| 2026-03-25 10:01:27 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:01:07 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:00:47 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-03-25 10:00:46 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:00:41 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:00:25 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:00:15 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:00:13 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-25 10:02:20 | Weraganthota (Mahaweli Ganga) | 1.87 | 🟢 Normal | 3.646 | 🔺 Rising |
| 2026-03-25 10:04:12 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-03-25 10:04:25 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-25 10:03:59 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-25 10:14:16 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-25 10:18:35 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-25 10:02:20 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:00:13 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:01:57 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:01:41 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:00:46 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:30:57 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:06:39 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:06:02 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:01:27 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:03:29 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:01:07 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:00:25 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:00:15 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:05:33 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:05:19 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:02:18 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:06:18 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:04:17 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:00:41 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:07:59 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:02:20 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:01:49 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-25 10:03:02 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-03-25 10:01:49 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-03-25 10:11:00 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.018 |  |
| 2026-03-25 10:00:47 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-03-25 09:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.030 |  |
| 2026-03-25 10:01:35 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | -0.032 |  |
| 2026-03-25 10:19:45 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.059 |  |
| 2026-03-25 10:04:08 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.066 |  |
| 2026-03-25 10:08:23 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.127 |  |
| 2026-03-25 10:01:55 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.229 |  |
| 2026-03-25 10:05:58 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -3.000 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)