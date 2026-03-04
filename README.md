# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--04_14:12:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **89,008 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-04 14:12:41 | Rathnapura (Kalu Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:11:43 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-03-04 14:11:24 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:09:53 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:08:04 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-03-04 14:07:48 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:07:43 | Thawalama (Gin Ganga) | 0.88 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-04 14:06:37 | Horowpothana (Yan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:06:23 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:06:05 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-03-04 14:05:51 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:05:30 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:05:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-04 14:04:48 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:04:32 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:04:07 | Panadugama (Nilwala Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-03-04 14:03:44 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-03-04 14:03:35 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.014 |  |
| 2026-03-04 14:03:34 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:03:32 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-03-04 14:03:24 | Peradeniya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:03:23 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-03-04 14:03:18 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:03:16 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | -0.052 |  |
| 2026-03-04 14:02:46 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:02:46 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-03-04 14:02:17 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:02:13 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-03-04 14:02:10 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:02:09 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-03-04 14:02:05 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-03-04 14:01:56 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:01:45 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 14:01:40 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:01:30 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:01:18 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:01:16 | Weraganthota (Mahaweli Ganga) | -1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:01:14 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-03-04 14:00:53 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:00:36 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 13:20:26 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-04 14:02:13 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-03-04 14:01:14 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-03-04 14:02:05 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-03-04 14:07:43 | Thawalama (Gin Ganga) | 0.88 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-04 14:05:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-04 14:01:45 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 14:00:36 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 14:01:16 | Weraganthota (Mahaweli Ganga) | -1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:03:34 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:01:56 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:01:18 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:06:37 | Horowpothana (Yan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:04:32 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:11:24 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:09:53 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:02:10 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:07:48 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:03:18 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:01:30 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:01:40 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:06:23 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:02:46 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:02:17 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:05:51 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:04:48 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:00:53 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:12:41 | Rathnapura (Kalu Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:03:24 | Peradeniya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-04 14:11:43 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-03-04 14:08:04 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-03-04 14:04:07 | Panadugama (Nilwala Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-03-04 14:02:46 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-03-04 14:03:32 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-03-04 14:02:09 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-03-04 14:03:23 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-03-04 14:03:44 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-03-04 14:06:05 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-03-04 14:03:35 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.014 |  |
| 2026-03-04 14:03:16 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | -0.052 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)