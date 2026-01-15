# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--16_04:05:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **46,803 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 04:05:59 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.032 |  |
| 2026-01-16 04:05:48 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-16 04:05:26 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.000 |  |
| 2026-01-16 04:05:14 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-16 04:04:59 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-01-16 04:04:27 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-16 04:04:25 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-01-16 04:03:59 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-16 04:03:37 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-16 04:03:16 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.229 |  |
| 2026-01-16 04:03:04 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-01-16 04:02:44 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-01-16 04:02:28 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-16 04:02:19 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.021 |  |
| 2026-01-16 04:02:07 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-16 04:01:56 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-01-16 04:01:46 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-16 04:01:33 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 04:01:12 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-16 04:00:46 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-16 03:55:18 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-16 03:48:58 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.035 |  |
| 2026-01-16 03:40:53 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-16 03:16:30 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-16 03:14:53 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-16 03:14:52 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-16 03:14:41 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-16 03:13:38 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.026 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 03:05:21 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 9.000 | 🔺 Rising |
| 2026-01-16 04:04:27 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-16 03:06:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-16 03:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-16 04:01:33 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 04:03:59 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-16 03:01:45 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-16 04:01:12 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:03:50 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-16 04:02:28 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-16 04:04:59 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-01-16 04:03:37 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-16 04:05:26 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.000 |  |
| 2026-01-16 04:00:46 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-16 04:01:46 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-16 03:16:30 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-16 03:14:53 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-16 03:40:53 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-16 03:14:41 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-16 04:05:14 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-16 04:03:04 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-01-16 02:18:26 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 03:05:39 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-16 03:04:19 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-01-16 04:02:07 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-16 04:01:56 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-01-16 04:05:48 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-16 04:02:44 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-01-16 04:04:25 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-01-16 04:02:19 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.021 |  |
| 2026-01-16 03:01:25 | Manampitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.025 |  |
| 2026-01-16 03:01:59 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | -0.025 |  |
| 2026-01-16 03:13:38 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.026 |  |
| 2026-01-16 04:05:59 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.032 |  |
| 2026-01-16 03:48:58 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.035 |  |
| 2026-01-15 18:02:13 | Thanthirimale (Malwathu Oya) | 1.83 | 🟢 Normal | -0.040 |  |
| 2026-01-16 04:03:16 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.229 |  |
| 2026-01-15 18:07:05 | Weraganthota (Mahaweli Ganga) | -2.39 | 🟢 Normal | -0.400 |  |
| 2026-01-16 03:04:09 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)