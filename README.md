# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_07:13:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **111,234 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 07:13:09 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:12:37 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:11:34 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:09:55 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:09:44 | Nagalagam Street (Kelani Ganga) | 0.32 | 🟢 Normal | -0.014 |  |
| 2026-03-30 07:08:00 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.063 |  |
| 2026-03-30 07:07:56 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-03-30 07:06:31 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:06:24 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-30 07:06:15 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-30 07:06:08 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.118 |  |
| 2026-03-30 07:05:03 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:04:56 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:04:39 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-30 07:04:37 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:04:35 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-03-30 07:04:27 | Ellagawa (Kalu Ganga) | 3.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-30 07:04:23 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.034 |  |
| 2026-03-30 07:04:22 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 07:04:13 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 07:03:59 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-30 07:03:46 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-03-30 07:03:27 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 07:03:12 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:02:59 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-30 07:02:46 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-03-30 07:02:35 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.112 |  |
| 2026-03-30 07:02:24 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:02:08 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:02:04 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:01:28 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.157 |  |
| 2026-03-30 07:01:22 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:01:07 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:00:52 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:00:31 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-30 07:00:23 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:00:11 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-03-30 06:31:27 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-30 06:22:55 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 07:00:11 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-03-30 07:04:35 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-03-30 07:06:24 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-30 07:02:59 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-30 07:03:59 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-30 07:04:39 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-30 07:06:15 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-30 07:00:31 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-30 07:04:27 | Ellagawa (Kalu Ganga) | 3.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-30 07:04:22 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 07:03:27 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 07:04:13 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 07:02:35 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:06:31 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:09:55 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:02:04 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:02:08 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:00:52 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:01:22 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:11:34 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:12:37 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:03:12 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:05:03 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:04:37 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:04:56 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:01:07 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:13:09 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:00:23 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:02:24 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-30 07:07:56 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-03-30 07:03:46 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-03-30 07:02:46 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-03-30 07:09:44 | Nagalagam Street (Kelani Ganga) | 0.32 | 🟢 Normal | -0.014 |  |
| 2026-03-30 06:02:53 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.026 |  |
| 2026-03-30 07:04:23 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.034 |  |
| 2026-03-30 07:08:00 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.063 |  |
| 2026-03-30 07:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.112 |  |
| 2026-03-30 07:06:08 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.118 |  |
| 2026-03-30 07:01:28 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.157 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)