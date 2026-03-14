# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--14_15:09:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,227 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 15:09:39 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.027 |  |
| 2026-03-14 15:09:31 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:08:55 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:06:56 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 15:05:17 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:05:08 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-03-14 15:05:02 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:04:45 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-03-14 15:04:37 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-14 15:04:25 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-14 15:04:16 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-03-14 15:04:03 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:03:59 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.029 |  |
| 2026-03-14 15:03:52 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-03-14 15:03:41 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.039 |  |
| 2026-03-14 15:03:35 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.069 |  |
| 2026-03-14 15:03:33 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.030 |  |
| 2026-03-14 15:03:06 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-14 15:02:45 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:02:44 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:02:37 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-14 15:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:02:26 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:02:26 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.027 |  |
| 2026-03-14 15:02:22 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.043 |  |
| 2026-03-14 15:02:17 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 15:02:05 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 15:02:05 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-14 15:01:54 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:01:40 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-03-14 15:01:34 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-03-14 15:01:28 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-14 15:01:26 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-14 15:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:01:05 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.021 |  |
| 2026-03-14 15:01:01 | Weraganthota (Mahaweli Ganga) | -2.62 | 🟢 Normal | -0.040 |  |
| 2026-03-14 15:00:13 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 15:05:08 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-03-14 15:01:34 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-03-14 15:03:52 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-03-14 15:01:26 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-14 15:03:06 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-14 15:02:05 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-14 14:07:11 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-14 15:01:28 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-14 15:04:25 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-14 15:02:05 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 15:02:17 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 15:06:56 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 15:04:37 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-14 15:05:17 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:00:13 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:01:54 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:05:02 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:04:03 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:02:45 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:02:44 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:09:31 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:08:55 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:02:26 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:02:37 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-14 15:01:40 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-03-14 15:04:16 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-03-14 15:01:05 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.021 |  |
| 2026-03-14 15:04:45 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-03-14 15:02:26 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.027 |  |
| 2026-03-14 15:09:39 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.027 |  |
| 2026-03-14 14:06:49 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.029 |  |
| 2026-03-14 15:03:59 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.029 |  |
| 2026-03-14 15:03:33 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.030 |  |
| 2026-03-14 15:03:41 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.039 |  |
| 2026-03-14 15:01:01 | Weraganthota (Mahaweli Ganga) | -2.62 | 🟢 Normal | -0.040 |  |
| 2026-03-14 15:02:22 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.043 |  |
| 2026-03-14 15:03:35 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)