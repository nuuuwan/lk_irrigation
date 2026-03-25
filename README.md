# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--25_19:18:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **107,210 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-25 19:18:29 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:14:09 | Moragaswewa (Deduru Oya) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:13:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | -0.008 |  |
| 2026-03-25 19:10:04 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:08:26 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-03-25 19:07:35 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:07:18 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.072 |  |
| 2026-03-25 19:06:46 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-03-25 19:06:13 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-25 19:04:47 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:04:36 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:04:35 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 19:04:21 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:03:35 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:03:15 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:03:13 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.010 |  |
| 2026-03-25 19:03:08 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:02:57 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:02:28 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:02:22 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:02:19 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:02:18 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-03-25 19:02:06 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.011 |  |
| 2026-03-25 19:02:05 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:02:00 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:01:55 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:01:43 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:01:43 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:01:29 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:01:28 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.051 |  |
| 2026-03-25 19:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:01:15 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:01:13 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-25 19:01:13 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:00:57 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-25 19:01:13 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-25 19:08:26 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-03-25 19:04:35 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 19:06:13 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-25 19:02:00 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:01:43 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:14:09 | Moragaswewa (Deduru Oya) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:01:43 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:02:57 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-25 18:00:33 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-25 18:00:29 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:10:04 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:04:47 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:00:57 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:04:21 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:03:15 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:01:55 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:03:35 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:01:29 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:01:13 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:02:28 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:02:22 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:02:19 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:04:36 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-25 18:02:01 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:07:35 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:18:29 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:01:15 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:02:05 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:03:08 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-25 19:13:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | -0.008 |  |
| 2026-03-25 19:06:46 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-03-25 19:02:18 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-03-25 19:03:13 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.010 |  |
| 2026-03-25 19:02:06 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.011 |  |
| 2026-03-25 19:01:28 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.051 |  |
| 2026-03-25 18:01:39 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.060 |  |
| 2026-03-25 19:07:18 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.072 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)