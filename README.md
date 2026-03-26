# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--26_12:11:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **107,843 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-26 12:11:41 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:09:16 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:08:17 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:07:25 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:07:05 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:06:58 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.019 |  |
| 2026-03-26 12:06:05 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:05:58 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:05:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.012 |  |
| 2026-03-26 12:05:10 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:05:03 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.049 |  |
| 2026-03-26 12:04:52 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:04:51 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:04:30 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:04:12 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:03:49 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-26 12:03:28 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:03:22 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | -0.010 |  |
| 2026-03-26 12:02:56 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-03-26 12:02:55 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-03-26 12:02:46 | Rathnapura (Kalu Ganga) | 0.37 | 🟢 Normal | -0.012 |  |
| 2026-03-26 12:02:40 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:02:37 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-03-26 12:02:36 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:02:29 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-03-26 12:02:24 | Weraganthota (Mahaweli Ganga) | -2.18 | 🟢 Normal | -0.099 |  |
| 2026-03-26 12:02:17 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | -0.079 |  |
| 2026-03-26 12:02:13 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:02:12 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:02:12 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:02:09 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.131 |  |
| 2026-03-26 12:02:07 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.106 |  |
| 2026-03-26 12:02:04 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-26 12:01:37 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.022 |  |
| 2026-03-26 12:01:32 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.039 |  |
| 2026-03-26 12:01:21 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-03-26 12:00:08 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-26 12:02:04 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-26 12:03:49 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-26 12:07:25 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:02:12 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:00:08 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:01:21 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:02:40 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-26 11:28:37 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-26 11:02:50 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:05:58 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:11:41 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:04:30 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:07:05 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:02:36 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:04:52 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:04:12 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:05:10 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:02:13 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:03:28 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:06:05 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:08:17 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-26 11:06:04 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:02:12 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:02:55 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-03-26 12:02:37 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-03-26 12:02:56 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-03-26 12:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-03-26 12:03:22 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | -0.010 |  |
| 2026-03-26 12:02:46 | Rathnapura (Kalu Ganga) | 0.37 | 🟢 Normal | -0.012 |  |
| 2026-03-26 12:05:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.012 |  |
| 2026-03-26 12:06:58 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.019 |  |
| 2026-03-26 12:01:37 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.022 |  |
| 2026-03-26 12:02:29 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-03-26 12:01:32 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.039 |  |
| 2026-03-26 12:05:03 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.049 |  |
| 2026-03-26 12:02:17 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | -0.079 |  |
| 2026-03-26 12:02:24 | Weraganthota (Mahaweli Ganga) | -2.18 | 🟢 Normal | -0.099 |  |
| 2026-03-26 12:02:07 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.106 |  |
| 2026-03-26 12:02:09 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)