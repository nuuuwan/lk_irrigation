# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--08_18:31:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **92,762 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 18:31:40 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:31:39 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:18:26 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | -0.008 |  |
| 2026-03-08 18:18:12 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-08 18:15:28 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:11:18 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:11:14 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:08:20 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:08:11 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.026 |  |
| 2026-03-08 18:06:32 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.058 |  |
| 2026-03-08 18:06:04 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:05:47 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:05:23 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:05:12 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-03-08 18:05:09 | Peradeniya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:04:52 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 18:04:24 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:04:20 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-03-08 18:04:08 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:04:08 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:03:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | -0.029 |  |
| 2026-03-08 18:03:41 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-03-08 18:03:18 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:03:05 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:02:45 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 18:02:42 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-03-08 18:02:40 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | -0.021 |  |
| 2026-03-08 18:02:31 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:02:25 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-03-08 18:02:24 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:02:15 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | -0.019 |  |
| 2026-03-08 18:02:13 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 18:02:02 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:01:37 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:01:36 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:01:17 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:01:15 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:01:09 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-03-08 18:00:41 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:00:30 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.085 |  |
| 2026-03-08 18:00:18 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-03-08 18:00:14 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 18:05:12 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-03-08 18:18:12 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-08 18:00:14 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 18:02:13 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 18:02:45 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 18:04:52 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 18:02:31 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:02:02 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:00:41 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:15:28 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:08:20 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:31:40 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:04:08 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:03:05 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:05:23 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:02:24 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:01:36 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:04:24 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:01:17 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:04:08 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:06:04 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:03:18 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:01:37 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:05:09 | Peradeniya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:05:47 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:01:15 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:18:26 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | -0.008 |  |
| 2026-03-08 18:02:25 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-03-08 18:03:41 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-03-08 18:01:09 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-03-08 18:04:20 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-03-08 18:02:15 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | -0.019 |  |
| 2026-03-08 18:02:40 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | -0.021 |  |
| 2026-03-08 18:00:18 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-03-08 18:08:11 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.026 |  |
| 2026-03-08 18:03:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | -0.029 |  |
| 2026-03-08 18:02:42 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-03-08 18:06:32 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.058 |  |
| 2026-03-08 18:00:30 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)