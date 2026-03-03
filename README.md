# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--03_09:05:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **87,914 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-03 09:05:56 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-03-03 09:05:55 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-03 09:04:54 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-03 09:04:41 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-03 09:04:11 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.089 |  |
| 2026-03-03 09:04:05 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.048 |  |
| 2026-03-03 09:03:54 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-03 09:03:43 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-03 09:03:38 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-03 09:03:35 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | -0.019 |  |
| 2026-03-03 09:03:32 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 09:03:26 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-03-03 09:03:25 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-03 09:03:21 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-03-03 09:03:05 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-03-03 09:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.051 |  |
| 2026-03-03 09:02:15 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-03 09:01:51 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-03 09:01:49 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-03-03 09:01:47 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-03 09:01:29 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-03 09:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.012 |  |
| 2026-03-03 09:01:09 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-03-03 09:00:55 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-03 09:00:44 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-03 09:00:26 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-03 09:00:22 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-03 09:00:20 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | -0.010 |  |
| 2026-03-03 08:23:45 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | -0.004 |  |
| 2026-03-03 08:20:42 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-03 08:13:51 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:13:44 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:12:45 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:12:18 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-03 09:03:25 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-03 09:03:38 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-03 08:20:42 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-03 09:02:15 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-03 09:01:29 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-03 09:04:41 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-03 09:00:44 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-03 09:03:32 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 09:01:47 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-03 09:00:22 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-03 09:05:55 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:12:18 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-03 09:01:51 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-03 09:03:21 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:13:51 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-03 07:18:11 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-03-03 09:04:54 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-03 09:00:55 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-03 09:00:26 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:13:44 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-03 09:03:54 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:09:54 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 09:03:43 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:23:45 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | -0.004 |  |
| 2026-03-03 09:05:56 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-03-03 09:03:26 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-03-03 09:01:49 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-03-03 09:00:20 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | -0.010 |  |
| 2026-03-03 08:05:52 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-03-03 09:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.012 |  |
| 2026-03-03 09:03:35 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | -0.019 |  |
| 2026-03-03 09:01:09 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-03-03 09:03:05 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-03-03 08:07:55 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.028 |  |
| 2026-03-03 09:04:05 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.048 |  |
| 2026-03-03 09:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.051 |  |
| 2026-03-03 08:07:21 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.058 |  |
| 2026-03-03 09:04:11 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.089 |  |
| 2026-03-03 07:05:25 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)