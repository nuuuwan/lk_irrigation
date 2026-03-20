# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--20_11:10:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **102,436 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 11:10:52 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.009 |  |
| 2026-03-20 11:08:28 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-20 11:08:08 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:08:05 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.019 |  |
| 2026-03-20 11:07:15 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-03-20 11:06:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-03-20 11:05:43 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:04:29 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.022 |  |
| 2026-03-20 11:04:16 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-03-20 11:04:11 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:03:59 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:03:56 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.075 |  |
| 2026-03-20 11:03:50 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-03-20 11:03:27 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-03-20 11:03:23 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -2.769 |  |
| 2026-03-20 11:03:22 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:03:10 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:03:09 | Weraganthota (Mahaweli Ganga) | -2.09 | 🟢 Normal | -0.115 |  |
| 2026-03-20 11:03:00 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-03-20 11:02:54 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-03-20 11:02:44 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -2.769 |  |
| 2026-03-20 11:02:33 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.023 |  |
| 2026-03-20 11:02:24 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-03-20 11:02:22 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.037 |  |
| 2026-03-20 11:02:17 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.051 |  |
| 2026-03-20 11:02:09 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:02:07 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.041 |  |
| 2026-03-20 11:02:04 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:02:00 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-03-20 11:01:57 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:01:50 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:01:35 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:01:33 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-03-20 11:01:21 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | -0.031 |  |
| 2026-03-20 11:01:20 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.040 |  |
| 2026-03-20 11:01:18 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-20 11:00:46 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:00:36 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:00:24 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 10:57:29 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 11:01:33 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-03-20 11:07:15 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-03-20 11:02:54 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-03-20 11:06:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-03-20 11:01:18 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-20 11:08:28 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-20 11:00:36 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:02:09 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:01:57 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:04:11 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:02:04 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:08:08 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:01:35 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:05:43 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:00:24 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:03:10 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:03:59 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:03:22 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:00:46 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:01:50 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 11:10:52 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.009 |  |
| 2026-03-20 11:02:24 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-03-20 11:03:50 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-03-20 11:03:27 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-03-20 11:03:00 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-03-20 11:02:00 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-03-20 10:57:29 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-03-20 11:08:05 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.019 |  |
| 2026-03-20 11:04:16 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-03-20 11:04:29 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.022 |  |
| 2026-03-20 11:02:33 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.023 |  |
| 2026-03-20 11:01:21 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | -0.031 |  |
| 2026-03-20 11:02:22 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.037 |  |
| 2026-03-20 11:01:20 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.040 |  |
| 2026-03-20 11:02:07 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.041 |  |
| 2026-03-20 11:02:17 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.051 |  |
| 2026-03-20 11:03:56 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.075 |  |
| 2026-03-20 11:03:09 | Weraganthota (Mahaweli Ganga) | -2.09 | 🟢 Normal | -0.115 |  |
| 2026-03-20 11:03:23 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -2.769 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)