# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--20_18:13:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **102,713 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 18:13:14 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-20 18:12:39 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-20 18:06:18 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.039 |  |
| 2026-03-20 18:05:30 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.021 |  |
| 2026-03-20 18:05:03 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.011 |  |
| 2026-03-20 18:04:36 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.114 |  |
| 2026-03-20 18:04:27 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.029 |  |
| 2026-03-20 18:04:17 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:04:16 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:04:07 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 18:03:52 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:03:50 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.055 |  |
| 2026-03-20 18:03:47 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | -0.019 |  |
| 2026-03-20 18:03:46 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:02:58 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:02:53 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.046 |  |
| 2026-03-20 18:02:51 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-20 18:02:49 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-03-20 18:02:46 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.030 |  |
| 2026-03-20 18:02:22 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:02:14 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-03-20 18:02:14 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:02:09 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-03-20 18:02:07 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.241 | 🔺 Rising |
| 2026-03-20 18:01:47 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:01:42 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.011 |  |
| 2026-03-20 18:01:37 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 18:01:29 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-20 18:01:28 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.022 |  |
| 2026-03-20 18:01:16 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.091 |  |
| 2026-03-20 18:01:15 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.034 |  |
| 2026-03-20 18:01:12 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.100 |  |
| 2026-03-20 18:01:10 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-03-20 18:00:45 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:00:44 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-03-20 18:00:22 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:00:18 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:00:15 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-20 18:00:12 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.053 |  |
| 2026-03-20 17:26:36 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-20 17:26:23 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.034 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 18:02:07 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.241 | 🔺 Rising |
| 2026-03-20 18:13:14 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-20 18:00:15 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-20 18:02:51 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-20 18:01:29 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-20 18:12:39 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-20 18:01:37 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 18:04:07 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 18:02:22 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:01:47 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:02:14 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:02:58 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:00:45 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:03:46 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:03:52 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:00:22 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:02:46 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:04:16 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:04:17 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:02:14 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-03-20 18:02:49 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-03-20 18:02:09 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-03-20 18:01:42 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.011 |  |
| 2026-03-20 18:05:03 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.011 |  |
| 2026-03-20 18:01:10 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-03-20 18:00:44 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-03-20 18:03:47 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | -0.019 |  |
| 2026-03-20 18:05:30 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.021 |  |
| 2026-03-20 18:01:28 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.022 |  |
| 2026-03-20 18:04:27 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.029 |  |
| 2026-03-20 18:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.030 |  |
| 2026-03-20 18:01:15 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.034 |  |
| 2026-03-20 18:06:18 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.039 |  |
| 2026-03-20 18:02:53 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.046 |  |
| 2026-03-20 18:00:12 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.053 |  |
| 2026-03-20 18:03:50 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.055 |  |
| 2026-03-20 18:01:16 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.091 |  |
| 2026-03-20 18:01:12 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.100 |  |
| 2026-03-20 18:04:36 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.114 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)