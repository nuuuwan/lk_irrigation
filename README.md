# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--03_19:14:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **88,319 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-03 19:14:03 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.018 |  |
| 2026-03-03 19:13:06 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:12:14 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-03-03 19:10:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.026 |  |
| 2026-03-03 19:08:01 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:07:53 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | -0.037 |  |
| 2026-03-03 19:07:43 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:07:36 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:07:08 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:06:50 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.101 |  |
| 2026-03-03 19:06:33 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:05:37 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:05:35 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:04:54 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:04:52 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-03 19:04:37 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.005 |  |
| 2026-03-03 19:04:26 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:04:04 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.050 |  |
| 2026-03-03 19:03:43 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-03 19:03:28 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.059 |  |
| 2026-03-03 19:03:27 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-03-03 19:02:41 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:02:32 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | -0.030 |  |
| 2026-03-03 19:02:26 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:02:24 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -108.000 |  |
| 2026-03-03 19:02:10 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:01:59 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -108.000 |  |
| 2026-03-03 19:01:52 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:01:35 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:01:31 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-03-03 19:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:01:20 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:01:19 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:01:00 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:00:55 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-03 19:00:43 | Horowpothana (Yan Oya) | 1.10 | 🟢 Normal | -0.012 |  |
| 2026-03-03 19:00:08 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:59:51 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-03 19:03:27 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-03-03 19:12:14 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-03-03 19:00:55 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-03 19:03:43 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-03 19:04:52 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-03 18:08:32 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-03 19:01:52 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:01:00 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:01:19 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:04:26 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:02:31 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:07:43 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:08:01 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:02:41 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:13:06 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:07:08 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:06:33 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:00:08 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:01:20 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:02:10 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:02:26 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:05:35 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:07:36 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:00:53 | Thanthirimale (Malwathu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:04:59 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:05:37 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:01:35 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:04:54 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-03 19:04:37 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.005 |  |
| 2026-03-03 19:00:43 | Horowpothana (Yan Oya) | 1.10 | 🟢 Normal | -0.012 |  |
| 2026-03-03 19:14:03 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.018 |  |
| 2026-03-03 19:10:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.026 |  |
| 2026-03-03 19:02:32 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | -0.030 |  |
| 2026-03-03 19:07:53 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | -0.037 |  |
| 2026-03-03 19:04:04 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.050 |  |
| 2026-03-03 19:03:28 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.059 |  |
| 2026-03-03 19:06:50 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.101 |  |
| 2026-03-03 19:02:24 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)