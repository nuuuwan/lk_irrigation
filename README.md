# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--09_09:05:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **93,304 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 09:05:45 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.010 |  |
| 2026-03-09 09:05:43 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-03-09 09:05:11 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-03-09 09:04:57 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-03-09 09:04:47 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-09 09:04:43 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 09:04:24 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.071 |  |
| 2026-03-09 09:03:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.058 |  |
| 2026-03-09 09:03:52 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.021 |  |
| 2026-03-09 09:03:43 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-09 09:03:41 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | -0.070 |  |
| 2026-03-09 09:03:37 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-03-09 09:03:35 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 09:03:22 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 09:03:15 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-09 09:03:15 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-09 09:03:11 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.272 |  |
| 2026-03-09 09:03:10 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-09 09:03:08 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 09:02:42 | Thanthirimale (Malwathu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-09 09:02:35 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-09 09:02:33 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-09 09:02:26 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-09 09:02:24 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 09:02:21 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.021 |  |
| 2026-03-09 09:02:17 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-09 09:02:06 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-09 09:01:55 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.096 |  |
| 2026-03-09 09:01:44 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 09:01:40 | Weraganthota (Mahaweli Ganga) | -2.69 | 🟢 Normal | -0.051 |  |
| 2026-03-09 09:01:28 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-03-09 09:00:39 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-09 08:18:36 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | -0.012 |  |
| 2026-03-09 08:15:07 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 09:05:11 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-03-09 09:03:15 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-09 09:03:10 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-09 09:03:35 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 09:01:44 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 09:02:24 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 09:00:39 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-09 09:03:22 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 09:03:43 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-09 08:04:37 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 09:03:15 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-09 09:03:08 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 08:00:41 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 09:02:33 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-09 09:02:17 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-09 09:02:26 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-09 09:02:35 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-09 09:02:06 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-09 09:04:43 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 09:02:42 | Thanthirimale (Malwathu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-09 08:15:07 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-09 09:05:43 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-03-09 09:05:45 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.010 |  |
| 2026-03-09 09:03:37 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-03-09 09:04:47 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-09 09:04:57 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-03-09 09:01:28 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-03-09 08:02:39 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-03-09 08:18:36 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | -0.012 |  |
| 2026-03-09 09:02:21 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.021 |  |
| 2026-03-09 09:03:52 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.021 |  |
| 2026-03-09 08:07:46 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.034 |  |
| 2026-03-09 09:01:40 | Weraganthota (Mahaweli Ganga) | -2.69 | 🟢 Normal | -0.051 |  |
| 2026-03-09 09:03:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.058 |  |
| 2026-03-09 09:03:41 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | -0.070 |  |
| 2026-03-09 09:04:24 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.071 |  |
| 2026-03-09 08:05:49 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.093 |  |
| 2026-03-09 09:01:55 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.096 |  |
| 2026-03-09 09:03:11 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.272 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)