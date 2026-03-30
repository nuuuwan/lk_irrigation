# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_19:34:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **111,706 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 19:34:28 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.020 |  |
| 2026-03-30 19:24:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.19 | 🟢 Normal | -0.015 |  |
| 2026-03-30 19:22:49 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-30 19:22:13 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-30 19:16:15 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.012 |  |
| 2026-03-30 19:15:28 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-30 19:14:02 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-30 19:09:46 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-03-30 19:06:24 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.046 |  |
| 2026-03-30 19:06:00 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-03-30 19:05:43 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.030 |  |
| 2026-03-30 19:05:31 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-03-30 19:05:28 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 19:02:16 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.343 | 🔺 Rising |
| 2026-03-30 19:06:00 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-03-30 19:00:53 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-03-30 19:09:46 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-03-30 19:01:36 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-30 19:14:02 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-30 19:02:34 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 19:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 19:04:29 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 18:07:18 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-30 19:02:53 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 19:00:43 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-30 19:15:28 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-30 19:00:58 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-30 19:02:45 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-30 19:05:31 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-03-30 19:03:48 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-30 19:04:03 | Dunamale (Aththanagalu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-30 19:04:40 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-30 19:02:15 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-30 19:02:05 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:00:31 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-30 19:22:49 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-30 19:01:23 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-30 19:02:29 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 19:03:41 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-30 19:02:48 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-03-30 19:02:27 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.011 |  |
| 2026-03-30 19:04:35 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-03-30 19:16:15 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.012 |  |
| 2026-03-30 19:01:42 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.013 |  |
| 2026-03-30 19:01:57 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | -0.013 |  |
| 2026-03-30 19:24:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.19 | 🟢 Normal | -0.015 |  |
| 2026-03-30 19:03:54 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-03-30 19:34:28 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.020 |  |
| 2026-03-30 19:05:43 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.030 |  |
| 2026-03-30 19:05:28 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-03-30 19:06:24 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.046 |  |
| 2026-03-30 18:03:12 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)