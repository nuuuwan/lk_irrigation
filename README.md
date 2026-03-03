# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--03_18:09:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **88,280 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-03 18:09:31 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:08:58 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:08:32 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-03 18:08:00 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:07:43 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:07:25 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:06:45 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:05:33 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:05:21 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:05:17 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:04:59 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:04:58 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:04:35 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:04:13 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-03 18:04:03 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.021 |  |
| 2026-03-03 18:03:56 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-03-03 18:03:10 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.030 |  |
| 2026-03-03 18:03:02 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-03-03 18:02:59 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | -0.058 |  |
| 2026-03-03 18:02:41 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:02:33 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:02:32 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:02:31 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:02:16 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:02:14 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-03 18:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.021 |  |
| 2026-03-03 18:02:06 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:01:58 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.159 |  |
| 2026-03-03 18:01:48 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:01:30 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.137 |  |
| 2026-03-03 18:01:27 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:01:26 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-03 18:01:24 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:00:53 | Thanthirimale (Malwathu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:00:43 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.013 |  |
| 2026-03-03 18:00:27 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:00:16 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-03 18:02:14 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-03 18:01:26 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-03 18:04:13 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-03 18:08:32 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-03 18:00:27 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:00:16 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:02:16 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:02:06 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:08:58 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:02:31 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 17:05:19 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:05:21 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:05:17 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:01:27 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:04:58 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:05:33 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:02:41 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:01:48 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:04:35 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:08:00 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 17:04:26 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:06:45 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:07:25 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:02:32 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:00:53 | Thanthirimale (Malwathu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:04:59 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:09:31 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:07:43 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:01:24 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:02:33 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:03:02 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-03-03 18:03:56 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-03-03 18:00:43 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.013 |  |
| 2026-03-03 18:04:03 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.021 |  |
| 2026-03-03 18:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.021 |  |
| 2026-03-03 18:03:10 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.030 |  |
| 2026-03-03 18:02:59 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | -0.058 |  |
| 2026-03-03 18:01:30 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.137 |  |
| 2026-03-03 18:01:58 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.159 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)