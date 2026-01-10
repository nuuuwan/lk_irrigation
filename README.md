# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--10_22:22:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **42,152 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 22:22:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.27 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-10 22:20:54 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:17:28 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:17:18 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:14:20 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:14:19 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:12:02 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | -0.018 |  |
| 2026-01-10 22:11:23 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-10 22:11:19 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:11:18 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2026-01-10 22:08:38 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-01-10 22:07:25 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.075 |  |
| 2026-01-10 22:07:22 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:06:35 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:06:33 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:06:26 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:06:03 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:06:01 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:05:38 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-01-10 22:05:27 | Padiyathalawa (Maduru Oya) | 1.48 | 🟢 Normal | -0.123 |  |
| 2026-01-10 22:04:08 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-01-10 22:03:56 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-10 22:03:51 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:03:15 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-01-10 22:03:12 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:03:05 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:03:01 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:02:46 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.033 |  |
| 2026-01-10 22:02:41 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:02:34 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-10 22:01:51 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-01-10 22:01:26 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:01:21 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-01-10 22:01:17 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.020 |  |
| 2026-01-10 22:00:24 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 22:11:18 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2026-01-10 22:03:15 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-01-10 22:05:38 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-01-10 22:02:34 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-10 22:22:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.27 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-10 22:11:23 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-10 22:03:56 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-10 22:06:01 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:00:12 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:01:26 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:20:54 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:17:18 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:04:22 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:03:51 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:11:19 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:03:05 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:03:12 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:07:22 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:06:26 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:06:35 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:01:50 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:14:20 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:02:41 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:03:01 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:01:35 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:17:28 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:06:03 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:06:33 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:08:38 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-01-10 22:01:51 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-01-10 22:00:24 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-10 22:01:21 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-01-10 22:12:02 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | -0.018 |  |
| 2026-01-10 18:02:45 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.020 |  |
| 2026-01-10 22:01:17 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.020 |  |
| 2026-01-10 22:04:08 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-01-10 22:02:46 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.033 |  |
| 2026-01-10 22:07:25 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.075 |  |
| 2026-01-10 22:05:27 | Padiyathalawa (Maduru Oya) | 1.48 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)