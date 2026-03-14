# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--14_11:21:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,072 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 11:21:47 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-14 11:15:16 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.008 |  |
| 2026-03-14 11:09:14 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.021 |  |
| 2026-03-14 11:09:00 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-14 11:07:41 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 11:07:24 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-03-14 11:07:08 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 11:06:46 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 11:06:22 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-14 11:06:11 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-14 11:05:35 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.026 |  |
| 2026-03-14 11:05:31 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.021 |  |
| 2026-03-14 11:05:14 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-14 11:05:03 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-14 11:04:34 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 11:07:24 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-03-14 11:01:13 | Weraganthota (Mahaweli Ganga) | -2.27 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-03-14 11:00:39 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-14 11:02:21 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-14 11:02:19 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-14 11:02:28 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-14 11:03:43 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-14 11:01:36 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-14 11:01:46 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-14 11:01:10 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 11:05:14 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-14 11:03:37 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 11:00:16 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 11:01:09 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-14 11:04:34 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-14 11:00:15 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 11:07:08 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 11:21:47 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-14 11:03:52 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-03-14 11:06:46 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:14:28 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-03-14 11:03:18 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-14 11:04:20 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | 0.000 |  |
| 2026-03-14 11:06:11 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-14 11:07:41 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 11:01:39 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-14 11:02:56 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 11:05:03 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-14 11:09:00 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-14 11:01:58 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-14 11:15:16 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.008 |  |
| 2026-03-14 11:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-03-14 11:06:22 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-14 11:05:31 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.021 |  |
| 2026-03-14 11:09:14 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.021 |  |
| 2026-03-14 11:01:08 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.022 |  |
| 2026-03-14 11:05:35 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.026 |  |
| 2026-03-14 11:03:26 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.040 |  |
| 2026-03-14 11:01:56 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.064 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)