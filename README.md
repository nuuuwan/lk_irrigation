# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--15_12:15:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **98,000 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 12:15:37 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-03-15 12:08:20 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-15 12:08:19 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-03-15 12:07:52 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-03-15 12:06:49 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:06:22 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.303 |  |
| 2026-03-15 12:06:13 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:05:57 | Thanamalwila (Kirindi Oya) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-03-15 12:05:57 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:05:52 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-03-15 12:05:48 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:05:13 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:05:13 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:05:01 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-15 12:04:37 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-03-15 12:04:26 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:04:25 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.019 |  |
| 2026-03-15 12:03:53 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | -0.020 |  |
| 2026-03-15 12:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-15 12:03:33 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:02:57 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.060 |  |
| 2026-03-15 12:02:54 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-03-15 12:02:49 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.030 |  |
| 2026-03-15 12:02:41 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:02:23 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | -0.021 |  |
| 2026-03-15 12:02:22 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.058 |  |
| 2026-03-15 12:02:10 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-03-15 12:02:04 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 12:01:54 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-03-15 12:01:45 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:01:43 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:01:41 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:01:29 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 12:01:21 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:01:18 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | -0.010 |  |
| 2026-03-15 12:01:01 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.548 |  |
| 2026-03-15 12:00:54 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.011 |  |
| 2026-03-15 12:00:14 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 12:08:19 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-03-15 12:02:10 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-03-15 12:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-15 12:05:01 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-15 12:02:54 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-03-15 12:15:37 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-03-15 12:07:52 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-03-15 12:08:20 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-15 12:01:29 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 12:02:04 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 12:03:33 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:05:57 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:02:41 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:01:43 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:01:04 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:05:13 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:06:49 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:01:45 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:04:26 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:05:48 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:06:13 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:01:41 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:05:13 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:01:21 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:05:52 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-03-15 12:01:54 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-03-15 12:00:14 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-03-15 12:01:18 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | -0.010 |  |
| 2026-03-15 12:00:54 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.011 |  |
| 2026-03-15 12:04:25 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.019 |  |
| 2026-03-15 12:03:53 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | -0.020 |  |
| 2026-03-15 12:05:57 | Thanamalwila (Kirindi Oya) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-03-15 12:02:23 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | -0.021 |  |
| 2026-03-15 12:04:37 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-03-15 12:02:49 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.030 |  |
| 2026-03-15 12:02:22 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.058 |  |
| 2026-03-15 12:02:57 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.060 |  |
| 2026-03-15 12:06:22 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.303 |  |
| 2026-03-15 12:01:01 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.548 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)